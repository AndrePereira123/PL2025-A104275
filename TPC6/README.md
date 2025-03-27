# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-6: Parser LL(1)

"Baseado nos materiais fornecidos na aula, cria um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor.

Exemplos de algumas frases:
```
2+3
67-(2+3*4)
(9-2)*(13-4)"
```

## Descrição do programa

- Gramática desenvolvida(baseada nas aulas teóricas):
  ```
  Exp    --- Termo Exp2     (p0)
  Exp2   --- "+" Exp        (p1)
           |"-" Exp          (p2)
           | Epsilon         (p3)
  
  Termo  --- Dator Termo2   (p4)
  Termo2 --- "*" Termo      (p5)
            | Epsilon        (p6)
  Fator  --- Num            (p7)
            | "(" Exp ")"    (p8)
  ```

Comecei por alterar o analisador léxico desenvolvido nas aulas para que suportasse a linguagem pretendida no ficheiro ["analisador_lexico.py"](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC6/analisador_lexico.py).

Para o [parser](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC6/parser%20LL(1).py) em si bastou-me criar 3 funções "rec" que "reconhecem" uma Expressão(Exp), Termo ou Fator e seguem as regras da gramática definida de forma a percorrer e interpretar as operações. O valor de resultado é mantido numa variável "valor" incrementada recursivamente à medida que são chamadas as funções, por exemplo, numa expressão (chamadas recursivas que não alteram o cálculo foram ignoradas): 
 
 ```(2+3)```
 
 - Primeiro a função "rec_FATOR()" identifica o parêntese esquerdo e declara o valor como "= rec_expressao()"
 - De forma recursiva a "rec_FATOR()" volta a executar e, desta vez, encontra o valor "2" que é retornado
 - A "rec_expressao()" admite que o próximo token é "+" reconhece-o e soma ao valor(2) o valor do termo seguinte
 - A "rec_FATOR()" reconhece o valor como o número 3 e retorna-o
 - A "rec_expressao()" retorna o valor 5(2+3)
 - Finalmente na "rec_FATOR()" o valor 5 é recebido, o parêntese direito identificado e o valor final retornado

Para facilitar a compreensão das impressões geradas pelo programa diminui a densidade das mesmas, comparado ao parser desenvolvido na aula no qual me baseei.

## Exemplo de utilização
Os prints foram simplificados (omitidos muitos deles) para facilitar a compreensão do processo.
```
Introduza uma expressão: (9-2)*(13-4)
Reconheci P7: Fator -- Num  9
Reconheci P7: Fator -- Num  2
Reconheci P2: Exp2 -- '-' Exp
Reconheci P0: Exp -- Termo Exp2
Reconheci P8: Fator -- '(' Exp ')'
Reconheci P7: Fator -- Num  13
Reconheci P7: Fator -- Num  4
Reconheci P2: Exp2 -- '-' Exp
Reconheci P0: Exp -- Termo Exp2
Reconheci P8: Fator -- '(' Exp ')'
Reconheci P5: Termo2 -- * Termo
Reconheci P0: Exp -- Termo Exp2
Resultado da Expressão: 63
```
