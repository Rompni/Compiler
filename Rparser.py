import sys
import ply.yacc as yacc
from lexer import tokens
import pprint, ast

pp = pprint.PrettyPrinter(indent=4)
ERROR = 0

precedence = (
    ("nonassoc", "PRINT"),
    ('left', "PLUS", "MINUS"),
    ('left', "TIMES", "DIVIDE"),
    ('left', "LPAREN", "RPAREN"),
    ('right', 'UMINUS'),
)

variables = {}


def p_start(p):
    """start : INIT body"""


def p_body(p):
    """body : LBRACE all_sentences RBRACE"""
    p[0] = p[2]

def p_all_sentences(p):
    """all_sentences : all_sentences list_sentences
                    | sentence"""


def p_list_sentences(p):
    """list_sentences : sentence"""


def p_sentence(p):
    """sentence : declaration
                | assign
                | sentence_while
                | sentence_for
                | sentence_if
                | print
                | empty"""


def p_expression_binop(p):
    """expression : expression PLUS expression
                    | expression MINUS expression
                    | expression TIMES expression
                    | expression DIVIDE expression"""

    if p[2] == "+":
        p[0] = p[1] + p[3]
    elif p[2] == "-":
        p[0] = p[1] - p[3]
    elif p[2] == "*":
        p[0] = p[1] * p[3]
    elif p[2] == "/":
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    """expression : MINUS expression %prec UMINUS"""
    p[0] = -p[2]


def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_expression_number(p):
    """expression : INTEGER
                 | FLOAT"""
    p[0] = p[1]


def p_expression_id(p):
    "expression : ID"
    global ERROR
    try:
        p[0] = variables[p[1]]
    except LookupError:
        ERROR = ("id no definida '%s'" % p[1])
        p[0] = 0


def p_sentence_while(p):
    """sentence_while : WHILE LPAREN condition RPAREN body"""


def p_sentence_for(p):
    """sentence_for : FOR LPAREN assign condition SEMI assign RPAREN body"""


def p_sentence_if(p):
    """sentence_if : IF LPAREN condition RPAREN body
                  | IF LPAREN condition RPAREN body ELSE LPAREN RPAREN body"""


def p_conditions(p):
    """conditions : LOR
                  | LAND
                  | LNOT
                  | LT
                  | GT
                  | LE
                  | GE
                  | EQ
                  | NE"""
    p[0] = p[1]


def p_booleans(p):
    """boolean : TRUE
                | FALSE"""
    p[0] = p[1]


def p_condition(p):
    """condition : expression conditions expression
                    """
    print(p[1], p[2], p[3])



def p_exprecondition(p):
    """expression : condition"""
    p[0] = p[1]


def p_declaration(p):
    """declaration : IDTYPE ID SEMI"""
    global ERROR

    if p[2] not in variables:
        print("new")
        variables[p[2]] = 0
    else:
        raise Exception("Variable declarada")





def p_booleans(p):
    """boolean : TRUE
                | FALSE"""
    p[0] = p[1]


def p_tvariable(p):
    """tvariable : STRING
                 | CHARACTER
                 | boolean
                 """
    p[0] = p[1]


def p_print_statement(p):
    """print : PRINT tvariable SEMI
            |  PRINT expression SEMI"""
    # para acceder al tipo de token p[n].type
    # para acceder al valor del token p[n].value
    #p[0] = {'name': p[1], 'value': p[2]}
    #print(p.slice)
    print(p[2])


def p_assign(p):
    """assign : IDTYPE ID EQUAL tvariable SEMI
                | IDTYPE ID EQUAL expression SEMI
                """
    global ERROR
    try:
        if p[2] is not variables:
            variables[p[2]] = p[4]
    except LookupError:
        ERROR = ("id definida '%s'" % p[1])
        p[0] = 0


def p_assignre(p):
    """assign : ID EQUAL tvariable SEMI
             | ID EQUAL expression SEMI
             """
    global ERROR
    try:
        if p[1] is variables:
            variables[p[1]] = p[3]
    except LookupError:
        ERROR = ("ID is not defined '%s" % p[1])
        p[0] = 0


def p_empty(p):
    """empty : """


def p_error(p):
    if ERROR:
        if p is not None:
            print('syntax error', p)
            print('line error: ', str(p.lineno))
    else:
        raise Exception(p)
        print('Sintax', 'error')


parser = yacc.yacc()
pp = pprint.PrettyPrinter(indent=4)


code = """
INIT 
{ 

    let $var := 3;
    IF($var > 4)
    {
        IF($var > 4)
        {
            IF($var > 4)
            {
                WHILE ( $x > 5)
                {
                    FOR ( let $var2 := 1 ; $var < 1 ; $var := $var + 1 ; ) 
                    {
                        IF ( $X == $var ) 
                        {
                            let $var3 := "Hola Mundo" ;                    
                        }
                        ELSE()
                        {
                            let $var4 := 'x';
                        }
                        
                    }
                } 
            }
        }
    }
}
"""

result = parser.parse(code)

pp.pprint(variables)

if result is not None:
    pp.pprint(result)


