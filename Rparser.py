import sys
import ply.yacc as yacc
from Rlexer import tokens
import pprint

pp = pprint.PrettyPrinter(indent=4)
ERROR = True
ERRORES = ""
variables = {}

precedence = (
    ("nonassoc", "PRINT"),
    ('left', "PLUS", "MINUS"),
    ('left', "TIMES", "DIVIDE"),
    ('left', "LPAREN", "RPAREN"),
    ('right', 'UMINUS'),
)


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
    try:
        if p[1] in variables:
            p[0] = variables[p[1]]
        else:
            print("entro")
            ERRORES = ("id no defined '%s'" % p[1])
            p[0] = 0
            raise Exception(ERRORES)
    except LookupError:
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
    #print(p[1], p[2], p[3])


def p_exprecondition(p):
    """expression : condition"""
    p[0] = p[1]


def p_declaration(p):
    """declaration : IDTYPE ID SEMI"""
    try:
        if p[2] not in variables:
            print("new")
            variables[p[2]] = 0
        else:
            ERRORES = "id defined '%s'" % p[2]
            raise Exception(ERRORES)
    except ValueError:
        print("Error")


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
    global ERRORES
    try:
        if p[2] not in variables:
            variables[p[2]] = p[4]
    except LookupError:
        ERRORES = "id defined '%s'" % p[1]
        p[0] = 0


def p_assignre(p):
    """assign : ID EQUAL tvariable SEMI
             | ID EQUAL expression SEMI
             """
    global ERROR
    try:
        if p[1] in variables:
            variables[p[1]] = p[3]
        else:
            ERRORES = ("ID is not defined '%s" % p[1])
            raise Exception(ERRORES)
    except LookupError:
        ERROR = ("ID is not defined '%s" % p[1])
        p[0] = 0


def p_empty(p):
    """empty : """


def p_error(p):
    global ERRORES
    if ERROR:
        if p is not None:
            print('syntax error', p)
            print('line error: ', str(p.lineno))
            ERRORES = "Line Error: " + str(p.value)
            raise Exception(ERRORES)
    else:
        ERRORES = "Syntax Error"
        print('Syntax', 'error')
        raise Exception(ERRORES)


parser = yacc.yacc()
pp = pprint.PrettyPrinter(indent=4)


code = """
INIT
{
    let $var := 3;
    let $x;
    let $X;
    IF($var > 4)
    {
        IF($var > 4)
        {
            IF($var > 4)
            {
                WHILE ( $x > 5)
                {
                    FOR ( let $var2 := 1 ; $var < 1 ; $x := $var + 1 ; )
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

#result = parser.parse(code)

#pp.pprint(variables)

#if result is not None:
#    pp.pprint(result)


