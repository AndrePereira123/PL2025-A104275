# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-5: Máquina de Vending

Neste TPC "Pediram-te para construir um programa que simule uma máquina de vending."

"A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço"


## Descrição do programa

Usufrui de um [ficheiro JSON](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC5/stock.json) , como sugerido, para ler e guardar os dados dos produtos da máquina. Para preencher o json criei um [script em python](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC5/preencher_json.py) que permite restaurar o estado inicial da máquina. Foram implementadas todas as funções requisitadas: 
 - **Listar** produtos
 - Inserir **moedas**
 - **Selecionar** produtos
 - Forma de "**sair**" do programa

Com estas funcionalidades foi necessária a implementação de uma lógica de saldo atual e função de impressão dessa quantidade num formato "**XeYc**" onde "e" simboliza os euros e "c" os cêntimos. Foi necessário um cálculo do troco e funcionalidade de impressão idêntica ao output sugerido.

Para além das funções obrigatórias implementei a opção de *repor* o stock de um produto; com está e algumas das funções mencionadas foram levados em consideração diversos cenários de prevenção e aviso de erro como:
 - Comando "**AJUDA**" que descreve todos os outros
 - Verificação de código de produto ao selecionar ou repor
 - Verificação de stock de produto ao selecionar(mínimo de 1) ou repor(limite max. de 20)
 - Aviso de saldo insuficiente ao selecionar produto

O JSON é atualizado apenas se o utilizador utilizar o comando "**SAIR**" para terminar o programa da forma pretendida, nesse momento os dados em memória são registados através de um ```json.dump()``` no ficheiro [stock.json](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC5/stock.json).

Usufrui de 3 livrarias de python:
 - [json](https://docs.python.org/3/library/json.html#module-json) para ler e escrever no ficheiro auxiliar
 - [re](https://docs.python.org/3/library/re.html#module-re) para facilitar a identificação das moedas inseridas com uma expressão regular e com a função "finditer" = ```moedas = re.finditer(r"(2e|1e|50c|20c|10c|5c)(?:,|\s)*", res[5:])```
 - [datetime](https://docs.python.org/3/library/datetime.html) para implementar a impressão da data atual como sugerido no exemplo do [enunciado](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC5/Enunciado.pdf)
from datetime import date

## Exemplo de utilização
```
2025-03-19 Máquina carregada com 18 produtos

Olá. Estou disponível para atender o seu pedido. (AJUDA para lista de comandos) >AJUDA
Comandos Disponiveis:
LISTAR- Lista produtos disponiveis com codigo quantidade e preco
MOEDA- Este comando seguindo de "2e" "1e" "50c" "20c" "10c" ou "5c", separados por virgulas e ponto no final, permite introduzir moedas na maquina
SELECIONAR- Este comando seguido de um codigo de produto permite comprá-lo, se o saldo for suficiente
REPOR- Permite repor o stock de um produto
SAIR- Terminar o programa e receber troco

Olá. Estou disponível para atender o seu pedido. (AJUDA para lista de comandos) >LISTAR
   cod     |         nome         | quantidade | preco 
-------------------------------------------------------------
   A01     |      Água 0.5L       |     20     |  0.7  
   A02     |    Coca-Cola 33cl    |     8      |  1.2  
   A03     |      Pepsi 33cl      |     6      |  1.2  
   A04     |  Sumo Laranja 33cl   |     5      |  1.3  
   A05     |       Red Bull       |     4      |  2.0  
   B01     |    Batatas Fritas    |     7      |  1.5  
   B02     |  Amendoins Torrados  |     6      |  1.3  
   B03     | Mix de Frutos Secos  |     5      |  1.8  
   B04     |  Bolacha Chocolate   |     9      |  1.6  
   B05     |       Snickers       |     8      |  1.4  
   B06     |         Twix         |     7      |  1.4  
   B07     |        KitKat        |     6      |  1.3  
   C01     |   Pastilha Mentol    |     12     |  0.8  
   C02     | Pastilha de Morango  |     10     |  0.8  
   D01     |    Café Expresso     |     15     |  0.9  
   D02     |      Cappuccino      |     10     |  1.5  
   D03     |   Chocolate Quente   |     8      |  1.6  
   D04     |      Chá Verde       |     5      |  1.2  

Olá. Estou disponível para atender o seu pedido. (AJUDA para lista de comandos) >MOEDA 2e 1e 50c
Saldo inicial: 0e0c
 + Moeda 2e => Saldo: 2e0c
 + Moeda 1e => Saldo: 3e0c
 + Moeda 50c => Saldo: 3e50c
Saldo atual: 3e50c

Olá. Estou disponível para atender o seu pedido. (AJUDA para lista de comandos) >SELECIONAR A01
-0e70c
Stock atualizado (19)
Pode retirar o produto dispensado "Água 0.5L"
Saldo = 2e80c

Olá. Estou disponível para atender o seu pedido. (AJUDA para lista de comandos) >REPOR
Código do produto a repor: >A01
"Água 0.5L" selecionado. Stock atual = 19
Qual o número de unidade a inserir? >2
O valor 2 é inválido, o limite de stock é 20.(20 < 19 + 2)
"Água 0.5L" selecionado. Stock atual = 19
Qual o número de unidade a inserir? >1
1 unidade de "Água 0.5L" foram inseridas. Stock atual = 20.

Olá. Estou disponível para atender o seu pedido. (AJUDA para lista de comandos) >SAIR

Pode retirar o troco: 1x 2e, 1x 50c, 1x 20c e 1x 10c.
Até à próxima
```

