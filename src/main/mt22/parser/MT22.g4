grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;


// --- COMMENT ---
C_COMMENT: '/*' (.)*? '*/' -> skip;
CPP_COMMENT: '//' ~[\r\n]* -> skip;

// Lexer
// --- KEYWORD ---
AUTO: 'auto';
BREAK: 'break';
FALSE: 'false';
FLOAT: 'float'; 
INTEGER: 'integer';
RETURN: 'return'; 
VOID: 'void';
OUT: 'out';
ARRAY: 'array';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
FUNCTION: 'function';
IF: 'if';
TRUE: 'true';
WHILE: 'while'; 
OF: 'of';
INHERIT: 'inherit';

// --- OPERATOR --- 
ADD: '+';
SUBTRACT: '-';
MUL: '*';
DIV: '/';
MOD: '%';

NEG: '!';
AND: '&&';
OR: '||';

EQUAL: '==';
DIFF: '!=';
LESS: '<';
LESS_EQUAL: '<=';
GREATER: '>';
GREATER_EQUAL: '>=';

CONCAT: '::';


// --- SEPERATORS ---
LRB: '(';
RRB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMI_COLON: ';';
COLON: ':';
LCB: '{';
RCB: '}';
ASSIGN: '=';

// --- LITERALS ---
INT_LIT: '0' | [1-9][0-9_]* {self.text = self.text.replace("_", "")};


// Consider case: without INT_LIT
FLOAT_LIT: (INT_LIT DECIMAL_PART? EXP_PART | INT_LIT DECIMAL_PART | DECIMAL_PART EXP_PART) {self.text = self.text.replace("_", "")};
fragment DIGIT: [0-9];
fragment DECIMAL_PART: '.' DIGIT+;
fragment EXP_PART: [eE] [+-]? DIGIT+;

// It will never match this token, it match TRUE, FALSE keyword above
BOOL_LIT: (TRUE | FALSE);

fragment ESCAPE: [\\][bfrnt'\\"];
STRING_LIT: '"' (ESCAPE | ~["\\] )* '"' {
	escapes = ['b', 'f', 'r', 'n', 't', '\'', '\\']
	self.text = self.text[1:-1].replace('\\"', '"')
	idx = self.text.find('\\')
	l = len(self.text)
	if idx != -1 and self.text[idx + 1] not in escapes:
		raise IllegalEscape(self.text[0:idx + 1])
};

fragment EXPR: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT;
ARRAY_LIT: '{' EXPR (',' ' '* EXPR ' '*)* '}';

// --- INDENTIFIER ---
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// [\\]~[bfrnt'\\"] 
ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: '"' [.]* '\\c'  {raise IllegalEscape(self.text) };
