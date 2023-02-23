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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01f8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0091\n\3\f")
        buf.write("\3\16\3\u0094\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\7\4\u009f\n\4\f\4\16\4\u00a2\13\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\64\7\64\u015f\n\64\f\64")
        buf.write("\16\64\u0162\13\64\3\64\5\64\u0165\n\64\3\65\3\65\5\65")
        buf.write("\u0169\n\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5")
        buf.write("\65\u0173\n\65\3\65\3\65\3\66\3\66\3\67\3\67\7\67\u017b")
        buf.write("\n\67\f\67\16\67\u017e\13\67\38\38\58\u0182\n8\38\68\u0185")
        buf.write("\n8\r8\168\u0186\39\39\59\u018b\n9\3:\5:\u018e\n:\3:\3")
        buf.write(":\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u01a2")
        buf.write("\n;\3<\3<\3<\7<\u01a7\n<\f<\16<\u01aa\13<\3<\3<\3<\3=")
        buf.write("\3=\3=\3=\5=\u01b3\n=\3>\3>\3>\3>\7>\u01b9\n>\f>\16>\u01bc")
        buf.write("\13>\3>\3>\7>\u01c0\n>\f>\16>\u01c3\13>\7>\u01c5\n>\f")
        buf.write(">\16>\u01c8\13>\3>\3>\3?\3?\7?\u01ce\n?\f?\16?\u01d1\13")
        buf.write("?\3@\6@\u01d4\n@\r@\16@\u01d5\3@\3@\3A\3A\3A\3B\3B\3B")
        buf.write("\3B\7B\u01e1\nB\fB\16B\u01e4\13B\3B\3B\5B\u01e8\nB\3B")
        buf.write("\3B\3C\3C\3C\3C\7C\u01f0\nC\fC\16C\u01f3\13C\3C\3C\3C")
        buf.write("\3C\4\u0092\u01e2\2D\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\2m\2o\2q\67s\2u\2w8y\2{9}:\177;\u0081<\u0083")
        buf.write("=\u0085>\3\2\17\4\2\f\f\17\17\3\2\63;\4\2\62;aa\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\4\2$$^^\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\13\f\17\17\"\"\3\2$$\3\2^^\n\2$$))^^ddhhppttvv\2\u0213")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2q\3\2\2\2\2w\3\2\2\2\2{\3\2\2\2\2}")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0085\3\2\2\2\3\u0087\3\2\2\2\5\u008c\3\2\2\2\7\u009a")
        buf.write("\3\2\2\2\t\u00a5\3\2\2\2\13\u00aa\3\2\2\2\r\u00b0\3\2")
        buf.write("\2\2\17\u00b6\3\2\2\2\21\u00bc\3\2\2\2\23\u00c4\3\2\2")
        buf.write("\2\25\u00cb\3\2\2\2\27\u00d0\3\2\2\2\31\u00d4\3\2\2\2")
        buf.write("\33\u00da\3\2\2\2\35\u00e2\3\2\2\2\37\u00e6\3\2\2\2!\u00ed")
        buf.write("\3\2\2\2#\u00f6\3\2\2\2%\u00f9\3\2\2\2\'\u00fe\3\2\2\2")
        buf.write(")\u0107\3\2\2\2+\u010a\3\2\2\2-\u010f\3\2\2\2/\u0115\3")
        buf.write("\2\2\2\61\u0118\3\2\2\2\63\u0120\3\2\2\2\65\u0122\3\2")
        buf.write("\2\2\67\u0124\3\2\2\29\u0126\3\2\2\2;\u0128\3\2\2\2=\u012a")
        buf.write("\3\2\2\2?\u012c\3\2\2\2A\u012f\3\2\2\2C\u0132\3\2\2\2")
        buf.write("E\u0135\3\2\2\2G\u0138\3\2\2\2I\u013a\3\2\2\2K\u013d\3")
        buf.write("\2\2\2M\u013f\3\2\2\2O\u0142\3\2\2\2Q\u0145\3\2\2\2S\u0147")
        buf.write("\3\2\2\2U\u0149\3\2\2\2W\u014b\3\2\2\2Y\u014d\3\2\2\2")
        buf.write("[\u014f\3\2\2\2]\u0151\3\2\2\2_\u0153\3\2\2\2a\u0155\3")
        buf.write("\2\2\2c\u0157\3\2\2\2e\u0159\3\2\2\2g\u0164\3\2\2\2i\u0172")
        buf.write("\3\2\2\2k\u0176\3\2\2\2m\u0178\3\2\2\2o\u017f\3\2\2\2")
        buf.write("q\u018a\3\2\2\2s\u018d\3\2\2\2u\u01a1\3\2\2\2w\u01a3\3")
        buf.write("\2\2\2y\u01b2\3\2\2\2{\u01b4\3\2\2\2}\u01cb\3\2\2\2\177")
        buf.write("\u01d3\3\2\2\2\u0081\u01d9\3\2\2\2\u0083\u01dc\3\2\2\2")
        buf.write("\u0085\u01eb\3\2\2\2\u0087\u0088\7g\2\2\u0088\u0089\7")
        buf.write("z\2\2\u0089\u008a\7r\2\2\u008a\u008b\7t\2\2\u008b\4\3")
        buf.write("\2\2\2\u008c\u008d\7\61\2\2\u008d\u008e\7,\2\2\u008e\u0092")
        buf.write("\3\2\2\2\u008f\u0091\13\2\2\2\u0090\u008f\3\2\2\2\u0091")
        buf.write("\u0094\3\2\2\2\u0092\u0093\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0093\u0095\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\7")
        buf.write(",\2\2\u0096\u0097\7\61\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\b\3\2\2\u0099\6\3\2\2\2\u009a\u009b\7\61\2\2\u009b\u009c")
        buf.write("\7\61\2\2\u009c\u00a0\3\2\2\2\u009d\u009f\n\2\2\2\u009e")
        buf.write("\u009d\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u00a0\3")
        buf.write("\2\2\2\u00a3\u00a4\b\4\2\2\u00a4\b\3\2\2\2\u00a5\u00a6")
        buf.write("\7c\2\2\u00a6\u00a7\7w\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\n\3\2\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af")
        buf.write("\7m\2\2\u00af\f\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\16\3\2\2\2\u00b6\u00b7\7h\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\20\3\2\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1")
        buf.write("\7i\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7t\2\2\u00c3\22")
        buf.write("\3\2\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\24\3\2\2\2\u00cb\u00cc\7x\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7f\2\2\u00cf\26")
        buf.write("\3\2\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3")
        buf.write("\7v\2\2\u00d3\30\3\2\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6")
        buf.write("\7t\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7{\2\2\u00d9\32\3\2\2\2\u00da\u00db\7d\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7n\2\2\u00de\u00df")
        buf.write("\7g\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7p\2\2\u00e1\34")
        buf.write("\3\2\2\2\u00e2\u00e3\7h\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5\36\3\2\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7p\2\2\u00eb\u00ec\7i\2\2\u00ec \3\2\2\2\u00ed\u00ee")
        buf.write("\7e\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7w\2\2\u00f4\u00f5\7g\2\2\u00f5\"\3\2\2\2\u00f6\u00f7")
        buf.write("\7f\2\2\u00f7\u00f8\7q\2\2\u00f8$\3\2\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7u\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd&\3\2\2\2\u00fe\u00ff\7h\2\2\u00ff\u0100")
        buf.write("\7w\2\2\u0100\u0101\7p\2\2\u0101\u0102\7e\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7k\2\2\u0104\u0105\7q\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106(\3\2\2\2\u0107\u0108\7k\2\2\u0108\u0109")
        buf.write("\7h\2\2\u0109*\3\2\2\2\u010a\u010b\7v\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010c\u010d\7w\2\2\u010d\u010e\7g\2\2\u010e,\3")
        buf.write("\2\2\2\u010f\u0110\7y\2\2\u0110\u0111\7j\2\2\u0111\u0112")
        buf.write("\7k\2\2\u0112\u0113\7n\2\2\u0113\u0114\7g\2\2\u0114.\3")
        buf.write("\2\2\2\u0115\u0116\7q\2\2\u0116\u0117\7h\2\2\u0117\60")
        buf.write("\3\2\2\2\u0118\u0119\7k\2\2\u0119\u011a\7p\2\2\u011a\u011b")
        buf.write("\7j\2\2\u011b\u011c\7g\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write("\7k\2\2\u011e\u011f\7v\2\2\u011f\62\3\2\2\2\u0120\u0121")
        buf.write("\7-\2\2\u0121\64\3\2\2\2\u0122\u0123\7/\2\2\u0123\66\3")
        buf.write("\2\2\2\u0124\u0125\7,\2\2\u01258\3\2\2\2\u0126\u0127\7")
        buf.write("\61\2\2\u0127:\3\2\2\2\u0128\u0129\7\'\2\2\u0129<\3\2")
        buf.write("\2\2\u012a\u012b\7#\2\2\u012b>\3\2\2\2\u012c\u012d\7(")
        buf.write("\2\2\u012d\u012e\7(\2\2\u012e@\3\2\2\2\u012f\u0130\7~")
        buf.write("\2\2\u0130\u0131\7~\2\2\u0131B\3\2\2\2\u0132\u0133\7?")
        buf.write("\2\2\u0133\u0134\7?\2\2\u0134D\3\2\2\2\u0135\u0136\7#")
        buf.write("\2\2\u0136\u0137\7?\2\2\u0137F\3\2\2\2\u0138\u0139\7>")
        buf.write("\2\2\u0139H\3\2\2\2\u013a\u013b\7>\2\2\u013b\u013c\7?")
        buf.write("\2\2\u013cJ\3\2\2\2\u013d\u013e\7@\2\2\u013eL\3\2\2\2")
        buf.write("\u013f\u0140\7@\2\2\u0140\u0141\7?\2\2\u0141N\3\2\2\2")
        buf.write("\u0142\u0143\7<\2\2\u0143\u0144\7<\2\2\u0144P\3\2\2\2")
        buf.write("\u0145\u0146\7*\2\2\u0146R\3\2\2\2\u0147\u0148\7+\2\2")
        buf.write("\u0148T\3\2\2\2\u0149\u014a\7]\2\2\u014aV\3\2\2\2\u014b")
        buf.write("\u014c\7_\2\2\u014cX\3\2\2\2\u014d\u014e\7\60\2\2\u014e")
        buf.write("Z\3\2\2\2\u014f\u0150\7.\2\2\u0150\\\3\2\2\2\u0151\u0152")
        buf.write("\7=\2\2\u0152^\3\2\2\2\u0153\u0154\7<\2\2\u0154`\3\2\2")
        buf.write("\2\u0155\u0156\7}\2\2\u0156b\3\2\2\2\u0157\u0158\7\177")
        buf.write("\2\2\u0158d\3\2\2\2\u0159\u015a\7?\2\2\u015af\3\2\2\2")
        buf.write("\u015b\u0165\7\62\2\2\u015c\u0160\t\3\2\2\u015d\u015f")
        buf.write("\t\4\2\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2")
        buf.write("\u0162\u0160\3\2\2\2\u0163\u0165\b\64\3\2\u0164\u015b")
        buf.write("\3\2\2\2\u0164\u015c\3\2\2\2\u0165h\3\2\2\2\u0166\u0168")
        buf.write("\5g\64\2\u0167\u0169\5m\67\2\u0168\u0167\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\5o8\2\u016b")
        buf.write("\u0173\3\2\2\2\u016c\u016d\5g\64\2\u016d\u016e\5m\67\2")
        buf.write("\u016e\u0173\3\2\2\2\u016f\u0170\5m\67\2\u0170\u0171\5")
        buf.write("o8\2\u0171\u0173\3\2\2\2\u0172\u0166\3\2\2\2\u0172\u016c")
        buf.write("\3\2\2\2\u0172\u016f\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0175\b\65\4\2\u0175j\3\2\2\2\u0176\u0177\t\5\2\2\u0177")
        buf.write("l\3\2\2\2\u0178\u017c\7\60\2\2\u0179\u017b\5k\66\2\u017a")
        buf.write("\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017dn\3\2\2\2\u017e\u017c\3\2\2")
        buf.write("\2\u017f\u0181\t\6\2\2\u0180\u0182\t\7\2\2\u0181\u0180")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184\3\2\2\2\u0183")
        buf.write("\u0185\5k\66\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187p\3\2\2")
        buf.write("\2\u0188\u018b\5+\26\2\u0189\u018b\5\r\7\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u0189\3\2\2\2\u018br\3\2\2\2\u018c\u018e")
        buf.write("\7\17\2\2\u018d\u018c\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u0190\7\f\2\2\u0190t\3\2\2\2\u0191")
        buf.write("\u0192\7^\2\2\u0192\u01a2\7d\2\2\u0193\u0194\7^\2\2\u0194")
        buf.write("\u01a2\7h\2\2\u0195\u0196\7^\2\2\u0196\u01a2\7t\2\2\u0197")
        buf.write("\u0198\7^\2\2\u0198\u01a2\7p\2\2\u0199\u019a\7^\2\2\u019a")
        buf.write("\u01a2\7v\2\2\u019b\u019c\7^\2\2\u019c\u01a2\7)\2\2\u019d")
        buf.write("\u019e\7^\2\2\u019e\u01a2\7^\2\2\u019f\u01a0\7^\2\2\u01a0")
        buf.write("\u01a2\7$\2\2\u01a1\u0191\3\2\2\2\u01a1\u0193\3\2\2\2")
        buf.write("\u01a1\u0195\3\2\2\2\u01a1\u0197\3\2\2\2\u01a1\u0199\3")
        buf.write("\2\2\2\u01a1\u019b\3\2\2\2\u01a1\u019d\3\2\2\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a2v\3\2\2\2\u01a3\u01a8\7$\2\2\u01a4\u01a7")
        buf.write("\5u;\2\u01a5\u01a7\n\b\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01ab\u01ac\7$\2\2\u01ac\u01ad\b<\5\2\u01adx\3\2\2\2")
        buf.write("\u01ae\u01b3\5g\64\2\u01af\u01b3\5i\65\2\u01b0\u01b3\5")
        buf.write("q9\2\u01b1\u01b3\5w<\2\u01b2\u01ae\3\2\2\2\u01b2\u01af")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3")
        buf.write("z\3\2\2\2\u01b4\u01b5\7}\2\2\u01b5\u01c6\5y=\2\u01b6\u01ba")
        buf.write("\7.\2\2\u01b7\u01b9\7\"\2\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01c1\5")
        buf.write("y=\2\u01be\u01c0\7\"\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c3")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01b6\3\2\2\2")
        buf.write("\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3")
        buf.write("\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca")
        buf.write("\7\177\2\2\u01ca|\3\2\2\2\u01cb\u01cf\t\t\2\2\u01cc\u01ce")
        buf.write("\t\n\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0~\3\2\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d2\u01d4\t\13\2\2\u01d3\u01d2\3\2\2")
        buf.write("\2\u01d4\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\b@\2\2\u01d8")
        buf.write("\u0080\3\2\2\2\u01d9\u01da\13\2\2\2\u01da\u01db\bA\6\2")
        buf.write("\u01db\u0082\3\2\2\2\u01dc\u01e2\7$\2\2\u01dd\u01e1\n")
        buf.write("\f\2\2\u01de\u01df\7^\2\2\u01df\u01e1\7$\2\2\u01e0\u01dd")
        buf.write("\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e7\3\2\2\2")
        buf.write("\u01e4\u01e2\3\2\2\2\u01e5\u01e8\5s:\2\u01e6\u01e8\7\2")
        buf.write("\2\3\u01e7\u01e5\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01e9")
        buf.write("\3\2\2\2\u01e9\u01ea\bB\7\2\u01ea\u0084\3\2\2\2\u01eb")
        buf.write("\u01f1\7$\2\2\u01ec\u01f0\n\f\2\2\u01ed\u01ee\7^\2\2\u01ee")
        buf.write("\u01f0\7$\2\2\u01ef\u01ec\3\2\2\2\u01ef\u01ed\3\2\2\2")
        buf.write("\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3")
        buf.write("\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f5")
        buf.write("\t\r\2\2\u01f5\u01f6\n\16\2\2\u01f6\u01f7\bC\b\2\u01f7")
        buf.write("\u0086\3\2\2\2\34\2\u0092\u00a0\u0160\u0164\u0168\u0172")
        buf.write("\u017c\u0181\u0186\u018a\u018d\u01a1\u01a6\u01a8\u01b2")
        buf.write("\u01ba\u01c1\u01c6\u01cf\u01d5\u01e0\u01e2\u01e7\u01ef")
        buf.write("\u01f1\t\b\2\2\3\64\2\3\65\3\3<\4\3A\5\3B\6\3C\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    C_COMMENT = 2
    CPP_COMMENT = 3
    AUTO = 4
    BREAK = 5
    FALSE = 6
    FLOAT = 7
    INTEGER = 8
    RETURN = 9
    VOID = 10
    OUT = 11
    ARRAY = 12
    BOOLEAN = 13
    FOR = 14
    STRING = 15
    CONTINUE = 16
    DO = 17
    ELSE = 18
    FUNCTION = 19
    IF = 20
    TRUE = 21
    WHILE = 22
    OF = 23
    INHERIT = 24
    ADD = 25
    SUBTRACT = 26
    MUL = 27
    DIV = 28
    MOD = 29
    NEG = 30
    AND = 31
    OR = 32
    EQUAL = 33
    DIFF = 34
    LESS = 35
    LESS_EQUAL = 36
    GREATER = 37
    GREATER_EQUAL = 38
    CONCAT = 39
    LRB = 40
    RRB = 41
    LSB = 42
    RSB = 43
    DOT = 44
    COMMA = 45
    SEMI_COLON = 46
    COLON = 47
    LCB = 48
    RCB = 49
    ASSIGN = 50
    INT_LIT = 51
    FLOAT_LIT = 52
    BOOL_LIT = 53
    STRING_LIT = 54
    ARRAY_LIT = 55
    ID = 56
    WS = 57
    ERROR_CHAR = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'expr'", "'auto'", "'break'", "'false'", "'float'", "'integer'", 
            "'return'", "'void'", "'out'", "'array'", "'boolean'", "'for'", 
            "'string'", "'continue'", "'do'", "'else'", "'function'", "'if'", 
            "'true'", "'while'", "'of'", "'inherit'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", 
            "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "C_COMMENT", "CPP_COMMENT", "AUTO", "BREAK", "FALSE", "FLOAT", 
            "INTEGER", "RETURN", "VOID", "OUT", "ARRAY", "BOOLEAN", "FOR", 
            "STRING", "CONTINUE", "DO", "ELSE", "FUNCTION", "IF", "TRUE", 
            "WHILE", "OF", "INHERIT", "ADD", "SUBTRACT", "MUL", "DIV", "MOD", 
            "NEG", "AND", "OR", "EQUAL", "DIFF", "LESS", "LESS_EQUAL", "GREATER", 
            "GREATER_EQUAL", "CONCAT", "LRB", "RRB", "LSB", "RSB", "DOT", 
            "COMMA", "SEMI_COLON", "COLON", "LCB", "RCB", "ASSIGN", "INT_LIT", 
            "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "ARRAY_LIT", "ID", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "C_COMMENT", "CPP_COMMENT", "AUTO", "BREAK", "FALSE", 
                  "FLOAT", "INTEGER", "RETURN", "VOID", "OUT", "ARRAY", 
                  "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "ELSE", 
                  "FUNCTION", "IF", "TRUE", "WHILE", "OF", "INHERIT", "ADD", 
                  "SUBTRACT", "MUL", "DIV", "MOD", "NEG", "AND", "OR", "EQUAL", 
                  "DIFF", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                  "CONCAT", "LRB", "RRB", "LSB", "RSB", "DOT", "COMMA", 
                  "SEMI_COLON", "COLON", "LCB", "RCB", "ASSIGN", "INT_LIT", 
                  "FLOAT_LIT", "DIGIT", "DECIMAL_PART", "EXP_PART", "BOOL_LIT", 
                  "NEWLINE", "ESCAPE", "STRING_LIT", "EXPR", "ARRAY_LIT", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[50] = self.INT_LIT_action 
            actions[51] = self.FLOAT_LIT_action 
            actions[58] = self.STRING_LIT_action 
            actions[63] = self.ERROR_CHAR_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
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

            	self.text = self.text[1:-1].replace("\\", "")

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise IllegalEscape(self.text[1:]) 

     


