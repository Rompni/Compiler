import ply.yacc as yacc
import lexer
import pprint

tokens = lexer.tokens

ERROR = True

#def p_inicio(p):
#   '''inicio : INICIO cuerpoInst FIN
#   | empty'''
#   pass


def p_all_sentences(p):
    """all_sentences : list_sentences sentence"""


def p_list_sentences(p):
    """list_sentences : sentence"""


def p_sentence(p):
    """sentence : declaration
                | assign"""
    print("sentence")


def p_declaration(p):
    """declaration : IDTYPE ID SEMI"""
    print("Declaration")

def p_tvariable(p):
    """tvariable : STRING
                 | ID
                 | INTEGER
                 | FLOAT
                 | CHARACTER"""

def p_assign(p):
    """assign : IDTYPE ID EQUAL tvariable SEMI"""
    print("Assign")


def p_error(p):
    if ERROR:
        if p is not None:
            print('syntax error', p)
            print('line error: ', str(p.lineno))
    else:
        raise Exception(p)
        #print('Sintax', 'error')


parser = yacc.yacc()
pp = pprint.PrettyPrinter(indent=4)
code = 'let $name := "asd" ;'
pp.pprint(parser.parse(code))
