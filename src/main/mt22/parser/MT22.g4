grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl+ EOF;

// TYPE
mttype: valueType | voidType;
valueType: atomicType | arrayType | autoType;

atomicType: BOOLEAN | INTEGER | FLOAT | STRING;

dimens: LSB INTLIT (CM INTLIT)* RSB;
arrayType: ARRAY dimens OF atomicType;

voidType: VOID;
autoType: AUTO;

// DECLARATION
decl: varDecl | funcDecl;


// VARIABLE DECLARATION
varDecl: varDeclShort | varDeclFull SC;

varDeclShort: ID (CM ID)* COLON valueType SC;

varDeclFull: ID CM varDeclFull CM exp | ID COLON valueType ASSIGN exp;


// FUNCTION DECLARATION
paramDecl: INHERIT? OUT? ID COLON valueType;
paramDecls: paramDecl (CM paramDecl)*;

funcDecl: ID COLON FUNCTION mttype LRB paramDecls? RRB (INHERIT ID)? blockStmt;


// LITERAL
literal: INTLIT | BOOLLIT | STRINGLIT | FLOATLIT | arraylit;
arraylit: LCB explist? RCB;

explist: exp (CM exp)*;

// EXPRESSION --
arrayCell: ID LSB explist RSB;
funcCall: ID LRB explist? RRB;

exp: exp1 CONCAT exp1 | exp1;
exp1: exp2 (EQUAL|DIFF|LESS|GREATER|LESSEQUAL|GREATEREQUAL) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUBTRACT) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NEG exp5 | exp6;
exp6: SUBTRACT exp6| exp7;
exp7: funcCall | arrayCell | operands | LRB exp RRB;

operands: literal | ID;

// --- STATEMENT ---
stmt:
	assignStmt SC
	| ifStmt
	| forStmt
	| whileStmt
	| doWhileStmt
	| breakStmt
	| contStmt
	| returnStmt
	| callStmt
	| blockStmt;

assignStmt: (ID | arrayCell) ASSIGN exp;

ifStmt: IF LRB exp RRB stmt (ELSE stmt)?;

callStmt: funcCall SC;

forStmt: FOR LRB assignStmt CM exp CM exp RRB stmt;

whileStmt: WHILE LRB exp RRB stmt;

doWhileStmt: DO blockStmt WHILE LRB exp RRB SC;

breakStmt: BREAK SC;

contStmt: CONTINUE SC;

returnStmt: RETURN exp? SC;

body: stmt body | varDecl body | ;
blockStmt: LCB body RCB;

// --- LITERALS ---
INTLIT: '0' | [1-9] DIGIT* ('_' DIGIT+)* {
	self.text = self.text.replace("_", "")
};

// Consider case: without INT_LIT
FLOATLIT: (INTLIT DECIMAL? EXP | INTLIT DECIMAL | DECIMAL EXP) {
	self.text = self.text.replace("_", "")
};
fragment DIGIT: [0-9];
fragment DECIMAL: '.' DIGIT*;
fragment EXP: [eE] [+-]? DIGIT+;

BOOLLIT: TRUE | FALSE;

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
STRINGLIT: '"' (ESCAPE | ~["\\])* '"' {
	self.text = self.text[1:-1]
};


// Lexer --- COMMENT ---
C_COMMENT: '/*' (.)*? '*/' -> skip;
CPP_COMMENT: '//' ~[\r\n]* -> skip;

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
LESSEQUAL: '<=';
GREATER: '>';
GREATEREQUAL: '>=';

CONCAT: '::';

// --- SEPERATORS ---
LRB: '(';
RRB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
CM: ',';
SC: ';';
COLON: ':';
LCB: '{';
RCB: '}';
ASSIGN: '=';


// --- INDENTIFIER ---
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE:
	'"' (~["] | '\\"')* ([\\]~[bfrnt'\\"]) {
	raise IllegalEscape(self.text[1:]) 
};
UNCLOSE_STRING:
	'"' (~["\\] | '\\"' | ESCAPE)*? (NEWLINE | EOF) {
	string_error = self.text[1:]
	if (string_error[-1] == "\n"):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
