grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: statement* EOF;

statement:
	varDeclStmt
	| funcDeclStmt
	| expr SEMI_COLON // use for testing purpose only
	| TRUE;

listID: ID (COMMA ID)*;
varDeclStmt:
	listID COLON typeDecl (ASSIGN expr (COMMA expr)*)? SEMI_COLON;
funcDeclStmt:
	ID ':' FUNCTION typeDecl LRB listParamDecl RRB blockStmt;
blockStmt: LCB statement* RCB;

listParamDecl: (paramDecl (COMMA paramDecl)*)?;
paramDecl: INHERIT? OUT? ID ':' typeDecl;
typeDecl:
	BOOLEAN
	| INTEGER
	| FLOAT
	| STRING
	| ARRAY
	| VOID
	| AUTO;

// -- EXPRESSION --
expr:
	int_expr
	| number_expr
	| bool_expr
	| string_expr
	| index_operator_expr;

int_expr: LRB int_expr RRB | int_expr MOD int_expr | INT_LIT | ID;

number_expr:
	LRB number_expr RRB
	| <assoc = right> number_expr DIV number_expr
	| number_expr MUL number_expr
	| number_expr SUBTRACT number_expr
	| number_expr ADD number_expr
	| INT_LIT
	| FLOAT_LIT
	| ID;

bool_expr:
	LRB bool_expr RRB
	| NEG bool_expr
	| bool_expr (AND | OR) bool_expr
	| number_expr (LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) number_expr
	| int_expr (EQUAL | DIFF) int_expr
	| bool_expr (EQUAL | DIFF) bool_expr
	| BOOL_LIT
	| ID
	;

string_expr: string_expr CONCAT string_expr | STRING_LIT | ID;

index_list: number_expr (COMMA number_expr)*;
index_operator_expr: ID LSB index_list RSB;

// --- COMMENT ---
C_COMMENT: '/*' (.)*? '*/' -> skip;
CPP_COMMENT: '//' ~[\r\n]* -> skip;

// Lexer --- KEYWORD ---
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
INT_LIT:
	'0'
	| [1-9][0-9_]* {self.text = self.text.replace("_", "")};

// Consider case: without INT_LIT
FLOAT_LIT: (
		INT_LIT DECIMAL_PART? EXP_PART
		| INT_LIT DECIMAL_PART
		| DECIMAL_PART EXP_PART
	) {self.text = self.text.replace("_", "")};
fragment DIGIT: [0-9];
fragment DECIMAL_PART: '.' DIGIT*;
fragment EXP_PART: [eE] [+-]? DIGIT+;

// It will never match this token, it match TRUE, FALSE keyword above
BOOL_LIT: (TRUE | FALSE);

fragment NEWLINE: '\r'? '\n';
fragment ESCAPE:
	'\\b'
	| '\\f'
	| '\\r'
	| '\\n'
	| '\\t'
	| '\\\''
	| '\\\\'
	| '\\"';
STRING_LIT:
	'"' (ESCAPE | ~["\\])* '"' {
	self.text = self.text[1:-1].replace("\\", "")
};

fragment EXPR: INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT;
ARRAY_LIT: '{' EXPR (',' ' '* EXPR ' '*)* '}';

// --- INDENTIFIER ---
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

// [\\]~[bfrnt'\\"] 
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:
	'"' (~["] | '\\"')*? (NEWLINE | EOF) {
	raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE:
	'"' (~["] | '\\"')* [\\]~[bfrnt'\\"] {
	raise IllegalEscape(self.text[1:]) 
};
