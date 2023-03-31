# import unittest
# from TestUtils import TestParser


# class ParserSuite(unittest.TestCase):
#     """Test program structure"""
#     def test_program_structure1(self):
#         input = """"""
#         expect = """Error on line 1 col 0: <EOF>"""
#         self.assertTrue(TestParser.test(input, expect, 201))

#     def test_program_structure2(self):
#         input = """a : integer;"""
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 202))

#     def test_program_structure3(self):
#         input = """a,b : float;
#                 main: function void() {}
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 203))

#     def test_program_structure4(self):
#         input = """main: function void(){} 
#             foo: function string(){}
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 204))

#     def test_program_structure5(self):
#         input = """foo: function auto() {}
#             a : integer;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 205))

#     def test_program_structure6(self):
#         input = """bar: function void() {}
#             if (a==b) 
#                 print(a);
#         """
#         expect = """Error on line 2 col 12: if"""
#         self.assertTrue(TestParser.test(input, expect, 206))

#     def test_program_structure7(self):
#         input = """
#             b : boolean = true;
#             c = b;
#         """
#         expect = """Error on line 3 col 14: ="""
#         self.assertTrue(TestParser.test(input, expect, 207))

#     def test_program_structure8(self):
#         input = """
#             break: function void() {}
#         """
#         expect = """Error on line 2 col 12: break"""
#         self.assertTrue(TestParser.test(input, expect, 208))

#     def test_program_structure9(self):
#         input = """
#             continue: integer = 2;
#         """
#         expect = """Error on line 2 col 12: continue"""
#         self.assertTrue(TestParser.test(input, expect, 209))

#     def test_program_structure10(self):
#         input = """
#             while = hello;
#         """
#         expect = """Error on line 2 col 12: while"""
#         self.assertTrue(TestParser.test(input, expect, 210))


#     """Test variable declaration"""
#     def test_variable_decleration1(self):
#         input = """
#             a: integer;
#             b: float;
#             c,d: auto;
#             f: boolean;
#             e,g,h: boolean;
#             i,j: array[3,4,5] of void;            
#         """
#         expect = """Error on line 7 col 33: void"""
#         self.assertTrue(TestParser.test(input, expect, 211))

#     def test_variable_decleration2(self):
#         input = """
#             a : integer = 3;
#             b,c : float = a+1,5;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 212))

#     def test_variable_decleration3(self):
#         input = """
#             a: auto = 3;
#             b,c,d: integer = 1,2;
#         """
#         expect = """Error on line 3 col 32: ;"""
#         self.assertTrue(TestParser.test(input, expect, 213))

#     def test_variable_decleration4(self):
#         input = """
#             a,b,c,d: float = 1+2,3,4,5,7+8;
#         """
#         expect = """Error on line 2 col 38: ,"""
#         self.assertTrue(TestParser.test(input, expect, 214))

#     def test_variable_decleration5(self):
#         input = """
#             a,b : array[5] of integer = {1,2,3},{2,3,4};
#             c: float = 2.2;
#             d: boolean = true;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 215))

#     """Test function declaration"""
#     def test_function_decleration1(self):
#         input = """
#             foo: function auto()           
#         """
#         expect = """Error on line 3 col 8: <EOF>"""
#         self.assertTrue(TestParser.test(input, expect, 216))

#     def test_function_decleration2(self):
#         input = """
#             main: function array[5] of string () {}
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 217))

#     def test_function_decleration3(self):
#         input = """
#             foo: function float (n : integer, inherit out a,b,c: float) {}
#         """
#         expect = """Error on line 2 col 59: ,"""
#         self.assertTrue(TestParser.test(input, expect, 218))

#     def test_function_decleration4(self):
#         input = """
#             main: function boolean (n: auto, b: integer, a: float) inherit foo {}
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 219))

#     def test_function_decleration5(self):
#         input = """
#             foo: function string (a: string, b: float) {}
#             main: function auto (a: void, b: float) {}
#         """
#         expect = """Error on line 3 col 36: void"""
#         self.assertTrue(TestParser.test(input, expect, 220))
    
#     """Test array index"""
#     def test_array_index1(self):
#         input = """
#             a : array [5] of string = {1,2,3};       
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 221))

#     def test_array_index2(self):
#         input = """
#             a : array [10] of float = {{1,2,4},{1,2,4},{1,2,4}};
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 222))

#     def test_array_index3(self):
#         input = """
#             a,b : array [2] of string = {},{};
#             main: function void ()
#             {
#                 return a[{1,2,3},2,3,4];
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 223))

#     def test_array_index4(self):
#         input = """
#             main: function void() {
#                 return a[1];
#                 return {1,2,3};
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 224))

#     def test_array_index5(self):
#         input = """
#             main: function void() {
#                 return a[id+1,a,c,true+false];
#                 return {1,2,3};
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 225))

#     """Test operator"""
#     def test_operator1(self):
#         input = """
#             a: integer = a::b;       
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 226))

#     def test_operator2(self):
#         input = """
#             a: boolean = True && False && True || False :: e;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 227))

#     def test_operator3(self):
#         input = """
#             a,b : string = 1+2+3*4+5+6,!True;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 228))

#     def test_operator4(self):
#         input = """
#             a: integer = a!=b + !2 + -2;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 229))

#     def test_operator5(self):
#         input = """
#                 b: integer = 2 || 2 + 3 / 3 + a[2] + c && d;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 230))

#     def test_operator6(self):
#         input = """
#             c : float = id + a[1,2,3,4] + -2 + -4 + !true + !false;    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 231))

#     def test_operator7(self):
#         input = """
#             a: string = !id > 3 + 2 / 5 <= 6; 
#         """
#         expect = """Error on line 2 col 40: <="""
#         self.assertTrue(TestParser.test(input, expect, 232))

#     def test_operator8(self):
#         input = """
#             a,b : string = 1+2+3*4+5+6,!True;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 233))

#     def test_operator9(self):
#         input = """
#             a: integer = a!=b + !2 + -2;
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 234))

#     def test_operator10(self):
#         input = """
#                 b: integer = !-2 + 3 + 3 <= >= 3;
#         """
#         expect = """Error on line 2 col 44: >="""
#         self.assertTrue(TestParser.test(input, expect, 235))

#     """Test statement"""
#     """Test assignment statement"""
#     def test_assign_stmt1(self):
#         input = """
#             main: function void() {
#                 a = 2,3,4;
#             }      
#         """
#         expect = """Error on line 3 col 21: ,"""
#         self.assertTrue(TestParser.test(input, expect, 236))

#     def test_assign_stmt2(self):
#         input = """
#             main: function void() {
#                 a = b + c - d - a[1,2,3];
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 237))

#     def test_assign_stmt3(self):
#         input = """
#             main: function void() {
#                 a = 2+4;
#                 b = "anc"+ "cfg" +5;
#                 c = 2.3;
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 238))

#     def test_assign_stmt4(self):
#         input = """
#             a : integer = 2;
#             main: function void() {
#                 if (a==1)
#                     a = a + 1;
#             }  
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 239))

#     def test_assign_stmt5(self):
#         input = """
#             foo : function integer() {}
#             main: function void() {
#                 a = foo();
#                 b = foo();
#                 a = b = foo();
#             }       
#         """
#         expect = """Error on line 6 col 22: ="""
#         self.assertTrue(TestParser.test(input, expect, 240))

#     def test_assign_stmt6(self):
#         input = """
#             main: function void() {
#                 a = b = c = 5;
#             }      
#         """
#         expect = """Error on line 3 col 22: ="""
#         self.assertTrue(TestParser.test(input, expect, 241))

#     def test_assign_stmt7(self):
#         input = """
#             main: function void() {
#                 b = a || 2 + 3 + foo(2,3,4,1+2);
#                 c = a_2 + 3 + 111_223;
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 242))

#     def test_assign_stmt8(self):
#         input = """
#             bar: function integer() {
#                 a = x**y + y**x;
#             }    
#         """
#         expect = """Error on line 3 col 22: *"""
#         self.assertTrue(TestParser.test(input, expect, 243))

#     def test_assign_stmt9(self):
#         input = """
#             main: function void() {
#                 do
#                 {
#                     a = a + 1;
#                     b = b + 1;
#                     c = c * 2;
#                     d = a || b && c + !c;
#                 }
#                 while (a==c);
#             }  
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 244))

#     def test_assign_stmt10(self):
#         input = """
#             foo : function integer() {
#                 d = inc(3) + 3;
#                 h = d + 2 + -2 + -3;
#             }       
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 245))

#     """Test if statement"""
#     def test_if_else_stmt1(self):
#         input = """
#             main: function void() {
#                 if (a+c=d)
#                     b = b + c;
#             }      
#         """
#         expect = """Error on line 3 col 23: ="""
#         self.assertTrue(TestParser.test(input, expect, 246))

#     def test_if_else_stmt2(self):
#         input = """
#             main: function void() {
#                 if (a > b > c)
#                     o = c - 1;
#                 else
#                     c = d - f;
#             }    
#         """
#         expect = """Error on line 3 col 26: >"""
#         self.assertTrue(TestParser.test(input, expect, 247))

#     def test_if_else_stmt3(self):
#         input = """
#             main: function void() {
#                 if (a==c)
#                     if (an + ad == cd)
#                         b = c + 1;
#                 else 
#                     c = abc;
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 248))

#     def test_if_else_stmt4(self):
#         input = """
#             a : integer = 2;
#             main: function void() {
#                 if ((a!=1) && (a==f) || (c=d))
#                     a = a + 1;
#             }  
#         """
#         expect = """Error on line 4 col 42: ="""
#         self.assertTrue(TestParser.test(input, expect, 249))

#     def test_if_else_stmt5(self):
#         input = """
#             main: function void() {
#                 if (a==c)
#                     if (c==d)
#                         b=c;
#                 else
#                     if ((f==c) && (g==h) || (c<=d))
#                         d=c;
#                     else
#                         b=c;
#             }       
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 250))

#     """Test for statement"""
#     def test_for_stmt1(self):
#         input = """
#             main: function void() {
#                 for (a = 1, a < 10 + 20, a + 1)
#                 {
                
#                 }
#             }      
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 251))

#     def test_for_stmt2(self):
#         input = """
#             main: function void() {
#                 for (b == 1, b < 10 , b + 1)
#                 {
#                     print(a[i]);
#                 }
#             }    
#         """
#         expect = """Error on line 3 col 23: =="""
#         self.assertTrue(TestParser.test(input, expect, 252))

#     def test_for_stmt3(self):
#         input = """
#             main: function void() {
#                 for (a=1,b<2,c+1)
#                     print(a[i]);
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 253))

#     def test_for_stmt4(self):
#         input = """
#             a : integer = 2;
#             main: function void() {
#                 for (a = 1,b<=20+30,c = c + 1)
#                     print(a[i]);
#             }  
#         """
#         expect = """Error on line 4 col 38: ="""
#         self.assertTrue(TestParser.test(input, expect, 254))

#     def test_for_stmt5(self):
#         input = """
#             main: function void() {
#                 for (c=2,c==3,c+1)
#                 {
                
#                 }
#             }       
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 255))

#     """Test while-do statement"""
#     def test_while_do_stmt1(self):
#         input = """
#             main: function void() {
#                 while ((a==b) && (c<=3));
#             }      
#         """
#         expect = """Error on line 3 col 40: ;"""
#         self.assertTrue(TestParser.test(input, expect, 256))

#     def test_while_do_stmt2(self):
#         input = """
#             main: function void() {
#                 while ((anc) + (cnd) == d)
#                 {
                
#                 }
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 257))

#     def test_while_do_stmt3(self):
#         input = """
#             main: function void() {
#                 while ((anc+nccc) || (aaaa+vc!=c)
#                 {
                
#                 }
#             }    
#         """
#         expect = """Error on line 4 col 16: {"""
#         self.assertTrue(TestParser.test(input, expect, 258))

#     def test_while_do_stmt4(self):
#         input = """
#             a : integer = 2;
#             main: function void() {
#                 while ((a<=c) || (c>=d) || (d==c))
#                     print(a);
#             }  
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 259))

#     def test_while_do_stmt5(self):
#         input = """
#             main: function void() {
#                 while ((a=c) || (d))
#                 {
                
#                 }
#             }       
#         """
#         expect = """Error on line 3 col 25: ="""
#         self.assertTrue(TestParser.test(input, expect, 260))

#     """Test do-while statement"""
#     def test_do_while_stmt1(self):
#         input = """
#             main: function void() {
#                 do
#                 {
                    
#                 }
#                 while (a==c);
#             }      
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 261))

#     def test_do_while_stmt2(self):
#         input = """
#             main: function void() {
#                 do
#                 while (a==c);
#             }    
#         """
#         expect = """Error on line 4 col 16: while"""
#         self.assertTrue(TestParser.test(input, expect, 262))

#     def test_do_while_stmt3(self):
#         input = """
#             main: function void() {
#                 do
#                 {
#                     a = a + 1;
#                     c = c + 1;
#                     return true;
#                 }
#                 while ((a==c) || (c==d));
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 263))

#     def test_do_while_stmt4(self):
#         input = """
#             a : integer = 2;
#             main: function void() {
#                 do
#                     c = c + 1;
#                 while (a==c);
#             }  
#         """
#         expect = """Error on line 5 col 20: c"""
#         self.assertTrue(TestParser.test(input, expect, 264))

#     def test_do_while_stmt5(self):
#         input = """
#             main: function void() {
#                 do
#                 {
#                     print(a[i]);
#                     a: integer = true;
#                     b = c;
#                 }
#                 while ((a==d) || (b>c));
#             }       
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 265))
    
#     """Test other statement"""
#     def test_other_stmt1(self):
#         input = """
#             main: function void() {
#                 return;
#             }      
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 266))

#     def test_other_stmt2(self):
#         input = """
#             main: function void() {
#                 return abc[1,2,3,4,5];
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 267))

#     def test_other_stmt3(self):
#         input = """
#             main: function void() {
#                 break;
#             }    
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 268))

#     def test_other_stmt4(self):
#         input = """
#             a : integer = 2;
#             main: function void() {
#                 break abc;
#             }  
#         """
#         expect = """Error on line 4 col 22: abc"""
#         self.assertTrue(TestParser.test(input, expect, 269))

#     def test_other_stmt5(self):
#         input = """
#             main: function void() {
#                 continue;
#                 continue abc;
#             }       
#         """
#         expect = """Error on line 4 col 25: abc"""
#         self.assertTrue(TestParser.test(input, expect, 270))

#     """Test simple program"""
#     def test_simple_program1(self):
#         input = """
#             foo: function auto() {
#                 a : integer;
#                 b = b + 1;
#                 for (b = 1, b < 3, c + 1)
#                     print(a[i]);
#             }           
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 271))

#     def test_simple_program2(self):
#         input = """
#             main: function array[5] of string () {
#                 if ((a!=b) && (b==c)) 
#                     a=b; 
#             }
#             foo: function float () {
#                 return ; 
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 272))

#     def test_simple_program3(self):
#         input = """
#             foo: function float (n : integer, inherit out a: float) {
#                 return true;
#             }
#             main: function void (out m : float, out a: float) inherit foo {
#                 continue;
#                 return true;
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 273))

#     def test_simple_program4(self):
#         input = """
#             main: function boolean (n: auto, b: integer, a: float) inherit foo {
#                 for (i=1,i<=10,i+1)
#                     print(i);
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 274))

#     def test_simple_program5(self):
#         input = """
#             foo: function string (a: string, b: float) {
#                 do {
#                     print("hello");
#                 }
#                 while (a==b);
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 275))

#     def test_simple_program6(self):
#         input = """
#             foo: function auto() {
#                 break anv;
#             }           
#         """
#         expect = """Error on line 3 col 22: anv"""
#         self.assertTrue(TestParser.test(input, expect, 276))

#     def test_simple_program7(self):
#         input = """
#             main: function array[5] of string () {
#                 if (a!=b) 
#                     a=b; 
#                 else
#                     if (a==b)
#                     {
#                         print(a);
#                         a = a + 1;
#                         b = b % 10;
#                     }
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 277))

#     def test_simple_program8(self):
#         input = """
#             foo: function float (n : integer, inherit out a: float) {
#                 return ;
#             }
#             a : integer = 3;
#             b : float = 2.5;
#             c : string = "anc_ac \\t \\b";
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 278))

#     def test_simple_program9(self):
#         input = """
#             main: function boolean (n: auto, b: integer, a: float) inherit foo {
#                 while (a=b)
#                     print("Hello");
#                 a==c;
#             }
#         """
#         expect = """Error on line 3 col 24: ="""
#         self.assertTrue(TestParser.test(input, expect, 279))

#     def test_simple_program10(self):
#         input = """
#             foo: function string (a: string, b: float) {
#                 foo(2,x+3,foo(3),a[3]);
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 280))

#     def test_simple_program11(self):
#         input = """
#             foo: function string (a: string, b: float) {
#                 c : integer = 2;
#                 d = c + 1;
#                 f : array [5] of string;
#                 f[1] = d + 2.5;
#                 return f[1];
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 281))

#     def test_simple_program12(self):
#         input = """
#             bar: function void (inherit out a: float, inherit out b: string) inherit foo {
#                 for (i = 1, i < 10, i + 1)
#                 {
#                     print(a[i,j,e,f]);
#                 }
#                 if (a[1]==2)
#                     return ;
#                 else
#                     break;
#                 foo(1+2,x+1,true);
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 282))

#     def test_simple_program13(self):
#         input = """
#             inc: function auto(a: integer, b: float)
#             {
#                 a = -1 + -2 + -3;
#                 b = a + a / b + a;
#                 while (a!=0)
#                     a = a - 1;
#                 return a;
#                 do
#                 {
#                     a = b + 1;
#                     d: integer = true;
#                     print("anc dbafd \\t \\f",d);
#                 }
#                 while (a==true);
#             }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 283))

#     def test_simple_program14(self):
#         input = """
#             foo: function void()
#             {
#                 a: integer = 1+2+3;
#                 b: float = 2.e3;
#                 c = !c + -!True;
#                 break;
#             }
#         """
#         expect = """Error on line 6 col 26: !"""
#         self.assertTrue(TestParser.test(input, expect, 284))

#     def test_simple_program15(self):
#         input = """
#             foo: function float(a : integer, b: float)
#             {
#                 if ((a==b) && (c==d)
#                     return true;
#                 else
#                     return false;
#             }
#         """
#         expect = """Error on line 5 col 20: return"""
#         self.assertTrue(TestParser.test(input, expect, 285))

#     """Test complex program"""
#     def test_complex_program1(self):
#         input = """x: integer = 65;
#         fact: function integer (n: integer) {
#             if (n == 0) return 1;
#             else return n * fact(n - 1);
#         }
#         inc: function void(out n: integer, delta: integer) {
#             n = n + delta;
#         }
#         main: function void() {
#             delta: integer = fact(3);
#             inc(x, delta);
#             a : array [0] of string;
#             printInteger(x);
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 286))

#     def test_complex_program2(self):
#         input = """
#         count: function boolean(n: integer)
#         {
#             i: integer;
#             c: integer = 0;
#             for (i=1,i<n,i+1)
#                 if (n%i==0)
#                     c = c + 1;
#             if (c == 2)
#                 return true;
#             else 
#                 return false;
#         }
#         main: function void() {
#             n : integer;
#             print("Input n:");
#             readInt(n);
#             if (count(n) == true)
#                 print("n is prime number");
#             else
#                 print("n is not prime number");
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 287))

#     def test_complex_program3(self):
#         input = """
#         check_palindrom: function boolean(s: string)
#         {
#             i: integer;
#             s1: string = "";
#             for (i=0,i<length(s),i+1)
#                 s1 = s1 + s[i]; 
#             if (s1==s)
#                 return true;
#             else 
#                 return false;
#         }
#         main: function void() {
#             s: string;
#             print("Input s:");
#             readString(s);
#             if (chec_palindrom(s) == true)
#                 print("s is palindrom string");
#             else
#                 print("s not is palindrom string");
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 288))

#     def test_complex_program4(self):
#         input = """
#         inc_x: function void(out x: integer, d: integer) 
#         {
#             x = x + d;
#         }
#         foo: function integer(n: integer)
#         {
#             i: integer;
#             sum: integer = 0;
#             for (i=0,i<n,inc_x(i,1))
#                 inc_x(sum,i);
#             return sum;
#         }
#         main: function void() {
#             n: integer;
#             print("Input n:");
#             readInteger(n);
#             print("The sum is ",foo(n));
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 289))

#     def test_complex_program5(self):
#         input = """
#         count: function boolean(n: integer)
#         {
#             i: integer;
#             c: integer = 0;
#             for (i=1,i<n,i+1)
#                 if (n%i==0)
#                     c = c + 1;
#             if (c == n)
#                 return true;
#             else 
#                 return false;
#         }
#         main: function void() {
#             n : integer;
#             print("Input n:");
#             readInt(n);
#             if (count(n) == true)
#                 print("n is perfect number");
#             else
#                 print("n is not perfect number");
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 290))

#     def test_complex_program6(self):
#         input = """
#         sum: function integer(n: integer)
#         {
#             total,dem : integer = 0,0;
#             do
#             {
#                 total = total + (n%10);
#                 dem = dem + 1;
#                 n = n % 10;
#             }
#             while (n!=0);
#         }
#         main: function void() {
#             n : integer;
#             print("Input n:");
#             readInt(n);
#             print("The sum is", sum(n));
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 291))
    
#     def test_complex_program7(self):
#         input = """
#         fibonacci: function integer(n: integer)
#         {
#             f: array[100] of integer;
#             f[0] = 1;
#             f[1] = 1;
#             i : integer;
#             for (i=2,i<n,i+1)
#                 f[i] = f[i-1] + f[i-2];
#             return f[n-1];
#         }
#         main: function void() {
#             n : integer;
#             print("Input n:");
#             readInt(n);
#             print("The nth fibonacci number is", fibonacci(n));
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 292))
    
#     def test_complex_program8(self):
#         input = """
#         f, a: array[10,10] of integer;
#         sum: function integer(n: integer, m: integer,x: integer, y:integer)
#         {
#             f[0,0] = 0;
#             i,j: integer = 0,0;
#             for (i=0,i<n,i+1)
#                 f[i,0] = 0;
#             for (j=0,j<m,j+1)
#                 f[0,j] = 0;
#             for (i = 1,i < n,i+1)
#                 for (j = 1, j < m,j+1)
#                     f[i,j] = f[i-1,j] + f[i,j-1] - f[i-1,j-1] + a[i-1,j-1];
#             return f[x-1,y-1];
#         }
#         main: function void() {
#             n,m : integer;
#             print("Input n:");
#             readInt(n);
#             print("Input m:");
#             readInt(m);
#             i,j: integer = 0,0;
#             for (i = 0,i < n,i+1)
#                 for (j = 0, j < m,j+1)
#                 {
#                     print("Input a[i,j]:");
#                     readInt(a[i,j]);
#                 }
#             x,y: integer;
#             print("Input x:");
#             readInt(x);
#             print("Input y:");
#             readInt(y);
#             print("The sum from 1,1 to x,y is", sum(n,m,x,y));
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 293))

#     def test_complex_program9(self):
#         input = """
#         s : string;
#         random: function string(n: integer)
#         {
#             i: integer;
#             s = "";
#             for (i = 0,i < n,i+1)
#                 s = s + randomChar();
#             return s;
#         }
#         main: function void() {
#             n : integer;
#             print("Input n:");
#             readInt(n);
#             print("The random string length n is ", random(n));
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 294))

#     def test_complex_program10(self):
#         input = """
#         foo: function boolean(x: integer) inherit bar 
#         {
#             if (x%2==0)
#                 return true;
#             else
#                 return false;
#         }
#         check: function void(n: integer)
#         {
#             i: integer;
#             for (i = 0,i < n,i+1)
#                 if (foo(i) == true)
#                     print(i);
#             return;
#         }
#         main: function void() {
#             n : integer;
#             print("Input n:");
#             readInt(n);
#             print("The even number from 0 to n is ");
#             check(n);
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 295))

#     def test_complex_program11(self):
#         input = """
#         a,b: array[10] of integer;
#         swap: function void(out a: array[10] of integer, out b: array[10] of integer, n: integer)
#         {
#             if (n>10)
#                 return;
#             else
#             {
#                 temp,i : integer;
#                 for (i=0,i<n,i+1)
#                 {
#                     temp=a[i];
#                     a[i]=b[i];
#                     b[i]=temp;
#                 }
#             }
#         }
#         main: function void() {
#             n : integer;
#             print("Input n:");
#             i : integer;
#             for (i=0,i<n,i+1)
#             {
#                 print("Input a[i]");
#                 readInteger(a[i]);
#             }
#             for (i=0,i<n,i+1)
#             {
#                 print("Input b[i]");
#                 readInteger(b[i]);
#             }
#             swap(a,b,n);
#             print("Array a and b after swapping:");
#             for (i=0,i<n,i+1)
#             {
#                 print(a[i]);
#             }
#             for (i=0,i<n,i+1)
#             {
#                 print(b[i]);
#             }
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 296))
    
#     def test_complex_program12(self):
#         input = """
#         freq: function integer(s: string,c:string)
#         {
#             count : integer =0;
#             i : auto;
#             for (i = 0,i<length(s),i+1)
#                 if (s[i]==c)
#                     count = count + 1;
#             return count;
#         }
#         main: function void() {
#             s,c : string;
#             print("Input s:");
#             readString(n);
#             print("Input c:");
#             readString(c);
#             print("The frequency of c in s is", freq(s,c));
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 297))
    
#     def test_complex_program13(self):
#         input = """
#         a: array[10] of integer;
#         find_max: function integer(n: integer)
#         {
#             max : integer = a[0];
#             i: integer = 0;
#             for (i=1,i<n,i+1)
#                 if (max<a[i])
#                     max = a[i];
#             return max;
#         }
#         main: function void() {
#             n: integer;
#             print("Input n:");
#             readInt(n);
#             i: integer = 0;
#             for (i = 0,i < n,i+1)
#             {
#                 print("Input a[i]:");
#                 readInt(a[i]);
#             }
#             print("The max number in arr is", max(n));
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 298))

#     def test_complex_program14(self):
#         input = """
#         foo: function void()
#         {
#             i: integer;
#             a: float = 1;
#             {
#                 c : integer = true;
#                 d,f,g: float = 1.2,3,4;
#                 for (i=0,i<c,i+1)
#                     print(g);
#             }
#         }
#         main: function auto() {
#             n : integer;
#             a_b_c: auto;
#             {
#                 foo();
#                 foo();
#                 hello_foo();
#             }
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 299))

#     def test_complex_program15(self):
#         input = """
#         foo: function boolean(x: integer) inherit bar 
#         {
#             r, s: integer;
#             r = 2.0;
#             a, b: array [5] of integer;
#             s = r * r * myPI;
#             a[0] = s;
#         }
#         main: function void() {
#             r, s: integer;
#             r = 2.0;
#             a, b: array [5] of integer;
#             s = r * r * myPI;
#             a[0] = s;
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 300))
import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """n : function array [ 17 ] of integer    ( ) { }    l3_O  : auto  ;   A , P , CS  : void  = iq   * ! si     && - AD   && WTeZi      != false    * g ( )    + f   * E       :: b ( )    <= ! KX   + wdBYj     || - r       , ! - n     + 0    || - P      == - y   - u    && M   / HI        , ! ! ! Uv      == Tb ( )    - - w   / h       :: - - n     - v   % ! Oviz      != ! Fp   - e     - b   || _L2AG    * C   * Yg         ;   u65 , A  : void  = _   && G    * - i     - - S5   + g      == r ( )      , p5   < E ( )    - - - G1tE         ;   _5JL : function array [ 80_7 ] of string    ( ) inherit o1Kj { RUD8 , Q  : void  = L ( )     :: y   % Kt    == ! R      , q   / z     :: nn   || Wv3       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        input = """Q : function integer   ( u : auto    ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = """Ch : function void  ( ) inherit X { qT , f , E , em3PC  : integer   ;  }    th : function auto  ( ) inherit Es { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        input = """sWxAz : function void  ( ) inherit Up8 { break ;   return l3   * Pv    > ! BORik      ;   Ko , M1ZH  : array [ 0 ] of integer    = ""     :: - Ji    < N     , Z   && O    >= j   % u     :: ! u    <= - r       ;  y  : void  = ""    >= 2       ;  }    PQc  : void  = ! d_    && - Q     - nhUf6Gk8   - Q    * V   + at       :: ! T ( )        ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        input = """CW , ZR  : void  ;   M , y  : string   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        input = """E , a  : array [ 0 ] of boolean    = ! ! h    && ! _      != 1262_5E7      , NxP3   + yg    * K7   || O     % ! l   / uunD         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        input = """v  : array [ 176_342_4_223239_4 , 0 , 1 ] of string    = - { }      != - w   * sKMk3    % ! o         ;   Bq : function void  ( ) inherit e { if ( ! q    > IL   * d      ) break ;     f  : void  ;  continue ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        input = """v , HR3 , lD  : void  = C ( )     :: MJ   % Dvtg   && D    + Ix   || Img        , ! y_ ( )     >= ! sW5   + L     && J     :: g     , - vY   - G    - - U       :: - ! s    - V   && O         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        input = """G  : array [ 6450_0_3 ] of string    ;   JGm , O2  : auto  = ! ! gQ4     || b1   || - qgiet      != bVo   && V    || q   - _tBM     || ! 1       :: Wwxc   || _ ( )     <= N ( )      , ! - Oaih   - D       :: - X1   * frT     * l   * E    + DG   - F1ZR         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        input = """Q : function auto  ( inherit vj : string     ) inherit f { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        input = """r , T  : void  = X0 ( )    * - ! kE      < ! o   || Zh     % - xML   || NZ       :: ""    != 5    / PfM   * dxyD0     * { }        , d    :: - zDOO   + cmcT_    - ooe_   * C         ;   Q : function array [ 49_00 ] of boolean    ( inherit out sdB : float    , out a7 : array [ 0 , 3 ] of string      ) inherit T { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        input = """Eg , x , sE , sp , Mz  : array [ 0 ] of string    ;   kQ : function auto  ( inherit MWg : auto    ) { h  : void  ;  if ( Qy   / D    == l   - EV     :: A   + dH    >= ix     ) return ;     }    LC9q8CbL : function integer   ( ) inherit n { JhZ ( )  ;   }    MyR  : array [ 0 , 0 ] of string    = - _Z   && o     / e_l   / p    - M   * t       :: P   + KK    || RF   - KL     - RG   - kY0    / TH   % I         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        input = """j0 : function array [ 0 , 2 , 6820_8 , 79_89450_004 , 0 ] of boolean    ( H : integer     ) { }    pw  : void  = - q   - y     + ! nv    && A   + OjL      < { }        ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        input = """D78 : function string   ( inherit vSR : array [ 0 ] of boolean      ) { }    Jq  : auto  = s   - p    * - GL     * - PO    * r   || YA8i      != ! RD    - K   + WJR     % ! - W       :: XG ( )    >= ! AFVgo   && lN    || ""         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        input = """sT  : array [ 77_43_0 ] of string    ;   G  : void  ;   i : function auto  ( ) inherit t { }    oCX : function array [ 0 , 0 , 0 ] of boolean    ( out j : void   , out La : array [ 4 , 0 , 91 , 9_3 , 4_6867 , 0 ] of integer     , x : void    ) inherit B { }    w : function auto  ( ) { Ry  : string   = lX   / RKH     :: p9   + V       ;  { continue ;   }   t , f  : boolean   = ! W     :: - nXIc      , L   + nK       ;  }    ksV4 : function auto  ( out rBBsY : auto    ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        input = """s : function auto  ( ) { if ( g   - p    < ! yV      ) break ;   else { }     eJ  : string   ;  Wc , E , UR , sT5 , s , Y  : void  = - F    != Vz   % s     :: ! U    > jQ   / J8Q4Ks      , J   % w    < Z   * M     :: - B5sD      , Z1   + B     :: u   && PX8f0      , ! l     :: ! vqG      , bf   || TZ    == y   - kEe      , ""    <= - p     :: xtS   % Fb    <= Xs ( )       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        input = """pQ : function array [ 0 ] of integer    ( ) inherit u1 { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        input = """D  : string   = ! - V     * ! p    % L   || C      > - ""    / A4q   + NLk         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        input = """G : function auto  ( ) { WZ  : auto  ;  JkrcU0p  : auto  = ASQ9o   || xif    > Ghd   * KRN     :: dnlA ( )    >= _q   * MOvOm       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        input = """M9JI  : string   = ! - eNC     > - BA ( )    && - d_         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        input = """M : function array [ 0 , 0 ] of string    ( inherit l : integer    , Q : string     ) { I , __  : auto  = N   >= vXoM   && Td     :: - O6    != aDK   - UO2v      , d   - Z     :: - p    == HLs   % K       ;  }    u , g , P  : boolean   ;   k  : array [ 0 ] of boolean    = L0   || r5i    / k6   && XtR     % - lu   - K      <= ! - UW8K     && - X   - T       :: ! SZ   - k    / Z   + vNE      == ! ! ftZ   + GfH         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        input = """Ii  : array [ 0 ] of float    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        input = """KR , c , k  : void  ;   YC  : array [ 0 ] of string    ;   T : function array [ 1 , 9_49 ] of string    ( ) inherit u { }    P : function array [ 0 ] of boolean    ( ) { while ( ! v     :: - L508    > ! e      ) { z , j , q , hAV , evw  : integer   ;  qrBRxD , a  : void  ;  }     while ( G   > R   + zfGbW      ) return ;     PJ  : string   ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        input = """w  : array [ 8 ] of integer    = ! Ja   - R     + ! ! CxX      != ! B   && - N       :: ! - Fn     * ! - XT      <= ! c    * nC    % G   / D   - y         ;   D : function void  ( ) inherit P { qk  : array [ 0 ] of string    = - g     :: N ( )    == _   + R       ;  }    Z , R , Y , Nf , W , c , qc , TNA  : auto  ;   t : function string   ( inherit mo : auto   , out w : auto    ) { d , p , DG6 , L  : boolean   ;  { { q , h , Nu , H , Gx , a  : float   ;  }   U  : array [ 0 , 5_0 ] of boolean    ;  return ;   }   rHP ( )  ;   wY , M  : auto  = Y   && t    != ! O8Eqad      , x   || i     :: ""       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        input = """V : function auto  ( ) { hWrG , _igft  : array [ 22 ] of float    = t   / az      , ! GG       ;  h , FFsjwb  : auto  ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        input = """uo : function array [ 0 ] of integer    ( out c : array [ 4 ] of float     , k : array [ 177 , 0 , 85_6_6 ] of float      ) { W , VV5Gl  : array [ 0 , 0 ] of float    ;  if ( iT   / r     :: j   * r3LqQ    != - _N4      ) return ;   else break ;     }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        input = """Dk , DM , qn , wLB5 , Mzq  : auto  = N   - i    && c   * fZ     + ! T0    || CYlIe       , lZBs   - H   + h     + - I    || M   + d17      > - - T     && ""    % SAxR   * v        , ! ! AN     + - ad   - l       :: ""    && W   + a_    + _s ( )        , m   - DFy    + a   % n     - ! qNC ( )        , - c     :: - ZEu8U    - s   && gg     || Fh   / i    % - t3b         ;   y : function auto  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        input = """q4 , y , F , R , sPl0 , E  : void  ;   B : function auto  ( ) inherit G { a , kQIU  : boolean   ;  ZYD , AaXmG , K , S , cR  : boolean   = ! NtL      , PQY   && GDG    >= M   * Vw3s      , Q ( )      , ! kp      , T   * y       ;  i  : array [ 0 ] of string    ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        input = """v : function void  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        input = """y0CN : function auto  ( ) { }    C : function void  ( ) { { }   m  : auto  = kOD8Ydp   / B    < W   * n       ;  ZSlS9  = ! J     :: - H2o    > y   || P      ;   k6c  : auto  ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        input = """K : function void  ( ) { tb  : array [ 0 , 7_08_8 , 8 ] of float    = Z0 ( )       ;  b  : array [ 0 ] of string    = Q   * APs     :: ee   && u       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        input = """T  : array [ 9 ] of boolean    = mh ( )    * A   * jXU5     * ! OrE   % j      > Z   * ec    || fT6   / l5     / QI   && Of    - - iST         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        input = """_  : void  ;   o , Ka , dT , u  : integer   = - ! z      :: - - ! XY      < j   * Yt43    + Pi4k7L   - ZF     || ! GfI       , I   != i ( )     :: - ! P     && - l   % yzjqS      <= - t   % y    / Jw   + s        , ! l    && true       , ! - ! Z       :: t ( )    && - O   + ALO      >= - ! i   / o         ;   l : function array [ 88 ] of float    ( ) inherit o { }    S , sI , Po  : array [ 0 ] of string    ;   o , fUR , O  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        input = """g , Z , fWv , Gg , cBWk1OVu  : void  ;   _b  : void  = NmeC   >= - ! L   % o       :: ! ! _    + ! f      == ! - s    || l4   - sWw         ;   LYy1YXF9h  : string   ;   JK : function void  ( ) { continue ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        input = """CL , E , Ts , y , pD , ZN , Qa4r  : auto  ;   H : function integer   ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        input = """S5D  : array [ 2 ] of float    ;   S : function float   ( inherit a : boolean     ) { g , e , b  : auto  ;  }    vb  : string   ;   OaW : function auto  ( out t : array [ 0 ] of boolean      ) inherit K { xn , R  : float   = _j ( )     :: - sE      , - u       ;  KF  : void  ;  hM , o , Cx , OMA3  : auto  ;  }    M , m_ , M  : string   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = """t , F  : void  = - p ( )     - ! s   || F        , ! gL ( )      :: - - NTtVz    || BY   || F      <= ! ! LS   && l         ;   I : function void  ( ) { kb  : integer   = b9ev   - CXW     :: A7L   / k    != - H       ;  A , Z , s  : array [ 0 ] of integer    = ZI   % E     :: Ak   && X      , - U     :: ! Hv    <= q0   - P      , qm   + C     :: GoZS4x   + n       ;  J , EF , g  : auto  ;  p  : float   ;  if ( h ( )     :: O   || P      ) XO ( )  ;   else { }     for ( X  = 1     :: WTWKZ   - J      , H   * TIx     :: x   || mF      , PqL8   % XZa    == ! n     :: WT   && RS    >= a     ) continue ;     }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_238(self):
        input = """K : function auto  ( r : auto   , inherit out bY : auto    ) inherit k { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        input = """A9 , Yf , p , TLt6B , Mc  : void  = - - S    - C   * Eqau        , - j   || T     && - w    + oEr   % f      >= D   && An    - v   + o5     % I   - agvHo   % gv        , false      , ! ! x   % i       :: w   - V    + GT   % p     - - Ogo   / xKG      <= ! g   / _    - J   / i0        , Ys    :: ! la3fJq    + - D     || ! JjR   && tH      > ! p4sZ    && x8   && C     + ! bj ( )         ;   s_ : function void  ( out N_ : void    ) inherit K { return ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        input = """Liim5uQ  : array [ 150_8_34_7_96 ] of string    = S ( )    == ! aS   + Oz3S     / ! MW ( )         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """A : function integer   ( out n : array [ 0 ] of integer     , inherit out B : array [ 7_3405_3923_4_8_6 ] of string      ) inherit N { Q , zm7S , W  : void  = - j      , ""      , llY   / fi       ;  B , X  : auto  ;  }    G , IP81 , FPOZvjAmD , KD2Ytzwh5  : auto  ;   YZ , v  : array [ 16_61_5 ] of float    = - TkB    % r    || - - YM        , ! - ! K         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_242(self):
        input = """kKa : function auto  ( inherit d : string    , e : array [ 0 , 1_2 , 740799_0_41_6 , 3 , 0 ] of string      ) inherit qrLw { break ;   continue ;   for ( yYM63P  = e ( )     :: ! SDX      , q ( )     :: - zepd8z    != - uHrSx      , Hl   + w     :: ! h    < QF1k   - m      ) continue ;     break ;   vpzL  : array [ 106_2_6 , 0 ] of boolean    ;  O ( )  ;   bkSHz  : string   = N   && V       ;  continue ;   }    g , uc , j  : array [ 6_06593 ] of integer    = - - g8vwX18    + - O        , - E    + C   / IG     || j1tmLTZQ   + W    - FiM   && TJD        , ! - ! Icv      != ! - ! Bh_         ;   H : function auto  ( inherit EYuTd : string     ) inherit Rj { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_243(self):
        input = """u0a , Bm , U  : array [ 54 ] of integer    = "ⶨ꣎"    + ! Lql    + X   + kB        , - ! T   || so        , ! - ! Yx      >= ! kQ   - U    * DcM   - I2tU         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_244(self):
        input = """OpMDq  : auto  = - O   || Gp5d    && o     > { }        ;   t , zg8  : array [ 0 ] of string    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_245(self):
        input = """o , Z  : float   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_246(self):
        input = """s : function array [ 0 ] of boolean    ( ) inherit R { }    ND  : auto  ;   bRe : function auto  ( t : void   , _gn : array [ 6_2 , 0 ] of boolean     , inherit out i : array [ 4_23001 ] of boolean      ) inherit Web { }    _ : function boolean   ( ) inherit r { }    M , f , V , Fq  : auto  ;   We : function string   ( inherit a : integer    , inherit ziYgP8 : array [ 8_3 , 71_5 , 0 ] of integer      ) { }    mW , n , mr  : array [ 7 , 0 ] of string    = - - pM     * p     :: ! - ! EV      > E     , B ( )    < ! - n     + g   - IQJz    * - jSU       :: - - em_nzLQ    + A ( )        , ! iW   / ka     || ! gZ    || w   * C         ;   DTV3 : function array [ 705 ] of integer    ( ) inherit fRi { continue ;   T  : array [ 0 ] of integer    = - d       ;  { Z  : void  ;  continue ;   W , P , K , v , IF , wq  : float   ;  }   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_247(self):
        input = """B : function auto  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_248(self):
        input = """c , ORA6U , Sq  : auto  = { }     && ""    || S2   && WHkE       :: BP   || KnA    % n    || ! - YCj      < - 14       , ! d    - Z   + c     - - ZP   && S      <= 0    + ! ! xAI        , - ! a   * rz      == - ! vI     + ! zU    - U   % ez         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_249(self):
        input = """Q  : array [ 2_04_92_7310_241_274_216_4 , 78073303 , 0 ] of float    = - - t   || v1         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_250(self):
        input = """vT : function void  ( out Cc : integer     ) { }    I : function void  ( inherit QpKEG_f : string     ) { }    AZQY , AR6  : array [ 351_69 , 0 ] of string    = ! CJ    - ! ! I       :: ! 601       , k   % pk   + t    * ! S      < oZ    :: - - mYp    && 5         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_251(self):
        input = """oP  : array [ 6 ] of integer    = e4s ( )     :: ! ! - dF      >= ! Y    + s   || E     * u ( )    - Eh   - r         ;   lxvjy4WY : function void  ( out Q : void   , Q : array [ 44_64_45_98779_9_0_52 ] of integer      ) inherit jg { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_252(self):
        input = """O  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_253(self):
        input = """cBwG : function void  ( ) inherit l { return b   && Y    != ! eW6ki9i      ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_254(self):
        input = """M , pc7  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_255(self):
        input = """o : function void  ( inherit out Y3b : boolean    , inherit out P1n_ : array [ 2455_8387 , 74 ] of boolean     , dS : auto    ) inherit gJ { { }   A ( )  ;   u  : void  = fNzVs   && a       ;  _ , D  : void  ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_256(self):
        input = """EPpe : function void  ( inherit out KG : boolean     ) { { }   do { continue ;   }  while ( z   - xOm     :: g   - r8X    == s   / S      ) ;   }    C  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_257(self):
        input = """F  : float   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_258(self):
        input = """W : function void  ( S : void   , inherit o : array [ 0 , 8780_11 , 38 ] of string     , inherit out R : void   , inherit IHoLtZ : array [ 2 , 0 , 0 , 0 ] of float     , inherit out zKo06Q : void    ) inherit fJyg { GGu3 , UlDK  : string   ;  H  = n   && _    == - CV     :: iAB   - S    < - O3      ;   break ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_259(self):
        input = """N : function array [ 0 ] of boolean    ( inherit o9kL : array [ 0 , 5_10_63 ] of string     , inherit out WKt : auto    ) inherit z { vox  : integer   ;  VaSX , h  : void  = a   % mR     :: ""      , U4   / k    >= I   % _     :: q   / Jl    > T      ;  }    r : function auto  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_260(self):
        input = """F7Yj : function float   ( ) inherit M { uS  : array [ 20_86_3_074 , 0 , 1_6780_8_3 ] of boolean    = HzWC ( )    <= - uhco     :: - k    == YW   - Oj9ON       ;  }    Q  : array [ 0 ] of boolean    ;   Jq , TfDn , C  : boolean   = - ! F    % - PU       :: "\t\b"    >= - - - K        , - ! Li     && N   % b    + UO   * c      != - w   / uMmz     % x   / ! k        , j   - w    && a   * Ao     % - l    * j   || q         ;   n  : array [ 3 , 9472_8 , 9_82_299_74 ] of float    ;   n : function auto  ( ) inherit dSZw { }    W , s , cEWjUU3 , v  : auto  = { }     <= ! ! c   + R        , S   - i9Ns    % - U     || ! f    % ! F      > B ( )      , ! X   * o     + A   + f    && ! J       :: - - J4   % qMUPe        , - i2b   && _7    * M   || e         ;   pK : function float   ( out XUj : string     ) { yU  : float   = E2BC5FEo   - M    <= X   || P       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_261(self):
        input = """W , j , Z , TI , _Au , Az , I  : string   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_262(self):
        input = """e : function void  ( ) { if ( b   + Vxn     :: s ( )    > pr   || CE      ) { x  : void  ;  }     ap9I , f_  : void  = - vMY    != V   - y     :: T   || MbJz      , Y   % QVe    < Tdd2   || r       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_263(self):
        input = """W , C  : array [ 7 , 0 , 0 ] of integer    ;   EC , uhF , CO  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_264(self):
        input = """pN  : auto  = 0    || Fz7   && - H         ;   E  : boolean   = ! - - l      == y   % Ky    % O5    * - s   && nt       :: ! MTs   % KU    + ! Ta         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_265(self):
        input = """etHv1c  : void  ;   Od , K  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_266(self):
        input = """k  : array [ 0 , 0 ] of string    = ! - E   / B      != ! d   / k     * ! _9   + Z         ;   nPU , KI , l , KK  : string   ;   m : function array [ 0 ] of boolean    ( inherit out G : string    , d : void    ) inherit Cu { }    A6sk : function array [ 6_81_31910 , 0 ] of boolean    ( inherit p : array [ 0 ] of float     , B : string    , out P : boolean    , M : void    ) inherit mD { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_267(self):
        input = """dg4  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_268(self):
        input = """a : function auto  ( inherit XQqOZ : void    ) inherit G { }    M4R , H  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_269(self):
        input = """f742i7P  : string   = ! ! T   + ELcj       :: N ( )    + - Uc     + o3tg   || QKk    - ""      >= ! ! - H         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_270(self):
        input = """r : function auto  ( ) { for ( JZ  = ! M      , - iW     :: EZ   < qrJ3NT0H   || DW      , - iYD      ) { }     }    TyT  : float   ;   uo : function array [ 0 , 0 ] of string    ( ) { }    Ls : function void  ( ) { return ;   }    qt  : float   = fNPG   || - Ny     / E ( )     == - Ld   + WnA    % KEN_o   - T4f       :: ! bfMTEdP97 ( )    - ! XSx      > "᤬"       ;   INqkw : function float   ( w : auto    ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_271(self):
        input = """Jt : function array [ 817_5196 , 34 ] of string    ( inherit XU : float    , out Vo : integer    , inherit out a : void    ) { }    OB : function float   ( inherit out gA : array [ 0 ] of boolean     , inherit out M : auto    ) inherit RA { }    QeB : function auto  ( inherit out Z : string     ) inherit A { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_272(self):
        input = """p : function array [ 0 , 0 ] of float    ( xF : void   , inherit r : auto    ) inherit vDBr { }    Wbg , jcs  : void  = - - W_    * MHu   + L       :: xfY   - ! R    % m       , ! ! M8    || nY2H8   && I         ;   r : function integer   ( ) { for ( E  = N ( )     :: v   && i    >= t   + k      , ! Hc     :: N   + n      , t   / VK    <= x   || b     :: - r      ) { }     wIP  : integer   = ! hO     :: 0       ;  R9 , kdg  : array [ 0 , 4 ] of integer    ;  V , hbh , Q0Z  : auto  ;  break ;   mZ2  : auto  ;  }    D : function auto  ( Q : auto   , inherit out M : array [ 0 ] of integer     , v : auto    ) inherit B { continue ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_273(self):
        input = """K : function array [ 5_4 , 6170_2 ] of string    ( ) inherit s { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_274(self):
        input = """VNr83 : function auto  ( _ : integer     ) inherit C9 { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_275(self):
        input = """O , FiwU , c , IE  : boolean   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_276(self):
        input = """Q : function auto  ( ) { E , zC , v , dD , oS  : auto  = - kHS     :: - c      , k   + Y    < - Z      , v ( )     :: - i    != u   && b      , Y   / Ua      , ! j7     :: ""    == S   * D       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_277(self):
        input = """AS , zjD , W , Y , i , G , Km0KNSN  : array [ 0 ] of string    = ! ! wc    - CKs   && Je       :: ! MSC_   || b    * T   % n      <= ! - V     + - i   || tv        , o   + H    * S   + x     + DqO   || Z    && V   + k      >= zFNxJ ( )    % Q01   % Bt     * ! 0       :: ! oO3    - N861   + X4fb9JmzH     - j      , ! ! ! d       :: 1_110_3_5    + - - z        , - - P     / QI   + DqXy    % ""      != ! - - o       :: - a   && s8c     || - V6   / y      < - r    % ! qH     / - ! Ft        , ""     :: ! U   + zy    || uo   * O      <= - rZ3j   || YjB     && Y   / enc   || rJ        , - jIrR   * B     + - D    / c   || ozcKggrq      > ! O   * h    - - u        , - wDDC ( )        ;   AH  : auto  ;   N , W  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_278(self):
        input = """b : function array [ 0 ] of string    ( c : float    , inherit out bx : string     ) inherit G { j , i  : boolean   = EAs   * _K    <= ! P      , ! Ese    > ! WVAsI     :: ! f    <= G   / a       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_279(self):
        input = """oS  : auto  ;   r : function void  ( ) inherit mf { egSl  : void  = I   + V    < - E       ;  }    Uxk : function auto  ( inherit out UKa : auto    ) inherit R { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_280(self):
        input = """BtQ : function auto  ( ) inherit K_ { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_281(self):
        input = """s1 : function array [ 0 ] of integer    ( inherit out u : array [ 0 , 0 ] of float      ) { Z , aw2z  : array [ 9 , 0 , 7_2 , 0 , 0 ] of float    = mQ   / w      , f   + Cd       ;  continue ;   do { { }   }  while ( - jr     :: w   || m      ) ;   }    V5 , vC , um  : string   = - 0     * O   || - eHcl       :: ! - wok   / V      > LrSc   / S    && - S_     % { }        , ! Itz   + Y     - - W    && DZh2   % i        , ! - D     <= ! O    - - w     * z ( )        ;   bh9Tvv : function auto  ( ) inherit pvbl { do { }  while ( - ty     :: ! GwtS      ) ;   yB , Gs , hgYFPb  : float   ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        input = """e , U  : auto  = - GKQ   / I     - - K   && F       :: - - N     || ! K    % M0   - d        , - Hp28    || J   && o     + ! R   - g         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = """Tl7pb , Oe , Z_ , sd , N  : void  = - l   / yIzlTV    / kj   + m5eabJ0E      != - F   % c     || - D   / M       :: - ! ""        , ! ! mL   * a9        , rD   % K9    || ! g     || ! _a      :: kHj   / m    + w   + d1L     && X ( )       , { }       , rQB   * ! DXvm   + L      >= MC   % d    || qXI   * z6c     && 999_84_7        ;   VJ , pI , kA , b7J , s  : auto  = J   / w    && ax   - vwlPw3y     % ! ! k        , u4 ( )      , j4   + x    && Am ( )     / ! Cqbj7y    / n ( )      == - ipceAb     :: - ! I5     || - k_   % Xa        , t ( )    >= Q ( )    || - j    && C   - eWa       :: mY   || l    && ""     || J    >= - ! bFJib     % - - y        , ! - Vg   - V       :: r   + o    && ! q     % L2U2 ( )     > S   || ! - xc         ;   X , fg0 , r2  : array [ 0 ] of float    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = """SBx8R8 : function array [ 3 ] of integer    ( ) inherit aMss { while ( - Y    <= VDDc ( )     :: ABX   / z      ) continue ;     return V5   + r    >= QE   && X     :: tNMn   + b      ;   A  : array [ 58_417_31 ] of string    ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = """A : function void  ( ) inherit AZ { }    A  : boolean   ;   Us , N  : auto  = - ug ( )     == ! V   + F4     % - - G       :: X   / AR    % ! nN4     * 0    - oX ( )      <= ! - fx    - - mI        , - ! j   - npI9Bu       :: - - oW     * ! ! F         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = """Dpqx2 , o5 , mg  : void  ;   oF9Gv  : void  ;   C0eN : function void  ( kB : array [ 0 , 0 , 41 , 6 , 0 , 7_9 , 0 ] of integer     , out nGY : boolean    , inherit uo8B : void    ) inherit n { epcuKu , bIs , t , t  : array [ 0 , 0 ] of integer    ;  Nv  : auto  ;  eD  : array [ 3 ] of boolean    ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = """XY  : void  ;   M4 , RiY  : string   = - OYw ( )     + ! ! Z      <= - n     :: false      , 41    <= w      ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = """zB5MQu , _  : array [ 8 ] of boolean    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = """E  : boolean   = - - poy   && p      >= true    % S   - S    || - KE       :: false    < ! ddDx       ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = """s0 , c , d , E , H  : float   ;   azZeN  : auto  = ! ! vF    && Y   / U      != - ah    - H   * OR     && ! Z    || _0   || d         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = """G : function void  ( ) inherit l24 { }    _ : function integer   ( ) inherit ave { mK ( )  ;   U  : void  ;  G ( )  ;   K , Qprb , y , W  : boolean   ;  }    d  : void  = ! - B   % s         ;   P : function auto  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = """j  : auto  = iubg   < ! - A    / qU   + yk       :: uye ( )    <= ! NK   || Uj    / eepFM   % zr         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = """c  : array [ 24_976_5_8_5583 , 0 , 0 ] of float    = G      ;   XT : function void  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = """ze56 : function void  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = """KL : function array [ 91_2 , 881644_1 , 0 , 0 , 9689 , 0 , 8044_8 ] of boolean    ( ) { w , lx  : auto  ;  }    w , HSg  : string   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = """YR0KzxJ0FR : function void  ( ) inherit Kw { u  : auto  ;  for ( x  = gR ( )      , - j    <= lu   % L     :: - cEi    <= r   + H      , ""    >= - V     :: e   / i      ) { q  : string   ;  y6  : auto  ;  uw , z9 , HOm  : auto  ;  s , fL  : string   ;  }     }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = """A , WLB , j , k  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = """lp3ZuZTX : function void  ( out h : void    ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = """rNc : function void  ( ) inherit TtMP { for ( hBC  = t ( )     :: lnr   + rsO      , - w      , 0    >= p   * P     :: ! W      ) break ;     }    z : function string   ( ) inherit i { while ( 0      ) return ;     AA  : array [ 0 , 0 ] of float    ;  uf  : void  ;  WSv  : array [ 7_07_01_8 , 5 , 3 ] of float    ;  qz_b , ZX  : float   ;  }    S0ff , bj , N2j  : array [ 9_081_90 ] of float    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        input = """LqfUtt : function array [ 48 , 0 , 9_47 ] of integer    ( ) inherit Z { }    g , xI , w  : array [ 8_37_03938_40 ] of string    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))

    def test_301(self):
        input = """H , q , e , xr  : array [ 927_69_03 ] of integer    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 301))

    def test_302(self):
        input = """W : function void  ( ) { n ( )  ;   d  : array [ 31_6_649 , 9 , 7597 , 0 , 0 , 0 , 643_5_981750_280 , 0 , 1 , 6490_8 ] of boolean    ;  while ( i   > G   - D      ) break ;     return F   / tMvk      ;   }    Ji , s , UY  : void  = i ( )    - u_EwBdm   && Yc     || ! A    && - gc      < AJv95L   - ""      :: false      , ! eJ   / er0    % ! L        , - ! nh     % ! P   % k         ;   JR : function void  ( ) inherit M { ka  = ! c     :: - _    >= - X      ;   iR ( )  ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 302))

    def test_303(self):
        input = """we  : void  = - qf   - S    && B   % ExML9       :: ! - SI    || - Wa      == - 9    && ! bj         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 303))

    def test_304(self):
        input = """U : function void  ( ) { }    N  : float   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 304))

    def test_305(self):
        input = """I  : void  ;   R : function void  ( inherit out cit : void    ) { v  : void  ;  while ( SQN2   || bK    < 5      ) continue ;     }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 305))

    def test_306(self):
        input = """z : function void  ( inherit out rwH : auto    ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 306))

    def test_307(self):
        input = """t  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 307))

    def test_308(self):
        input = """Q , Hn , J  : void  ;   QY : function void  ( p : boolean    , LS5n : void   , J : integer     ) inherit aK { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 308))

    def test_309(self):
        input = """s : function float   ( ) { U , W9 , _ , ai  : integer   = XP   + v      , NFL   - PI    <= - zLkI     :: ! pU    == UIAn ( )      , E   * q    == - he      , D1SvZ   - s     :: T ( )       ;  }    VXG  : void  = - TTb2LPP   / W    * nr   / R         ;   uw  : auto  = - - j    + c1   || J         ;   t : function array [ 8 , 0 ] of integer    ( ) { while ( kyD   && e    > i   || t     :: - v      ) Jfy ( )  ;     do { }  while ( l   / Tg     :: - KN    > i   / D      ) ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 309))

    def test_310(self):
        input = """d , B , OAA  : string   = Y   || w    - D   + np     * false     <= ! n    || tF   + iK     * 0    / ! b       :: q ( )    - RU   && d    % U   && Ll03        , - - - O      != ! U ( )    * ! hZ       :: jf9k84 ( )    || - P     || ! ATgDR0   - yy71        , - U   - C     % L     :: ! f ( )    - HWV   * _      < Z ( )       ;   Y : function void  ( ) inherit N5v { }    z : function void  ( ) { }    i_1 , D , u  : array [ 9_64_7 ] of string    = ! - HH    - YJ   && MI      >= l     , Ut   % PJyMf    - GZG   * FD     * - - z5      == I   * VD7Ud   * T6c    + HFX   - gI        , zL   * W    / S_DLn    + ! - k      < ! b   + BW    / ! A4E         ;   MTDU  : array [ 0 ] of float    = - ws   || Xnh    && - MO      >= - P     :: V   - UO    && - l     && N ( )     < oo ( )       ;   rt  : array [ 12_28 , 8_8 ] of boolean    = d   < ku   - _    - vbx   - Bh     - - ! T         ;   B , tHkfA , y , jR1  : void  ;   we , SBYM , PX , CXj2PQt  : void  = h   < - ! P   && WGc       :: - ""       , ! by   && x     - ! i   || N      >= ! - Drg    && J   - W       :: ! qt   % U     - ! t   % nL      == - - z   - k5        , ! n    || mJ   + kapX5     - M   && Atdo01L    && r   || r       :: ! ""       , - - 9      >= ! - _N     / - qf    && - L       :: - ! EpRQ   - Qb         ;   fo : function boolean   ( inherit i : void    ) inherit I { zZE , U  : array [ 2 , 0 ] of boolean    ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 310))

    def test_311(self):
        input = """RK : function auto  ( ) inherit B { c  : array [ 0 ] of integer    = p0cyD   + K     :: c ( )       ;  nn  : auto  ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 311))

    def test_312(self):
        input = """wm  : array [ 585 ] of float    = - QCYwFZO5    || lpD   * Fmh    && f   % yN       :: - mt   && l     - ! D   - M         ;   G  : integer   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 312))

    def test_313(self):
        input = """tjj : function auto  ( ) inherit f { s  : array [ 0 ] of boolean    = j   || b7_     :: - l       ;  }    C : function void  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 313))

    def test_314(self):
        input = """K : function auto  ( ) { }    U : function void  ( ) inherit S { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 314))

    def test_315(self):
        input = """zMp , TM , TMIp , F , Em , z , c , UrDJ  : void  = z   - S    * R   && g     % { }       :: ! N   * s    && ! yv        , 9e9    < ! - I   / Lx        , m   * h    - _2LKIjL   || _     % H   / VL    / u   + Am9      >= ! N    / di4    % E ( )       , 0    == ! ! e     % - XaB7   || Kj        , ! ! c    && ""       :: - 0     && S   - by    - X   - kK      == - L   - i     || ! o   - MU        , - - p     || 0     == t3   / o    && - i     && - B    && E   && u       :: ! ""     / c   % x    || - U      <= AbEx ( )      , - ! K   % xJ      < ! true      :: - - AH    - s   || P        , - Yx   - R     % - 6      > { }      :: ! ! yIe   - D         ;   W9e  : array [ 0 , 6_07 ] of integer    = ! - - E         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 315))

    def test_316(self):
        input = """J  : auto  ;   A : function auto  ( inherit o : auto   , inherit c : array [ 0 ] of string      ) inherit H { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 316))

    def test_317(self):
        input = """P  : void  = - ! M   && U       :: - q   && t    && e   % XS      != ! ! sx   || dO         ;   a_Z , e  : boolean   = ! HU     :: ! - ! X        , ! { }      > _ ( )       ;   ne : function void  ( out h : string     ) { }    VTs : function void  ( ) { }    qwiJ  : auto  = RWGMD ( )    > - D   - Zy    % hL   && e         ;   b33 : function float   ( inherit out Ewot : array [ 0 ] of integer      ) { sB , sy  : auto  = o   * S    == - di      , - wA    < - Y       ;  return ;   o  : void  ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 317))

    def test_318(self):
        input = """o : function auto  ( ) { }    sCFg : function float   ( ) inherit aJf { return q3e8W   + xn     :: - yN9    >= ! P      ;   while ( l   % l      ) break ;     if ( ! wjjJ    == y   && e      ) { }     }    _vEe6  : void  ;   sw  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 318))

    def test_319(self):
        input = """O , PJXzSX , qx , r , Cx1  : array [ 0 , 3_0 ] of integer    = 7369_0615304_9    - ! j   - vRgOJB       :: - false     >= ! - ! MLB        , ! - ! q      < ! - V    * i   * c       :: OQy   % x   + rTa     || s   * t    % v   || jf        , - pHm    < ! ""     + ! X4xJ   + s       :: false    * rreoV6   || q    * - v      >= { }       , - - wCth    + AVz     <= rFhOwB   || C    * C   / UM9Q3     - Y8   || i    % - A       :: - D    < k     , x   + ! oP    * 0       :: ! GB    && cszj   * wVY     / ! _k    / - tRN         ;   Q : function auto  ( ) { n  : boolean   ;  }    e9qL  : auto  = - ! c   * vKZ       :: - ! spNTVjWJ     - ! - hD         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 319))

    def test_320(self):
        input = """ob : function float   ( inherit out U : boolean     ) inherit YN { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 320))

    def test_321(self):
        input = """K : function auto  ( ) inherit sY { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 321))

    def test_322(self):
        input = """R : function string   ( out NQ : float     ) inherit sB { }    h : function boolean   ( v1 : array [ 45 , 1_67 , 1 , 9 , 0 ] of boolean      ) { rBi , U  : auto  ;  l  : boolean   ;  }    iKO , Ja5 , K8 , b , yg , E3  : float   = - ! ! _        , - fLql ( )     || d_P ( )    || - wwnCaw       :: eUR   + AX    - ! T     * R   && E    - - H      < 8    && GVg   * QMZ     + - ! T        , ! ! ""      > QN ( )     :: u   % d    + - uLkKB     || ! m2   - d      >= ! Q2    % - q   - tI5        , ! - W   - Yl        , - p0    - a7NR   + BFM     * - - D      >= ! F2   - bc     && reW   * G1R    || y   / rM4        , - ! t   || La      >= ! ! v     && - 0         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 322))

    def test_323(self):
        input = """Pl8 , M  : float   = ! Wr   / k2e    || zX   + h      <= N4   && z5    - Q   / N0     + ! Ds2      :: - ! v     || - lm       , e ( )     :: - _U    && m   || P     + ! I    || eg   && _g         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 323))

    def test_324(self):
        input = """f : function array [ 7_256 , 62_31 , 4 , 4_25 , 192932_0_4_4 ] of string    ( ) inherit rM { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 324))

    def test_325(self):
        input = """w , _e , tr8 , in , j  : auto  ;   Z , k  : void  = n   <= U     , ! ! IHa    * m   / k      < - ! eQN   % e       :: { }     < ! i   / bxb     - DZ   || E6    % wf   && l         ;   poDt  : void  = M   % E    + z7    / - k    / p8v7z   - KKL      <= TNw    :: - Xei ( )    / - eo         ;   K , to0 , I  : string   ;   GxI : function float   ( p : array [ 0 , 0 , 3 , 8_802_4_2_97_8 , 544 ] of integer     , out o : auto    ) { B , uczLC , zJ_ , ZwD0  : auto  = ! f    <= - p     :: IOT   - uZ      , B   || e    > FAFL_U4YmE7n ( )     :: - T      , ""    != UO     , y5   - xRw       ;  break ;   e  : array [ 0 , 0 ] of integer    ;  }    G : function auto  ( ) inherit QSNW81 { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 325))

    def test_326(self):
        input = """c8 : function auto  ( inherit qQ : string     ) { }    Ze : function string   ( ) { { D3  : float   ;  return ;   }   A  : array [ 0 ] of string    = ""       ;  }    _ , U , Yrr , sY  : auto  ;   lkw : function boolean   ( uDI : array [ 0 , 0 , 5 , 0 , 0 , 2 , 303_05 , 0 , 0 ] of integer     , inherit out QR : array [ 4_8 , 0 , 76_7 , 0 ] of float      ) { g  : array [ 0 ] of integer    = gk ( )       ;  continue ;   kK  : auto  ;  }    FuW : function void  ( inherit w1 : auto    ) { P  : string   ;  eRbKC7 , OY6  : void  = - cz      , omiTSs   * Ye       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 326))

    def test_327(self):
        input = """F : function float   ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 327))

    def test_328(self):
        input = """o : function void  ( ) inherit z { continue ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 328))

    def test_329(self):
        input = """l  : array [ 0 , 0 ] of boolean    = - c   / e    || s   && JuM_q         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 329))

    def test_330(self):
        input = """AI15  : array [ 838_512_1_9234 , 0 ] of float    ;   tn : function void  ( inherit out dla : array [ 0 ] of integer     , inherit out x2 : auto   , inherit Iy : void   , out U : auto   , inherit W : array [ 0 , 6_698 , 0 ] of boolean     , b : array [ 4_82_81_4_890 ] of float      ) { EB_XWsyl  : void  ;  Iyw , bD , Dm8l , k , b , yI , VA , M  : auto  = ocL8   / R     :: ! kSml      , m   - O    != EnT     , P   + Y     :: - f    >= jCy89   % OK      , i4   && OpYqY    != ! oSeOG      , w   - n      , _w   && z      , f   + I1    < ""      , U ( )     :: M      ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 330))

    def test_331(self):
        input = """F : function auto  ( ) { for ( _Ie  = f   - iPg    >= a3Q5E   - jW      , s   + qQ    == N   + YJ     :: O   - dDG    > p   + S      , ! xc      ) HMe ( )  ;     while ( - j      ) continue ;     while ( u   + qV     :: Z   / i    > - qXj      ) { }     }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 331))

    def test_332(self):
        input = """e  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 332))

    def test_333(self):
        input = """R7  : void  ;   S : function void  ( inherit out dm : void    ) inherit Fj { }    d , U  : string   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 333))

    def test_334(self):
        input = """sJX : function boolean   ( out Q : boolean    , inherit F : auto   , out p : void    ) { P  = g1Sp8 ( )    != d   + c      ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 334))

    def test_335(self):
        input = """a8z  : auto  = 0    * - ! YmZ      >= ! w   + m7G     && ""    || Q   && W       :: - ! z   || VX      < - b    * i   % oCHQkNMc6     / V   * AeeU    && ! pYZ         ;   Pja : function boolean   ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 335))

    def test_336(self):
        input = """V  : array [ 884631_916_75 ] of boolean    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 336))

    def test_337(self):
        input = """XBk  : integer   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 337))

    def test_338(self):
        input = """gj  : array [ 8_12_75 , 9_6_7 , 2_09206 ] of string    = - PGerBBS    && ! V     || false     <= - ""     || - sGw    && im   * BP       :: o   + ! ! _      >= - - U   + S34         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 338))

    def test_339(self):
        input = """n  : string   = ! O       ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 339))

    def test_340(self):
        input = """p  : integer   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 340))

    def test_341(self):
        input = """be : function auto  ( e : auto    ) { u6 ( )  ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 341))

    def test_342(self):
        input = """SM : function void  ( ) { cxOR , hxN , q  : void  ;  }    Q , F2  : void  = ! uLXI   / fZ    + ! SmENFi      != "\\\\\r"    / ww   + ! D        , ! - ! Q8B2IS      <= ! Dc ( )     - - Z    && ! O       :: ! x   + ! j         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 342))

    def test_343(self):
        input = """KNYLFaX : function auto  ( ) inherit Y { }    AmF : function auto  ( ) { b_ , z782nh  : string   ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 343))

    def test_344(self):
        input = """h7BY : function void  ( out m9 : boolean     ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 344))

    def test_345(self):
        input = """q , Z , t , N  : void  = tg1   % E    % - E     + ! - L38M      >= ! - W   % yK       :: ! ! d    % _   + n      != - ! G    / W ( )        , Bt5   == - ! 0        , dI    :: G   % Q    / wn   * dK     + ! ! Ho      <= { }     && ! dB    * w   % l        , { }     * MQws   || - Q       :: - G   * Zr     - ! M   % WEO         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 345))

    def test_346(self):
        input = """O : function auto  ( ) { }    S : function array [ 8_0 , 0 , 0 , 8_3_3_9 , 5 , 1_1_02_16932_44 ] of boolean    ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 346))

    def test_347(self):
        input = """s : function void  ( inherit C : void    ) inherit BB20 { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 347))

    def test_348(self):
        input = """L : function void  ( inherit umo : auto   , out HV : array [ 9_66 ] of float     , out A : array [ 5 , 43_3 ] of string      ) { break ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 348))

    def test_349(self):
        input = """GIz , e0  : array [ 0 , 2_0897 ] of float    = ! { }       :: ! e ( )     && ! qd12   * yEDTCi198        , ! ! M    && kT   / o       :: ! EE    / - eev     * ! m   - o      >= { }     || ! - d0sCE         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 349))

    def test_350(self):
        input = """br  : integer   = ""    - ""     + - G   % k         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 350))

    def test_351(self):
        input = """u , b  : array [ 92 ] of string    ;   nE  : void  ;   r : function void  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 351))

    def test_352(self):
        input = """Jbd_ : function array [ 17_0_4 ] of integer    ( ) { A  : auto  ;  { }   for ( s2drc1z  = - L     :: M ( )    == E   + W      , 0      , i5   || U    != D ( )     :: - Kob      ) { }     }    K : function auto  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 352))

    def test_353(self):
        input = """yPh : function float   ( ) { while ( qkuH3   % bp     :: v   && W      ) return ;     }    R9 , H  : void  = - - - Y      > A   || xv    + dVk   || e     / ! - tG       :: false    == 0      , ! i   + t    + l      :: ! immWOB   - c    && ! Z      > dcV   || P    / z   + I     + gkAhxI   / y   + Tky         ;   o7 : function auto  ( ) inherit Be4o { }    s  : float   = B ( )    <= - OO   - O     && F   && MLws    - ey   && cx         ;   g177I , Q , wG  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 353))

    def test_354(self):
        input = """_eA , dox , DBN , qI , k  : void  = U   - d    || Tq   % Pv     + j      , ""     :: false      , V   || - ! J      <= ! N5FcG   - F     - { }       :: ! kM    - gg   / O    + - hG        , ! q    >= - p7    + _f_   % P     + i   / o1    && - B        , - mo ( )        ;   STcH : function auto  ( ) { while ( tr   || f4zjlf    != emw2   / Zrdvav      ) { }     while ( I   + L     :: L     ) P ( )  ;     do { }  while ( - N      ) ;   }    M : function void  ( ) { T  : array [ 0 , 0 ] of string    = K   && e8Het    >= WDe   * UumR     :: - c    >= p0k   - s       ;  }    l : function integer   ( ) inherit Ll { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 354))

    def test_355(self):
        input = """ydt , a6  : array [ 5179_3_30 ] of integer    = ! - FD    && e4n   * a        , ! - CE    - - h9M      <= ""    + m   && u8     + dpde     :: - ! p   * zl         ;   VZgYYfu : function void  ( out RjBsu : auto    ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 355))

    def test_356(self):
        input = """Ur  : array [ 0 , 0 , 0 ] of integer    = ! PLg2   / Y    - ! a         ;   x  : array [ 77416_6 , 0 ] of integer    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 356))

    def test_357(self):
        input = """_B3 : function array [ 119_8_9 ] of float    ( out X : void    ) { }    p : function string   ( inherit out e : float    , u : auto    ) { E , bf  : auto  ;  return ;   z , x3  : string   ;  Mk  : integer   = - U     :: qGXfM   && ku       ;  }    PK : function void  ( ) { e  : integer   ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 357))

    def test_358(self):
        input = """xt : function auto  ( ) { wigf ( )  ;   cFh  : float   = h   - OSKg    <= D ( )     :: ju   / m       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 358))

    def test_359(self):
        input = """Gl3 : function void  ( ) inherit m { for ( rK  = - RM     :: V   * xf    == f   * P      , i   || _      , 9    >= ! sDf      ) break ;     }    k : function float   ( ) inherit Y { }    J  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 359))

    def test_360(self):
        input = """  YQr : integer   ;   I , XA  : array [ 0 ] of string    ;   T : function auto  ( ) { do { }  while ( - B    < E   || r      ) ;   U  : void  = F      ;  }    B9D : function auto  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 360))

    def test_361(self):
        input = """y_X : function array [ 0 ] of boolean    ( inherit Jn : array [ 8_0 , 13_0_0 , 463_00_4044 ] of integer     , jZ : string    , inherit g : array [ 0 , 0 , 7_6 ] of boolean     , out QglDU : void    ) { }    UG , bV , c , c , N , w  : integer   = ! 8     % x   + S    / g      :: ! RE9B    != ! z   + A1    + ! hy        , xed   + HY    / Y   || oI     * v   || z_   + j       :: 8013_2284_0_8_40      , - ""    / ! _q      < ! ! l   + WmX        , I   && O    || e   + JS6     % ! udU    && xr   % qoU4      > j   / UQF    / - K     - ! ICe   * fH       :: M   || EQz    - osM   - J     * y   || igJ    * Yp   || Zj      <= - _   % Z     || e   - J    - z   || Pd        , RSU   + H    || w1   - C     && J4   + P    || i   - HV        , - 0     - - G   / H       :: - Qwj   % J    || - b         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 361))

    def test_362(self):
        input = """Oz , X  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 362))

    def test_363(self):
        input = """D : function auto  ( ) inherit V { Sp , osT  : array [ 9 , 0 ] of integer    ;  continue ;   }    BjC , Mo  : void  = FZ   - - P     - oF ( )      :: ""    * - dC4     && iQ      , - OyWo   && ZuEux7UgGTh     && p   / n0    && ! _ztt7       :: IY      ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 363))

    def test_364(self):
        input = """q , L  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 364))

    def test_365(self):
        input = """U2n : function boolean   ( inherit H : array [ 0 ] of string     , out tt : integer     ) inherit WFaHIQHYC { }    I , l , nea , J8 , D5w  : integer   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 365))

    def test_366(self):
        input = """aZ  : auto  ;   ZO : function float   ( out zV : array [ 29_3250 , 0 ] of string     , out o : array [ 409_56 , 0 , 1_18_6 ] of integer     , e : string    , N : void    ) { { return ;   }   KgEz  : void  = gr2E ( )    < i    :: D   / Y       ;  Z  : string   ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 366))

    def test_367(self):
        input = """ux : function array [ 4 ] of boolean    ( ) { while ( ws ( )    > - TR      ) DQ ( )  ;     }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 367))

    def test_368(self):
        input = """Aq  : float   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 368))

    def test_369(self):
        input = """V : function string   ( inherit V : string     ) { }    I : function auto  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 369))

    def test_370(self):
        input = """eE : function array [ 930_34_46_2_4 , 1_7 , 630 ] of string    ( out Ii1Q : auto   , mv : array [ 5_8638 ] of boolean      ) inherit L { A9c ( )  ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 370))

    def test_371(self):
        input = """r , Bb  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 371))

    def test_372(self):
        input = """D  : auto  = - ! - I       :: - - KF     % sQ    <= YP      ;   f  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 372))

    def test_373(self):
        input = """x9C : function void  ( ) inherit XCZ { if ( W2   >= YKN   / e     :: ! S    >= ! Pu0EeT      ) return ;   else return ;     }    X : function auto  ( out q : void    ) inherit Ij { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 373))

    def test_374(self):
        input = """SP : function auto  ( out Od : auto   , C : array [ 0 ] of boolean     , out n : auto    ) { }    U , cq , kP  : boolean   = { }     < ! P    || i   + H     - bS9   || x3    || f      :: - J    - X   - VJ    || ! t        , s   > - vDy   - b     * ! ! s       :: ! O   + z6   && XM      != ! QT      , 1763_0e-6       ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 374))

    def test_375(self):
        input = """dm , uAo5  : float   = T ( )      , L   > - ! U   * l         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 375))

    def test_376(self):
        input = """cO  : integer   = Z   - Bf7B    && ""     || - omzW    || H   || i         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 376))

    def test_377(self):
        input = """z : function array [ 2 , 2 , 2 ] of boolean    ( inherit out nfU : void   , inherit out v0Bc : array [ 84_8653_20 ] of boolean      ) inherit t { }    Y47F : function string   ( ) inherit A { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 377))

    def test_378(self):
        input = """om  : array [ 27 ] of integer    = SLs1 ( )    <= - - I   && jE       :: ! XE   && fb    - a_   % V      <= w      ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 378))

    def test_379(self):
        input = """vz , UJi  : auto  = - ! koF    + ! N      == - WH   || p     % - p    % ! tm        , - TU   + nh     / T   * L    && - mmxO      != - t   - G     * ""    * ""         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 379))

    def test_380(self):
        input = """r : function auto  ( ) { c , oiU  : auto  ;  }    A : function string   ( ) { break ;   }    Iu4of : function auto  ( out Eus : boolean     ) { }    W  : array [ 0 ] of integer    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 380))

    def test_381(self):
        input = """eP6 , Chg , F , H  : array [ 0 , 0 ] of float    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 381))

    def test_382(self):
        input = """F : function void  ( inherit out pr : float     ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 382))

    def test_383(self):
        input = """p , t  : float   ;   CD : function array [ 0 , 5385 ] of boolean    ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 383))

    def test_384(self):
        input = """HEmt : function auto  ( inherit L : auto   , inherit Rfx : array [ 2 ] of float      ) inherit g { }    J : function auto  ( inherit g : array [ 46 ] of integer      ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 384))

    def test_385(self):
        input = """pIK  : void  = Uhe   * Fz    || AOK7   / e     % - J    || yE   + L       :: ! w    / v   && p5     || ! nKa    && iE ( )      < - - Sz     && Bl   % v    - zt   + v         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 385))

    def test_386(self):
        input = """Y : function auto  ( ) inherit i { }    mNMd1  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 386))

    def test_387(self):
        input = """t , MYB , M_  : array [ 0 ] of float    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 387))

    def test_388(self):
        input = """j , G  : void  = ! - ZSr     / ! b   && p      >= rj    :: a   || c6    && - p     || ! m   - L      > { }     * 2    - A   && nl        , UR   * NUFbQb    * - W     + - a        ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 388))

    def test_389(self):
        input = """a  : float   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 389))

    def test_390(self):
        input = """m  : array [ 446 , 6 ] of float    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 390))

    def test_391(self):
        input = """S  : integer   = ""     :: w ( )    || q ( )     || xg   + L   - DT         ;   _ , rEii  : float   = ! ! UI   - G        , - r4YN0    - k5   || x     && FA    < m4    :: ! m   / VC     / ! O6G    * - I      > ! ZO2   - rW    / - db         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 391))

    def test_392(self):
        input = """B : function void  ( inherit N : auto    ) { r , RX  : array [ 0 , 8 ] of float    = - S     :: ! ye      , ! I1p    <= ! cR       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 392))

    def test_393(self):
        input = """Ir : function boolean   ( ) { v , RY , h  : void  = ww   && Hrc      , RQA   - QMk      , - c    > xF   * o1HL       ;  }    b8i , B  : void  = ! u   && wQ     - ! - o      > - Ac   % z    % w   - u        , DS ( )    + - M     && T ( )     >= - K   - MsjU    || eI   % B       :: s6SG ( )    != M_      ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 393))

    def test_394(self):
        input = """r2  : void  ;   Tl : function array [ 5_3 , 11_52_4 ] of integer    ( inherit HwyHPRAX3MAZ : void    ) inherit V { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 394))

    def test_395(self):
        input = """peIEih : function float   ( inherit out K : auto    ) inherit Z { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 395))

    def test_396(self):
        input = """oX : function auto  ( out v9 : auto    ) { k3  : array [ 4_238_5_5166 , 21_780 ] of integer    = ! n       ;  }    s , w  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 396))

    def test_397(self):
        input = """WW , b_j5ZCv , Cu4B  : void  = ! ! l   || n9        , ""    * - U   - DZy       :: waKv ( )    < ! ! B     % mve   && N    - NeS8SX4G   || wMdG3        , rj ( )    && { }         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 397))

    def test_398(self):
        input = """suk , db , U  : boolean   = - _g   - H     && ! Kw    % - jei       :: ! w   * d    * s ( )        , - 0     < - p   - e    % A ( )       :: N   + w    / VI    / ! v   - jf        , ! ""     || ! t    * b   - z         ;   p2  : auto  = WfpEv ( )    / Y    - iN ( )      :: gi   < - - oo    / x   + gS         ;   ag : function auto  ( inherit out EbW : void   , inherit o : array [ 4 , 0 ] of float      ) inherit s { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 398))

    def test_399(self):
        input = """b : function array [ 0 ] of boolean    ( out r : void   , inherit L : array [ 37_3 ] of float     , FVVzb2 : void    ) inherit j { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 399))

    def test_400(self):
        input = """J , i , O , n  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 400))

    def test_401(self):
        input = """YI  : string   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 401))

    def test_402(self):
        input = """F  : array [ 0 ] of float    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 402))

    def test_403(self):
        input = """T : function array [ 0 , 0 , 3_5129892_27_7 ] of string    ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 403))

    def test_404(self):
        input = """CGkXv37 : function auto  ( out V : string    , wm : auto   , inherit out d : auto    ) inherit _2E { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 404))

    def test_405(self):
        input = """CVm : function auto  ( out n : void    ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 405))

    def test_406(self):
        input = """XYUGiX  : void  = ! Y4   || niF    - vW   || Pwk       :: - UH    + ! v     * qg ( )    || q5     >= - mZ    && JH5Nm   && G     || Jcm ( )    / K   + Xa         ;   _K  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 406))

    def test_407(self):
        input = """Ukl  : void  = ! - dx     * ! CT   - Q       :: - d   * lGB    / vY   || J         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 407))

    def test_408(self):
        input = """N : function float   ( out P6fq : float    , out zy0Pa : array [ 72 , 987 , 0 ] of string     , out R : integer    , O : float     ) inherit O2 { { qoZ  : auto  ;  continue ;   R , WOz , n  : auto  ;  }   Eh  : array [ 51_6_732 ] of boolean    = pD   * gFM     :: ! r    <= x   % iB       ;  o  = - FJ      ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 408))

    def test_409(self):
        input = """x , U , X , bO3y  : string   ;   j : function void  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 409))

    def test_410(self):
        input = """H : function auto  ( ) { }    b , t , Rmzfse , U , X  : void  = - iv   || _     - - - ks4iH      <= T   / XW    && m   && C2     % ! Ve   - y        , ! ! yR     || b   - PxX    - a   + HsW      >= - oXl    * Ne   || S     && - - f       :: G   % ! V   - LW      <= "࠰"    && - AM    * dV   || Wm        , ! ! - qp6_M       :: m   || - f     && eq   - A    / ! L      >= ! aK    * ! J     && x   - E7    % ! KOD        , - PY   * TK     && oS   - qF    || v   || v      < - - KJfVy    / - Z        , - L ( )    + Sc   && Q      != - L    || ! h     || U   || G    % M8   && E       :: - g   + m    || XGm   && M      >= - K   % XE8    || ! OF         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 410))

    def test_411(self):
        input = """k : function array [ 0 ] of float    ( ) inherit Sp { }    ngO  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 411))

    def test_412(self):
        input = """wB  : float   ;   v , F  : auto  = OE   > ! p   && Q     || ! O    % r   && _        , ! B   && jE    + V   - y         ;   U_e4  : array [ 2 ] of string    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 412))

    def test_413(self):
        input = """xIh : function array [ 38_8_3 ] of string    ( ) inherit Pk { }    aO : function array [ 0 , 0 , 0 , 0 , 0 ] of integer    ( ) { }    ZJy3 , fD , J , nL1z , n  : void  = ! tp2yVBY0   && A    && M5   + n      <= ! ! BTT    + ! TNW        , VK   || ! m     || X   - c    / ! twB        , - Xioxd   - C     + { }        , - a ( )     / - H   || jY       :: - - csuWj   / j        , ! - O_LQ     && z ( )      :: { }     <= 3    && R   + Bj     / x   * N    - ""         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 413))

    def test_414(self):
        input = """U : function auto  ( ) { v ( )  ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 414))

    def test_415(self):
        input = """Eqq  : array [ 0 , 0 , 26_69_9 ] of boolean    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 415))

    def test_416(self):
        input = """Rz : function boolean   ( out G : auto    ) inherit a_ZVg { }    L : function string   ( i : float     ) inherit mX { }    O4W : function array [ 0 , 921 , 0 ] of integer    ( dkht : void   , out l1 : auto   , inherit out cVBtae : array [ 0 , 5 ] of boolean     , inherit q : array [ 879 , 0 , 0 ] of boolean     , out e : void   , inherit out c : void   , inherit out n : auto    ) inherit nJ { Q , eA8Puc , v , Xa , G  : float   = ! VGWb      , - X     :: fe   % M    != G   * Hl      , - H    <= - Ue3     :: E   && xtqNY    > qr   - fL4j      , U1n   * i      , a   && x     :: P      ;  }    y : function array [ 3_6 ] of boolean    ( ) inherit G { S ( )  ;   }    L , iXT  : string   ;   L7 : function string   ( out M : auto    ) inherit P { d , KP , Z , KYM  : array [ 26_32513 , 4 , 44_84 ] of float    = ! Jr     :: 0      , GN     , _0   * N35L    <= zoPg   || Kn6d      , r   / V    <= - o     :: - cP    == K   / e       ;  }    eW : function array [ 0 , 96 ] of boolean    ( inherit cn : auto    ) { }    YMh : function float   ( out V : array [ 0 , 74 ] of string     , inherit out k1A : auto   , inherit ga : auto    ) { }    H : function float   ( ) { s2Z , A3a  : float   = ! y      , oaG3JXZS   / z       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 416))

    def test_417(self):
        input = """AIu  : void  = - gJ   % Qj    / Z   % i      != Q ( )     :: g ( )    % iI1x   || yq_X    || 7         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 417))

    def test_418(self):
        input = """r4HZAxN , Coc4 , cDHQ , JQ , ao , od  : void  = jmjx   * J4    || - u     / ""     != Djb   - - S    || fqF   - _       :: Ux ( )    && - - cN        , - ""    % R   - P2      > s   % Wy    || c    && ""    * ! Hk       :: - - X     - q   / oJJ    && kl   + xoV      != ! ! - Kq        , true    > t   + Q    && - HQn     - _b   / c    || - Jy        , o   / u    || Z2naO   * my     % Zu   || - DgeA      >= - _9    && z   - LG7     - - ! t1       :: - p   && P     - Tu    == - - a     % ! xDVLzT   + n        , P   || u74G   || H     + 0    - - b      >= false     :: ! - d   * WEc      > 66_11664_4.e-6      , ! _   && V1     / - L   / i      == - X       ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 418))

    def test_419(self):
        input = """JYr , P , OQMFP88FWVs , qGB , metJF  : void  = h   && k   - J    || oq   % e       :: mwDqs   < ! ! ! h        , ! f   % X     || ! Hqh    % ! r      <= - - X   % m       :: _   - vt    % ! y     || B   && a    + q4l ( )        , yrpX   + L    || _u31   % Bsb8yX     && L ( )    && ! uB7X6        , ! ! dlB1     * - - b        , { }     && 2    - a   * z       :: - A    - B   - E5W     - "\'"        ;   sUlN , Gixx , I  : auto  ;   F : function void  ( ) inherit V_ { kU2  = ! V     :: T   && iI    > - CQFR      ;   { { }   }   O  : array [ 2 ] of integer    ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 419))

    def test_420(self):
        input = """n : function void  ( ) inherit Y { }    Kf  : integer   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 420))

    def test_421(self):
        input = """Dku : function integer   ( inherit Jm : void   , out TqG : integer     ) inherit K { while ( - T0a    > L   % Qm     :: p   == - c      ) W ( )  ;     }    fu3 , y , j  : array [ 21 ] of boolean    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 421))

    def test_422(self):
        input = """C : function integer   ( ) inherit au8lcQO { if ( Ni   && L     :: qck   && QJ    >= Zs   && FwI      ) break ;   else continue ;     }    fk : function void  ( Gh : void   , inherit out RcFbY : void   , Jp : string    , U : string    , jt : void   , inherit out C : array [ 1 , 12_9 ] of string      ) inherit J1vvp { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 422))

    def test_423(self):
        input = """M : function auto  ( ) inherit c { do { continue ;   I , O  : auto  ;  }  while ( U ( )      ) ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 423))

    def test_424(self):
        input = """at , q6yw , i , c  : string   ;   oCt : function float   ( ) { }    Tu : function void  ( ) { }    m  : string   ;   S : function array [ 0 ] of integer    ( X : void    ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 424))

    def test_425(self):
        input = """rQ , I  : boolean   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 425))

    def test_426(self):
        input = """QR4  : void  ;   C  : auto  = - ! ""       :: - eEB ( )    * kN   && LuJ         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 426))

    def test_427(self):
        input = """J : function auto  ( ) { if ( ! y    > Y_    :: acp   * ND      ) break ;   else break ;     break ;   Bp ( )  ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 427))

    def test_428(self):
        input = """fDh , UjkU  : array [ 0 , 1 ] of integer    = ""    + 5    % - UwLG2      != - V   % Y    * L   + UZBt       :: ! ! w       , ! - DW1c   && Q      != ! - auJ ( )       :: ! d   || P     - h   / o   % d         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 428))

    def test_429(self):
        input = """s6 : function auto  ( F : array [ 6 , 0 ] of float     , inherit IP : array [ 27 , 0 , 71_84_136283_4 , 0 ] of boolean      ) { n , p , x , C , y , Ecp , s  : void  ;  do { }  while ( A   * s    > - GFax      ) ;   if ( - B    >= - N      ) break ;   else W ( )  ;     VOA  : array [ 0 , 0 ] of string    = B   == YCb4NI   + V     :: Jp   + _AfC    == qdt   % RUnJ       ;  }    b , V7_ , cP3GWz8 , oy , OB  : auto  = ! ""     < ! I   % P5     + - Dw   * X       :: - ZP      , i ( )    < - ! n    + x   - K        , ! T   % mK    && m   && B      != U7   + fE   / KWOos     + qW   - s    + ADvt ( )       :: ik ( )    == false      , ! - n3a    + kg   * TgQ      > { }       , ! - yb     + - fY81lEK    && r     != Ul   && G    % 0     || fgGdupv1   * P8    || j   + s       :: - - j   || I      >= - JA    - ! bCdLyaHj     / cxVX   - DZ    / vF ( )         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 429))

    def test_430(self):
        input = """pV : function array [ 2 ] of boolean    ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 430))

    def test_431(self):
        input = """Y7 , Gh  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 431))

    def test_432(self):
        input = """G , G , B  : auto  = 8401_3_92      , qng   + D    - mnie   * J     / ! 5      == - ! V   / CPCZi       :: sR   * ! H ( )        , kG   % aJ    - ! _     - Ww   % voW    % E   + GxrBju      != yY ( )       ;   wGy : function boolean   ( w2 : string     ) { for ( mKl  = ! MG    < W0uvW   / Z     :: ie   + i    >= H   + I      , _   > B ( )     :: ""    > ! F      , RB8   - _F    == - _6z      ) T ( )  ;     while ( - DO    != PL   * go     :: Ov1Eo   && r    > N   * W      ) return ;     }    k  : integer   ;   Kd  : void  ;   kLq  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 432))

    def test_433(self):
        input = """P : function void  ( DYq : integer     ) { }    yu  : array [ 803 , 0 ] of integer    = E   / c    + - D     % Q   % k   - _F      <= - rd    || ! b     / - g    + GSO   - v4       :: y      ;   b , g , Va  : void  ;   b  : auto  = ! ! Jh    || - rr       :: _XR   < ! j ( )     + un   && C    - J   / W         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 433))

    def test_434(self):
        input = """U : function void  ( inherit out b4 : auto   , F : array [ 6 ] of string     , inherit out dIhKgvT : auto   , inherit out vHj : array [ 0 ] of integer      ) inherit K { B_ , G  : array [ 0 ] of boolean    ;  break ;   break ;   return ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 434))

    def test_435(self):
        input = """z  : string   ;   Vk : function array [ 42 , 0 ] of boolean    ( inherit J : array [ 78_4_1 ] of integer     , out l : array [ 7 , 5373_8 ] of float     , inherit b : array [ 0 , 1 , 7_6 , 3_0_701 ] of boolean      ) { KP , __7  : array [ 0 ] of float    = Q   / a      , I ( )       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 435))

    def test_436(self):
        input = """olZ5  : array [ 6 ] of integer    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 436))

    def test_437(self):
        input = """t : function void  ( ) { }    T : function integer   ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 437))

    def test_438(self):
        input = """PZ : function void  ( ) inherit I { }    O : function boolean   ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 438))

    def test_439(self):
        input = """z , sX , l , tw  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 439))

    def test_440(self):
        input = """u : function array [ 0 ] of integer    ( ) inherit J { continue ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 440))

    def test_441(self):
        input = """w : function void  ( inherit out BC : void    ) inherit Q { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 441))

    def test_442(self):
        input = """L1iH : function string   ( ) { }    fb : function auto  ( ) { w , v  : void  ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 442))

    def test_443(self):
        input = """B  : float   ;   yvHWbhL  : integer   = - GT    > ! ! ! U3zq         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 443))

    def test_444(self):
        input = """i3Q : function void  ( inherit out W : void    ) { t ( )  ;   H , T  : integer   = jyMf   * zy0    <= 6     :: i   + pZT      , ! hwbsqqy     :: - kb       ;  }    D : function integer   ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 444))

    def test_445(self):
        input = """qZ  : void  = d   - E    / k   % H     || lCC    == q ( )       ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 445))

    def test_446(self):
        input = """Zv : function array [ 0 , 0 , 73 , 90 , 6_5_3 ] of boolean    ( inherit qzw : array [ 1 , 0 ] of float      ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 446))

    def test_447(self):
        input = """T : function auto  ( d : auto    ) { do { vk , DuGG , P  : float   ;  }  while ( ! hx7E     :: J   + UE      ) ;   }    pdLr : function array [ 20 , 0 ] of float    ( inherit out x : auto    ) { Gr  : array [ 0 , 5_2_9 ] of integer    = pAh   + O     :: Rm      ;  g , G , t40 , I , ps , x  : auto  ;  }    l : function integer   ( ) { OrN , Z , VI , TLM  : array [ 0 , 51 , 0 , 0 ] of integer    = - F      , lODW   / kf    == ! W     :: ! Ti    != k   || nih      , w   % q    > - e     :: G   * g      , 7    <= n   % Z       ;  UO , ja  : void  ;  }    b : function array [ 524008 ] of boolean    ( ) { lc  : void  = uGz   % _6Y       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 447))

    def test_448(self):
        input = """N , _a  : boolean   = - DMasAk   % Z     - Fwu   / iIC    / L   + IjEHy       :: - AKm    / R ( )     - KYw   / gQ    - y7   % oqr      > ! X8   * e6h    - ! i        , X      ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 448))

    def test_449(self):
        input = """WE , g , s  : void  = ! V   + HT    - hlGB   - s      < - W    / YmDn   || h     + ! Wa    % Yz4   / v       :: - UP   + mMe    % - BQ      > xO   % o    - ! yQ     || mN7He   && AwB    / sP9   + a        , - - tGzJUop ( )      != 0    % bLZ ( )      :: ""      , H ( )    - kC   / E8Z   || G         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 449))

    def test_450(self):
        input = """N : function void  ( ) inherit Fp { }    LviPFiYlKK  : array [ 35_094574_069 ] of boolean    = Y   * gP    && - lDP     + ! imQ    / r ( )      > M ( )    && Ty   + nJ   / E         ;   L2 : function boolean   ( ) inherit AEp { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 450))

    def test_451(self):
        input = """NA  : string   = ! N   / q    || V   + l       :: d   && - MZ   + A      < - - tv9     % ! c   * P         ;   a : function void  ( ) { t , fkO  : float   = bf   > e9   || r     :: ! t    > ! rMXOtwD8k5i      , bIeeDcA ( )       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 451))

    def test_452(self):
        input = """hQ : function string   ( out Dr : void    ) inherit gAyLR { JS  : boolean   ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 452))

    def test_453(self):
        input = """K  : string   = true       ;   c , QZGtFPg  : auto  = - false      :: - W   && Ut     % - e5j   % jV        , ! - r    + cU      :: l   || T    / g   % G     || vpE ( )    && Xj   / r         ;   I , o  : string   ;   b : function array [ 0 , 2 , 4_0_2_133_56_2 , 0 ] of string    ( ) { return ;   C , f  : void  ;  r  : integer   ;  }    y , kC6 , Kb , y , I , uaj  : auto  = K   - Q0b   + SU     - ! uy   * b      < - - LAg    && ! NU       :: - z    % - vv     && - ""      >= - - n    - ""        , - - w_     && ! l   * Z      != - ! Q   + W        , - ""       , ! - k    && ! y      != dr ( )     :: ! 4     + x   * _    % hZZA   || E      < ZG4   / z    % i   * hW     && mF   + IM    || L0pv ( )        , ! ! K5TwJcS     && ! fI   + UF      < ! kJz   || n7    && M ( )        , ! ni4f   || m    && AU   + e      < ! Nvq     :: ! i    || SE    + ! ! Pzmv         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 453))

    def test_454(self):
        input = """Z : function array [ 294 , 6456_42 ] of boolean    ( ) inherit siLfTAA { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 454))

    def test_455(self):
        input = """W0Iw , sv  : array [ 7_8 , 1_5 , 156212 , 0 , 9 , 3_631_2 , 856_301_9 , 9 ] of integer    = ! qvGS ( )      :: - ! QQDYx   * z        , - lr    - Oid   || b9B8d     / Kb    <= - ! 0         ;   qaTo  : integer   = ! p   * hv     * - pMT    * r   * v         ;   S : function void  ( ) inherit M { while ( o   + Q     :: MQ9X ( )      ) return ;     break ;   do { }  while ( - r      ) ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 455))

    def test_456(self):
        input = """pK , x  : integer   ;   Bsw : function integer   ( ) inherit S { j  : string   = ""     :: M   * f    >= - YL       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 456))

    def test_457(self):
        input = """g  : auto  = ! ! Q5   && L       :: ! - ABgdE    - ! AGILj02         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 457))

    def test_458(self):
        input = """x : function float   ( bD : float     ) { v , U  : auto  = H   - a     :: - t      , ! a     :: c   * iBPV    <= ! U       ;  lP , R , R , r , Ck  : boolean   = r8   + ic    <= pib     , y   % v    > Fff7   / YWi      , Va   != ! oKp      , - P8M    <= eo    :: - H      , LNa1   - T    < ! vgy       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 458))

    def test_459(self):
        input = """wMh , ML  : integer   ;   o  : void  = u3   + M   / X    - ! Hhe         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 459))

    def test_460(self):
        input = """U : function integer   ( ) inherit ce { for ( P  = QOB ( )    >= cfrV4s   * V     :: m   * At    == E   + M      , Q   < PGe ( )      , Uc   - p      ) { Yv1U3S  : void  ;  }     }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 460))

    def test_461(self):
        input = """h : function auto  ( inherit out R : float     ) { }    Y : function void  ( inherit e : void   , inherit AE : integer     ) inherit N { Z  : array [ 0 , 0 ] of string    = mE   % z     :: ! dW    < vl   - orH       ;  ibE_  : boolean   ;  }    TI1 : function string   ( ) inherit I { }    y : function void  ( E : void    ) inherit Op { }    u  : integer   = ""    / - iC     || bILc0   || Af   - Ku      == Zl0   - m   * _     && 62_968        ;   H : function float   ( N4 : array [ 0 , 0 ] of float     , n : boolean     ) { }    B : function void  ( ) inherit bz { p , JT  : boolean   ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 461))

    def test_462(self):
        input = """tu8 : function void  ( ) { vKk , SCR9  : auto  = - r    > - J     :: B   + w4    >= o   - rZJ      , - q     :: cK   * dV9       ;  }    taBm2t  : boolean   ;   U9JQ  : array [ 6_1 ] of float    = - il    + Se ( )     && gJ6   / yqG    - aqc   || Xx       :: IibhXbEaJ      ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 462))

    def test_463(self):
        input = """h : function array [ 0 , 0 ] of string    ( inherit out B : string    , out xI : auto    ) { }    Xi : function float   ( ) { }    tr  : boolean   ;   A5  : float   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 463))

    def test_464(self):
        input = """c , h , m , BgV , I65W7 , eFX6 , n7 , nKvn , g , x  : array [ 4 , 0 ] of integer    = - cP5   - vqBobtTRY     - - ""        , - MN    || ! GmcwYgZHw     || ""       , G    :: - ! R     % V    >= - { }        , ! Z    + f_PHb   || w     * - _   - P        , - 7    - j   / C        , ! 7     + ! A    || H   % Ed      != - h   && FpJg     % Gka6TG   && icq    && qYd   || Wbw       :: Uyg   - e9    && ! o     * ""    * B4SO5uWLY   + q      != - - A     / M   % c    - g   * h        , ! - n2   || TC        , ! - G8C     / - E1    || - fQaAI      != Htm   * Ss6qv   || s     / K   % Y    || yf   / KeTL       :: ! 0       , ! 0     && t ( )    - s   * bLq       :: - ! ! _        , b4   - EX   / BAb     && - O    - q   * A      < ! ! 0       :: ! CYql    && N   % M     || u4   || X    && b   + IyS         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 464))

    def test_465(self):
        input = """sc : function float   ( inherit V : void    ) inherit V { i  : array [ 0 ] of integer    = - w    != C   * G       ;  continue ;   break ;   c , Ri , Bi , J7  : string   = - xKj     :: TCS   - j    < - X      , o    :: - M    == a   / M      , A   / wHSJ5    < ! e      , o   * M       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 465))

    def test_466(self):
        input = """m  : integer   = { }     || Ec   % E    + O6SA ( )      <= ! ony   - hL1     - - - c       :: dj      ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 466))

    def test_467(self):
        input = """eA  : auto  = - w ( )     - J   || x_    % ! L         ;   wYA1wJ : function array [ 1 , 0 , 3_8 , 0 ] of boolean    ( ) { continue ;   fAa  : array [ 8 ] of integer    = ""    < man   - un4       ;  { jT , vU  : float   ;  { { }   }   }   rAC ( )  ;   L  : array [ 0 ] of float    = - W    < - A8id       ;  { }   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 467))

    def test_468(self):
        input = """Dj : function void  ( wxk : auto    ) inherit mhf { }    oy7 : function float   ( ) { }    p : function array [ 0 , 0 , 89_04499_17 , 5 , 599 ] of integer    ( ) inherit y_ { }    ul , Zp  : integer   = ! w ( )     % dZ9H   - - W        , - - a    && E   && f      != ! C   - ""       :: - R   / bw2x    / wS   + bI      == P   && Q    || W   * kgy     - D ( )    * QF   + S         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 468))

    def test_469(self):
        input = """C  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 469))

    def test_470(self):
        input = """I : function boolean   ( ) inherit i337q { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 470))

    def test_471(self):
        input = """TRs4 : function float   ( srXJ : void    ) { continue ;   continue ;   { }   bk  = ! UFQ     :: YWt   + t    >= HX ( )      ;   }    r : function integer   ( ) inherit G { return ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 471))

    def test_472(self):
        input = """F  : void  = - nA   + - t       :: Z ( )       ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 472))

    def test_473(self):
        input = """W : function void  ( inherit out wD : void   , out _ : void   , out FK : boolean     ) { }    k : function void  ( ) inherit e { FrjO ( )  ;   }    w : function auto  ( ) inherit Gt { return ""    <= tn   - E2T      ;   zc  = E   || eJd    >= _    :: R   / x    > ! cIDi3_      ;   }    Ek6d  : array [ 29_8_4 ] of boolean    = _   + MnjF    || s    % N     :: 88_77       ;   qxP  : auto  = "\t጑"    >= ! - ! Hf       :: M1   && x    - ! PL     % ! jt ( )         ;   b : function auto  ( y : integer    , inherit J : void   , inherit out J5 : void    ) inherit J { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 473))

    def test_474(self):
        input = """fCBJg : function void  ( ) inherit h { while ( uc   + H4    >= j   + If      ) { _  : auto  ;  rT90 , bO , XS  : float   ;  }     M , d  : void  ;  while ( ! o    == - uT     :: - _      ) { aMS  : auto  ;  }     break ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 474))

    def test_475(self):
        input = """AP  : array [ 0 , 0 , 0 , 8 ] of float    = ! H   * Fw   / h      > RK    :: "\t"    < "\""       ;   t : function auto  ( out R : integer    , inherit G : array [ 0 ] of boolean      ) inherit O { while ( _   || o      ) return ;     }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 475))

    def test_476(self):
        input = """QSH  : string   ;   yee  : integer   = ""    - c ( )     && qYn8yt   % hwN    - _   || iZ_i      > t   || V    && - a     || ! - HCJk49       :: Z   + xZ    + V   / y7wg     || ! W   + PMEP         ;   iTK9 , r  : auto  ;   A  : void  = P   - ! Bs4    - A   + SA5      > e   * MRXq    || rB   * nix     * 0    + ! CcUb       :: { }     / - Y   % bR      == { }     || gdam ( )        ;   a  : void  ;   II  : string   ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 476))

    def test_477(self):
        input = """P : function void  ( out m : auto   , Y : auto   , out t : array [ 0 ] of boolean     , inherit kLOu : integer     ) inherit T { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 477))

    def test_478(self):
        input = """p : function void  ( ) { HU  : auto  = CHpt   || ddsc    == WTq ( )     :: V   / e    <= z      ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 478))

    def test_479(self):
        input = """o : function auto  ( inherit H : float    , inherit Zi : string     ) { F  = TC ( )    <= GvJ7   || opXN_uK6      ;   }    n : function void  ( j : auto    ) { }    I : function array [ 5_5 , 776 ] of string    ( ) inherit yJ { hx  : boolean   ;  }    v4G : function void  ( inherit out H : auto    ) inherit l { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 479))

    def test_480(self):
        input = """j  : string   ;   dR , _  : array [ 8 , 56_0 , 0 ] of float    = M   && h    / 1     + YW ( )      :: Z   + T    && oQ   && I     || Gz   * S_    || - y4BG9s        , kt ( )    + Q4   / eCF68IhyEW    && v        ;   L2p7  : float   ;   B , e  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 480))

    def test_481(self):
        input = """S , E , q , t , z9  : float   = 8    && ! iaaiSa9    - ! k      == ! rV   - AVT    || N   / D_A1       :: - n    && L   % ZLV_N     - dk   * bF    % - K        , ! FtjcU ( )     < - d   + sFK     && - ! Go        , ! ! Q     && ! d     == f ( )      , G   && ya    % ! Y     - y    <= - W   % T6R    / _l ( )        , ! - I    && OG9Nxmh ( )      > 3       ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 481))

    def test_482(self):
        input = """e : function auto  ( ) inherit AT { WmO_3TYfP , lY , X  : void  ;  }    q : function boolean   ( L9FO : void   , inherit _lB : void   , out M : void    ) { }    j5p : function auto  ( ) inherit RcEL { R  : float   ;  if ( uSt   * gRcNj    < W   - O8     :: ""      ) return ;     }    Ro , V , lXFQ , VW , kWGFC , f , t8re , h  : void  = ! t ( )       , - ! A     || u   % Uu2q6e9fPEZ    + oble   || y        , - tDM    || M   + e     - V ( )       , T ( )    <= ! - G3TdMR   - L        , ! - B     / true      :: { }     == - eI   + U    && iol_   / I        , ! ! CaYkG    && - O4        , r ( )    != - - PN   % w       :: ! UZ    / M ( )     - ! b   + L      == ! LwMh30   + O55     + ZjQv9g   + wv    - KE ( )        , ! ! xb    % 1      > ! MZ   / L ( )       :: ieP ( )    >= y ( )       ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 482))

    def test_483(self):
        input = """i : function void  ( ) { }    Sw , IQ  : integer   = - - B    || ! G      >= e   / V   || FsmP     / c     :: ! x    >= - - Jj     + - GtxOz    && - kMB        , true    - - Pz    || l5IoE     >= ! D   || a     / ! - c       :: ! upM   + jt     + - ! N         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 483))

    def test_484(self):
        input = """Unw : function auto  ( inherit g : array [ 0 , 0 , 0 , 83_5_6_73_43 ] of string     , inherit mi : void    ) inherit B_ { }    TWlE4 : function float   ( out mR : float    , inherit Pnr4 : array [ 41006 ] of boolean      ) inherit Wov { }    Z , c , za , c7  : auto  ;   B : function void  ( ) { continue ;   J  = B   && nE3S    > ! v      ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 484))

    def test_485(self):
        input = """E  : void  = DEV   == - l   * AGugkN    + l   % IiD         ;   n  : boolean   = - ! XWS    - 2      != ! w    % ! nFd     + D ( )        ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 485))

    def test_486(self):
        input = """K : function string   ( out A : auto   , u : string     ) { eW  = ! Y4E     :: LQ   || c      ;   }    DR  : array [ 7_0 , 792_6200199 , 55 , 0 ] of float    = - _xt2 ( )     > - r    + tn    || Bh   * J    && ! R       :: - - pIeT   || N2         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 486))

    def test_487(self):
        input = """AR  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 487))

    def test_488(self):
        input = """Wn : function string   ( ) inherit dIAJh5 { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 488))

    def test_489(self):
        input = """dSh  : integer   ;   xf , L , oF , q , A , eC , ea  : array [ 77_34_144 , 5 ] of integer    = - Ps ( )     && ! u    && q   || n        , "𑤕"    || - gSu    % ! P8       :: - ! IE2     - I   + m    * T   || UE        , D    :: 0    + ! ! ZBA      > - - cc4W     % - K   - Eq        , ! ! - Z      < k   - - bHB     || ! - ex        , ! i    - ! X6 ( )       :: - ! GBA    / ! Q        , ! ! s   % gO      >= D   - bmhp    || P   * a     - 5_2      :: { }     < - K   * bkRaQ     / - COeYOJ ( )        , - nZ    * cyqom   + Ke     || hF3   - k    || Nj1   - b       :: { }     || - m   % OE      <= - ! SNq   * qFoyd         ;   b : function auto  ( inherit out P : void   , out pE : array [ 34_11 , 0 ] of float      ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 489))

    def test_490(self):
        input = """e : function auto  ( ) inherit g { if ( UQ   + bXHx    != z   / h      ) continue ;     }    DZ : function auto  ( ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 490))

    def test_491(self):
        input = """Ua : function auto  ( ) { return Id   - C     :: Ob   + ssS      ;   }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 491))

    def test_492(self):
        input = """V_  : float   ;   JuA5 : function void  ( out m : auto    ) { L  : array [ 25 , 8_03_5 ] of integer    ;  F , sPcFS  : void  ;  continue ;   if ( - J    == t   && Km      ) break ;   else pv ( )  ;     mAW , J  : string   = - yH9    != fnK     , H    :: ! w       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 492))

    def test_493(self):
        input = """IBZf : function integer   ( inherit P : auto   , inherit y : void   , inherit out m : auto    ) inherit Z { }    vch , w  : string   ;   b : function string   ( ) inherit z { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 493))

    def test_494(self):
        input = """Y : function auto  ( ) { { { }   }   while ( S   || N    > S   || _     :: UD   / n      ) { R3 ( )  ;   z  : void  ;  }     D , m , Ei  : array [ 82 ] of integer    = ""      , n   || dyp     :: ""      , ad   % bUGcVts3     :: h   && Z    > lO   / w       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 494))

    def test_495(self):
        input = """B  : auto  ;   fk  : void  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 495))

    def test_496(self):
        input = """BGByBH  : auto  ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 496))

    def test_497(self):
        input = """r , X5C , kdy , f  : array [ 0 , 0 ] of boolean    ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 497))

    def test_498(self):
        input = """X : function array [ 8_3 ] of integer    ( U : integer     ) { T  : float   = E   || wu       ;  }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 498))

    def test_499(self):
        input = """N : function array [ 9 ] of string    ( m : array [ 6711 ] of boolean      ) { }    sH  : string   = - ! q   % Zd2       :: - k00vA   + H    - l   || d      != bt   % hDjk    - ! V     % L   - F    * Dwt   - E         ;   T19PA : function void  ( out m : integer    , out B : auto    ) { break ;   J , w , HzP  : array [ 2049_580 ] of integer    = h   && TAi1P    > c     , ! SjlU8      , R   && S     :: ! M    <= ! ZrE6t       ;  myDpV , Q5O  : auto  ;  }    tqV  : auto  ;   Zi , AzBLU , M , DH  : auto  ;   N  : void  = { }     % - ! s      < ! u   / j    - E   / sK         ;   """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 499))

    def test_500(self):
        input = """a : function float   ( YxA : array [ 0 , 0 , 587 ] of float      ) { }    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 500))
