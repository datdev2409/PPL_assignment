from PreChecker import PreChecker
from Visitor import Visitor
from StaticError import *
from Utils import *
from AST import *


class PO():
    def __init__(self, env, stack, proto):
        self.env = env
        self.stack = stack
        self.proto = proto


class Param():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f"{self.name}:{self.type}"

    def __repr__(self):
        return f"{self.name}:{self.type}"


class FuncType(Type):
    def __init__(self, name, return_type, params, inherit: str or None):
        self.name = name
        self.return_type = return_type
        self.params = params
        self.inherit = inherit

    def __str__(self):
        return f"Func({self.name}, {str(self.return_type)}, {str(self.params)})"

    def __repr__(self):
        return f"Func({self.name}, {str(self.return_type)}, {str(self.params)})"


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, [])

    def lookupProto(self, name, proto) -> FuncDecl | None:
        return proto[name] if name in proto else None

    def lookupEnv(self, name, env) -> Type | None:
        for e in env:
            if name in e:
                return e[name]
        return None

    def inferType(self, expr: Expr, typ, o: PO):
        if type(expr) is FuncCall:
            func = self.lookupProto(expr.name, o.proto)
            if type(func.return_type) is not AutoType:
                return
            func.return_type = typ

        elif type(expr) is Id:
            name = expr.name
            for env in o.env:
                if name in env and type(env[name]) is AutoType:
                    env[name] = typ

    def checkAssign(self, lhs_type, rhs_type):
        if type(lhs_type) is VoidType or type(rhs_type) is VoidType:
            return False
        # type coerce
        elif type(lhs_type) is FloatType:
            if type(rhs_type) in [IntegerType, FloatType]:
                return FloatType()
        elif type(lhs_type) == type(rhs_type):
            return lhs_type

        return False

    # Convert array of param declaration in function to dict
    def toEnv(self, params: list[ParamDecl], init = {}):
        env = init
        for param in params:
            env[param.name] = param.typ

        return env

    def _checkInLoop(self, o: PO):
        for e in o.stack:
            if type(e) in [DoWhileStmt, WhileStmt, ForStmt]:
                return True
        return False

    def _createEnv(self, o, env):
        return PO(env + o.env, o.stack, o.proto)

    def pushToStack(self, o, ast):
        return PO(o.env, [ast] + o.stack, o.proto)

    def _lookup(self, name, o: PO) -> Type | FuncType | None:
        for env in o.env:
            if name in env:
                return env[name]
        return None

    def _lookup_func(self, funcName, o: PO):
        for env in o.env:
            if funcName in env:
                return env[funcName]

        if funcName in o.proto:
            return o.proto[funcName]

        return None

    def isFuncType(self, o):
        return type(o) is FuncType

    def checkArgs(self, func: FuncType, passing_args, o):
        params: list[ParamDecl] = func.params
        args: list(Type) = list(
            map(lambda arg: self.visit(arg, o), passing_args))

        if len(args) != len(params):
            return False

        for i in range(len(args)):
            if type(params[i].typ) is AutoType:
                params[i].typ = args[i]

            elif type(args[i]) is AutoType:
                exp = passing_args[i]
                self.inferType(exp, func.params[i], o)

            if not self.checkAssign(params[i].typ, args[i]):
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

    # self, dimensions: List[int], typ: AtomicType
    def visitArrayType(self, ast: ArrayType, o):
        return ast

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
                if not self.isFuncType(env[ast.name]):
                    return env[ast.name]
                break

        raise Undeclared(Identifier(), ast.name)

    # name: str, cell: List[Expr]
    def visitArrayCell(self, ast: ArrayCell, o):
        # Check type name
        arr = self._lookup(ast.name, o)
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        # Check type expr
        for exp in ast.cell:
            exp_type = self.visit(exp, o)
            if type(exp_type) is not IntegerType:
                raise TypeMismatchInExpression(ast)

        # Base case, ArrayType([3], AtomicType)
        n_cell = len(ast.cell)
        n_dimen = len(arr.dimensions)
        if n_dimen == n_cell:
            return arr.typ
        elif n_dimen < n_cell:
            raise TypeMismatchInExpression(ast)

        new_dimes = arr.dimensions.copy()
        for i in range(0, n_dimen - n_cell):
            new_dimes.pop(0)

        return ArrayType(new_dimes, arr.typ)

    # Literals
    def visitIntegerLit(self, ast: IntegerLit, o):
        return IntegerType()

    def visitFloatLit(self, ast: FloatLit, o):
        return FloatType()

    def visitStringLit(self, ast: StringLit, o):
        return StringType()

    def visitBooleanLit(self, ast: BooleanLit, o):
        return BooleanType()

    def compareArrayType(self, arr_lhs: ArrayType, arr_rhs: ArrayType):
        if arr_lhs.dimensions != arr_rhs.dimensions:
            return False
        elif type(arr_lhs.typ) is FloatType and type(arr_rhs) is IntegerType:
            return True
        elif type(arr_rhs) != type(arr_lhs):
            return False
        return True

    def visitArrayLit(self, ast: ArrayLit, o):
        # dont care case array with 0 element
        element_type = self.visit(ast.explist[0], o)
        exp_types = list(map(lambda e: self.visit(e, o), ast.explist))

        for exp_type in exp_types:
            if type(element_type) is FloatType and type(exp_type) is IntegerType:
                continue

            elif type(element_type) is IntegerType and type(exp_type) is FloatType:
                element_type = FloatType()
                continue

            elif type(exp_type) is ArrayType and self.compareArrayType(element_type, exp_type):
                if type(exp_type.typ) is FloatType:
                    element_type = exp_type

            elif type(element_type) != type(exp_type):
                raise IllegalArrayLiteral(ast)

            elif type(element_type) is ArrayType and not self.compareArrayType(element_type, exp_type):
                raise IllegalArrayLiteral(ast)
            
            

        # element_type is ArrayType
        if type(element_type) is ArrayType:
            array = element_type
            dimens = [len(ast.explist)] + array.dimensions
            return ArrayType(dimens, array.typ)

        return ArrayType([len(ast.explist)], element_type)

    def visitFuncCall(self, ast: FuncCall, o: PO):
        func = self.lookupProto(ast.name, o.proto)
        if func is None or not self.isFuncType(func):
            raise Undeclared(Function(), ast.name)

        # Check parameter passing
        if not self.checkArgs(func, ast.args, o):
            raise TypeMismatchInExpression(ast)

        # Check return type
        if type(func.return_type) is VoidType:
            raise TypeMismatchInExpression(ast)

        return func.return_type

    # lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast: AssignStmt, o: PO):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)

        # infer for function with auto type
        if type(lhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is AutoType and type(rhs) is AutoType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs) is AutoType:
            self.inferType(ast.lhs, rhs, o)
            return
        elif type(rhs) is AutoType:  # rhs -> id
            self.inferType(ast.rhs, lhs, o)
            return
        elif not self.checkAssign(lhs, rhs):
            raise TypeMismatchInStatement(ast)

    # body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast: BlockStmt, o: PO):
        local = [{}]
        new_o = PO(local + o.env, o.stack, o.proto)
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
        variable_type = self.visit(ast.init.lhs, o)
        cond_type = self.visit(ast.cond, o)
        upd_type = self.visit(ast.upd, o)
        if type(variable_type) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        elif type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        elif type(upd_type) is not IntegerType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, self.pushToStack(o, ast))

    # cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast: WhileStmt, o):
        cond_type = self.visit(ast.cond, o)
        if type(cond_type) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, self.pushToStack(o, ast))

    # cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast: DoWhileStmt, o):
        self.visit(ast.stmt, self.pushToStack(o, ast))

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

    def visitReturnStmt(self, ast: ReturnStmt, o: PO):
        # Get type of expression
        etype = self.visit(ast.expr, o) if ast.expr is not None else VoidType()

        # Check return stmt in function or not
        func = None
        for block in o.stack:
            if type(block) is FuncType:
                func = block
                break

        # Check type function and type of return
        if type(func.return_type) is AutoType:
            func.return_type = etype
            o.proto[func.name] = func

        elif type(func.return_type) is FloatType:
            if type(etype) not in [IntegerType, FloatType]:
                raise TypeMismatchInStatement(ast)

        elif type(func.return_type) != type(etype):
            raise TypeMismatchInStatement(ast)

    # name: str, args: List[Expr]
    def visitCallStmt(self, ast: CallStmt, o: PO):
        func = self.lookupProto(ast.name, o.proto)
        if func is None:
            raise Undeclared(Function(), ast.name)

        # Check parameter passing and infertype
        if not self.checkArgs(func, ast.args, o):
            raise TypeMismatchInStatement(ast)

        # Infer auto type
        # if type(func.return_type) is AutoType:
        #     func.return_type = VoidType()

    # name:  str, typ:  Type, init:  Expr or None
    def visitVarDecl(self, ast: VarDecl, o):
        # Check redeclared variable
        if ast.name in o.env[0]:
            raise Redeclared(Variable(), ast.name)

        if ast.init is None:
            if type(ast.typ) is AutoType:
                raise Invalid(Variable(), ast.name)

            o.env[0][ast.name] = ast.typ
            return

        # ast.init != None
        lhs = ast.typ
        rhs = self.visit(ast.init, o)

        if type(rhs) is VoidType:
            raise TypeMismatchInVarDecl(ast)
        if type(lhs) is AutoType and type(rhs) is AutoType:
            raise TypeMismatchInVarDecl(ast)
        elif type(lhs) is AutoType:
            o.env[0][ast.name] = rhs
            return
        elif type(rhs) is AutoType:  # rhs -> id
            self.inferType(ast.init, lhs, o)
            o.env[0][ast.name] = lhs
            return
        elif type(rhs) is ArrayType and type(lhs) is ArrayType:
            if lhs.dimensions != rhs.dimensions:
                raise TypeMismatchInVarDecl(ast)
            elif type(lhs.typ) is FloatType and type(rhs.typ) in [FloatType, IntegerType]:
                o.env[0][ast.name] = FloatType()
            elif type(lhs.typ) != type(rhs.typ):
                raise TypeMismatchInVarDecl(ast)

        elif not self.checkAssign(lhs, rhs):
            raise TypeMismatchInVarDecl(ast)

        o.env[0][ast.name] = lhs

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
    def visitFuncDecl(self, ast: FuncDecl, o: PO):
        # Check redeclared function
        if ast.name in o.env[0]:
            raise Redeclared(Function(), ast.name)

        # Check inherit
        parent_params = [{}]
        if ast.inherit is not None:
            parent = self.lookupProto(ast.inherit, o.proto)
            if parent is None:
                raise Undeclared(Function(), ast.inherit)

            parent_params = [{}]
            for param in parent.params:
                if param.inherit:
                    self.visit(param, parent_params)

        # Check redeclared parameter
        local = parent_params
        for param in ast.params:
            self.visit(param, local)

        # Get function proto
        proto: FuncDecl = self.lookupProto(ast.name, o.proto)

        local = [self.toEnv(proto.params, parent_params[0])]

        new_o = PO(local + o.env, [proto] + o.stack, o.proto)
        self.visit(ast.body, new_o)

        o.env[0][ast.name] = proto

    # decls:  [Decl]
    def checkNoEntryPoint(self, o: PO):
        name = "main"
        mainFunc = self.lookupProto(name, o.proto)
        if mainFunc is None:
            raise NoEntryPoint()
        elif type(mainFunc) is not FuncType:
            raise NoEntryPoint()
        elif len(mainFunc.params) != 0:
            raise NoEntryPoint()
        elif type(mainFunc.return_type) is not VoidType:
            raise NoEntryPoint()
        elif mainFunc.inherit is not None:
            raise NoEntryPoint()

    def visitProgram(self, ast: Program, o):
        o = PO([{}], [], {})
        p = PreChecker(ast)
        o.proto = p.check()

        for decl in ast.decls:
            self.visit(decl, o)

        # Test no entry point
        self.checkNoEntryPoint(o)

        return o.env


class PreChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, {})

    def visitFuncDecl(self, ast: FuncDecl, o):
        o[ast.name] = FuncType(ast.name, ast.return_type, ast.params, ast.inherit)

    def visitProgram(self, ast: Program, o):
        o = {}
        for decl in ast.decls:
            self.visit(decl, o)

        return o
