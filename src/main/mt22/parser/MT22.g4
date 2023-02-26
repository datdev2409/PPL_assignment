grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: declaration+ EOF;

// --- DECLARATION
declaration: variable_decl | function_decl;

element_type: BOOLEAN | INTEGER | FLOAT | STRING;
array_type:
	'array' LSB INT_LIT (COMMA INT_LIT)* RSB OF element_type;

type_decl: element_type | array_type | VOID | AUTO;

id_list: ID (COMMA ID)*;
expr_list: expr (COMMA expr)*;

variable_decl:
	variable_decl_short
	| variable_decl_long SEMI_COLON;

variable_decl_short: id_list COLON type_decl SEMI_COLON;
variable_decl_long:
	ID COMMA variable_decl_long COMMA expr
	| sub_variable_decl;
sub_variable_decl: ID COLON type_decl ASSIGN expr;

param_decl: INHERIT? OUT? ID COLON (element_type | array_type | AUTO);
param_decl_list: (param_decl (COMMA param_decl)*)?;

function_decl:
	ID COLON FUNCTION type_decl LRB param_decl_list RRB (
		INHERIT ID
	)? block_stat;

// -- EXPRESSION --
expr:
	int_expr
	| number_expr
	| bool_expr
	| string_expr
	| index_operator_expr
	| function_call
	| ARRAY_LIT;

int_expr:
	LRB int_expr RRB
	| <assoc = right> SUBTRACT int_expr
	| int_expr (MOD | MUL | DIV) int_expr
	| int_expr (ADD | SUBTRACT) int_expr
	| INT_LIT
	| function_call
	| index_operator_expr
	| ID;

number_expr:
	<assoc = right> SUBTRACT number_expr
	| LRB number_expr RRB
	| <assoc = right> number_expr DIV number_expr
	| int_expr
	| number_expr MUL number_expr
	| number_expr SUBTRACT number_expr
	| number_expr ADD number_expr
	| INT_LIT
	| FLOAT_LIT
	| function_call
	| index_operator_expr
	| ID;

bool_expr:
	LRB bool_expr RRB
	| <assoc = right> NEG bool_expr
	| bool_expr (AND | OR) bool_expr
	| number_expr (LESS | GREATER | LESS_EQUAL | GREATER_EQUAL) number_expr
	| int_expr (EQUAL | DIFF) int_expr
	| bool_expr (EQUAL | DIFF) bool_expr
	| (TRUE | FALSE)
	| function_call
	| index_operator_expr
	| ID;

string_expr:
	string_expr CONCAT string_expr
	| STRING_LIT
	| ID
	| function_call
	| index_operator_expr;

index_list: number_expr (COMMA number_expr)*;
index_operator_expr: ID LSB index_list RSB;

function_call: ID LRB (expr (COMMA expr)*)? RRB;

// --- STATEMENT ---
statement:
	assignment_stat
	| if_stat
	| for_stat
	| white_stat
	| do_while_stat
	| break_stat
	| continue_stat
	| return_stat
	| call_stat
	| block_stat
	| declaration
	| expr SEMI_COLON;

assignment_stat: (ID | index_operator_expr) ASSIGN expr SEMI_COLON;

if_stat: IF LRB bool_expr RRB statement (ELSE statement)?;

for_stat:
	FOR LRB ID ASSIGN int_expr COMMA bool_expr COMMA int_expr RRB statement;

white_stat: WHILE LRB bool_expr RRB statement;

do_while_stat: DO block_stat WHILE LRB bool_expr RRB SEMI_COLON;

break_stat: BREAK SEMI_COLON;

continue_stat: CONTINUE SEMI_COLON;

return_stat: RETURN expr? SEMI_COLON;

call_stat: (special_func | function_call) SEMI_COLON;

block_stat: LCB statement* RCB;

// --- SPECIAL FUNCTIONS
special_func:
	read_integer_func
	| print_integer_func
	| read_float_func
	| write_float_func
	| read_boolean_func
	| print_boolean_func
	| read_string_func
	| print_string_func
	| super_func
	| prevent_default_func;

read_integer_func: 'readInteger' LRB RRB;
print_integer_func: 'printInteger' LRB int_expr RRB;
read_float_func: 'readFloat' LRB RRB;
write_float_func: 'writeFloat' LRB number_expr RRB;
read_boolean_func: 'readBoolean' LRB RRB;
print_boolean_func: 'printBoolean' LRB bool_expr RRB;
read_string_func: 'readString' LRB RRB;
print_string_func: 'printString' LRB string_expr RRB;
super_func: 'super' LRB expr* RRB;
prevent_default_func: 'preventDefault' LRB RRB;

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
	| [1-9] [0-9]* ('_' [0-9]+)* {self.text = self.text.replace("_", "")};

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
	self.text = self.text[1:-1]
};

fragment EXPR: STRING_LIT | INT_LIT | FLOAT_LIT | BOOL_LIT | ARRAY_LIT;
ARRAY_LIT: '{' EXPR (COMMA EXPR )* '}';

// --- INDENTIFIER ---
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

// [\\]~[bfrnt'\\"] 
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
