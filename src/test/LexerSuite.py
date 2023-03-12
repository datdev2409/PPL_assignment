import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test1(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    def test2(self):
        self.assertTrue(TestLexer.test("zavc123", "zavc123,<EOF>", 102))

    def test3(self):
        self.assertTrue(TestLexer.test("A1", "A1,<EOF>", 103))
    def test4(self):
        self.assertTrue(TestLexer.test("CDA", "CDA,<EOF>", 104))

    """Check mix ID"""
    def test5(self):
        self.assertTrue(TestLexer.test("df8U", "df8U,<EOF>", 105))
    def test6(self):
        self.assertTrue(TestLexer.test("alohaH", "alohaH,<EOF>", 106))
    def test7(self):
        self.assertTrue(TestLexer.test("nata", "nata,<EOF>", 107))
    def test8(self):
        self.assertTrue(TestLexer.test("0A4", "0,A4,<EOF>", 108))

    def test9(self):
        self.assertTrue(TestLexer.test("_nato", "_nato,<EOF>", 109))
    def test10(self):
        self.assertTrue(TestLexer.test("_zaU", "_zaU,<EOF>", 110))
    def test11(self):
        self.assertTrue(TestLexer.test("Narora", "Narora,<EOF>", 111))
    def test12(self):
        self.assertTrue(TestLexer.test("12ab34_", "12,ab34_,<EOF>", 112))
    def test13(self):
        self.assertTrue(TestLexer.test("dfas_abc", "dfas_abc,<EOF>", 113))
    def test14(self):
        self.assertTrue(TestLexer.test("_9_Z_123", "_9_Z_123,<EOF>", 114))
    def test15(self):
        self.assertTrue(TestLexer.test("noto", "noto,<EOF>", 115))
    def test16(self):
        self.assertTrue(TestLexer.test("#kefjske", "Error Token #", 116))
    def test17(self):
        self.assertTrue(TestLexer.test("@kjsdf", "Error Token @", 117))
    def test18(self):
        self.assertTrue(TestLexer.test("__123", "__123,<EOF>", 118))

    def test19(self):
        self.assertTrue(TestLexer.test("1234", "1234,<EOF>", 119))
    def test20(self):
        self.assertTrue(TestLexer.test("567", "567,<EOF>", 120))
    def test21(self):
        self.assertTrue(TestLexer.test("1_2", "12,<EOF>", 121))
    def test22(self):
        self.assertTrue(TestLexer.test("22_", "22,_,<EOF>", 122))
    def test23(self):
        self.assertTrue(TestLexer.test("1_3", "13,<EOF>", 123))

    def test24(self):
        self.assertTrue(TestLexer.test("12_2.e-3", "122.e-3,<EOF>", 124))
    def test25(self):
        self.assertTrue(TestLexer.test("122_12.12e+3", "12212.12e+3,<EOF>", 125))
    def test26(self):
        self.assertTrue(TestLexer.test("_1234.e124", "_1234,.e124,<EOF>", 126))
   
    def test27(self):
        self.assertTrue(TestLexer.test("124.0000001", "124.0000001,<EOF>", 127))
    def test28(self):
        self.assertTrue(TestLexer.test("0000000.000000", "0,0,0,0,0,0,0.000000,<EOF>", 128))
    def test29(self):
        self.assertTrue(TestLexer.test("1_124.123", "1124.123,<EOF>", 129))
    def test30(self):
        self.assertTrue(TestLexer.test("1_1_2.", "112.,<EOF>", 130))
    
    def test31(self):
        self.assertTrue(TestLexer.test("124e3", "124e3,<EOF>", 131))
    def test32(self):
        self.assertTrue(TestLexer.test("123_2e-000000", "1232e-000000,<EOF>", 132))
    def test33(self):
        self.assertTrue(TestLexer.test("1_2_4e12_32", "124e12,_32,<EOF>", 133))
    def test34(self):
        self.assertTrue(TestLexer.test("123e+3", "123e+3,<EOF>", 134))

    def test35(self):
        self.assertTrue(TestLexer.test(".e3", ".e3,<EOF>", 135))
    def test36(self):
        self.assertTrue(TestLexer.test(".0000e-0", ".0000e-0,<EOF>", 136))
    def test37(self):
        self.assertTrue(TestLexer.test(".112e+3", ".112e+3,<EOF>", 137))
    def test38(self):
        self.assertTrue(TestLexer.test(".1e+3_3", ".1e+3,_3,<EOF>", 138))

    def test39(self):
        self.assertTrue(TestLexer.test("\" ato? \"", " ato? ,<EOF>", 139))
    def test40(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\"", "This is a string containing tab \\t,<EOF>", 140))
    def test41(self):
        self.assertTrue(TestLexer.test("\"Hi, My name \\b is \\n John\"", "Hi, My name \\b is \\n John,<EOF>", 141))
    def test42(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\" Where is John? \\\"\" ", "He asked me: \\\" Where is John? \\\",<EOF>", 142))
    def test43(self):
        self.assertTrue(TestLexer.test("\"This \\' is a \\' sentence\"", "This \\' is a \\' sentence,<EOF>", 143))
    def test44(self):
        self.assertTrue(TestLexer.test("\"How \\\\ are \\r you?\"", "How \\\\ are \\r you?,<EOF>", 144))
    def test45(self):
        self.assertTrue(TestLexer.test("\"I will \\f be there \\b for you\"", "I will \\f be there \\b for you,<EOF>", 145))
    def test46(self):
        self.assertTrue(TestLexer.test("\"Now \\b \\f I \\'m \\r \\n \\t \\\' \\\\ here\" ", "Now \\b \\f I \\'m \\r \\n \\t \\\' \\\\ here,<EOF>", 146))
    def test47(self):
        self.assertTrue(TestLexer.test("\"This is \\t \\b \\f the end.\"", "This is \\t \\b \\f the end.,<EOF>", 147))
    def test48(self):
        self.assertTrue(TestLexer.test("\"Hello, what \\'are\\' you doing ?\"", "Hello, what \\'are\\' you doing ?,<EOF>", 148))
        
    """Check unclosed string"""
    def test49(self):
        self.assertTrue(TestLexer.test("\" What are you doing?", "Unclosed String:  What are you doing?", 149))
    def test50(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t", "Unclosed String: This is a string containing tab \\t", 150))
    def test51(self):
        self.assertTrue(TestLexer.test("\"Hi, My name \\b is \\n John", "Unclosed String: Hi, My name \\b is \\n John", 151))
    def test52(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\" Where is John? \\\"", "Unclosed String: He asked me: \\\" Where is John? \\\"", 152))
    def test53(self):
        self.assertTrue(TestLexer.test("\"This \\' is a \\' sentence", "Unclosed String: This \\' is a \\' sentence", 153))

    """Check illegal string"""
    def test54(self):
        self.assertTrue(TestLexer.test("\" What are you doing? \\a", "Illegal Escape In String:  What are you doing? \\a", 154))
    def test55(self):
        self.assertTrue(TestLexer.test("\"This is a string \\h containing tab \\t", "Illegal Escape In String: This is a string \\h", 155))
    def test56(self):
        self.assertTrue(TestLexer.test("\"Hi, My name \\b \\w is \\n John", "Illegal Escape In String: Hi, My name \\b \\w", 156))
    def test57(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\" \\c Where is John? \\\"", "Illegal Escape In String: He asked me: \\\" \\c", 157))
    def test58(self):
        self.assertTrue(TestLexer.test("\"This \\' is a \\' \\m sentence", "Illegal Escape In String: This \\' is a \\' \\m", 158))

    "Check boolean literal"
    def test59(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 159))
    def test60(self):
        self.assertTrue(TestLexer.test("false true", "false,true,<EOF>", 160))

    "Check operator"
    def test61(self):
        self.assertTrue(TestLexer.test("==-==", "==,-,==,<EOF>", 161))
    def test62(self):
        self.assertTrue(TestLexer.test("123+321", "123,+,321,<EOF>", 162))
    def test63(self):
        self.assertTrue(TestLexer.test("[1+3,1,abc]", "[,1,+,3,,,1,,,abc,],<EOF>", 163))
    def test64(self):
        self.assertTrue(TestLexer.test("1!=2", "1,!=,2,<EOF>", 164))
    def test65(self):
        self.assertTrue(TestLexer.test("123&&333 123%1", "123,&&,333,123,%,1,<EOF>", 165))
    def test66(self):
        self.assertTrue(TestLexer.test("-3-4-1-5", "-,3,-,4,-,1,-,5,<EOF>", 166))
    def test67(self):
        self.assertTrue(TestLexer.test("abc<=abc", "abc,<=,abc,<EOF>", 167))
    def test68(self):
        self.assertTrue(TestLexer.test("===", "==,=,<EOF>", 168))
    def test69(self):
        self.assertTrue(TestLexer.test("abc::::abc", "abc,::,::,abc,<EOF>", 169))
    def test70(self):
        self.assertTrue(TestLexer.test("====", "==,==,<EOF>", 170))

    """Check keywords && seperator"""
    def test71(self):
        self.assertTrue(TestLexer.test("auto break boolean do else false float", "auto,break,boolean,do,else,false,float,<EOF>", 171))
    def test72(self):
        self.assertTrue(TestLexer.test("for function if integer return string true", "for,function,if,integer,return,string,true,<EOF>", 172))
    def test73(self):
        self.assertTrue(TestLexer.test("while void out continue of inherit array", "while,void,out,continue,of,inherit,array,<EOF>", 173))
    def test74(self):
        self.assertTrue(TestLexer.test("+-*/%!&&||==!=<<=>>=::", "+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>", 174))
    def test75(self):
        self.assertTrue(TestLexer.test("()[].,;:{}=", "(,),[,],.,,,;,:,{,},=,<EOF>", 175))

    """Check complex"""
    def test76(self):
        self.assertTrue(TestLexer.test("a: integer;", "a,:,integer,;,<EOF>", 176))
    def test77(self):
        self.assertTrue(TestLexer.test("""{
            r = r * a[0];
            b,c: array [4] of string;
        }""", "{,r,=,r,*,a,[,0,],;,b,,,c,:,array,[,4,],of,string,;,},<EOF>", 177))
    def test78(self):
        self.assertTrue(TestLexer.test("foo(3);", "foo,(,3,),;,<EOF>", 178))
    def test79(self):
        self.assertTrue(TestLexer.test("""{
            abc = a[0,1,2];
            return true;
        }""", "{,abc,=,a,[,0,,,1,,,2,],;,return,true,;,},<EOF>", 179))
    def test80(self):
        self.assertTrue(TestLexer.test("if a!=b a=b; ", "if,a,!=,b,a,=,b,;,<EOF>", 180))
    def test81(self):
        self.assertTrue(TestLexer.test("""{
            for (a=1,a<0,a=a+1) 
                b=b+1;
        }""", "{,for,(,a,=,1,,,a,<,0,,,a,=,a,+,1,),b,=,b,+,1,;,},<EOF>", 181))
    def test82(self):
        self.assertTrue(TestLexer.test("a,b,c,d: integer = 2,3,4,5;", "a,,,b,,,c,,,d,:,integer,=,2,,,3,,,4,,,5,;,<EOF>", 182))
    def test83(self):
        self.assertTrue(TestLexer.test("""{
            main: function void() {}
        }""", "{,main,:,function,void,(,),{,},},<EOF>", 183))
    def test84(self):
        self.assertTrue(TestLexer.test("do {} while a=b;", "do,{,},while,a,=,b,;,<EOF>", 184))
    def test85(self):
        self.assertTrue(TestLexer.test("""
            foo: function void(a : integer, out x:float) inherit bar {}
        """, "foo,:,function,void,(,a,:,integer,,,out,x,:,float,),inherit,bar,{,},<EOF>", 185))
    
    def test86(self):
        self.assertTrue(TestLexer.test("1..1..1..1", "1.,.,1.,.,1.,.,1,<EOF>", 186))
    def test87(self):
        self.assertTrue(TestLexer.test("1a___1___a1", "1,a___1___a1,<EOF>", 187))
    def test88(self):
        self.assertTrue(TestLexer.test("{1_32,2_12,3_12,4_1,5_4}", "{1_32,2_12,3_12,4_1,5_4},<EOF>", 188))
    def test89(self):
        self.assertTrue(TestLexer.test("""{
            r, s: int;
            r = 2.0;
            a, b: array [5] of int;
            s = r * r * myPI;
            a[0] = s;
            }
        """, "{,r,,,s,:,int,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>", 189))
    def test90(self):
        self.assertTrue(TestLexer.test("_____________", "_____________,<EOF>", 190))

    """Test comment"""
    def test91(self):
        self.assertTrue(TestLexer.test("// hello world", "<EOF>", 191))
    def test92(self):
        self.assertTrue(TestLexer.test("// ancnnnnn a \n anc", "anc,<EOF>", 192))
    def test93(self):
        self.assertTrue(TestLexer.test("// THIS IS A \t \b \z COMMENT", "<EOF>", 193))
    def test94(self):
        self.assertTrue(TestLexer.test("// This \t is \b a \w beautiful \w moment", "<EOF>", 194))
    def test95(self):
        self.assertTrue(TestLexer.test("// This // is // a // beautiful // moment", "<EOF>", 195))
    
    def test96(self):
        self.assertTrue(TestLexer.test("/* This is a comment */", "<EOF>", 196))
    def test97(self):
        self.assertTrue(TestLexer.test("""
         /* hellllooo
                holllloo
                    hellllloooo
                                */
        """, "<EOF>", 197))
    def test98(self):
        self.assertTrue(TestLexer.test("""
            /* /* \t \a \b \a \f \t */
        """, "<EOF>", 198))
    def test99(self):
        self.assertTrue(TestLexer.test(""" /* /*
            Just a small test for assignment
        */ */
        """, "*,/,<EOF>", 199))
    def test100(self):
        self.assertTrue(TestLexer.test("""
            /* \\This is a comment */
        """, "<EOF>", 200))

    

