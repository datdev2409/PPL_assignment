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
        input = """a, b, c: integer = expr,expr,expr"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    
    def test_func_decl(self):
        input = """fact: function integer (out n: integer) {a: integer;b:float=expr;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

