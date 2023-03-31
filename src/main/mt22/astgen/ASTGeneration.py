from functools import reduce
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decl+ EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decls = reduce(lambda acc, decl : acc +  self.visit(decl), ctx.decl(), [])
        return Program(decls)

    # mttype: atomicType | arrayType | voidType | autoType;
    def visitMttype(self, ctx:MT22Parser.MttypeContext):
        if ctx.voidType() != None:
            return self.visit(ctx.voidType())
        return self.visit(ctx.valueType())


    # valueType: atomicType | arrayType | autoType;
    def visitValueType(self, ctx:MT22Parser.ValueTypeContext):
        if ctx.atomicType() != None:
            return self.visit(ctx.atomicType())
        elif ctx.arrayType() != None:
            return self.visit(ctx.arrayType())
        return self.visit(ctx.autoType())


    # Visit a parse tree produced by MT22Parser#atomicType.
    # atomicType: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        if ctx.BOOLEAN() != None:
            return BooleanType()
        elif ctx.INTEGER() != None:
            return IntegerType()
        elif ctx.FLOAT() != None:
            return FloatType()
        return StringType()


    # dimens: LSB INTLIT (CM INTLIT)* RSB;
    def visitDimens(self, ctx:MT22Parser.DimensContext):
        return [int(x.getText()) for x in ctx.INTLIT()]


    # arrayType: ARRAY dimens OF atomicType;
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        dimensions = self.visit(ctx.dimens())
        atomicType = self.visit(ctx.atomicType())
        return ArrayType(dimensions, atomicType)


    # Visit a parse tree produced by MT22Parser#voidType.
    def visitVoidType(self, ctx:MT22Parser.VoidTypeContext):
        return VoidType()


    # Visit a parse tree produced by MT22Parser#autoType.
    def visitAutoType(self, ctx:MT22Parser.AutoTypeContext):
        return AutoType()


    # decl: varDecl | funcDecl;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.varDecl() != None:
            return self.visit(ctx.varDecl())
        return self.visit(ctx.funcDecl())


    # varDecl: varDeclShort | varDeclFull SC;
    def visitVarDecl(self, ctx:MT22Parser.VarDeclContext):
        if ctx.varDeclShort() != None:
            return self.visit(ctx.varDeclShort())
        return self.visit(ctx.varDeclFull())


    # varDeclShort: ID (CM ID)* COLON mttype SC;
    def visitVarDeclShort(self, ctx:MT22Parser.VarDeclShortContext):
        ids = ctx.ID()
        type = self.visit(ctx.mttype())
        return list(map(lambda id : VarDecl(id.getText(), type), ids))


    # varDeclFull: ID CM varDeclFull CM exp | ID COLON valueType ASSIGN exp;
    # a b c 0 1 2
    # c 0
    # b c 1 0
    # a b c 2 1 0
    def visitVarDeclFull(self, ctx:MT22Parser.VarDeclFullContext):
        if ctx.ASSIGN() != None:
            type = self.visit(ctx.mttype())
            exp = self.visit(ctx.exp())
            return [VarDecl(ctx.ID().getText(), type, exp)]

        p = self.visit(ctx.varDeclFull())
        ids = [ctx.ID().getText()] + [x.name for x in p]
        exps = [x.init for x in p] + [self.visit(ctx.exp())] 
        type = p[0].typ
        return [VarDecl(ids[i], type, exps[i]) for i in range(len(ids))]


    # paramDecl: INHERIT? OUT? ID COLON mttype;
    def visitParamDecl(self, ctx:MT22Parser.ParamDeclContext):
        name = ctx.ID().getText()
        type = self.visit(ctx.mttype())
        return ParamDecl(name, type, ctx.OUT() != None, ctx.INHERIT() != None)


    # paramDecls: paramDecl (CM paramDecl)*;
    def visitParamDecls(self, ctx:MT22Parser.ParamDeclsContext):
        return [self.visit(x) for x in ctx.paramDecl()]


    # funcDecl: ID COLON FUNCTION mttype LRB paramDecls? RRB (INHERIT ID)? blockStmt;
    def visitFuncDecl(self, ctx:MT22Parser.FuncDeclContext):
        name = ctx.ID(0).getText()
        returnType = self.visit(ctx.mttype())
        paramList = self.visit(ctx.paramDecls()) if ctx.paramDecls() != None else []
        inherit = ctx.ID(1).getText() if ctx.INHERIT() != None else None
        body = self.visit(ctx.blockStmt())
        return [FuncDecl(name, returnType, paramList, inherit, body)]


    # Visit a parse tree produced by MT22Parser#literal.
    # literal: INTLIT | BOOLLIT | STRINGLIT | FLOATLIT | arraylit;
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INTLIT() != None:
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT() != None:
            val = ctx.FLOATLIT().getText()
            if val[0] == ".":
                val = "0" + val
            return FloatLit(float(val))
        elif ctx.BOOLLIT() != None:
            val = True if ctx.BOOLLIT().getText() == "true" else False
            return BooleanLit(val)
        elif ctx.STRINGLIT() != None:
            return StringLit(ctx.STRINGLIT().getText())
        return self.visit(ctx.arraylit())


    # arraylit: LCB explist? RCB;
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        explist = self.visit(ctx.explist()) if ctx.explist() != None else []
        return ArrayLit(explist)


    # explist: exp (CM exp)*;
    def visitExplist(self, ctx:MT22Parser.ExplistContext):
        return [self.visit(x) for x in ctx.exp()]


    # arrayCell: ID LSB explist RSB;
    def visitArrayCell(self, ctx:MT22Parser.ArrayCellContext):
        return ArrayCell(self.ID().getText(), self.visit(ctx.explist()))


    # funcCall: ID LRB explist? RRB;
    def visitFuncCall(self, ctx:MT22Parser.FuncCallContext):
        explist = self.visit(ctx.explist()) if ctx.explist() != None else []
        return FuncCall(ctx.ID().getText(), explist)


    # exp: exp1 CONCAT exp1 | exp1;
    def visitExp(self, ctx:MT22Parser.ExpContext):
        if ctx.CONCAT() != None:
            op = ctx.CONCAT().getText()
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinExpr(op, left, right)
        return self.visit(ctx.exp1(0))


    # exp1: exp2 (EQUAL|DIFF|LESS|GREATER|LESSEQUAL|GREATEREQUAL) exp2 | exp2;
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp2(0))
            right = self.visit(ctx.exp2(1))
            return BinExpr(op, left, right)
        return self.visit(ctx.exp2(0))


    # exp2: exp2 (AND | OR) exp3 | exp3;
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinExpr(op, left, right)
        return self.visit(ctx.exp3())


    # exp3: exp3 (ADD | SUBTRACT) exp4 | exp4;
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            return BinExpr(op, left, right)
        return self.visit(ctx.exp4())


    # exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            return BinExpr(op, left, right)
        return self.visit(ctx.exp5())


    # exp5: NEG exp5 | exp6;
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        if ctx.NEG() != None:
            op = ctx.NEG().getText()
            return UnExpr(op, self.visit(ctx.exp5()))
        return self.visit(ctx.exp6())


    # exp6: SUBTRACT exp6| exp7;
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        if ctx.SUBTRACT() != None:
            op = ctx.SUBTRACT().getText()
            return UnExpr(op, self.visit(ctx.exp6()))
        return self.visit(ctx.exp7())

    # exp7: funcCall | arrayCell | operands | LRB exp RRB;
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.exp())


    # Visit a parse tree produced by MT22Parser#operands.
    # operands: literal | ID;
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        if ctx.ID() != None:
            return Id(ctx.ID().getText())
        return self.visit(ctx.literal())


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))


    # assignStmt: (ID | arrayCell) ASSIGN exp SC;
    def visitAssignStmt(self, ctx:MT22Parser.AssignStmtContext):
        lhs = Id(ctx.ID().getText()) if ctx.ID() != None else self.visit(ctx.arrayCell())
        rhs = self.visit(ctx.exp())
        return AssignStmt(lhs, rhs)


    # ifStmt: IF LRB exp RRB stmt (ELSE stmt)?;
    def visitIfStmt(self, ctx:MT22Parser.IfStmtContext):
        cond = self.visit(ctx.exp())
        tstmt = self.visit(ctx.stmt(0))
        fstmt = self.visit(ctx.stmt(1)) if ctx.stmt(1) != None else None
        return IfStmt(cond, tstmt, fstmt)

    # callStmt: funcCall SC;
    def visitCallStmt(self, ctx:MT22Parser.CallStmtContext):
        funcCall = self.visit(ctx.funcCall())
        name = funcCall.name
        exps = funcCall.args
        return CallStmt(name, exps)

    # forStmt: FOR LRB assignStmt CM exp CM exp RRB stmt;
    def visitForStmt(self, ctx:MT22Parser.ForStmtContext):
        init = self.visit(ctx.assignStmt())
        cond = self.visit(ctx.exp(0))
        upd = self.visit(ctx.exp(1))
        stmt = self.visit(ctx.stmt())
        return ForStmt(init, cond, upd, stmt)


    # whileStmt: WHILE LRB exp RRB stmt;
    def visitWhileStmt(self, ctx:MT22Parser.WhileStmtContext):
        cond = self.visit(ctx.exp())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(cond, stmt)


    # doWhileStmt: DO blockStmt WHILE LRB exp RRB SC;
    def visitDoWhileStmt(self, ctx:MT22Parser.DoWhileStmtContext):
        cond = self.visit(ctx.exp())
        stmt = self.visit(ctx.blockStmt())
        return DoWhileStmt(cond, stmt)


    # breakStmt: BREAK SC;
    def visitBreakStmt(self, ctx:MT22Parser.BreakStmtContext):
        return BreakStmt()


    # contStmt: CONTINUE SC;
    def visitContStmt(self, ctx:MT22Parser.ContStmtContext):
        return ContinueStmt()


    # returnStmt: RETURN exp? SC;
    def visitReturnStmt(self, ctx:MT22Parser.ReturnStmtContext):
        exp = self.visit(ctx.exp()) if ctx.exp() != None else None
        return ReturnStmt(exp)

    # body: stmt body | varDecl body | ;
    def visitBody(self, ctx:MT22Parser.BodyContext):
        if ctx.stmt() != None:
            return [self.visit(ctx.stmt())] + self.visit(ctx.body())
        elif ctx.varDecl() != None:
            return self.visit(ctx.varDecl()) + self.visit(ctx.body())
        return []

    # Visit a parse tree produced by MT22Parser#blockStmt.
    # blockStmt: LCB body RCB;
    def visitBlockStmt(self, ctx:MT22Parser.BlockStmtContext):
        return BlockStmt(self.visit(ctx.body()))

