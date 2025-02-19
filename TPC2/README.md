# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-2: Análise de um dataset de obras musicais

"Neste TPC, é proibido usar o módulo CSV do Python;
Deverás ler o dataset, processá-lo e criar os seguintes resultados:
  - Lista ordenada alfabeticamente dos compositores musicais;
  - Distribuição das obras por período: quantas obras catalogadas em cada período;
  - Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período."

[PDF original](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC2/tpc2.pdf) || [Dataset](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC2/obras.csv)

## Descrição do programa

O [programa](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC2/programa.py) foi desenvolvido em python, sem recurso ao móduli CSV como requisitado. Defini duas funções: "main" e "guardar_informacao"; ao executar o programa a função main é chamada e começa por abrir o [ficheiro csv](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC2/obras.csv) e ignorar a primeira linha com um "next" uma vez que esta serve apenas de cabeçalho para o dataset, de seguida o ficheiro é percorrido linha a linha e os dados das linhas são acumulados numa variável "instancia_em_texto", processo este que apenas termina quando terminarmos de ler uma instáncia do ficheiro csv. 
 - No ficheiro disponibilizado destaca-se o facto de os dados referentes a uma única obra ocuparem mais que uma linha.

Para determinar quando uma instáncia(detalhes referentes a uma só obra) termina defini uma expressão regular : 
 - ```Padrao_Regex = '^.*?;.*?;\d{4};.*?;.*?;\d\d:\d\d:\d\d;\d*'```

Com a suporte da livraria "[re](https://docs.python.org/3/library/re.html)" utilizei um "re.match" e o regex para garantir que as obras fossem corretamente divididas. Para obter os dados necessários criei uma função "guardar_informacao" que é chamada para cada uma das instáncias de dados recolhidos e guarda esses mesmos dados em 3 campos:
  - "Lista_Compositores" - uma lista com os nomes dos compositores ordenados alfabeticamente
  - "N_Obras_por_periodo" - um dicionario com o "periodo" da obra como chave e o número total de obras como valor
  - "Obras-por-periodo" -  um dicionario com o "periodo" da obra como chave e uma lista com os nomes de todas as obras desse periodo ordenadas alfabeticamente
##### --Para inserir os nomes de obras/compositores de forma ordenada e eficiente usufruí da livraria "[bysect](https://docs.python.org/3/library/bisect.html)"--

A expressão regular simplifica a seleção dos dados, pelo que basta evocar a funcão "re.search" na mesma e delimitar por parêntises os dados requisitados p.e. :
    
    Nome_obra = re.search(r'(^.*?);.*?;\d{4};.*?;.*?;\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    
    Compositor = re.search(r'^.*?;.*?;\d{4};.*?;(.*?);\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    
    Periodo = re.search(r'^.*?;.*?;\d{4};(.*?);.*?;\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1))

Vale ressaltar a flag "re.DOTALL" que foi necessária dado o facto da "instancia_em_texto" conter todas as linhas associadas a cada obra com vários "\n" que devem ser incluidos no "." de forma a registar todo o texto entre dois ";".

Finalmente, com todos os dados relevantes registados, a função "main" apresenta um menu textual simples que permite imprimir toda a informação.

## Utilização
**Menu**
```
Selecione uma opção:
1.Lista ordenada alfabeticamente dos compositores musicais.
2.Distribuição das obras por período.(número)
3.Dicionário de obras por período.
4.Sair.
```
**Opção 1**
```
Alessandro Stradella
Antonio Maria Abbatini
Bach, Johann Christoph
Bach, Johann Michael
Bach, Johann Michael
Bach, Wilhelm Friedemann
Bach, Wilhelm Friedemann
...
Titelouze, Jean
Titelouze, Jean
Tomaso Albinoni
Viadana, Lodovico Grossi da
Viadana, Lodovico Grossi da
Weldon, John
Weldon, John
Weldon, John
Wilhelmine of Prussia

```
**Opção 2**
```
Período: Barroco         || NºObras: 26
Período: Clássico        || NºObras: 15
Período: Medieval        || NºObras: 48
Período: Renascimento    || NºObras: 41
Período: Século XX       || NºObras: 18
Período: Romântico       || NºObras: 19
Período: Contemporâneo   || NºObras: 7

Número total de obras: 174
```
**Opção 3**
```
--------------------------
Período "Barroco":

Ab Irato || Die Ideale, S.106
Fantasy No. 2 || Hungarian Rhapsody No. 16
...
The Rondo || Transcendental Études
Études Op. 25 || Études Op.10

--------------------------


--------------------------
Período "Clássico":

Bamboula, Op. 2 || Capriccio Italien
Czech Suite || French Overture
...
Stabat Mater || Suite for Orchestra in B minor
Zärtliche Liebe ||
--------------------------


--------------------------
Período "Medieval":

Adagio in B minor || Ballade No.1
Ballades, Op. 10 || Barcarole Op. 60
...
Valses Sentimentales || Variations in F minor
Variations on a Theme of Corelli, Op. 42 || Wedding day at Troldhaugen

--------------------------


--------------------------
Período "Renascimento":

Bagatelles, Opus 119 || Bagatelles, Opus 33
Cantatas, BWV 141-150 || Carnival Overture
Estampes || Fantaisie brillante, Op. 22
Festklänge, S.101 || Funeral March in Memory of Rikard Nordraak
...
Transcendental Études || Valse romantique
Variation on a Waltz by Diabelli || Vers la flamme
Études Op. 25 ||
--------------------------


--------------------------
Período "Século XX":

Berceuse || Eleven Chorale Preludes, Op. 122
Fürchte dich nicht || Hungarian Rhapsody No. 17
...
Symphonic Poem No.1, Ce qu'on entend sur la montagne || The Storm, Op.76
Variations on a Theme of Chopin, Op. 22 || Études Op. 25

--------------------------


--------------------------
Período "Romântico":

Book II || Fantasy No. 4
Feu d'artifice || Feuilles d'Album
...
Waltzes, Op. 34 || Études Op. 25
Études Op.10 ||
--------------------------


--------------------------
Período "Contemporâneo":

Impromptu, Op. 36 || Les cinq doigts
...
Études Op. 25 ||
--------------------------

```
