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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\3\2\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\7\4&\n\4")
        buf.write("\f\4\16\4)\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\62\n\5")
        buf.write("\f\5\16\5\65\13\5\5\5\67\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\7\7F\n\7\f\7\16\7I\13\7\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\7\nT\n\n\f\n\16\nW\13")
        buf.write("\n\5\nY\n\n\3\13\5\13\\\n\13\3\13\5\13_\n\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\3\7\2")
        buf.write("\6\6\t\n\f\f\16\17\21\21\2d\2\31\3\2\2\2\4 \3\2\2\2\6")
        buf.write("\"\3\2\2\2\b*\3\2\2\2\n:\3\2\2\2\fC\3\2\2\2\16L\3\2\2")
        buf.write("\2\20N\3\2\2\2\22X\3\2\2\2\24[\3\2\2\2\26\30\5\4\3\2\27")
        buf.write("\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\34\3\2\2\2\33\31\3\2\2\2\34\35\7\2\2\3\35\3\3\2\2")
        buf.write("\2\36!\5\b\5\2\37!\5\n\6\2 \36\3\2\2\2 \37\3\2\2\2!\5")
        buf.write("\3\2\2\2\"\'\7:\2\2#$\7/\2\2$&\7:\2\2%#\3\2\2\2&)\3\2")
        buf.write("\2\2\'%\3\2\2\2\'(\3\2\2\2(\7\3\2\2\2)\'\3\2\2\2*+\5\6")
        buf.write("\4\2+,\7\61\2\2,\66\5\16\b\2-.\7\64\2\2.\63\5\20\t\2/")
        buf.write("\60\7/\2\2\60\62\5\20\t\2\61/\3\2\2\2\62\65\3\2\2\2\63")
        buf.write("\61\3\2\2\2\63\64\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2")
        buf.write("\66-\3\2\2\2\66\67\3\2\2\2\678\3\2\2\289\7\60\2\29\t\3")
        buf.write("\2\2\2:;\7:\2\2;<\7\61\2\2<=\7\25\2\2=>\5\16\b\2>?\7*")
        buf.write("\2\2?@\5\22\n\2@A\7+\2\2AB\5\f\7\2B\13\3\2\2\2CG\7\62")
        buf.write("\2\2DF\5\4\3\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2")
        buf.write("HJ\3\2\2\2IG\3\2\2\2JK\7\63\2\2K\r\3\2\2\2LM\t\2\2\2M")
        buf.write("\17\3\2\2\2NO\7\3\2\2O\21\3\2\2\2PU\5\24\13\2QR\7/\2\2")
        buf.write("RT\5\24\13\2SQ\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V")
        buf.write("Y\3\2\2\2WU\3\2\2\2XP\3\2\2\2XY\3\2\2\2Y\23\3\2\2\2Z\\")
        buf.write("\7\32\2\2[Z\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2]_\7\r\2\2^]")
        buf.write("\3\2\2\2^_\3\2\2\2_`\3\2\2\2`a\7:\2\2ab\7\61\2\2bc\5\16")
        buf.write("\b\2c\25\3\2\2\2\f\31 \'\63\66GUX[^")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'expr'", "<INVALID>", "<INVALID>", "'auto'", 
                     "'break'", "'false'", "'float'", "'integer'", "'return'", 
                     "'void'", "'out'", "'array'", "'boolean'", "'for'", 
                     "'string'", "'continue'", "'do'", "'else'", "'function'", 
                     "'if'", "'true'", "'while'", "'of'", "'inherit'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", 
                     "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "C_COMMENT", "CPP_COMMENT", 
                      "AUTO", "BREAK", "FALSE", "FLOAT", "INTEGER", "RETURN", 
                      "VOID", "OUT", "ARRAY", "BOOLEAN", "FOR", "STRING", 
                      "CONTINUE", "DO", "ELSE", "FUNCTION", "IF", "TRUE", 
                      "WHILE", "OF", "INHERIT", "ADD", "SUBTRACT", "MUL", 
                      "DIV", "MOD", "NEG", "AND", "OR", "EQUAL", "DIFF", 
                      "LESS", "LESS_EQUAL", "GREATER", "GREATER_EQUAL", 
                      "CONCAT", "LRB", "RRB", "LSB", "RSB", "DOT", "COMMA", 
                      "SEMI_COLON", "COLON", "LCB", "RCB", "ASSIGN", "INT_LIT", 
                      "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "ARRAY_LIT", 
                      "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_listID = 2
    RULE_varDeclStmt = 3
    RULE_funcDeclStmt = 4
    RULE_blockStmt = 5
    RULE_typeDecl = 6
    RULE_expr = 7
    RULE_listParamDecl = 8
    RULE_paramDecl = 9

    ruleNames =  [ "program", "statement", "listID", "varDeclStmt", "funcDeclStmt", 
                   "blockStmt", "typeDecl", "expr", "listParamDecl", "paramDecl" ]

    EOF = Token.EOF
    T__0=1
    C_COMMENT=2
    CPP_COMMENT=3
    AUTO=4
    BREAK=5
    FALSE=6
    FLOAT=7
    INTEGER=8
    RETURN=9
    VOID=10
    OUT=11
    ARRAY=12
    BOOLEAN=13
    FOR=14
    STRING=15
    CONTINUE=16
    DO=17
    ELSE=18
    FUNCTION=19
    IF=20
    TRUE=21
    WHILE=22
    OF=23
    INHERIT=24
    ADD=25
    SUBTRACT=26
    MUL=27
    DIV=28
    MOD=29
    NEG=30
    AND=31
    OR=32
    EQUAL=33
    DIFF=34
    LESS=35
    LESS_EQUAL=36
    GREATER=37
    GREATER_EQUAL=38
    CONCAT=39
    LRB=40
    RRB=41
    LSB=42
    RSB=43
    DOT=44
    COMMA=45
    SEMI_COLON=46
    COLON=47
    LCB=48
    RCB=49
    ASSIGN=50
    INT_LIT=51
    FLOAT_LIT=52
    BOOL_LIT=53
    STRING_LIT=54
    ARRAY_LIT=55
    ID=56
    WS=57
    ERROR_CHAR=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.ID:
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclStmt(self):
            return self.getTypedRuleContext(MT22Parser.VarDeclStmtContext,0)


        def funcDeclStmt(self):
            return self.getTypedRuleContext(MT22Parser.FuncDeclStmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.varDeclStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.funcDeclStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_listID




    def listID(self):

        localctx = MT22Parser.ListIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_listID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MT22Parser.ID)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.COMMA:
                self.state = 33
                self.match(MT22Parser.COMMA)
                self.state = 34
                self.match(MT22Parser.ID)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listID(self):
            return self.getTypedRuleContext(MT22Parser.ListIDContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(MT22Parser.TypeDeclContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_varDeclStmt




    def varDeclStmt(self):

        localctx = MT22Parser.VarDeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.listID()
            self.state = 41
            self.match(MT22Parser.COLON)
            self.state = 42
            self.typeDecl()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.ASSIGN:
                self.state = 43
                self.match(MT22Parser.ASSIGN)
                self.state = 44
                self.expr()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MT22Parser.COMMA:
                    self.state = 45
                    self.match(MT22Parser.COMMA)
                    self.state = 46
                    self.expr()
                    self.state = 51
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 54
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(MT22Parser.TypeDeclContext,0)


        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def listParamDecl(self):
            return self.getTypedRuleContext(MT22Parser.ListParamDeclContext,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockStmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcDeclStmt




    def funcDeclStmt(self):

        localctx = MT22Parser.FuncDeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcDeclStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MT22Parser.ID)
            self.state = 57
            self.match(MT22Parser.COLON)
            self.state = 58
            self.match(MT22Parser.FUNCTION)
            self.state = 59
            self.typeDecl()
            self.state = 60
            self.match(MT22Parser.LRB)
            self.state = 61
            self.listParamDecl()
            self.state = 62
            self.match(MT22Parser.RRB)
            self.state = 63
            self.blockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockStmt




    def blockStmt(self):

        localctx = MT22Parser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MT22Parser.LCB)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.ID:
                self.state = 66
                self.statement()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_typeDecl




    def typeDecl(self):

        localctx = MT22Parser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.AUTO) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.VOID) | (1 << MT22Parser.ARRAY) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_expr




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MT22Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ParamDeclContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_listParamDecl




    def listParamDecl(self):

        localctx = MT22Parser.ListParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listParamDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 78
                self.paramDecl()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MT22Parser.COMMA:
                    self.state = 79
                    self.match(MT22Parser.COMMA)
                    self.state = 80
                    self.paramDecl()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typeDecl(self):
            return self.getTypedRuleContext(MT22Parser.TypeDeclContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_paramDecl




    def paramDecl(self):

        localctx = MT22Parser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 88
                self.match(MT22Parser.INHERIT)


            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 91
                self.match(MT22Parser.OUT)


            self.state = 94
            self.match(MT22Parser.ID)
            self.state = 95
            self.match(MT22Parser.COLON)
            self.state = 96
            self.typeDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





