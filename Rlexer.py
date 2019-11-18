import ply.lex as lex
import re

ERROR2 = ""
tokens = (
    # Literals (identifier, integer constant, float constant, string constant, char const)
    "ID", 'IDTYPE', 'INTEGER', 'FLOAT', 'STRING', 'CHARACTER',

    # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'OR', 'AND', 'NOT',
    'XOR', 'LSHIFT', 'RSHIFT', 'LOR', 'LAND', 'LNOT', 'LT', 'GT',
    'LE', 'GE', 'EQ', 'NE',
    # Assignment
    'EQUAL',
    # Delimeters ( ) [ ] { } , . ;
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'COMMA', 'PERIOD', 'SEMI', 'COLON'

)

reserved = (
    'INIT',
    'END',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'TRUE',
    'FALSE',
    'PRINT'
)
tokens = tokens + reserved

# Asignations

t_EQUAL = r':='

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_OR = r'\|'
t_AND = r'&'
t_NOT = r'~'
t_XOR = r'\^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'

#

t_IDTYPE = r'let'


def t_CHARACTER(t):
    r'(L)?\'([^\\\n]|(\\.))*?\''
    return t


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print("error", t.value)
        t.value = str("")
    return t


def t_ID(t):
    r'\$[A-Za-z_][A-Za-z0-9_]*'
    return t


def t_INTEGER(t):
    r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
    try:
        t.value = int(t.value)
    except ValueError:
        print("integer value too large", t.value)
        t.value = 0
    return t


def t_FLOAT(t):
    r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("error", t.value)
        t.value = 0.0
    return t


def t_PRINT(t):
    r'PRINT'
    return t


# Reserved
def t_INIT(t):
    r'INIT'
    return t


def t_IF(t):
    r'IF'
    return t


def t_ELSE(t):
    r'ELSE'
    return t


def t_WHILE(t):
    r'WHILE'
    return t


def t_FOR(t):
    r'FOR'
    return t


def t_TRUE(t):
    r'TRUE'
    return t


def t_FALSE(t):
    r'FALSE'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


t_ignore = ' \t\n'


#def t_error(t):
#    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
#    t.lexer.skip(1)

def t_error(t):
    #raise SyntaxError("Unknown symbol %r" % (t.value[0],))
    raise Exception(t)
    #print("Skipping", repr(t.value[0]))
    #t.lexer.skip(1)


lexer = lex.lex()
