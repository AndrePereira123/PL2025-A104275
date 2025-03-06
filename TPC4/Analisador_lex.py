

import ply.lex as lex

tokens = (
 'COMMENT',
 'NUMBER',
 'PLUS',
 'MINUS',
 'TIMES',
 'DIVIDE',
 'LPAREN',
 'RPAREN',
 'PALAVRA',
 'INTERRO',
 'PONTO',
 'AT',
 'ASPA',
 'DPONTOS',
 'CHAVEDIR',
 'CHAVEESQ'
)

t_COMMENT = r'\#'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PALAVRA = r'([a-z]|[A-Z])+'
t_INTERRO = r'\?'
t_PONTO = r'\.'
t_AT = r'@'
t_ASPA = r'\"'
t_DPONTOS = r':'
t_CHAVEDIR = r'\}'
t_CHAVEESQ = r'\{'

# A regular expression rule with some action code
def t_NUMBER(t):
 r'\d+'
 t.value = int(t.value)
 return t
# Define a rule so we can track line numbers
def t_newline(t):
 r'\n+'
 t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule

def t_error(t):
 print("Illegal character '%s'" % t.value[0])
 t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()


file = open("./texto_exemplo.txt","r",encoding = "utf-8")
data = file.read()

lexer.input(data)

Contagem_instancias = {}



cor1 = "\033[92m"
cor2 = "\033[91m"
amarelo = "\033[93m"
RESET = "\033[0m"  

for i, tok in enumerate(lexer):
    color = cor1 if i % 2 == 0 else cor2  

    if tok.type in Contagem_instancias:
        Contagem_instancias[tok.type] += 1
    else:
        Contagem_instancias[tok.type] = 1

    print(f"{color}{tok.type:<10}: {tok.value:^15}   Linha: {tok.lineno}   Posição: {tok.lexpos}{RESET}")




print(f"{amarelo}\n||",end=" ")
for k,v in Contagem_instancias.items():
   print(f"{v} {k}",end=" || ")
print(f"\n{RESET}")