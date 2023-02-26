import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program2(self):
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
        input = """main: function void () {
            true;
            }"""
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
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test_function_declaration(self):
        input = """fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    
    def test_function_declaration2(self):
        input = """inc: function void (out n: integer, delta: integer) {
            n = n + delta;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_function_declaration3(self):
        input = """main: function void () {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    # Test expression
    def test_arithmetic_operator(self):
        input = """main: function void () {
            a = 5 -- 10.5 / 3 * 2 % 4;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_boolean_operator(self):
        input = """main: function void () {
            !true && false && abc || (abc > 3) ;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test_string_operator(self):
        input = """main: function void () {
            \"hello world\" :: \"My name is\";
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_string_operator2(self):
        input = """main: function void () {
            \"hello world\" :: \"My name is;
            }"""
        expect = "My name is;"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_string_operator3(self):
        input = """main: function void () {
            abc :: \"12_3\";}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_relational_operator(self):
        input = """main: function void () {
            5 > 2;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_index_operator(self):
        input = """main: function void () {
            abc[1, 2, 3, 5 + 4];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    # Test statement
    def test_assignment_statement(self):
        input = """main: function void () {
            a = 10 + 20 * 30;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    
    def test_assignment_statement2(self):
        input = """main: function void () {
            a[1,2] = 10;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_if_statement(self):
        input = """
            main: function void () {
                if (true) {a = 10 + 20 * 30;}
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_if_statement2(self):
        input = """main: function void () {
            if (1 == 2) {a = 10 + 20 * 30;} else a = 10; c = 20;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_for_statement(self):
        input = """main: function void () {
            for (i = 1, i < 10, i + 1) {a = 10;}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_for_statement2(self):
        input = """main: function void () {
            for (i = 1, i < 10,) {a = 10;}
            }"""
        expect = "Error on line 2 col 31: )"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_while_statement(self):
        input = """main: function void () {
            while (true) a = 10;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_while_statement2(self):
        input = """main: function void () {
            while(1) a = 20;
            }"""
        expect = "Error on line 2 col 19: )"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_do_while_statement(self):
        input = """main: function void () {
            do
            {
                a = 10;
                a = 20;
            }
            while(true);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_do_while_statement2(self):
        input = """main: function void () {
            do
            {
                a = 10;
                a = 30;
            }
            while(true);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_break_statement(self):
        input = """main: function void () {
            break;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_break_statement2(self):
        input = """main: function void () {
            break a + 1;
            }"""
        expect = "Error on line 2 col 18: a"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_continue_statement(self):
        input = """main: function void () {
            continue;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_continue_statement2(self):
        input = """main: function void () {
            continue a + 1;
            }"""
        expect = "Error on line 2 col 21: a"
        self.assertTrue(TestParser.test(input, expect, 235))

    # Test functions
    def test_read_integer(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_print_integer(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    
    # Random test
    def test_random1(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_random2(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_random3(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_random4(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_random5(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_random6(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_random7(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_random8(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_random9(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_random10(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_random11(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_random12(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_random13(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_random14(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_random15(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_random16(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_random17(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_random18(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_random19(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_random20(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_random21(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_random22(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_random23(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_random24(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_random25(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_random26(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_random27(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_random28(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_random29(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_random30(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_random31(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_random32(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_random33(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_random34(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_random35(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_random36(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_random37(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_random38(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_random39(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_random40(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_random41(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_random42(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_random43(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_random44(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_random45(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_random46(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_random47(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_random48(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_random49(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_random50(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_random51(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_random52(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_random53(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_random54(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_random55(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_random56(self):
        input = """main: function void () {
            readinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_random57(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_random58(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_random59(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_random60(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_random61(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_random62(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_random63(self):
        input = """main: function void () {
            printinteger();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
