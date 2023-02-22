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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01cc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\7\2\u0088\n\2\f\2\16\2\u008b\13\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\7\3\u0096\n\3\f\3\16\3\u0099\13\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\7\63\u0156")
        buf.write("\n\63\f\63\16\63\u0159\13\63\3\63\5\63\u015c\n\63\3\64")
        buf.write("\3\64\5\64\u0160\n\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\5\64\u016a\n\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\6\66\u0172\n\66\r\66\16\66\u0173\3\67\3\67\5\67\u0178")
        buf.write("\n\67\3\67\6\67\u017b\n\67\r\67\16\67\u017c\38\38\58\u0181")
        buf.write("\n8\39\39\39\3:\3:\3:\7:\u0189\n:\f:\16:\u018c\13:\3:")
        buf.write("\3:\3:\3;\3;\3;\3;\5;\u0195\n;\3<\3<\3<\3<\7<\u019b\n")
        buf.write("<\f<\16<\u019e\13<\3<\3<\7<\u01a2\n<\f<\16<\u01a5\13<")
        buf.write("\7<\u01a7\n<\f<\16<\u01aa\13<\3<\3<\3=\3=\7=\u01b0\n=")
        buf.write("\f=\16=\u01b3\13=\3>\6>\u01b6\n>\r>\16>\u01b7\3>\3>\3")
        buf.write("?\3?\3?\3@\3@\3A\3A\7A\u01c3\nA\fA\16A\u01c6\13A\3A\3")
        buf.write("A\3A\3A\3A\3\u0089\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\2k\2m\2o\66q\2s\67u\2w8y9{:};\177<\u0081=\3\2\17")
        buf.write("\4\2\f\f\17\17\3\2\63;\4\2\62;aa\3\2\62;\4\2GGgg\4\2-")
        buf.write("-//\3\2^^\n\2$$))^^ddhhppttvv\4\2$$^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\3\2\60\60\2\u01dc\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("o\3\2\2\2\2s\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2")
        buf.write("\2\2\5\u0091\3\2\2\2\7\u009c\3\2\2\2\t\u00a1\3\2\2\2\13")
        buf.write("\u00a7\3\2\2\2\r\u00ad\3\2\2\2\17\u00b3\3\2\2\2\21\u00bb")
        buf.write("\3\2\2\2\23\u00c2\3\2\2\2\25\u00c7\3\2\2\2\27\u00cb\3")
        buf.write("\2\2\2\31\u00d1\3\2\2\2\33\u00d9\3\2\2\2\35\u00dd\3\2")
        buf.write("\2\2\37\u00e4\3\2\2\2!\u00ed\3\2\2\2#\u00f0\3\2\2\2%\u00f5")
        buf.write("\3\2\2\2\'\u00fe\3\2\2\2)\u0101\3\2\2\2+\u0106\3\2\2\2")
        buf.write("-\u010c\3\2\2\2/\u010f\3\2\2\2\61\u0117\3\2\2\2\63\u0119")
        buf.write("\3\2\2\2\65\u011b\3\2\2\2\67\u011d\3\2\2\29\u011f\3\2")
        buf.write("\2\2;\u0121\3\2\2\2=\u0123\3\2\2\2?\u0126\3\2\2\2A\u0129")
        buf.write("\3\2\2\2C\u012c\3\2\2\2E\u012f\3\2\2\2G\u0131\3\2\2\2")
        buf.write("I\u0134\3\2\2\2K\u0136\3\2\2\2M\u0139\3\2\2\2O\u013c\3")
        buf.write("\2\2\2Q\u013e\3\2\2\2S\u0140\3\2\2\2U\u0142\3\2\2\2W\u0144")
        buf.write("\3\2\2\2Y\u0146\3\2\2\2[\u0148\3\2\2\2]\u014a\3\2\2\2")
        buf.write("_\u014c\3\2\2\2a\u014e\3\2\2\2c\u0150\3\2\2\2e\u015b\3")
        buf.write("\2\2\2g\u0169\3\2\2\2i\u016d\3\2\2\2k\u016f\3\2\2\2m\u0175")
        buf.write("\3\2\2\2o\u0180\3\2\2\2q\u0182\3\2\2\2s\u0185\3\2\2\2")
        buf.write("u\u0194\3\2\2\2w\u0196\3\2\2\2y\u01ad\3\2\2\2{\u01b5\3")
        buf.write("\2\2\2}\u01bb\3\2\2\2\177\u01be\3\2\2\2\u0081\u01c0\3")
        buf.write("\2\2\2\u0083\u0084\7\61\2\2\u0084\u0085\7,\2\2\u0085\u0089")
        buf.write("\3\2\2\2\u0086\u0088\13\2\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\u008b\3\2\2\2\u0089\u008a\3\2\2\2\u0089\u0087\3\2\2\2")
        buf.write("\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\7")
        buf.write(",\2\2\u008d\u008e\7\61\2\2\u008e\u008f\3\2\2\2\u008f\u0090")
        buf.write("\b\2\2\2\u0090\4\3\2\2\2\u0091\u0092\7\61\2\2\u0092\u0093")
        buf.write("\7\61\2\2\u0093\u0097\3\2\2\2\u0094\u0096\n\2\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u009a\u009b\b\3\2\2\u009b\6\3\2\2\2\u009c\u009d")
        buf.write("\7c\2\2\u009d\u009e\7w\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7q\2\2\u00a0\b\3\2\2\2\u00a1\u00a2\7d\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7m\2\2\u00a6\n\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7n\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\f\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7n\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\16\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8")
        buf.write("\7i\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7t\2\2\u00ba\20")
        buf.write("\3\2\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7p\2\2\u00c1\22\3\2\2\2\u00c2\u00c3\7x\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7f\2\2\u00c6\24")
        buf.write("\3\2\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\26\3\2\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7{\2\2\u00d0\30\3\2\2\2\u00d1\u00d2\7d\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7p\2\2\u00d8\32")
        buf.write("\3\2\2\2\u00d9\u00da\7h\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7t\2\2\u00dc\34\3\2\2\2\u00dd\u00de\7u\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7i\2\2\u00e3\36\3\2\2\2\u00e4\u00e5")
        buf.write("\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7w\2\2\u00eb\u00ec\7g\2\2\u00ec \3\2\2\2\u00ed\u00ee")
        buf.write("\7f\2\2\u00ee\u00ef\7q\2\2\u00ef\"\3\2\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7u\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4$\3\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7")
        buf.write("\7w\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd&\3\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7h\2\2\u0100(\3\2\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7w\2\2\u0104\u0105\7g\2\2\u0105*\3")
        buf.write("\2\2\2\u0106\u0107\7y\2\2\u0107\u0108\7j\2\2\u0108\u0109")
        buf.write("\7k\2\2\u0109\u010a\7n\2\2\u010a\u010b\7g\2\2\u010b,\3")
        buf.write("\2\2\2\u010c\u010d\7q\2\2\u010d\u010e\7h\2\2\u010e.\3")
        buf.write("\2\2\2\u010f\u0110\7k\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7j\2\2\u0112\u0113\7g\2\2\u0113\u0114\7t\2\2\u0114\u0115")
        buf.write("\7k\2\2\u0115\u0116\7v\2\2\u0116\60\3\2\2\2\u0117\u0118")
        buf.write("\7-\2\2\u0118\62\3\2\2\2\u0119\u011a\7/\2\2\u011a\64\3")
        buf.write("\2\2\2\u011b\u011c\7,\2\2\u011c\66\3\2\2\2\u011d\u011e")
        buf.write("\7\61\2\2\u011e8\3\2\2\2\u011f\u0120\7\'\2\2\u0120:\3")
        buf.write("\2\2\2\u0121\u0122\7#\2\2\u0122<\3\2\2\2\u0123\u0124\7")
        buf.write("(\2\2\u0124\u0125\7(\2\2\u0125>\3\2\2\2\u0126\u0127\7")
        buf.write("~\2\2\u0127\u0128\7~\2\2\u0128@\3\2\2\2\u0129\u012a\7")
        buf.write("?\2\2\u012a\u012b\7?\2\2\u012bB\3\2\2\2\u012c\u012d\7")
        buf.write("#\2\2\u012d\u012e\7?\2\2\u012eD\3\2\2\2\u012f\u0130\7")
        buf.write(">\2\2\u0130F\3\2\2\2\u0131\u0132\7>\2\2\u0132\u0133\7")
        buf.write("?\2\2\u0133H\3\2\2\2\u0134\u0135\7@\2\2\u0135J\3\2\2\2")
        buf.write("\u0136\u0137\7@\2\2\u0137\u0138\7?\2\2\u0138L\3\2\2\2")
        buf.write("\u0139\u013a\7<\2\2\u013a\u013b\7<\2\2\u013bN\3\2\2\2")
        buf.write("\u013c\u013d\7*\2\2\u013dP\3\2\2\2\u013e\u013f\7+\2\2")
        buf.write("\u013fR\3\2\2\2\u0140\u0141\7]\2\2\u0141T\3\2\2\2\u0142")
        buf.write("\u0143\7_\2\2\u0143V\3\2\2\2\u0144\u0145\7\60\2\2\u0145")
        buf.write("X\3\2\2\2\u0146\u0147\7.\2\2\u0147Z\3\2\2\2\u0148\u0149")
        buf.write("\7=\2\2\u0149\\\3\2\2\2\u014a\u014b\7<\2\2\u014b^\3\2")
        buf.write("\2\2\u014c\u014d\7}\2\2\u014d`\3\2\2\2\u014e\u014f\7\177")
        buf.write("\2\2\u014fb\3\2\2\2\u0150\u0151\7?\2\2\u0151d\3\2\2\2")
        buf.write("\u0152\u015c\7\62\2\2\u0153\u0157\t\3\2\2\u0154\u0156")
        buf.write("\t\4\2\2\u0155\u0154\3\2\2\2\u0156\u0159\3\2\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015a\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u015a\u015c\b\63\3\2\u015b\u0152")
        buf.write("\3\2\2\2\u015b\u0153\3\2\2\2\u015cf\3\2\2\2\u015d\u015f")
        buf.write("\5e\63\2\u015e\u0160\5k\66\2\u015f\u015e\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\5m\67\2")
        buf.write("\u0162\u016a\3\2\2\2\u0163\u0164\5e\63\2\u0164\u0165\5")
        buf.write("k\66\2\u0165\u016a\3\2\2\2\u0166\u0167\5k\66\2\u0167\u0168")
        buf.write("\5m\67\2\u0168\u016a\3\2\2\2\u0169\u015d\3\2\2\2\u0169")
        buf.write("\u0163\3\2\2\2\u0169\u0166\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016c\b\64\4\2\u016ch\3\2\2\2\u016d\u016e\t\5\2")
        buf.write("\2\u016ej\3\2\2\2\u016f\u0171\7\60\2\2\u0170\u0172\5i")
        buf.write("\65\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174l\3\2\2\2\u0175\u0177")
        buf.write("\t\6\2\2\u0176\u0178\t\7\2\2\u0177\u0176\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u017b\5i\65\2")
        buf.write("\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017a\3")
        buf.write("\2\2\2\u017c\u017d\3\2\2\2\u017dn\3\2\2\2\u017e\u0181")
        buf.write("\5)\25\2\u017f\u0181\5\13\6\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181p\3\2\2\2\u0182\u0183\t\b\2\2\u0183")
        buf.write("\u0184\t\t\2\2\u0184r\3\2\2\2\u0185\u018a\7$\2\2\u0186")
        buf.write("\u0189\5q9\2\u0187\u0189\n\n\2\2\u0188\u0186\3\2\2\2\u0188")
        buf.write("\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2")
        buf.write("\u018a\u018b\3\2\2\2\u018b\u018d\3\2\2\2\u018c\u018a\3")
        buf.write("\2\2\2\u018d\u018e\7$\2\2\u018e\u018f\b:\5\2\u018ft\3")
        buf.write("\2\2\2\u0190\u0195\5e\63\2\u0191\u0195\5g\64\2\u0192\u0195")
        buf.write("\5o8\2\u0193\u0195\5s:\2\u0194\u0190\3\2\2\2\u0194\u0191")
        buf.write("\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("v\3\2\2\2\u0196\u0197\7}\2\2\u0197\u01a8\5u;\2\u0198\u019c")
        buf.write("\7.\2\2\u0199\u019b\7\"\2\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("\u019e\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019d\u019f\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a3\5")
        buf.write("u;\2\u01a0\u01a2\7\"\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u0198\3\2\2\2")
        buf.write("\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3")
        buf.write("\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac")
        buf.write("\7\177\2\2\u01acx\3\2\2\2\u01ad\u01b1\t\13\2\2\u01ae\u01b0")
        buf.write("\t\f\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2z\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4\u01b6\t\r\2\2\u01b5\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3")
        buf.write("\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\b>\2\2\u01ba|\3")
        buf.write("\2\2\2\u01bb\u01bc\13\2\2\2\u01bc\u01bd\b?\6\2\u01bd~")
        buf.write("\3\2\2\2\u01be\u01bf\13\2\2\2\u01bf\u0080\3\2\2\2\u01c0")
        buf.write("\u01c4\7$\2\2\u01c1\u01c3\t\16\2\2\u01c2\u01c1\3\2\2\2")
        buf.write("\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3")
        buf.write("\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8")
        buf.write("\7^\2\2\u01c8\u01c9\7e\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb")
        buf.write("\bA\7\2\u01cb\u0082\3\2\2\2\26\2\u0089\u0097\u0157\u015b")
        buf.write("\u015f\u0169\u0173\u0177\u017c\u0180\u0188\u018a\u0194")
        buf.write("\u019c\u01a3\u01a8\u01b1\u01b7\u01c4\b\b\2\2\3\63\2\3")
        buf.write("\64\3\3:\4\3?\5\3A\6")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    C_COMMENT = 1
    CPP_COMMENT = 2
    AUTO = 3
    BREAK = 4
    FALSE = 5
    FLOAT = 6
    INTEGER = 7
    RETURN = 8
    VOID = 9
    OUT = 10
    ARRAY = 11
    BOOLEAN = 12
    FOR = 13
    STRING = 14
    CONTINUE = 15
    DO = 16
    ELSE = 17
    FUNCTION = 18
    IF = 19
    TRUE = 20
    WHILE = 21
    OF = 22
    INHERIT = 23
    ADD = 24
    SUBTRACT = 25
    MUL = 26
    DIV = 27
    MOD = 28
    NEG = 29
    AND = 30
    OR = 31
    EQUAL = 32
    DIFF = 33
    LESS = 34
    LESS_EQUAL = 35
    GREATER = 36
    GREATER_EQUAL = 37
    CONCAT = 38
    LRB = 39
    RRB = 40
    LSB = 41
    RSB = 42
    DOT = 43
    COMMA = 44
    SEMI_COLON = 45
    COLON = 46
    LCB = 47
    RCB = 48
    ASSIGN = 49
    INT_LIT = 50
    FLOAT_LIT = 51
    BOOL_LIT = 52
    STRING_LIT = 53
    ARRAY_LIT = 54
    ID = 55
    WS = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'false'", "'float'", "'integer'", "'return'", 
            "'void'", "'out'", "'array'", "'boolean'", "'for'", "'string'", 
            "'continue'", "'do'", "'else'", "'function'", "'if'", "'true'", 
            "'while'", "'of'", "'inherit'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

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

    ruleNames = [ "C_COMMENT", "CPP_COMMENT", "AUTO", "BREAK", "FALSE", 
                  "FLOAT", "INTEGER", "RETURN", "VOID", "OUT", "ARRAY", 
                  "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "ELSE", 
                  "FUNCTION", "IF", "TRUE", "WHILE", "OF", "INHERIT", "ADD", 
                  "SUBTRACT", "MUL", "DIV", "MOD", "NEG", "AND", "OR", "EQUAL", 
                  "DIFF", "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                  "CONCAT", "LRB", "RRB", "LSB", "RSB", "DOT", "COMMA", 
                  "SEMI_COLON", "COLON", "LCB", "RCB", "ASSIGN", "INT_LIT", 
                  "FLOAT_LIT", "DIGIT", "DECIMAL_PART", "EXP_PART", "BOOL_LIT", 
                  "ESCAPE", "STRING_LIT", "EXPR", "ARRAY_LIT", "ID", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[49] = self.INT_LIT_action 
            actions[50] = self.FLOAT_LIT_action 
            actions[56] = self.STRING_LIT_action 
            actions[61] = self.ERROR_CHAR_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
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

            	escapes = ['b', 'f', 'r', 'n', 't', '\'', '\\']
            	self.text = self.text[1:-1].replace('\\"', '"')
            	idx = self.text.find('\\')
            	l = len(self.text)
            	if idx != -1 and self.text[idx + 1] not in escapes:
            		raise IllegalEscape(self.text[0:idx + 1])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text) 
     


