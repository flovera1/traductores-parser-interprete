# To change this template, choose Tools | Templates
# and open the template in the editor.

import lex
import yacc

#definimos los tokens
tokens = ('TkComentario','TkWith','TkDo','TkBool','TkIf',
    'TkIdent','TkString','TkNum','TkTrue','TkFalse','TkComa',
    'TkPuntoYComa','TkParAbre','TkParCierra','TkMas','TkMenos','TkMult',
    'TkDiv','TkMod','TkConjuncion','TkDisyuncion','TkNegacion','TkMenor',
    'TkMenorIgual','TkMayor','TkMayorIgual','TkIgual','TkDesigual','TkAsignacion')
#
#tokens = (
#    'NAME','NUMBER',
#    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
#    'LPAREN','RPAREN',
#    )

# Expresiones regulares


def t_TkComentario(t):
    r'\#.*'
    pass
    # No return value. Token discarded


#palabras claves
t_TkWith  = r'with'
t_TkDo = r'do'
t_TkBool = r'bool'
t_TkIf = r'if'

#variable
#TkIdent = r''
#strings
#TkString

#numeros
def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_TkTrue          = r'true'
t_TkFalse         = r'false'
t_TkComa          = r'[,]'
t_TkPuntoYComa    = r';'
t_TkParAbre       = r'\('
t_TkParCierra     = r'\)'
t_TkMas           = r'\+'
t_TkMenos         = r'-'
t_TkMult          = r'\*'
t_TkDiv           = r'/'
t_TkMod           = r'\%'
t_TkConjuncion    = r'/\\'
t_TkDisyuncion    = r'\\/'
#
#falta la negacion
#TkNegacion = r''

t_TkMenor      = r'<'
t_TkMenorIgual = r'<='
t_TkMayor      = r'>'
t_TkMayorIgual = r'>='
t_TkIgual      = r'='
t_TkDesigual   = r'/='
t_TkAsignacion = r':='

#t_PLUS    =
#t_MINUS   =
#t_TIMES   = r'\*'
#t_DIVIDE  = r'/'
#t_EQUALS  = r'='
#t_LPAREN  = r'\('
#t_RPAREN  = r'\)'
#t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
#

# Caracteres ignorados
t_ignore = '\s\t\n'


def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)



# Construimos el lexer
import ply.lex as lex
lex.lex()

# Reglas de precedencia para los operadores aritmeticos y logicos

#precedence = (
#    ('left','PLUS','MINUS'),
#    ('left','TIMES','DIVIDE'),
#    ('right','UMINUS'),
#    )

# dictionary of names (for storing variables)
names = {}
#
#def p_statement_assign(p):
#    'statement : NAME EQUALS expression'
#    names[p[1]] = p[3]
#
#def p_statement_expr(p):
#    'statement : expression'
#    print p[1]
##
#def p_expression_binop(p):
#    '''expression : expression PLUS expression
#                  | expression MINUS expression
#                  | expression TIMES expression
#                  | expression DIVIDE expression'''
#    if p[2] == '+'  : p[0] = p[1] + p[3]
#    elif p[2] == '-': p[0] = p[1] - p[3]
#    elif p[2] == '*': p[0] = p[1] * p[3]
#    elif p[2] == '/': p[0] = p[1] / p[3]
#
#def p_expression_uminus(p):
#    'expression : MINUS expression %prec UMINUS'
#    p[0] = -p[2]
#
#def p_expression_group(p):
#    'expression : LPAREN expression RPAREN'
#    p[0] = p[2]
#
def p_expression_number(p):
    'expression : TkNum'
    p[0] = p[1]
#
#def p_expression_name(p):
#    'expression : NAME'
#    try:
#        p[0] = names[p[1]]
#    except LookupError:
#        print "Undefined name '%s'" % p[1]
#        p[0] = 0



def p_error(p):
    print "Syntax error at '%s'" % p.value

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    yacc.parse(s)
