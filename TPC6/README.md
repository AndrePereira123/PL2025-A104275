# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-6: Parser LL(1)

Neste TPC pediram nos para desenvolver um parser LL(1).


## Descrição do programa

Para facilitar a compreesao e evitar redundancia reconhecer um "Fator" como "Num" acontece com 1 linha de print so.
- Gramatica desenvolvida
- Prints baseados nas aulas


## Exemplo de utilização
```
Introduza uma expressão: ((1+3)*(2)*(4)*(9-3)-(432))
Derivando por P4: Fator --> '(' Exp ')'
Derivando por P4: Fator --> '(' Exp ')'
Reconheci P4: Fator --> Num
Derivando por P1: Exp --> Termo + Termo
Reconheci P4: Fator --> Num
Reconheci P1: Exp --> Termo + Termo
Reconheci P4: Fator --> '(' Exp ')'
Derivando por P3: Termo --> Fator * Fator
Derivando por P4: Fator --> '(' Exp ')'
Reconheci P4: Fator --> Num
Reconheci P4: Fator --> '(' Exp ')'
Reconheci P3: Termo --> Fator * Fator
Derivando por P3: Termo --> Fator * Fator
Derivando por P4: Fator --> '(' Exp ')'
Reconheci P4: Fator --> Num
Reconheci P4: Fator --> '(' Exp ')'
Reconheci P3: Termo --> Fator * Fator
Derivando por P3: Termo --> Fator * Fator
Derivando por P4: Fator --> '(' Exp ')'
Reconheci P4: Fator --> Num
Derivando por P2: Exp --> Termo - Termo
Reconheci P4: Fator --> Num
Reconheci P2: Exp --> Termo - Termo
Reconheci P4: Fator --> '(' Exp ')'
Reconheci P3: Termo --> Fator * Fator
Derivando por P2: Exp --> Termo - Termo
Derivando por P4: Fator --> '(' Exp ')'
Reconheci P4: Fator --> Num
Reconheci P4: Fator --> '(' Exp ')'
Reconheci P2: Exp --> Termo - Termo
Reconheci P4: Fator --> '(' Exp ')'
Resultado da Expressão: -240
```

