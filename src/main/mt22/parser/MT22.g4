grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: statement* EOF;

// --- DECLARATION
declaration: variable_decl | function_decl;
type_decl:
	BOOLEAN
	| INTEGER
	| FLOAT
	| STRING
	| ARRAY
	| VOID
	| AUTO;
id_list: ID (COMMA ID)*;
variable_decl: id_list COLON type_decl (ASSIGN expr (COMMA expr)*)? SEMI_COLON;

param_decl: INHERIT? OUT? ID COLON type_decl;
function_decl: 	ID ':' FUNCTION type_decl LRB param_decl RRB (INHERIT ID)? block_stat;


// -- EXPRESSION --
expr:
	int_expr
	| number_expr
	| bool_expr
	| string_expr
	| index_operator_expr
	| function_call;

int_expr:
	LRB int_expr RRB
	| int_expr MOD int_expr
	| INT_LIT
	| ID;

number_expr:
	LRB number_expr RRB
	| <assoc = right> SUBTRACT number_expr
	| <assoc = right> number_expr DIV number_expr
	| number_expr MUL number_expr
	| number_expr SUBTRACT number_expr
	| number_expr ADD number_expr
	| INT_LIT
	| FLOAT_LIT
	| ID;

bool_expr:
	LRB bool_expr RRB
	| <assoc = right> NEG bool_expr
	| bool_expr (AND | OR) bool_expr
	| number_expr (LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) number_expr
	| int_expr (EQUAL | DIFF) int_expr
	| bool_expr (EQUAL | DIFF) bool_expr
	| BOOL_LIT
	| ID;

string_expr: string_expr CONCAT string_expr | STRING_LIT | ID;

index_list: number_expr (COMMA number_expr)*;
index_operator_expr: ID LSB index_list RSB;

function_call: ID LRB (expr (COMMA expr)*)? RRB;

// --- STATEMENT ---
statement: 
		assignment_stat
		| if_stat 
		| for_stat 
		| white_stat;

var_declaration_stat:
	listID COLON typeDecl (ASSIGN expr (COMMA expr)*)? SEMI_COLON;
listID: ID (COMMA ID)*;

func_declaration_stat:
	ID ':' FUNCTION typeDecl LRB listParamDecl RRB block_stat;

assignment_stat: ID ASSIGN expr SEMI_COLON;
if_stat: IF LRB expr RRB statement (ELSE statement)?;
for_stat:
	FOR LRB ID ASSIGN int_expr COMMA bool_expr COMMA expr RRB statement;
white_stat: WHILE LRB bool_expr RRB statement;
do_while_stat: DO block_stat WHILE LRB bool_expr RRB SEMI_COLON;
break_stat: BREAK SEMI_COLON;
continue_stat: CONTINUE SEMI_COLON;
return_stat: RETURN expr? SEMI_COLON;
call_stat: function_call SEMI_COLON;
block_stat: LCB statement* RCB;

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

// --- SPECIAL FUNCTIONS
read_integer_func: 'readInteger()';
print_integer_func: 'readInteger()';
read_float_func: 'readInteger()';
write_float_func: 'readInteger()';
read_boolean_func: 'readInteger()';
print_boolean_func: 'readInteger()';
read_string_func: 'readString';
print_string_func: 'readString';
super_func_func: 'readString';
prevent_default_func: 'readString';

// Lexer
// --- COMMENT ---
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
