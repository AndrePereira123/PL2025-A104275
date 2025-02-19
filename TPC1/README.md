# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-1: Somador on/off

  Para o primeiro trabalho semanal foi proposta a realização de um acumulador de dígitos. Este "somador" deve:
   1. Somar sequências de dígitos encontradas num texto
   2. A string "Off" em qualquer combinação de caracteres maiúsculos ou minúsculos deve desativar o comportamento e a string "On" deve realizar o oposto
   3. Sempre que é encontrado um caractere '=' o resultado no momento deve ser impresso

### Descrição do programa 
 O programa começa por requisitar ao utilizador o nome do ficheiro a ler que deve encontrar-se na pasta raiz do mesmo [TPC1](https://github.com/AndrePereira123/PL2025-A104275/tree/main/TPC1), por "default", ou seja caso não seja inserido qualquer caractere , abre o ficheiro ["texto1.txt"](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC1/texto_teste_1.txt) no qual se encontra um excerto da wikipédia alterado com a introdução de alguns excertos "on", "off" e "=". O programa percorre o ficheiro de texto caractere a caractere e: 
 
 - Regista caracteres que correspondam a um dígito numa lista ate que o caractere seguinte se trate de um não digito e , nesse caso, calcula o valor associado à sequência de dígitos e soma ao valor total no acumulador;
   
 - Regista os últimos 5 caracteres lidos, tranformando-os em minúscula com a função "lower()", e, caso os caracteres apresentem o padrão: " " "o" "f" "f" " " ou " " "o" "n" " ", altera o estado do programa, se possível.

 De modo a fornecer uma aplicação mais "user friendly" implementei vários prints que refletem o que se passa ao decorrer da execução do programa.
 Tomei a decisão de ignorar instâncias de "on" e "off" que estivessem no meio de palavras p.e. "Redondo" ou "offline" para facilitar a utilização efetiva do algoritmo.

## Utilização
Segue-se os prints resultantes da utilização do algoritmo sob o ficheiro [texto1](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC1/texto_teste_1.txt) incluído com o 
programa.

**Output**
```
Soma desativada
Resultado nº1: 0
Resultado nº2: 0
Resultado nº3: 0
Soma ativada
|| Valor 1778 encontrado||
|| Valor 27 encontrado||
|| Valor 1783 encontrado||
|| Valor 1793 encontrado||
Resultado nº4: 5381
|| Valor 1805 encontrado||
|| Valor 1812 encontrado||
|| Valor 1817 encontrado||
Soma desativada
Resultado nº5: 10815
Soma ativada
|| Valor 1982 encontrado||
|| Valor 2006 encontrado||
|| Valor 2009 encontrado||
Soma desativada
Soma ativada
|| Valor 2011 encontrado||
Resultado nº6: 18823
```
No output gerado podemos verificar 4 auxílios textuais: o "Soma desativada" e "Soma ativada" que transmitem, respetivamente, sendo encontrada uma string "off" ou "on" e o comportamento do programa foi atualizado correspondentemente; o "|| Valor x encontrado ||" sempre que alguma sequência de dígitos é encontrada, transformada em valor inteiro e somada ao acumulador total; e por fim os "Resultado nºx: y" que imprimem o valor atual no acumulador (y) e incrementam o valor x de modo a refletir a quantidade de vezes que o resultado foi requisitado ao encontrar a string "=".
