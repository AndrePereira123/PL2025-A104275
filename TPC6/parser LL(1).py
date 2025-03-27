"""Baseado nos materiais fornecidos na aula, cria um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor.

Exemplos de algumas frases:

2+3
67-(2+3*4)
(9-2)*(13-4)"""


from analisador_lexico import lexer

prox_simb = ('Erro', '', 0, 0)


def parserError(simb):
    print("Erro sintático, token inesperado:", simb)
    exit(1)


def rec_term(simb):
    global prox_simb
    if prox_simb and prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)


def rec_FATOR():
    global prox_simb
    if prox_simb.type == 'NUM':
        valor = int(prox_simb.value)
        rec_term('NUM')
        print("Reconheci P7: Fator --> Num ", valor)
        return valor
    elif prox_simb.type == 'LPAR':
      ##   print("Derivando por P8: Fator --> '(' Exp ')'")
        rec_term('LPAR')
        valor = rec_expressao()
        rec_term('RPAR')
        print("Reconheci P8: Fator --> '(' Exp ')'")
        return valor
    else:
        parserError(prox_simb)
        return 0


def rec_TERMO():
  ##   print("Derivando por P4: Termo --> Fator Termo2")
    valor = rec_FATOR()
    while prox_simb and prox_simb.type == 'TIMES':
       ##      print("Derivando por P5: Termo2 --> * Termo")
            rec_term('TIMES')
            valor *= rec_FATOR()
            print("Reconheci P5: Termo2 --> * Termo")
    ## print("Reconheci P6: Termo2 --> ''")
    ## print("Reconheci P4: Termo --> Fator Termo2")
    return valor


def rec_expressao():
   ##  print("Derivando por P0: Exp --> Termo Exp2")
    valor = rec_TERMO()
    while prox_simb and prox_simb.type in ['PLUS', 'MINUS']:
        if prox_simb.type == 'PLUS':
      ##       print("Derivando por P1: Exp2 --> '+' Exp")
            rec_term('PLUS')
            valor += rec_TERMO()
            print("Reconheci P1: Exp2 --> '+' Exp")
        elif prox_simb.type == 'MINUS':
     ##        print("Derivando por P2: Exp2 --> '-' Exp")
            rec_term('MINUS')
            valor -= rec_TERMO()
            print("Reconheci P2: Exp2 --> '-' Exp")
    
   ## print("Reconheci P3: Exp2 --> ''")
    print("Reconheci P0: Exp --> Termo Exp2")
    return valor


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    resultado = rec_expressao()
    
    if prox_simb and prox_simb.type != 'EOF':
        parserError(prox_simb)
    
    print("Resultado da Expressão:", resultado)


# Entrada do usuário
linha = input("Introduza uma expressão: ")
rec_Parser(linha)
