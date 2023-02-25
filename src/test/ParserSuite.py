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
        input = """true"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    
    # Test statement
    def test_assignment_statement(self):
        input = """a = 10 + 20 * 30;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

