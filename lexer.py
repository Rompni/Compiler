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
t_ID = r'\$[A-Za-z_][A-Za-z0-9_]*'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''
t_IDTYPE = r'let'


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
    t.value = float(t.value)
    return t

def t_PRINT(t):
    r'PRINT'
    return t

# Reserved
t_INIT = r'INIT'
t_END = r'END'
t_IF = r'IF'
t_ELSE = r'ELSE'
t_WHILE = r'WHILE'
t_FOR = r'FOR'
t_TRUE = r'TRUE'
t_FALSE = r'FALSE'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


t_ignore = ' \t\n'


def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)


lexer = lex.lex()
