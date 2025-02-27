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

## Utilização
