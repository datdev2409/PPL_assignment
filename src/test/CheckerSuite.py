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
        input = """
        a: function integer (n: integer) {
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

    def test_index_operator(self):
        input = """
        a: array [2, 3] of integer;
        b: auto = a[1];
        c: auto = b[2];
        d: auto = c[1];
        main: function void () {
        }
        """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 404))

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

    def test_assign_stmt2(self):
        input = """
        a: integer;
        foo: function integer() {}
        main: function void () {
            foo = 1;
        }"""
        expect = "Undeclared Identifier: foo"
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

    def test_must_in_loop(self):
        input = """
        a: integer;
        main: function void () {
            i: integer;
            for (i = 1, i < 10, i + 1) {
                continue;
                break;
            }
            break;
        }"""
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_return_stmt(self):
        input = """
        a: integer;
        main: function void () {
            i: integer;
            for (i = 1, i < 10, i + 1) {
                continue;
                a: boolean;
                if (a) {
                    break;
                }
                break;
                return;
            }
            break;
        }"""
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_call_stmt(self):
        input = """
        a: integer;
        sum: function float (a: float, b: integer) {
            return a + b;
        }
        main: function void () {
            b: integer = 12;
            a: float = sum(b, 3);
            sum(true, 2);
        }"""
        expect = "Type mismatch in statement: CallStmt(sum, BooleanLit(True), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_auto_func(self):
        input = """
        a: integer;
        foo: function auto () {
            if (true) a = 10;
        }
        main: function void () {
            a = foo();
            c: auto = foo();
            d: boolean = foo();
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(d, BooleanType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_auto_func2(self):
        input = """
        a: integer;
        foo: function auto () {
            if (true) a = 10;
        }
        main: function void () {
            a: float = foo();
            c: auto = foo();
            d: boolean = c;
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(d, BooleanType, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_auto_vardecl(self):
        input = """
        foo: function auto (a: integer, b: integer) {
            
        }
        main: function void () {
            // a = true;
            b: integer = foo(1, 2);
        }
        a: auto = foo(1, 2) + 1;
        c: auto = 1;
        d: boolean = foo(1, 3);
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(d, BooleanType, FuncCall(foo, [IntegerLit(1), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_array_lit(self):
        input = """
        a: array [2, 3] of integer;
        foo: function integer (a: integer, b: float) {

        } 
        main: function void () {
            c: array [2, 3] of integer = {{1, 2, 3}, {3, 4}};
        }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(4)])])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_array_lit2(self):
        input = """
        a: array [2, 3] of integer;
        b: auto = {1.2, 2.3, 3.4};
        c: auto = {{{1}, {2}}, {{3}, {4}}, {{5}, {6}}};
        main: function void () {
            a = {{1,2,3}, {3,4,5}};
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(5)])]))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_array_lit3(self):
        input = """
        a: array [3] of integer = {1, 2, 3};
        b: array [3] of float = a;
        c: array [4] of integer = a;
        main: function void () {
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, ArrayType([4], IntegerType), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_array_lit4(self):
        input = """
        a: auto = {1, 2, 3, 4.0, 5};
        c: auto = {3, 4.0};
        b: array [2, 2] of integer = {{1, 2}, {3, true}};
        main: function void () {
        }
        """
        expect = "Type mismatch in expression: VarDecl(b, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), Id(c)]))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_no_entry_point(self):
        input = """
        main: array [2, 3] of integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_no_entry_point2(self):
        input = """
        main: function void (a: integer) {

        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_no_entry_point3(self):
        input = """
        main: function integer () {

        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_hoisting_func(self):
        input = """
        main: function integer () {
            a: integer = foo();
        }
        foo: function integer() {
            return 1;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_hoisting_func2(self):
        input = """
        a: integer;
        main: function void () {
            a = foo();
            c: auto = foo();
        }
        foo: function auto () {
            if (true) a = 10;
            return true;
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_hoisting_func2(self):
        input = """
        a: integer;
        boo: function auto() {
            return true;
        }
        main: function void () {
            d: boolean = boo();
            e: integer = boo();
            a = foo();
            c: auto = foo();
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, FuncCall(boo, []))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_inherit(self):
        input = """
        boo: function auto() inherit foo {
        }
        main: function void () {
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_inherit_2(self):
        input = """
        boo: function auto() inherit foo {
            a = 10;
            b = 20;
        }
        foo: function void(inherit a: integer) {

        }
        main: function void () {
        }
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_inherit_2(self):
        input = """
        boo: function auto() inherit foo {
            a = 10;
            b = 20;
        }
        foo: function void(inherit a: integer) {

        }
        main: function void () {
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 419))


    def test_inherit_3(self):
        input = """
        boo: function auto() inherit foo {
            a = 10;
            b = 20;
        }
        foo: function void(inherit a: integer, a: integer) {

        }
        main: function void () {
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_inherit_4(self):
        input = """
        foo: function void(inherit a: integer, a: integer) {

        }
        boo: function auto() inherit foo {
            a = 10;
            b = 20;
        }
        main: function void () {
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_program_1(self):
        input=""""""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_program_2(self):
        input="""foo: function void()
        {
            
        }
        """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_program_3(self):
        input="""a:integer;"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_program_4(self):
        input="""a: float;
                 foo: function void() {}"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_program_5(self):
        input="""a: float;
                 main: function integer() {}"""
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,405))

    """Test variable declaration"""

    def test_vardecl_1(self):
        input="""
            a: float;
            b: integer;
            a: string;
            """
        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_vardecl_2(self):
        input="""
            c: string;
            d: string;
            a: string = c::d;
            e: boolean = 2;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(e, BooleanType, IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_vardecl_3(self):
        input="""
            a: auto;
            """
        expect="Invalid Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_vardecl_4(self):
        input="""
            a: integer = 1.2;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_vardecl_5(self):
        input="""
            a: float = 2;
            b: integer = 2;
            b: string;
            """
        expect="Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_vardecl_6(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = a + b;
            d: integer = c;
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, IntegerType, Id(c))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_vardecl_7(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {a,b};
            d: array [2] of float = {"a","b"};
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, ArrayType([2], FloatType), ArrayLit([StringLit(a), StringLit(b)]))"
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_vardecl_8(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {a,b,"d"};
            """
        expect="Illegal array literal: ArrayLit([Id(a), Id(b), StringLit(d)])"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_vardecl_9(self):
        input="""
            a: float = 2;
            b: integer = 2;
            c: auto = {{a,b},{a,b}};
            d: array [2] of integer = c[0];
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, ArrayType([2], IntegerType), ArrayCell(c, [IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_vardecl_10(self):
        input="""
            a: integer;
            b: array [2,2] of float;
            c: auto = b[2];
            d: integer = c[1];
            """
        expect="Type mismatch in Variable Declaration: VarDecl(d, IntegerType, ArrayCell(c, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input,expect,415))

    """Test function declaration"""
    def test_funcdecl_1(self):
        input="""
            a: function integer(b: integer, c:integer) inherit d {}
            main: function void()
            {
            
            }
            """
        expect="Undeclared Function: d"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_funcdecl_2(self):
        input="""
            a: integer;
            a: function integer(b: integer, c:integer){}
            main: function void()
            {
            
            }
            """
        expect="Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_funcdecl_3(self):
        input="""
            a: integer;
            b: function integer(c: integer, d:integer) inherit a{}
            main: function void()
            {
            
            }
            """
        expect="Undeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_funcdecl_4(self):
        input="""
            bar : function void (out n : integer, a:float) inherit foo{}
            foo : function auto (inherit n: float, n: integer){} 
            """
        expect="Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_funcdecl_5(self):
        input="""
            bar : function void (out n : integer, a:float) inherit foo{} 
            foo : function auto (inherit n: float){} 
            """
        expect="Invalid Parameter: n"
        self.assertTrue(TestChecker.test(input,expect,420))


    def test_funcdecl_6(self):
        input="""
            bar : function void (a:float) inherit foo{} 
            foo : function auto (inherit n: float){} 
            """
        expect="Invalid statement in function: bar"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_funcdecl_7(self):
        input="""
            bar : function void (a:float) inherit foo{} 
            foo : function auto (){} 
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_funcdecl_8(self):
        input="""
            bar : function void (a:float) inherit foo{
                super();
            } 
            foo : function auto (){} 
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_funcdecl_9(self):
        input="""
            bar : function void (a:float) inherit foo{
                super();
            } 
            foo : function auto (){} 
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_funcdecl_10(self):
        input="""
            bar : function void (a:float) inherit foo{
                preventDefault();
            } 
            foo : function auto (){} 
            """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_funcdecl_11(self):
        input="""
            bar : function void (a:float) inherit foo{
                preventDefault(a);
            } 
            foo : function auto (){} 
            """
        expect="Type mismatch in statement: CallStmt(preventDefault, Id(a))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_funcdecl_12(self):
        input="""
            bar : function void (a:float) inherit foo{
                super(a);
            } 
            foo : function auto (){} 
            """
        expect="Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_funcdecl_13(self):
        input="""
            bar : function void (a:float) inherit foo{
                super(a,a);
            } 
            foo : function auto (a: float, b: integer){} 
            """
        expect="Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_funcdecl_14(self):
        input="""
            bar : function void (a:float) inherit foo{
                super(a,a,a);
            } 
            foo : function auto (a: float, b: integer){} 
            """
        expect="Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_funcdecl_15(self):
        input="""
            foo: function integer (a: integer, b: auto) inherit bar 
            {
                preventDefault();
                if (a==1)
                {
                    b: integer;
                    b = 1 + foo(1,2);
                    foo(1,2)
                }
                b=1.3;
            }

            """
        expect="Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_funcdecl_16(self):
        input="""
            bar: integer;
            foo: function integer (a: integer, b: auto) inherit bar 
            {
                preventDefault();
                if (a==1)
                {
                    b: integer;
                }
            }
            bar: function integer(inherit c: integer)
            {
            
            }
            """
        expect="Redeclared Function: bar"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_funcdecl_17(self):
        input="""
            bar: integer;
            foo: function integer (a: integer, b: auto) inherit bar 
            {
                preventDefault();
                if (a==1)
                {
                    b: integer;
                }
            }
            """
        expect="Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_funcdecl_18(self):
        input="""
            foo: function integer (a: integer, b: auto)
            {
                preventDefault();
                if (a==1)
                {
                    b: integer;
                }
            }
            """
        expect="Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_funcdecl_19(self):
        input="""
            foo: function integer (a: integer, b: auto)
            {
                super();
                if (a==1)
                {
                    b: integer;
                }
            }
            """
        expect="Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_funcdecl_20(self):
        input="""
            bar: function integer(n: integer, n: integer) {}
            foo: function integer (a: integer, b: auto) inherit bar
            {
                super(1,2);
            }
            """
        expect="Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input,expect,435))

    """Test statement"""
    def test_stmt_1(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if (b==1)
                {
                
                }
                else
                {
                    if (a<2.0)
                    {
                    
                    }
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(<, Id(a), FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,436))
    
    def test_stmt_2(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if (a==1)
                {
                
                }
                else
                {
                    if (a<2.0)
                    {
                    
                    }
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(<, Id(a), FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_stmt_3(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if ((a==1) && (b=="a"))
                {
                
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(==, Id(b), StringLit(a))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_stmt_4(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if ((b<2.0) && (b==a))
                {
                
                }
                else
                {
                    if (b==1)
                    {
                    
                    }
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(==, Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_stmt_5(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                if ((1!=true) && (b==a))
                {
                
                }
                else
                {
                    if (b<2)
                    {
                    
                    }
                }
            }
            """
        expect="Type mismatch in expression: BinExpr(!=, IntegerLit(1), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_stmt_6(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                b = 1 + a;
            }
            """
        expect="Type mismatch in expression: BinExpr(+, IntegerLit(1), Id(a))"
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_stmt_7(self):
        input="""
            foo: function integer (a: boolean, b: auto)
            {
                b = a;
                a = b + 1;
            }
            """
        expect="Type mismatch in expression: BinExpr(+, Id(b), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_stmt_8(self):
        input="""
            foo: function integer (a: integer, b: auto)
            {
                b = "1"::a;
            }
            """
        expect="Type mismatch in expression: BinExpr(::, StringLit(1), Id(a))"
        self.assertTrue(TestChecker.test(input,expect,443))
        
    def test_stmt_9(self):
        input="""
            foo: function integer (a: string, b: auto)
            {
                b = a + "1";
            }
            """
        expect="Type mismatch in expression: BinExpr(+, Id(a), StringLit(1))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_stmt_10(self):
        input="""
            foo: function integer (a: auto, b: auto)
            {
                c: integer = a;
                b = a + 1.0;
                printInteger(a);
            }
            """
        expect="Type mismatch in expression: BinExpr(<, Id(b), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect,445))
