import ply.lex as lex
import re

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
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'COMMA', 'PERIOD', 'SEMI'

)

reserved = (
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
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
t_SEMI = ';'

t_ID = r'\$[A-Za-z_][A-Za-z0-9_]*'
t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''
t_IDTYPE = 'let'

t_ignore = ' \t'


def t_error(t):
    print("Illegal character '{0}' at line {1}".format(t.value[0], t.lineno))
    t.lexer.skip(1)


lexer = lex.lex()
