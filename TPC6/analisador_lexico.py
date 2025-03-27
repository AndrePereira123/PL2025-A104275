# listas_analex.py
# 2023-03-21 by jcr
# ----------------------

"""
2+3
67-(2+3*4)
(9-2)*(13-4)
"""

import ply.lex as lex

tokens = ('NUM', 'PLUS', 'MINUS', 'LPAR', 'RPAR', 'TIMES')

t_NUM = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAR = r'\('
t_RPAR = r'\)'
t_TIMES = r'\*'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t '

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()






