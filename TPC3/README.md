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
      <li>Primeiro item</li>
      <li>Segundo item</li>
      <li>Terceiro item</li>
      </ol>
  - Links no formato "**\[página x\]\(http://www.link_pagina.com\)**" para "**\<a href="http://www.link_pagina.com"\>página x\</a\>**"
  - Imagens no formato  "**!\[nome da imagem\]\(http://www.link_imagem.com\)**" para "**\<img src="www.link_imagem.com" alt="nome da imagem"/\>**"



[PDF original](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC3/tpc3.pdf)

## Descrição do programa

O [conversor](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC3/Conversor.py) que desenvolvi usufrui de várias expressões regulares para encontrar e substituir as instâncias de texto que necessitam ser alteradas. O programa foi desenvolvido em python e, ao executar, o [ficheiro original](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC3/Original.md) que contem um excerto em MarkDown, é lido e convertido para o [ficheiro de "output"](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC3/output.html) no formato html. 
###Regex utilizados:
  - ``` ^(#+)(\s+.+) ``` para identificar títulos;
  - ``` \*\*(.+?)\*\* ``` e ``` \*(.+?)\* ```  para identificar texto a negrito e em itálico respetivamente;
  - ``` ((?:\d+\.\s[^\n]+\n)+) ``` para identificar listas;
  - ``` \[(.+?)\]\((.+?)\)(\n?) ``` para identificar links;
  - ``` \!\[(.+?)\]\((.+?)\)(\n?) ``` para identificar links de imagens.

Em todos os casos, exceto as listas, bastou um uso simples da função [sub()](https://docs.python.org/3/library/re.html#re.sub) da livraria [re](https://docs.python.org/3/library/re.html); para as listas recorri a um processo mais complexo: primeiro são registadas todas as listas encontradas numa variável "listas", depois, para cada lista encontrada, as linhas são percorridas, é removido o identificador inicial da linha e são delimitadas pelo identificador html "\<li\>...\</li\>", as linhas são registadas numa "lista_html" e no final esta mesma lista é guardada no conjunto de "listas_em_html" e é inserido o identificador "\<ol\>" no início da lista e "\</ol\>" no final. 

## Utilização

### Ficheiro MarkDown (in)
```
# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-3: Conversor MarkDown para HTML
## Dois 
### Tres
#### Quatro
##### Cinco
###### Seis

Texto com teste de **bold** com *italico* e tudo mais para ver se *funciona* com as **novas** coisa que foram de *facto* **implementadas**

1. prim item
2. Segundo item
3. Terceiro item


1. seg item
2. Segundo item
3. Terceiro item


Como se vê na imagem seguinte: ![imagem dum... coelho?](https://raw.githubusercontent.com/AndrePereira123/PL2025-A104275/refs/heads/main/TPC3/imagem.jpg)
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como pode ser consultado em [link de teste](http://www.google.pt)


Como se vê na imagem seguinte: ![imagem dum... coelho?](https://raw.githubusercontent.com/AndrePereira123/PL2025-A104275/refs/heads/main/TPC3/imagem.jpg)

Texto com teste de **bold** com *italico* e tudo mais para ver se *funciona* com as **novas** coisa que foram de *facto* **implementadas**

1. prim item
2. Segundo item
3. Terceiro item


1. seg item
2. Segundo item
3. Terceiro item
```
### Ficheiro HTML (out)
```
<!DOCTYPE html>  <html> <head> <style> body { background-color: #121212; color: #ffffff; text-align:center;font-size:2rem;} </style> </head><h1>PL2025-A104275 || André Filipe Soares Pereira || A104275</h1>
<h1>TPC-3: Conversor MarkDown para HTML</h1>
<h2>Dois</h2>
<h3>Tres</h3>
<h4>Quatro</h4>
<h5>Cinco</h5>
<h6>Seis</h6>

Texto com teste de <b>bold</b> com <i>italico</i> e tudo mais para ver se <i>funciona</i> com as <b>novas</b> coisa que foram de <i>facto</i> <b>implementadas</b>

<ol>
<li>seg item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>


<ol>
<li>prim item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>


Como se vê na imagem seguinte: <img src="https://raw.githubusercontent.com/AndrePereira123/PL2025-A104275/refs/heads/main/TPC3/imagem.jpg" alt="imagem dum... coelho?" width="100"/>

Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

Como pode ser consultado em <a href="http://www.google.pt">link de teste</a>



Como se vê na imagem seguinte: <img src="https://raw.githubusercontent.com/AndrePereira123/PL2025-A104275/refs/heads/main/TPC3/imagem.jpg" alt="imagem dum... coelho?" width="100"/>


Texto com teste de <b>bold</b> com <i>italico</i> e tudo mais para ver se <i>funciona</i> com as <b>novas</b> coisa que foram de <i>facto</i> <b>implementadas</b>

<ol>
<li>seg item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>


<ol>
<li>prim item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```
