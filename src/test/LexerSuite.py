import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_keyword(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("auto break false float integer return void out array boolean for string continue do else function if true while of inherit", "auto,break,false,float,integer,return,void,out,array,boolean,for,string,continue,do,else,function,if,true,while,of,inherit,<EOF>", 100))

    def test_operator(self):
        self.assertTrue(TestLexer.test("+-*/%!&&||==!= ::< <= > >=", "+,-,*,/,%,!,&&,||,==,!=,::,<,<=,>,>=,<EOF>", 101))
    
    def test_seperators(self):
        self.assertTrue(TestLexer.test("()[].,;:{}=", "(,),[,],.,,,;,:,{,},=,<EOF>", 102))
    
    def test_c_comment_basic(self):
        self.assertTrue(TestLexer.test("/* hello wo124321 */", "<EOF>", 103))
    
    def test_c_comment_error(self):
        self.assertTrue(TestLexer.test("/* hello */world */", "world,*,/,<EOF>", 104))
    
    def test_c_comment_advance(self):
        self.assertTrue(TestLexer.test("/* hello \n */auto", "auto,<EOF>", 105))

    def test_cpp_comment_basic(self):
        self.assertTrue(TestLexer.test("//hello world auto", "<EOF>", 106))
    
    def test_cpp_comment_error(self):
        self.assertTrue(TestLexer.test("// hel//lo \n\n chao", "chao,<EOF>", 107))

    def test_int_lit(self):
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 108))

    def test_int_lit2(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 109))
    
    def test_float_lit(self):
        self.assertTrue(TestLexer.test(".234e3", ".234e3,<EOF>", 110))

    def test_float_lit2(self):
        self.assertTrue(TestLexer.test("1_234.5_67", "1234.5,_67,<EOF>", 111))

    def test_float_lit3(self):
        self.assertTrue(TestLexer.test("1.2e3", "1.2e3,<EOF>", 112))
    
    def test_bool_lit(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 113))

    def test_string_lit(self):
        self.assertTrue(TestLexer.test('"He asked me: \\"Where is John?\\""', 'He asked me: "Where is John?",<EOF>', 114))
    
    def test_string_lit(self):
        self.assertTrue(TestLexer.test("\"This is \ca string containing tab \t\"", 'This is a string containing tab \t,<EOF>', 115))
    # def test_escape_quote(self):
    #     self.assertTrue(TestLexer.test('\\"', '\\",<EOF>', 115))

    def test_array_lit(self):
        self.assertTrue(TestLexer.test("{1, 5, 7, 12}", "{1, 5, 7, 12},<EOF>", 116))
    
    def test_array_lit2(self):
        self.assertTrue(TestLexer.test("{1,2,3}", "{1,2,3},<EOF>", 117))

    def test_indentifier(self):
        self.assertTrue(TestLexer.test("WriteLn", "WriteLn,<EOF>", 118))

    

