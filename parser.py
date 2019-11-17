import ply.yacc as yacc
import lexer
import pprint

tokens = lexer.tokens

ERROR = 1


def p_start(p):
    """start : INIT body"""
    print("start")


def p_body(p):
    """body : LBRACE all_sentences RBRACE"""


def p_all_sentences(p):
    """all_sentences : list_sentences sentence
                    """


def p_list_sentences(p):
    """list_sentences : sentence"""


def p_sentence(p):
    """sentence : declaration
                | assign
                | function_dec
                | empty"""


def p_declaration(p):
    """declaration : IDTYPE ID SEMI"""


def p_booleans(p):
    """boolean : TRUE
                | FALSE"""


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
                    | empty"""



def p_tvariable(p):
    """tvariable : STRING
                 | ID
                 | INTEGER
                 | FLOAT
                 | CHARACTER
                 | boolean"""


def p_assign(p):
    """assign : IDTYPE ID EQUAL tvariable SEMI"""


def p_empty(p):
    """empty : """


def p_error(p):
    if ERROR:
        if p is not None:
            print('syntax error', p)
            print('line error: ', str(p.lineno))
    else:
        raise Exception(p)
        #print('Sintax', 'error')


parser = yacc.yacc()
#pp = pprint.PrettyPrinter(indent=4)
#code = 'INIT { WHILE ( $x > 5 ) {} }'
#pp.pprint(parser.parse(code))
