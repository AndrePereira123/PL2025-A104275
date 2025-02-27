# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-3: Conversor MarkDown para HTML

Neste tpc foi requisitada a implementação de um conversor de ficheiros no formato markdown para html tendo em conta a conversão de:
  - Linhas iniciadas por "#","##",etc. para "\<h1\>...\</h1\>","\<h2\>...\</h2\>",etc.
  - Texto entre "**" e "*" (**bold** e *itálico*) para "\<b\>bold\</b\>" e "\<i\>itálico\</i\>"
  - Listas numeradas (p.e):
    
        1. Primeiro item
    
        2. Segundo item
    
        3. Terceiro item
    Para:
    ```
      <ol>
      <li>seg item</li>
      <li>Segundo item</li>
      <li>Terceiro item</li>
      </ol>
  - Links no formato \[página x\]\(http://www.link.com\)
  - Imagens no formato  !\[nome da imagem\]\(http://www.link_imagem.com\)


[PDF original](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC3/tpc3.pdf)



## Descrição do programa

O [programa](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC2/programa.py) foi desenvolvido em python, sem recurso ao módulo CSV como requisitado. Defini duas funções: "main" e "guardar_informacao"; ao executar o programa a função main é chamada e começa por abrir o [ficheiro csv](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC2/obras.csv) e ignorar a primeira linha com um "next" uma vez que esta serve apenas de cabeçalho para o dataset, de seguida o ficheiro é percorrido linha a linha e os dados das linhas são acumulados numa variável "instancia_em_texto", processo este que apenas termina quando terminarmos de ler uma instância do ficheiro csv. 
 - No ficheiro disponibilizado destaca-se o facto de os dados referentes a uma única obra ocuparem mais que uma linha.

Para determinar quando uma instância(detalhes referentes a uma só obra) termina defini uma expressão regular: 
 - ```Padrao_Regex = '^.*?;.*?;\d{4};.*?;.*?;\d\d:\d\d:\d\d;\d*'```

Com a suporte da livraria "[re](https://docs.python.org/3/library/re.html)" utilizei um "re.match" e o regex para garantir que as obras fossem corretamente divididas. Para obter os dados necessários criei uma função "guardar_informacao" que é chamada para cada uma das instâncias de dados recolhidos e guarda esses mesmos dados em 3 campos:
  - "Lista_Compositores" - uma lista com os nomes dos compositores ordenados alfabeticamente
  - "N_Obras_por_periodo" - um dicionário com o "período" da obra como chave e o número total de obras como valor
  - "Obras-por-periodo" -  um dicionário com o "período" da obra como chave e uma lista com os nomes de todas as obras desse periodo ordenadas alfabeticamente
##### --Para inserir os nomes de obras/compositores de forma ordenada e eficiente usufruí da livraria "[bysect](https://docs.python.org/3/library/bisect.html)"--

A expressão regular simplifica a seleção dos dados, pelo que basta evocar a função "re.search" na mesma e delimitar por parênteses os dados requisitados p.e. :
    
    Nome_obra = re.search(r'(^.*?);.*?;\d{4};.*?;.*?;\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    
    Compositor = re.search(r'^.*?;.*?;\d{4};.*?;(.*?);\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    
    Periodo = re.search(r'^.*?;.*?;\d{4};(.*?);.*?;\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1))

Vale ressaltar a FLAG "re.DOTALL" que foi necessária dado o facto de a "instancia_em_texto" conter todas as linhas associadas a cada obra com vários "\n" que devem ser incluídos no "." de forma a registar todo o texto entre dois ";".

Finalmente, com todos os dados relevantes registados, a função "main" apresenta um menu textual simples que permite imprimir toda a informação.

## Utilização
