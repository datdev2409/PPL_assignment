import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_redeclared_variable1(self):
        input = """a: integer; b: float; a: float;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_variable2(self):
        input = """a: function integer (n: integer) {
        }
        b: integer;
        a: float;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_variable3(self):
        input = """a: function integer (n: integer) {
  b: integer = 1;
}
c: function integer (n: integer) {
  b: integer = 2;
}
b: integer;
e: float;
e: integer;"""
        expect = "Redeclared Variable: e"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_function(self):
        input = """a: integer;a: function integer (n: integer) {
        }
        b: integer;
        a: float;"""
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_params(self):
        input = """a: function integer (n: integer, n: float) {
  b: integer = 1;
}"""
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_type_mismatch_vardecl(self):
        input = """main: function void () {
  a: integer = 10;
  b: float = 12.5;
  c: boolean = 1;
}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(c, BooleanType, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_undeclared_variable(self):
        input = """func: function void () {
  b: integer = 1; 
}

main: function void () {
  a: integer = b;
}"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 403))

#     def test_undeclared_variable2(self):
#         input = """main: function void () {
# }"""
#         expect = "Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input, expect, 403))

    def test_unexpr1(self):
        input = """
        main: function void () {
            a: integer = -1;
            b: float = -1.2;
            c: boolean = !true;
            d: string = -"abc";
        }"""
        expect = "Type mismatch in expression: UnExpr(-, StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_unexpr2(self):
        input = """
        main: function void () {
            a: boolean = !1;
        }"""
        expect = "Type mismatch in expression: UnExpr(!, IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_binexpr_arithmetic1(self):
        input = """
        main: function void () {
            a: integer = 1 + 2;
            b: integer = a - 3;
            c: float = 1 + 1.2 + a;
            d: integer = 2 * 2;
            f: integer = 4 / 5;
            g: float = 4 / 4.0;
            e: integer = 2 * 3.4;
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, BinExpr(*, IntegerLit(2), FloatLit(3.4)))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_binexpr_arithmetic2(self):
        input = """
        main: function void () {
            a: integer = 3 % 4;
            b: integer = 2 % 5.3;
        }"""
        expect = "Type mismatch in expression: BinExpr(%, IntegerLit(2), FloatLit(5.3))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_binexpr_arithmetic2(self):
        input = """
        main: function void () {
            a: integer = 3 % 4;
            b: integer = 2 % 5.3;
        }"""
        expect = "Type mismatch in expression: BinExpr(%, IntegerLit(2), FloatLit(5.3))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_assign_stmt(self):
        input = """
        a: integer;
        main: function void () {
            a = !false;
            a: boolean = false;
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(a), UnExpr(!, BooleanLit(False)))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_if_stmt(self):
        input = """
        a: integer;
        main: function void () {
            i: integer;
            for (i = 1, i < 10, i + 1) {
                a: integer = 1;
                if (a) {
                    c: integer;
                }
            }
        }"""
        expect = "Type mismatch in statement: IfStmt(Id(a), BlockStmt([VarDecl(c, IntegerType)]))"
        self.assertTrue(TestChecker.test(input, expect, 403))


    def test_for_stmt(self):
        input = """
        a: integer;
        main: function void () {
            i: integer;
            for (i = 1, i + 10, i + 1) {
                a: boolean = false;
                if (a) {
                    c: integer;
                }
            }
        }"""
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(a, BooleanType, BooleanLit(False)), IfStmt(Id(a), BlockStmt([VarDecl(c, IntegerType)]))]))"
        self.assertTrue(TestChecker.test(input, expect, 403))
