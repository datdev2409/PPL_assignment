# Generated from /Users/congdat/Desktop/PPL_assignment/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'false'", "'float'", "'integer'", "'return'", "'void'", 
                     "'out'", "'array'", "'boolean'", "'for'", "'string'", 
                     "'continue'", "'do'", "'else'", "'function'", "'if'", 
                     "'true'", "'while'", "'of'", "'inherit'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", 
                     "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
                     "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "C_COMMENT", "CPP_COMMENT", "AUTO", "BREAK", 
                      "FALSE", "FLOAT", "INTEGER", "RETURN", "VOID", "OUT", 
                      "ARRAY", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
                      "ELSE", "FUNCTION", "IF", "TRUE", "WHILE", "OF", "INHERIT", 
                      "ADD", "SUBTRACT", "MUL", "DIV", "MOD", "NEG", "AND", 
                      "OR", "EQUAL", "DIFF", "LESS", "LESS_EQUAL", "GREATER", 
                      "GREATER_EQUAL", "CONCAT", "LRB", "RRB", "LSB", "RSB", 
                      "DOT", "COMMA", "SEMI_COLON", "COLON", "LCB", "RCB", 
                      "ASSIGN", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
                      "ARRAY_LIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    C_COMMENT=1
    CPP_COMMENT=2
    AUTO=3
    BREAK=4
    FALSE=5
    FLOAT=6
    INTEGER=7
    RETURN=8
    VOID=9
    OUT=10
    ARRAY=11
    BOOLEAN=12
    FOR=13
    STRING=14
    CONTINUE=15
    DO=16
    ELSE=17
    FUNCTION=18
    IF=19
    TRUE=20
    WHILE=21
    OF=22
    INHERIT=23
    ADD=24
    SUBTRACT=25
    MUL=26
    DIV=27
    MOD=28
    NEG=29
    AND=30
    OR=31
    EQUAL=32
    DIFF=33
    LESS=34
    LESS_EQUAL=35
    GREATER=36
    GREATER_EQUAL=37
    CONCAT=38
    LRB=39
    RRB=40
    LSB=41
    RSB=42
    DOT=43
    COMMA=44
    SEMI_COLON=45
    COLON=46
    LCB=47
    RCB=48
    ASSIGN=49
    INT_LIT=50
    FLOAT_LIT=51
    BOOL_LIT=52
    STRING_LIT=53
    ARRAY_LIT=54
    ID=55
    WS=56
    ERROR_CHAR=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





