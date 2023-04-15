from Visitor import Visitor
from StaticError import *
from Utils import *
from AST import *


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, [])

    def _checkValidAssign(self, lhs_type, rhs_type):
        if type(lhs_type) in [VoidType, ArrayType]:
            return False
        elif type(lhs_type) is FloatType:
            if type(rhs_type) in [IntegerType, FloatType]:
                return FloatType()
        elif type(lhs_type) == type(rhs_type):
            return lhs_type

        return False

    def visitIntegerType(self, ast: IntegerType, o):
        return IntegerType()

    def visitFloatType(self, ast: FloatType, o):
        return FloatType()

    def visitBooleanType(self, ast: BooleanType, o):
        return BooleanType()

    def visitStringType(self, ast: StringType, o):
        return StringType()

    def visitArrayType(self, ast: ArrayType, o):
        return ArrayType()

    def visitAutoType(self, ast: AutoType, o):
        return AutoType()

    def visitVoidType(self, ast: VoidType, o):
        return VoidType()

    # op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast: BinExpr, o):
        ltype = self.visit(ast.left, o)
        rtype = self.visit(ast.right, o)

        if ast.op in ["-", "+", "*", "/"]:
            if type(ltype) not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(ast)

            if type(rtype) not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(ast)

            if type(ltype) is FloatType or type(rtype) is FloatType:
                return FloatType()

            return IntegerType()

        elif ast.op == "%":
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()

        elif ast.op in ["&&", "||"]:
            if type(ltype) is BooleanType and type(rtype) is BooleanType:
                return BooleanType()

        elif ast.op == "::":
            if type(ltype) is StringType and type(rtype) is StringType:
                return StringType()

        elif ast.op in ["==", "!="]:
            if type(ltype) not in [IntegerType, BooleanType]:
                raise TypeMismatchInExpression(ast)
            if type(rtype) not in [IntegerType, BooleanType]:
                raise TypeMismatchInExpression(ast)
            if type(ltype) != type(rtype):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

        elif ast.op in [">", "<", ">=", "<="]:
            if type(ltype) not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(ast)

            if type(rtype) not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(ast)

            return BooleanType()

        raise TypeMismatchInExpression(ast)

    # op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, o):
        etype = self.visit(ast.val, o)
        if ast.op == "-":
            if type(etype) not in [FloatType, IntegerType]:
                raise TypeMismatchInExpression(ast)
            return etype

        elif ast.op == "!":
            if type(etype) is BooleanType:
                return BooleanType()

        raise TypeMismatchInExpression(ast)

    def visitId(self, ast: Id, o):
        for env in o:
            if ast.name in env:
                return env[ast.name]

        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast: ArrayCell, o): pass

    # Literals
    def visitIntegerLit(self, ast: IntegerLit, o):
        return IntegerType()

    def visitFloatLit(self, ast: FloatLit, o):
        return FloatType()

    def visitStringLit(self, ast: StringLit, o):
        return StringType()

    def visitBooleanLit(self, ast: BooleanLit, o):
        return BooleanType()

    def visitArrayLit(self, ast: ArrayLit, o):
        return ArrayType()

    # Statements
    def visitFuncCall(self, ast: FuncCall, o): pass

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast: AssignStmt, o):
        lhs_type = self.visit(ast.lhs, o)
        rhs_type = self.visit(ast.rhs, o)

        if self._checkValidAssign(lhs_type, rhs_type) is False:
            raise TypeMismatchInStatement(ast)

        return lhs_type

    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast: BlockStmt, o):
        local = [{}]
        for stmt in ast.body:
            self.visit(stmt, local + o)

    # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast: IfStmt, o):
        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.tstmt, o)
        if ast.fstmt is not None:
            self.visit(ast.fstmt, o)

    # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast: ForStmt, o):
        variable_type = self.visit(ast.init, o)
        cond_type = self.visit(ast.cond, o)
        upd_type = self.visit(ast.upd, o)
        if type(variable_type) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        elif type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        elif type(upd_type) is not IntegerType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, o)

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast: WhileStmt, o):
        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, o)

    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast: DoWhileStmt, o):
        self.visit(ast.stmt, o)

        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)

    def visitBreakStmt(self, ast: BreakStmt, o): pass
    def visitContinueStmt(self, ast: ContinueStmt, o): pass
    def visitReturnStmt(self, ast: ReturnStmt, o): pass
    def visitCallStmt(self, ast: CallStmt, o): pass

    # name:  str, typ:  Type, init:  Expr or None
    def visitVarDecl(self, ast:  VarDecl, o):
        # Check redeclared variable
        if ast.name in o[0]:
            raise Redeclared(Variable(), ast.name)

        # Check invalid variable declaration
        if type(ast.typ) is AutoType and ast.init is None:
            raise Invalid(Variable(), ast.name)

        if ast.init is not None:
            init_type = self.visit(ast.init, o)
            lhs_type = ast.typ
            if self._checkValidAssign(lhs_type, init_type) is False:
                raise TypeMismatchInVarDecl(ast)

        o[0][ast.name] = ast.typ

    # name: str, typ: Type, out: bool, inherit: bool
    def visitParamDecl(self, ast: ParamDecl, o):
        if ast.name in o[0]:
            raise Redeclared(Parameter(), ast.name)

        o[0][ast.name] = ast.typ

    # name: str
    # return_type: Type
    # params: [ParamDecl]
    # inherit: str or None
    # body: Blockstmt
    def visitFuncDecl(self, ast: FuncDecl, o):
        # Check redeclared function
        if ast.name in o[0]:
            raise Redeclared(Function(), ast.name)

        local = [{}]
        for param in ast.params:
            self.visit(param, local)

        # new_o = {'env': local + o.env, 'stack': ast + o.stack}

        self.visit(ast.body, local + o)
        o[0][ast.name] = ast.return_type

    # decls:  [Decl]
    def visitProgram(self, ast: Program, o):
        o = [{}]
        # o = {'env': [{}], 'stack': []}
        for decl in ast.decls:
            self.visit(decl, o)

        return o
