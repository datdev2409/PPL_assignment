# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\u01bf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\7")
        buf.write("\2\u0086\n\2\f\2\16\2\u0089\13\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\7\3\u0094\n\3\f\3\16\3\u0097\13\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\7\63\u0154\n")
        buf.write("\63\f\63\16\63\u0157\13\63\3\63\5\63\u015a\n\63\3\64\3")
        buf.write("\64\5\64\u015e\n\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\5\64\u0168\n\64\3\64\3\64\3\65\3\65\3\66\3\66\6")
        buf.write("\66\u0170\n\66\r\66\16\66\u0171\3\67\3\67\5\67\u0176\n")
        buf.write("\67\3\67\6\67\u0179\n\67\r\67\16\67\u017a\38\38\58\u017f")
        buf.write("\n8\39\39\39\39\79\u0185\n9\f9\169\u0188\139\39\39\39")
        buf.write("\3:\3:\3:\3:\5:\u0191\n:\3;\3;\3;\3;\7;\u0197\n;\f;\16")
        buf.write(";\u019a\13;\3;\3;\7;\u019e\n;\f;\16;\u01a1\13;\7;\u01a3")
        buf.write("\n;\f;\16;\u01a6\13;\3;\3;\3<\3<\7<\u01ac\n<\f<\16<\u01af")
        buf.write("\13<\3=\6=\u01b2\n=\r=\16=\u01b3\3=\3=\3>\3>\3>\3?\3?")
        buf.write("\3@\3@\3@\3\u0087\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\2k\2m\2o\66q\67s\2u8w9y:{;}<\177=\3\2\r\4\2\f\f")
        buf.write("\17\17\3\2\63;\4\2\62;aa\3\2\62;\4\2GGgg\4\2--//\3\2^")
        buf.write("^\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2")
        buf.write("\u01cf\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0081")
        buf.write("\3\2\2\2\5\u008f\3\2\2\2\7\u009a\3\2\2\2\t\u009f\3\2\2")
        buf.write("\2\13\u00a5\3\2\2\2\r\u00ab\3\2\2\2\17\u00b1\3\2\2\2\21")
        buf.write("\u00b9\3\2\2\2\23\u00c0\3\2\2\2\25\u00c5\3\2\2\2\27\u00c9")
        buf.write("\3\2\2\2\31\u00cf\3\2\2\2\33\u00d7\3\2\2\2\35\u00db\3")
        buf.write("\2\2\2\37\u00e2\3\2\2\2!\u00eb\3\2\2\2#\u00ee\3\2\2\2")
        buf.write("%\u00f3\3\2\2\2\'\u00fc\3\2\2\2)\u00ff\3\2\2\2+\u0104")
        buf.write("\3\2\2\2-\u010a\3\2\2\2/\u010d\3\2\2\2\61\u0115\3\2\2")
        buf.write("\2\63\u0117\3\2\2\2\65\u0119\3\2\2\2\67\u011b\3\2\2\2")
        buf.write("9\u011d\3\2\2\2;\u011f\3\2\2\2=\u0121\3\2\2\2?\u0124\3")
        buf.write("\2\2\2A\u0127\3\2\2\2C\u012a\3\2\2\2E\u012d\3\2\2\2G\u012f")
        buf.write("\3\2\2\2I\u0132\3\2\2\2K\u0134\3\2\2\2M\u0137\3\2\2\2")
        buf.write("O\u013a\3\2\2\2Q\u013c\3\2\2\2S\u013e\3\2\2\2U\u0140\3")
        buf.write("\2\2\2W\u0142\3\2\2\2Y\u0144\3\2\2\2[\u0146\3\2\2\2]\u0148")
        buf.write("\3\2\2\2_\u014a\3\2\2\2a\u014c\3\2\2\2c\u014e\3\2\2\2")
        buf.write("e\u0159\3\2\2\2g\u0167\3\2\2\2i\u016b\3\2\2\2k\u016d\3")
        buf.write("\2\2\2m\u0173\3\2\2\2o\u017e\3\2\2\2q\u0180\3\2\2\2s\u0190")
        buf.write("\3\2\2\2u\u0192\3\2\2\2w\u01a9\3\2\2\2y\u01b1\3\2\2\2")
        buf.write("{\u01b7\3\2\2\2}\u01ba\3\2\2\2\177\u01bc\3\2\2\2\u0081")
        buf.write("\u0082\7\61\2\2\u0082\u0083\7,\2\2\u0083\u0087\3\2\2\2")
        buf.write("\u0084\u0086\13\2\2\2\u0085\u0084\3\2\2\2\u0086\u0089")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0087\u0085\3\2\2\2\u0088")
        buf.write("\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008b\7,\2\2")
        buf.write("\u008b\u008c\7\61\2\2\u008c\u008d\3\2\2\2\u008d\u008e")
        buf.write("\b\2\2\2\u008e\4\3\2\2\2\u008f\u0090\7\61\2\2\u0090\u0091")
        buf.write("\7\61\2\2\u0091\u0095\3\2\2\2\u0092\u0094\n\2\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3")
        buf.write("\2\2\2\u0098\u0099\b\3\2\2\u0099\6\3\2\2\2\u009a\u009b")
        buf.write("\7c\2\2\u009b\u009c\7w\2\2\u009c\u009d\7v\2\2\u009d\u009e")
        buf.write("\7q\2\2\u009e\b\3\2\2\2\u009f\u00a0\7d\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4")
        buf.write("\7m\2\2\u00a4\n\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\f\3\2\2\2\u00ab\u00ac\7h\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7c\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\16\3\2\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7i\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7t\2\2\u00b8\20")
        buf.write("\3\2\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\22\3\2\2\2\u00c0\u00c1\7x\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7f\2\2\u00c4\24")
        buf.write("\3\2\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\26\3\2\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce")
        buf.write("\7{\2\2\u00ce\30\3\2\2\2\u00cf\u00d0\7d\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7p\2\2\u00d6\32")
        buf.write("\3\2\2\2\u00d7\u00d8\7h\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da")
        buf.write("\7t\2\2\u00da\34\3\2\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7k\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7i\2\2\u00e1\36\3\2\2\2\u00e2\u00e3")
        buf.write("\7e\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7w\2\2\u00e9\u00ea\7g\2\2\u00ea \3\2\2\2\u00eb\u00ec")
        buf.write("\7f\2\2\u00ec\u00ed\7q\2\2\u00ed\"\3\2\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2$\3\2\2\2\u00f3\u00f4\7h\2\2\u00f4\u00f5")
        buf.write("\7w\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7e\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7p\2\2\u00fb&\3\2\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe")
        buf.write("\7h\2\2\u00fe(\3\2\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7w\2\2\u0102\u0103\7g\2\2\u0103*\3")
        buf.write("\2\2\2\u0104\u0105\7y\2\2\u0105\u0106\7j\2\2\u0106\u0107")
        buf.write("\7k\2\2\u0107\u0108\7n\2\2\u0108\u0109\7g\2\2\u0109,\3")
        buf.write("\2\2\2\u010a\u010b\7q\2\2\u010b\u010c\7h\2\2\u010c.\3")
        buf.write("\2\2\2\u010d\u010e\7k\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7j\2\2\u0110\u0111\7g\2\2\u0111\u0112\7t\2\2\u0112\u0113")
        buf.write("\7k\2\2\u0113\u0114\7v\2\2\u0114\60\3\2\2\2\u0115\u0116")
        buf.write("\7-\2\2\u0116\62\3\2\2\2\u0117\u0118\7/\2\2\u0118\64\3")
        buf.write("\2\2\2\u0119\u011a\7,\2\2\u011a\66\3\2\2\2\u011b\u011c")
        buf.write("\7\61\2\2\u011c8\3\2\2\2\u011d\u011e\7\'\2\2\u011e:\3")
        buf.write("\2\2\2\u011f\u0120\7#\2\2\u0120<\3\2\2\2\u0121\u0122\7")
        buf.write("(\2\2\u0122\u0123\7(\2\2\u0123>\3\2\2\2\u0124\u0125\7")
        buf.write("~\2\2\u0125\u0126\7~\2\2\u0126@\3\2\2\2\u0127\u0128\7")
        buf.write("?\2\2\u0128\u0129\7?\2\2\u0129B\3\2\2\2\u012a\u012b\7")
        buf.write("#\2\2\u012b\u012c\7?\2\2\u012cD\3\2\2\2\u012d\u012e\7")
        buf.write(">\2\2\u012eF\3\2\2\2\u012f\u0130\7>\2\2\u0130\u0131\7")
        buf.write("?\2\2\u0131H\3\2\2\2\u0132\u0133\7@\2\2\u0133J\3\2\2\2")
        buf.write("\u0134\u0135\7@\2\2\u0135\u0136\7?\2\2\u0136L\3\2\2\2")
        buf.write("\u0137\u0138\7<\2\2\u0138\u0139\7<\2\2\u0139N\3\2\2\2")
        buf.write("\u013a\u013b\7*\2\2\u013bP\3\2\2\2\u013c\u013d\7+\2\2")
        buf.write("\u013dR\3\2\2\2\u013e\u013f\7]\2\2\u013fT\3\2\2\2\u0140")
        buf.write("\u0141\7_\2\2\u0141V\3\2\2\2\u0142\u0143\7\60\2\2\u0143")
        buf.write("X\3\2\2\2\u0144\u0145\7.\2\2\u0145Z\3\2\2\2\u0146\u0147")
        buf.write("\7=\2\2\u0147\\\3\2\2\2\u0148\u0149\7<\2\2\u0149^\3\2")
        buf.write("\2\2\u014a\u014b\7}\2\2\u014b`\3\2\2\2\u014c\u014d\7\177")
        buf.write("\2\2\u014db\3\2\2\2\u014e\u014f\7?\2\2\u014fd\3\2\2\2")
        buf.write("\u0150\u015a\7\62\2\2\u0151\u0155\t\3\2\2\u0152\u0154")
        buf.write("\t\4\2\2\u0153\u0152\3\2\2\2\u0154\u0157\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2")
        buf.write("\u0157\u0155\3\2\2\2\u0158\u015a\b\63\3\2\u0159\u0150")
        buf.write("\3\2\2\2\u0159\u0151\3\2\2\2\u015af\3\2\2\2\u015b\u015d")
        buf.write("\5e\63\2\u015c\u015e\5k\66\2\u015d\u015c\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\5m\67\2")
        buf.write("\u0160\u0168\3\2\2\2\u0161\u0162\5e\63\2\u0162\u0163\5")
        buf.write("k\66\2\u0163\u0168\3\2\2\2\u0164\u0165\5k\66\2\u0165\u0166")
        buf.write("\5m\67\2\u0166\u0168\3\2\2\2\u0167\u015b\3\2\2\2\u0167")
        buf.write("\u0161\3\2\2\2\u0167\u0164\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169\u016a\b\64\4\2\u016ah\3\2\2\2\u016b\u016c\t\5\2")
        buf.write("\2\u016cj\3\2\2\2\u016d\u016f\7\60\2\2\u016e\u0170\5i")
        buf.write("\65\2\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172l\3\2\2\2\u0173\u0175")
        buf.write("\t\6\2\2\u0174\u0176\t\7\2\2\u0175\u0174\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177\u0179\5i\65\2")
        buf.write("\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017a\u017b\3\2\2\2\u017bn\3\2\2\2\u017c\u017f")
        buf.write("\5)\25\2\u017d\u017f\5\13\6\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017fp\3\2\2\2\u0180\u0186\7$\2\2\u0181")
        buf.write("\u0182\t\b\2\2\u0182\u0185\t\t\2\2\u0183\u0185\n\t\2\2")
        buf.write("\u0184\u0181\3\2\2\2\u0184\u0183\3\2\2\2\u0185\u0188\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\7$\2\2\u018a")
        buf.write("\u018b\b9\5\2\u018br\3\2\2\2\u018c\u0191\5e\63\2\u018d")
        buf.write("\u0191\5g\64\2\u018e\u0191\5o8\2\u018f\u0191\5q9\2\u0190")
        buf.write("\u018c\3\2\2\2\u0190\u018d\3\2\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u018f\3\2\2\2\u0191t\3\2\2\2\u0192\u0193\7}\2\2")
        buf.write("\u0193\u01a4\5s:\2\u0194\u0198\7.\2\2\u0195\u0197\7\"")
        buf.write("\2\2\u0196\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019f\5s:\2\u019c\u019e\7\"\2\2\u019d")
        buf.write("\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3")
        buf.write("\2\2\2\u01a2\u0194\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01a8\7\177\2\2\u01a8v\3\2\2\2\u01a9")
        buf.write("\u01ad\t\n\2\2\u01aa\u01ac\t\13\2\2\u01ab\u01aa\3\2\2")
        buf.write("\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01aex\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b2")
        buf.write("\t\f\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b6\b=\2\2\u01b6z\3\2\2\2\u01b7\u01b8\13\2\2")
        buf.write("\2\u01b8\u01b9\b>\6\2\u01b9|\3\2\2\2\u01ba\u01bb\13\2")
        buf.write("\2\2\u01bb~\3\2\2\2\u01bc\u01bd\13\2\2\2\u01bd\u01be\b")
        buf.write("@\7\2\u01be\u0080\3\2\2\2\25\2\u0087\u0095\u0155\u0159")
        buf.write("\u015d\u0167\u0171\u0175\u017a\u017e\u0184\u0186\u0190")
        buf.write("\u0198\u019f\u01a4\u01ad\u01b3\b\b\2\2\3\63\2\3\64\3\3")
        buf.write("9\4\3>\5\3@\6")
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
                  "STRING_LIT", "EXPR", "ARRAY_LIT", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[55] = self.STRING_LIT_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
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
            	print(idx)
            	if idx != -1 and self.text[idx + 1] not in escapes:
            		raise IllegalEscape(self.text[0:idx])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text)
     


