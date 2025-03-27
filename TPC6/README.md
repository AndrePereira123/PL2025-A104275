# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-6: Parser LL(1)

Neste TPC pediram nos para desenvolver um parser LL(1).


## Descrição do programa

Para facilitar a compreesao e evitar redundancia reconhecer um "Fator" como "Num" acontece com 1 linha de print so.
- Gramatica desenvolvida
- Prints baseados nas aulas


## Exemplo de utilização
```
Introduza uma expressão: (9-2)*(13-4)
Reconheci P7: Fator --> Num  9
Reconheci P7: Fator --> Num  2
Reconheci P2: Exp2 --> '-' Exp
Reconheci P0: Exp --> Termo Exp2
Reconheci P8: Fator --> '(' Exp ')'
Reconheci P7: Fator --> Num  13
Reconheci P7: Fator --> Num  4
Reconheci P2: Exp2 --> '-' Exp
Reconheci P0: Exp --> Termo Exp2
Reconheci P8: Fator --> '(' Exp ')'
Reconheci P5: Termo2 --> * Termo
Reconheci P0: Exp --> Termo Exp2
Resultado da Expressão: 63
```

