import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program2(self):
        # """Simple program: int main() {} """
        input = """a, b, c: integer = 2+4*3,2,3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    
    def test_func_decl(self):
        input = """fact: function integer (out n: integer) {a: integer;b:float=expr;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    
    def test_func_decl2(self):
        input = """x: integer = 65; 
            fact: function integer (n: integer) {
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_expression(self):
        input = """x: integer = (2+3)*4/5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_expression2(self):
        input = """x: boolean = true || false;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_expression3(self):
        input = """true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    
    # Test declarations
    def test_variable_declaration(self):
        input = """a,b,c:integer = 1,2,3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_variable_declaration2(self): #! it must return error
        input = """a,b,c:integer = 1;"""
        expect = "Error on line 1 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_variable_declaration3(self): 
        input = """a,b,c:integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_variable_declaration4(self): 
        input = """a,b,c:integer = 1,2,3;\na,b,c:integer = 1,2,3,4+5;"""
        expect = "Error on line 2 col 21: ,"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    def test_function_declaration(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test_function_declaration2(self):
        input = """inc: function void (out n: integer, delta: integer) {
            n = n + delta;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_function_declaration3(self):
        input = """main: function void () {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    # Test expression
    def test_arithmetic_operator(self):
        input = """a = 5 -- 10.5 / 3 * 2 % 4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_boolean_operator(self):
        input = """!true && false && abc || (abc > 3) ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    
    def test_string_operator(self):
        input = """\"hello world\" :: \" My name is;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    # Test statement
    def test_assignment_statement(self):
        input = """a = 10 + 20 * 30;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    
    # Test functions
    def test_read_integer(self):
        input = """abc(1, 2, 3);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

