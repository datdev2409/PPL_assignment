from Visitor import Visitor
from StaticError import *
from AST import *


class PreChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, {})

    def visitParamDecl(self, ast: ParamDecl, o):
        return o + [Param(ast.name, ast.typ)]

    def visitFuncDecl(self, ast: FuncDecl, o):
        params = []
        for param in ast.params:
            params = self.visit(param, params)

        o[ast.name] = FuncType(ast.name, ast.return_type, params, ast.inherit)

    def visitProgram(self, ast: Program, o):
        o = {}
        for decl in ast.decls:
            self.visit(decl, o)

        return o


class Param():
    def __init__(self, name, type):
        self.name = name
        self.type = type


class FuncType():
    def __init__(self, name, return_type, params, inherit: str or None):
        self.name = name
        self.return_type = return_type
        self.params = params
        self.inherit = inherit

    def __str__(self):
        return f"Func({self.name}, {str(self.return_type)}, {str(self.params)})"

    def __repr__(self):
        return f"Func({self.name}, {str(self.return_type)}, {str(self.params)})"
