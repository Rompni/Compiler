import sys
import ply.yacc as yacc
from lexer import tokens
import pprint

pp = pprint.PrettyPrinter(indent=4)
ERROR = 1


def p_start(p):
    """start : INIT body"""


def p_body(p):
    """body : LBRACE all_sentences RBRACE"""


def p_all_sentences(p):
    """all_sentences : all_sentences list_sentences
                    | sentence"""


def p_list_sentences(p):
    """list_sentences : sentence"""


def p_sentence(p):
    """sentence : declaration
                | function_dec
                | assign
                | empty"""


def p_declaration(p):
    """declaration : IDTYPE ID SEMI"""


def p_booleans(p):
    """boolean : TRUE
                | FALSE"""
    p[0] = p[1]


def p_operators(p):
    """operator : LOR
                | LAND
                | LNOT
                | LT
                | GT
                | LE
                | GE
                | EQ
                | NE"""


def p_print_statement(p):
    """print : PRINT tvariable SEMI
            | PRINT ID SEMI"""
    p[0] = {'name': p[1], 'value': p[2]}
    print(p[0])


def p_expression(p):
    """expression : tvariable operator tvariable"""


def p_function_condition(p):
    """function_cond : IF LPAREN expression RPAREN body
                    | IF LPAREN expression RPAREN body ELSE body"""


def p_function_iteration(p):
    """function_iter : iteration_statement"""


def p_iteration_statement(p):
    """iteration_statement : FOR LPAREN ID COLON ID RPAREN body
                          | WHILE LPAREN expression RPAREN body"""


def p_function_declaration(p):
    """function_dec : function_iter function_dec
                    | function_cond function_dec
                    | print
                    | empty"""


def p_tvariable(p):
    """tvariable : STRING
                 | ID
                 | INTEGER
                 | FLOAT
                 | CHARACTER
                 | boolean"""
    p[0] = p[1]


def p_assign(p):
    """assign : IDTYPE ID EQUAL tvariable SEMI
                | ID EQUAL tvariable SEMI
                """


def p_empty(p):
    """empty : """


def p_error(p):
    if ERROR:
        if p is not None:
            print('syntax error', p)
            print('line error: ', str(p.lineno))
    else:
        raise Exception(p)
        # print('Sintax', 'error')


parser = yacc.yacc()

pp = pprint.PrettyPrinter(indent=4)

code = """INIT { 
    PRINT 10;
}"""

result = parser.parse(code)

if result is not None:
    pp.pprint(result)

# error al declarar
