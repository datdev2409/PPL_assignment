# Generated from /Users/congdat/Desktop/PPL_assignment/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u027b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\7\f\u0111\n\f\f\f\16\f\u0114\13\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u011f\n\r\f\r\16\r\u0122")
        buf.write("\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3=\7=\u01df\n=\f=\16=\u01e2\13=\3=\3=\6=\u01e6")
        buf.write("\n=\r=\16=\u01e7\7=\u01ea\n=\f=\16=\u01ed\13=\3=\5=\u01f0")
        buf.write("\n=\3>\3>\5>\u01f4\n>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u01fe")
        buf.write("\n>\3>\3>\3?\3?\3@\3@\7@\u0206\n@\f@\16@\u0209\13@\3A")
        buf.write("\3A\5A\u020d\nA\3A\6A\u0210\nA\rA\16A\u0211\3B\3B\5B\u0216")
        buf.write("\nB\3C\5C\u0219\nC\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\5D\u022d\nD\3E\3E\3E\7E\u0232\nE\f")
        buf.write("E\16E\u0235\13E\3E\3E\3E\3F\3F\3F\3F\3F\5F\u023f\nF\3")
        buf.write("G\3G\3G\3G\3G\7G\u0246\nG\fG\16G\u0249\13G\3G\3G\3H\3")
        buf.write("H\7H\u024f\nH\fH\16H\u0252\13H\3I\6I\u0255\nI\rI\16I\u0256")
        buf.write("\3I\3I\3J\3J\3J\3K\3K\3K\3K\7K\u0262\nK\fK\16K\u0265\13")
        buf.write("K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\7L\u0271\nL\fL\16L\u0274")
        buf.write("\13L\3L\3L\5L\u0278\nL\3L\3L\4\u0112\u0272\2M\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("\2\177\2\u0081\2\u0083@\u0085\2\u0087\2\u0089A\u008b\2")
        buf.write("\u008dB\u008fC\u0091D\u0093E\u0095F\u0097G\3\2\16\4\2")
        buf.write("\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4\2--//\4\2$$^^\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\3\2$$\3\2^^")
        buf.write("\n\2$$))^^ddhhppttvv\2\u0298\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\3\u0099\3\2\2\2\5\u00a5\3\2\2\2\7\u00b2\3\2\2\2\t\u00bc")
        buf.write("\3\2\2\2\13\u00c7\3\2\2\2\r\u00d3\3\2\2\2\17\u00e0\3\2")
        buf.write("\2\2\21\u00eb\3\2\2\2\23\u00f7\3\2\2\2\25\u00fd\3\2\2")
        buf.write("\2\27\u010c\3\2\2\2\31\u011a\3\2\2\2\33\u0125\3\2\2\2")
        buf.write("\35\u012a\3\2\2\2\37\u0130\3\2\2\2!\u0136\3\2\2\2#\u013c")
        buf.write("\3\2\2\2%\u0144\3\2\2\2\'\u014b\3\2\2\2)\u0150\3\2\2\2")
        buf.write("+\u0154\3\2\2\2-\u015a\3\2\2\2/\u0162\3\2\2\2\61\u0166")
        buf.write("\3\2\2\2\63\u016d\3\2\2\2\65\u0176\3\2\2\2\67\u0179\3")
        buf.write("\2\2\29\u017e\3\2\2\2;\u0187\3\2\2\2=\u018a\3\2\2\2?\u018f")
        buf.write("\3\2\2\2A\u0195\3\2\2\2C\u0198\3\2\2\2E\u01a0\3\2\2\2")
        buf.write("G\u01a2\3\2\2\2I\u01a4\3\2\2\2K\u01a6\3\2\2\2M\u01a8\3")
        buf.write("\2\2\2O\u01aa\3\2\2\2Q\u01ac\3\2\2\2S\u01af\3\2\2\2U\u01b2")
        buf.write("\3\2\2\2W\u01b5\3\2\2\2Y\u01b8\3\2\2\2[\u01ba\3\2\2\2")
        buf.write("]\u01bd\3\2\2\2_\u01bf\3\2\2\2a\u01c2\3\2\2\2c\u01c5\3")
        buf.write("\2\2\2e\u01c7\3\2\2\2g\u01c9\3\2\2\2i\u01cb\3\2\2\2k\u01cd")
        buf.write("\3\2\2\2m\u01cf\3\2\2\2o\u01d1\3\2\2\2q\u01d3\3\2\2\2")
        buf.write("s\u01d5\3\2\2\2u\u01d7\3\2\2\2w\u01d9\3\2\2\2y\u01ef\3")
        buf.write("\2\2\2{\u01fd\3\2\2\2}\u0201\3\2\2\2\177\u0203\3\2\2\2")
        buf.write("\u0081\u020a\3\2\2\2\u0083\u0215\3\2\2\2\u0085\u0218\3")
        buf.write("\2\2\2\u0087\u022c\3\2\2\2\u0089\u022e\3\2\2\2\u008b\u023e")
        buf.write("\3\2\2\2\u008d\u0240\3\2\2\2\u008f\u024c\3\2\2\2\u0091")
        buf.write("\u0254\3\2\2\2\u0093\u025a\3\2\2\2\u0095\u025d\3\2\2\2")
        buf.write("\u0097\u026b\3\2\2\2\u0099\u009a\7t\2\2\u009a\u009b\7")
        buf.write("g\2\2\u009b\u009c\7c\2\2\u009c\u009d\7f\2\2\u009d\u009e")
        buf.write("\7K\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\u00a2\7i\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\4\3\2\2\2\u00a5\u00a6\7r\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7K\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7i\2\2\u00af\u00b0")
        buf.write("\7g\2\2\u00b0\u00b1\7t\2\2\u00b1\6\3\2\2\2\u00b2\u00b3")
        buf.write("\7t\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6")
        buf.write("\7f\2\2\u00b6\u00b7\7H\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\b")
        buf.write("\3\2\2\2\u00bc\u00bd\7y\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2")
        buf.write("\7H\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7c\2\2\u00c5\u00c6\7v\2\2\u00c6\n\3\2\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7f\2\2\u00cb\u00cc\7D\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1")
        buf.write("\7c\2\2\u00d1\u00d2\7p\2\2\u00d2\f\3\2\2\2\u00d3\u00d4")
        buf.write("\7r\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7p\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7D\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7p\2\2\u00df\16")
        buf.write("\3\2\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7f\2\2\u00e4\u00e5\7U\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7i\2\2\u00ea\20\3\2\2\2\u00eb\u00ec")
        buf.write("\7r\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7U\2\2\u00f1\u00f2")
        buf.write("\7v\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7i\2\2\u00f6\22\3\2\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\u00f9\7w\2\2\u00f9\u00fa\7r\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7t\2\2\u00fc\24\3\2\2\2\u00fd\u00fe")
        buf.write("\7r\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7x\2\2\u0101\u0102\7g\2\2\u0102\u0103\7p\2\2\u0103\u0104")
        buf.write("\7v\2\2\u0104\u0105\7F\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107\u0108\7c\2\2\u0108\u0109\7w\2\2\u0109\u010a")
        buf.write("\7n\2\2\u010a\u010b\7v\2\2\u010b\26\3\2\2\2\u010c\u010d")
        buf.write("\7\61\2\2\u010d\u010e\7,\2\2\u010e\u0112\3\2\2\2\u010f")
        buf.write("\u0111\13\2\2\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2")
        buf.write("\2\u0112\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0115")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116\7,\2\2\u0116")
        buf.write("\u0117\7\61\2\2\u0117\u0118\3\2\2\2\u0118\u0119\b\f\2")
        buf.write("\2\u0119\30\3\2\2\2\u011a\u011b\7\61\2\2\u011b\u011c\7")
        buf.write("\61\2\2\u011c\u0120\3\2\2\2\u011d\u011f\n\2\2\2\u011e")
        buf.write("\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0120\3")
        buf.write("\2\2\2\u0123\u0124\b\r\2\2\u0124\32\3\2\2\2\u0125\u0126")
        buf.write("\7c\2\2\u0126\u0127\7w\2\2\u0127\u0128\7v\2\2\u0128\u0129")
        buf.write("\7q\2\2\u0129\34\3\2\2\2\u012a\u012b\7d\2\2\u012b\u012c")
        buf.write("\7t\2\2\u012c\u012d\7g\2\2\u012d\u012e\7c\2\2\u012e\u012f")
        buf.write("\7m\2\2\u012f\36\3\2\2\2\u0130\u0131\7h\2\2\u0131\u0132")
        buf.write("\7c\2\2\u0132\u0133\7n\2\2\u0133\u0134\7u\2\2\u0134\u0135")
        buf.write("\7g\2\2\u0135 \3\2\2\2\u0136\u0137\7h\2\2\u0137\u0138")
        buf.write("\7n\2\2\u0138\u0139\7q\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write("\7v\2\2\u013b\"\3\2\2\2\u013c\u013d\7k\2\2\u013d\u013e")
        buf.write("\7p\2\2\u013e\u013f\7v\2\2\u013f\u0140\7g\2\2\u0140\u0141")
        buf.write("\7i\2\2\u0141\u0142\7g\2\2\u0142\u0143\7t\2\2\u0143$\3")
        buf.write("\2\2\2\u0144\u0145\7t\2\2\u0145\u0146\7g\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7w\2\2\u0148\u0149\7t\2\2\u0149\u014a")
        buf.write("\7p\2\2\u014a&\3\2\2\2\u014b\u014c\7x\2\2\u014c\u014d")
        buf.write("\7q\2\2\u014d\u014e\7k\2\2\u014e\u014f\7f\2\2\u014f(\3")
        buf.write("\2\2\2\u0150\u0151\7q\2\2\u0151\u0152\7w\2\2\u0152\u0153")
        buf.write("\7v\2\2\u0153*\3\2\2\2\u0154\u0155\7c\2\2\u0155\u0156")
        buf.write("\7t\2\2\u0156\u0157\7t\2\2\u0157\u0158\7c\2\2\u0158\u0159")
        buf.write("\7{\2\2\u0159,\3\2\2\2\u015a\u015b\7d\2\2\u015b\u015c")
        buf.write("\7q\2\2\u015c\u015d\7q\2\2\u015d\u015e\7n\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015f\u0160\7c\2\2\u0160\u0161\7p\2\2\u0161.\3")
        buf.write("\2\2\2\u0162\u0163\7h\2\2\u0163\u0164\7q\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165\60\3\2\2\2\u0166\u0167\7u\2\2\u0167\u0168")
        buf.write("\7v\2\2\u0168\u0169\7t\2\2\u0169\u016a\7k\2\2\u016a\u016b")
        buf.write("\7p\2\2\u016b\u016c\7i\2\2\u016c\62\3\2\2\2\u016d\u016e")
        buf.write("\7e\2\2\u016e\u016f\7q\2\2\u016f\u0170\7p\2\2\u0170\u0171")
        buf.write("\7v\2\2\u0171\u0172\7k\2\2\u0172\u0173\7p\2\2\u0173\u0174")
        buf.write("\7w\2\2\u0174\u0175\7g\2\2\u0175\64\3\2\2\2\u0176\u0177")
        buf.write("\7f\2\2\u0177\u0178\7q\2\2\u0178\66\3\2\2\2\u0179\u017a")
        buf.write("\7g\2\2\u017a\u017b\7n\2\2\u017b\u017c\7u\2\2\u017c\u017d")
        buf.write("\7g\2\2\u017d8\3\2\2\2\u017e\u017f\7h\2\2\u017f\u0180")
        buf.write("\7w\2\2\u0180\u0181\7p\2\2\u0181\u0182\7e\2\2\u0182\u0183")
        buf.write("\7v\2\2\u0183\u0184\7k\2\2\u0184\u0185\7q\2\2\u0185\u0186")
        buf.write("\7p\2\2\u0186:\3\2\2\2\u0187\u0188\7k\2\2\u0188\u0189")
        buf.write("\7h\2\2\u0189<\3\2\2\2\u018a\u018b\7v\2\2\u018b\u018c")
        buf.write("\7t\2\2\u018c\u018d\7w\2\2\u018d\u018e\7g\2\2\u018e>\3")
        buf.write("\2\2\2\u018f\u0190\7y\2\2\u0190\u0191\7j\2\2\u0191\u0192")
        buf.write("\7k\2\2\u0192\u0193\7n\2\2\u0193\u0194\7g\2\2\u0194@\3")
        buf.write("\2\2\2\u0195\u0196\7q\2\2\u0196\u0197\7h\2\2\u0197B\3")
        buf.write("\2\2\2\u0198\u0199\7k\2\2\u0199\u019a\7p\2\2\u019a\u019b")
        buf.write("\7j\2\2\u019b\u019c\7g\2\2\u019c\u019d\7t\2\2\u019d\u019e")
        buf.write("\7k\2\2\u019e\u019f\7v\2\2\u019fD\3\2\2\2\u01a0\u01a1")
        buf.write("\7-\2\2\u01a1F\3\2\2\2\u01a2\u01a3\7/\2\2\u01a3H\3\2\2")
        buf.write("\2\u01a4\u01a5\7,\2\2\u01a5J\3\2\2\2\u01a6\u01a7\7\61")
        buf.write("\2\2\u01a7L\3\2\2\2\u01a8\u01a9\7\'\2\2\u01a9N\3\2\2\2")
        buf.write("\u01aa\u01ab\7#\2\2\u01abP\3\2\2\2\u01ac\u01ad\7(\2\2")
        buf.write("\u01ad\u01ae\7(\2\2\u01aeR\3\2\2\2\u01af\u01b0\7~\2\2")
        buf.write("\u01b0\u01b1\7~\2\2\u01b1T\3\2\2\2\u01b2\u01b3\7?\2\2")
        buf.write("\u01b3\u01b4\7?\2\2\u01b4V\3\2\2\2\u01b5\u01b6\7#\2\2")
        buf.write("\u01b6\u01b7\7?\2\2\u01b7X\3\2\2\2\u01b8\u01b9\7>\2\2")
        buf.write("\u01b9Z\3\2\2\2\u01ba\u01bb\7>\2\2\u01bb\u01bc\7?\2\2")
        buf.write("\u01bc\\\3\2\2\2\u01bd\u01be\7@\2\2\u01be^\3\2\2\2\u01bf")
        buf.write("\u01c0\7@\2\2\u01c0\u01c1\7?\2\2\u01c1`\3\2\2\2\u01c2")
        buf.write("\u01c3\7<\2\2\u01c3\u01c4\7<\2\2\u01c4b\3\2\2\2\u01c5")
        buf.write("\u01c6\7*\2\2\u01c6d\3\2\2\2\u01c7\u01c8\7+\2\2\u01c8")
        buf.write("f\3\2\2\2\u01c9\u01ca\7]\2\2\u01cah\3\2\2\2\u01cb\u01cc")
        buf.write("\7_\2\2\u01ccj\3\2\2\2\u01cd\u01ce\7\60\2\2\u01cel\3\2")
        buf.write("\2\2\u01cf\u01d0\7.\2\2\u01d0n\3\2\2\2\u01d1\u01d2\7=")
        buf.write("\2\2\u01d2p\3\2\2\2\u01d3\u01d4\7<\2\2\u01d4r\3\2\2\2")
        buf.write("\u01d5\u01d6\7}\2\2\u01d6t\3\2\2\2\u01d7\u01d8\7\177\2")
        buf.write("\2\u01d8v\3\2\2\2\u01d9\u01da\7?\2\2\u01dax\3\2\2\2\u01db")
        buf.write("\u01f0\7\62\2\2\u01dc\u01e0\t\3\2\2\u01dd\u01df\t\4\2")
        buf.write("\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de")
        buf.write("\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01eb\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e3\u01e5\7a\2\2\u01e4\u01e6\t\4\2\2")
        buf.write("\u01e5\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e5\3")
        buf.write("\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e3")
        buf.write("\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ec\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed\u01eb\3\2\2\2")
        buf.write("\u01ee\u01f0\b=\3\2\u01ef\u01db\3\2\2\2\u01ef\u01dc\3")
        buf.write("\2\2\2\u01f0z\3\2\2\2\u01f1\u01f3\5y=\2\u01f2\u01f4\5")
        buf.write("\177@\2\u01f3\u01f2\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5\u01f6\5\u0081A\2\u01f6\u01fe\3\2")
        buf.write("\2\2\u01f7\u01f8\5y=\2\u01f8\u01f9\5\177@\2\u01f9\u01fe")
        buf.write("\3\2\2\2\u01fa\u01fb\5\177@\2\u01fb\u01fc\5\u0081A\2\u01fc")
        buf.write("\u01fe\3\2\2\2\u01fd\u01f1\3\2\2\2\u01fd\u01f7\3\2\2\2")
        buf.write("\u01fd\u01fa\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0200\b")
        buf.write(">\4\2\u0200|\3\2\2\2\u0201\u0202\t\4\2\2\u0202~\3\2\2")
        buf.write("\2\u0203\u0207\7\60\2\2\u0204\u0206\5}?\2\u0205\u0204")
        buf.write("\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0208\3\2\2\2\u0208\u0080\3\2\2\2\u0209\u0207\3\2\2\2")
        buf.write("\u020a\u020c\t\5\2\2\u020b\u020d\t\6\2\2\u020c\u020b\3")
        buf.write("\2\2\2\u020c\u020d\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u0210")
        buf.write("\5}?\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0082\3\2\2\2\u0213")
        buf.write("\u0216\5=\37\2\u0214\u0216\5\37\20\2\u0215\u0213\3\2\2")
        buf.write("\2\u0215\u0214\3\2\2\2\u0216\u0084\3\2\2\2\u0217\u0219")
        buf.write("\7\17\2\2\u0218\u0217\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u021a\3\2\2\2\u021a\u021b\7\f\2\2\u021b\u0086\3\2\2\2")
        buf.write("\u021c\u021d\7^\2\2\u021d\u022d\7d\2\2\u021e\u021f\7^")
        buf.write("\2\2\u021f\u022d\7h\2\2\u0220\u0221\7^\2\2\u0221\u022d")
        buf.write("\7t\2\2\u0222\u0223\7^\2\2\u0223\u022d\7p\2\2\u0224\u0225")
        buf.write("\7^\2\2\u0225\u022d\7v\2\2\u0226\u0227\7^\2\2\u0227\u022d")
        buf.write("\7)\2\2\u0228\u0229\7^\2\2\u0229\u022d\7^\2\2\u022a\u022b")
        buf.write("\7^\2\2\u022b\u022d\7$\2\2\u022c\u021c\3\2\2\2\u022c\u021e")
        buf.write("\3\2\2\2\u022c\u0220\3\2\2\2\u022c\u0222\3\2\2\2\u022c")
        buf.write("\u0224\3\2\2\2\u022c\u0226\3\2\2\2\u022c\u0228\3\2\2\2")
        buf.write("\u022c\u022a\3\2\2\2\u022d\u0088\3\2\2\2\u022e\u0233\7")
        buf.write("$\2\2\u022f\u0232\5\u0087D\2\u0230\u0232\n\7\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2\2")
        buf.write("\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0236\3")
        buf.write("\2\2\2\u0235\u0233\3\2\2\2\u0236\u0237\7$\2\2\u0237\u0238")
        buf.write("\bE\5\2\u0238\u008a\3\2\2\2\u0239\u023f\5\u0089E\2\u023a")
        buf.write("\u023f\5y=\2\u023b\u023f\5{>\2\u023c\u023f\5\u0083B\2")
        buf.write("\u023d\u023f\5\u008dG\2\u023e\u0239\3\2\2\2\u023e\u023a")
        buf.write("\3\2\2\2\u023e\u023b\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023d\3\2\2\2\u023f\u008c\3\2\2\2\u0240\u0241\7}\2\2")
        buf.write("\u0241\u0247\5\u008bF\2\u0242\u0243\5m\67\2\u0243\u0244")
        buf.write("\5\u008bF\2\u0244\u0246\3\2\2\2\u0245\u0242\3\2\2\2\u0246")
        buf.write("\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2")
        buf.write("\u0248\u024a\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\7")
        buf.write("\177\2\2\u024b\u008e\3\2\2\2\u024c\u0250\t\b\2\2\u024d")
        buf.write("\u024f\t\t\2\2\u024e\u024d\3\2\2\2\u024f\u0252\3\2\2\2")
        buf.write("\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0090\3")
        buf.write("\2\2\2\u0252\u0250\3\2\2\2\u0253\u0255\t\n\2\2\u0254\u0253")
        buf.write("\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0254\3\2\2\2\u0256")
        buf.write("\u0257\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0259\bI\2\2")
        buf.write("\u0259\u0092\3\2\2\2\u025a\u025b\13\2\2\2\u025b\u025c")
        buf.write("\bJ\6\2\u025c\u0094\3\2\2\2\u025d\u0263\7$\2\2\u025e\u0262")
        buf.write("\n\13\2\2\u025f\u0260\7^\2\2\u0260\u0262\7$\2\2\u0261")
        buf.write("\u025e\3\2\2\2\u0261\u025f\3\2\2\2\u0262\u0265\3\2\2\2")
        buf.write("\u0263\u0261\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0266\3")
        buf.write("\2\2\2\u0265\u0263\3\2\2\2\u0266\u0267\t\f\2\2\u0267\u0268")
        buf.write("\n\r\2\2\u0268\u0269\3\2\2\2\u0269\u026a\bK\7\2\u026a")
        buf.write("\u0096\3\2\2\2\u026b\u0272\7$\2\2\u026c\u0271\n\7\2\2")
        buf.write("\u026d\u026e\7^\2\2\u026e\u0271\7$\2\2\u026f\u0271\5\u0087")
        buf.write("D\2\u0270\u026c\3\2\2\2\u0270\u026d\3\2\2\2\u0270\u026f")
        buf.write("\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0273\3\2\2\2\u0272")
        buf.write("\u0270\3\2\2\2\u0273\u0277\3\2\2\2\u0274\u0272\3\2\2\2")
        buf.write("\u0275\u0278\5\u0085C\2\u0276\u0278\7\2\2\3\u0277\u0275")
        buf.write("\3\2\2\2\u0277\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279")
        buf.write("\u027a\bL\b\2\u027a\u0098\3\2\2\2\34\2\u0112\u0120\u01e0")
        buf.write("\u01e7\u01eb\u01ef\u01f3\u01fd\u0207\u020c\u0211\u0215")
        buf.write("\u0218\u022c\u0231\u0233\u023e\u0247\u0250\u0256\u0261")
        buf.write("\u0263\u0270\u0272\u0277\t\b\2\2\3=\2\3>\3\3E\4\3J\5\3")
        buf.write("K\6\3L\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    C_COMMENT = 11
    CPP_COMMENT = 12
    AUTO = 13
    BREAK = 14
    FALSE = 15
    FLOAT = 16
    INTEGER = 17
    RETURN = 18
    VOID = 19
    OUT = 20
    ARRAY = 21
    BOOLEAN = 22
    FOR = 23
    STRING = 24
    CONTINUE = 25
    DO = 26
    ELSE = 27
    FUNCTION = 28
    IF = 29
    TRUE = 30
    WHILE = 31
    OF = 32
    INHERIT = 33
    ADD = 34
    SUBTRACT = 35
    MUL = 36
    DIV = 37
    MOD = 38
    NEG = 39
    AND = 40
    OR = 41
    EQUAL = 42
    DIFF = 43
    LESS = 44
    LESS_EQUAL = 45
    GREATER = 46
    GREATER_EQUAL = 47
    CONCAT = 48
    LRB = 49
    RRB = 50
    LSB = 51
    RSB = 52
    DOT = 53
    COMMA = 54
    SEMI_COLON = 55
    COLON = 56
    LCB = 57
    RCB = 58
    ASSIGN = 59
    INT_LIT = 60
    FLOAT_LIT = 61
    BOOL_LIT = 62
    STRING_LIT = 63
    ARRAY_LIT = 64
    ID = 65
    WS = 66
    ERROR_CHAR = 67
    ILLEGAL_ESCAPE = 68
    UNCLOSE_STRING = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'auto'", "'break'", "'false'", 
            "'float'", "'integer'", "'return'", "'void'", "'out'", "'array'", 
            "'boolean'", "'for'", "'string'", "'continue'", "'do'", "'else'", 
            "'function'", "'if'", "'true'", "'while'", "'of'", "'inherit'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", 
            "'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "C_COMMENT", "CPP_COMMENT", "AUTO", "BREAK", "FALSE", "FLOAT", 
            "INTEGER", "RETURN", "VOID", "OUT", "ARRAY", "BOOLEAN", "FOR", 
            "STRING", "CONTINUE", "DO", "ELSE", "FUNCTION", "IF", "TRUE", 
            "WHILE", "OF", "INHERIT", "ADD", "SUBTRACT", "MUL", "DIV", "MOD", 
            "NEG", "AND", "OR", "EQUAL", "DIFF", "LESS", "LESS_EQUAL", "GREATER", 
            "GREATER_EQUAL", "CONCAT", "LRB", "RRB", "LSB", "RSB", "DOT", 
            "COMMA", "SEMI_COLON", "COLON", "LCB", "RCB", "ASSIGN", "INT_LIT", 
            "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "ARRAY_LIT", "ID", "WS", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "C_COMMENT", "CPP_COMMENT", "AUTO", 
                  "BREAK", "FALSE", "FLOAT", "INTEGER", "RETURN", "VOID", 
                  "OUT", "ARRAY", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                  "DO", "ELSE", "FUNCTION", "IF", "TRUE", "WHILE", "OF", 
                  "INHERIT", "ADD", "SUBTRACT", "MUL", "DIV", "MOD", "NEG", 
                  "AND", "OR", "EQUAL", "DIFF", "LESS", "LESS_EQUAL", "GREATER", 
                  "GREATER_EQUAL", "CONCAT", "LRB", "RRB", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI_COLON", "COLON", "LCB", "RCB", "ASSIGN", 
                  "INT_LIT", "FLOAT_LIT", "DIGIT", "DECIMAL_PART", "EXP_PART", 
                  "BOOL_LIT", "NEWLINE", "ESCAPE", "STRING_LIT", "EXPR", 
                  "ARRAY_LIT", "ID", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.INT_LIT_action 
            actions[60] = self.FLOAT_LIT_action 
            actions[67] = self.STRING_LIT_action 
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text[1:]) 

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	string_error = self.text[1:]
            	if (string_error[-1] == "\n"):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     


