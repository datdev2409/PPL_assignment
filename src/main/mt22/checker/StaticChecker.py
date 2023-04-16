from Visitor import Visitor
from StaticError import *
from Utils import *
from AST import *


class PassingObject():
    def __init__(self, env, stack):
        self.env = env
        self.stack = stack


class FuncType():
    def __init__(self, name, return_type, params, inherit: str or None):
        self.name = name
        self.return_type = return_type
        self.params = params
        self.inherit = inherit

    def __str__(self):
        return f"Func({self.name}, {str(self.return_type)})"

    def __repr__(self):
        return f"Func({self.name}, {str(self.return_type)})"


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, [])

    def _checkValidAssign(self, lhs_type, rhs_type):
        if type(lhs_type) in [VoidType, ArrayType]:
            return False
        elif type(rhs_type) in [VoidType, ArrayType]:
            return False
        # type coerce
        elif type(lhs_type) is FloatType:
            if type(rhs_type) in [IntegerType, FloatType]:
                return FloatType()
        elif type(lhs_type) == type(rhs_type):
            return lhs_type

        return False

    def _checkInLoop(self, o: PassingObject):
        for e in o.stack:
            if type(e) in [DoWhileStmt, WhileStmt, ForStmt]:
                return True
        return False

    def _createPassingObject(self, env, stack):
        return PassingObject(env, stack)

    def _createEnv(self, o, env):
        return PassingObject(env + o.env, o.stack)

    def _pushToStack(self, o, ast):
        return PassingObject(o.env, [ast] + o.stack)

    def _lookup(self, name, o: PassingObject) -> Type | FuncType | None:
        for env in o.env:
            if name in env:
                return env[name]
        return None

    def _isFunc(self, o):
        return type(o) is FuncType

    def _checkParaPassing(self, func: FuncType, args, o):
        arg_types = list(map(lambda arg: self.visit(arg, o), args))
        param_types = func.params

        if len(arg_types) != len(param_types):
            return False

        for i in range(0, len(arg_types)):
            if not self._checkValidAssign(param_types[i], arg_types[i]):
                return False

        return True

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
        for env in o.env:
            if ast.name in env:
                if not self._isFunc(env[ast.name]):
                    return env[ast.name]
                break

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

    def visitFuncCall(self, ast: FuncCall, o: PassingObject):
        func = self._lookup(ast.name, o)
        if func is None or not self._isFunc(func):
            raise Undeclared(Function(), ast.name)

        # Check parameter passing
        if not self._checkParaPassing(func, ast.args, o):
            raise TypeMismatchInStatement(ast)

        return func.return_type

    # lhs: LHS, rhs: Expr

    def visitAssignStmt(self, ast: AssignStmt, o):
        lhs_type = self.visit(ast.lhs, o)
        rhs_type = self.visit(ast.rhs, o)

        # infer for function with auto type
        if type(rhs_type) is FuncType:
            func = rhs_type
            if type(func.return_type) is AutoType:
                func.return_type = lhs_type

        if self._checkValidAssign(lhs_type, rhs_type) is False:
            raise TypeMismatchInStatement(ast)

        return lhs_type

    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast: BlockStmt, o):
        local = [{}]
        new_o = self._createPassingObject(local + o.env, o.stack)
        for stmt in ast.body:
            self.visit(stmt, new_o)

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

        self.visit(ast.stmt, self._pushToStack(o, ast))

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast: WhileStmt, o):
        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, self._pushToStack(o, ast))

    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast: DoWhileStmt, o):
        self.visit(ast.stmt, self._pushToStack(o, ast))

        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)

    def visitBreakStmt(self, ast: BreakStmt, o):
        isInLoop = self._checkInLoop(o)
        if not isInLoop:
            raise MustInLoop(ast)

    def visitContinueStmt(self, ast: ContinueStmt, o):
        isInLoop = self._checkInLoop(o)
        if not isInLoop:
            raise MustInLoop(ast)

    def visitReturnStmt(self, ast: ReturnStmt, o: PassingObject):
        exp_type = VoidType() if ast.expr is None else self.visit(ast.expr, o)
        for e in o.stack:
            if not self._isFunc(e):
                continue

            if type(e.return_type) is VoidType and type(exp_type) is VoidType:
                return
            elif not self._checkValidAssign(e.return_type, exp_type):
                raise TypeMismatchInStatement(ast)

    # name: str, args: List[Expr]
    def visitCallStmt(self, ast: CallStmt, o):
        func = self._lookup(ast.name, o)
        if func is None or not self._isFunc(func):
            raise Undeclared(Function(), ast.name)

        # Check parameter passing
        if not self._checkParaPassing(func, ast.args, o):
            raise TypeMismatchInStatement(ast)

        # Infer auto type
        if type(func.return_type) is AutoType:
            func.return_type = VoidType()

    # name:  str, typ:  Type, init:  Expr or None

    def visitVarDecl(self, ast: VarDecl, o):
        # Check redeclared variable
        if ast.name in o.env[0]:
            raise Redeclared(Variable(), ast.name)

        # Autotype
        if type(ast.typ) is AutoType:
            if ast.init is None:
                raise Invalid(Variable(), ast.name)

            rhs_type = self.visit(ast.init, o)
            if type(rhs_type) in [AutoType, ArrayType, VoidType]:
                raise TypeMismatchInVarDecl(ast)

            o.env[0][ast.name] = rhs_type
            return

        if ast.init is not None:
            init_type = self.visit(ast.init, o)
            lhs_type = ast.typ
            if not self._checkValidAssign(lhs_type, init_type):
                raise TypeMismatchInVarDecl(ast)

        o.env[0][ast.name] = ast.typ

    # name: str, typ: Type, out: bool, inherit: bool
    def visitParamDecl(self, ast: ParamDecl, o):
        if ast.name in o[0]:
            raise Redeclared(Parameter(), ast.name)

        o[0][ast.name] = ast.typ
        return ast.typ

    # name: str
    # return_type: Type
    # params: [ParamDecl]
    # inherit: str or None
    # body: Blockstmt
    def visitFuncDecl(self, ast: FuncDecl, o):
        # Check redeclared function
        if ast.name in o.env[0]:
            raise Redeclared(Function(), ast.name)

        local = [{}]
        params = []
        for param in ast.params:
            params.append(self.visit(param, local))

        func = FuncType(ast.name, ast.return_type, params, ast.inherit)
        new_o = PassingObject(local + o.env, [func] + o.stack)
        self.visit(ast.body, new_o)

        o.env[0][ast.name] = func

    # decls:  [Decl]
    def visitProgram(self, ast: Program, o):
        o = PassingObject([{}], [])
        for decl in ast.decls:
            self.visit(decl, o)

        return o.env
