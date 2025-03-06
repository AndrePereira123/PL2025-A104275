# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-4: Analisador Léxico

Neste TPC foi necessário "Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:"
```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
```

## Descrição do programa

Foi necessario identificar cada token individual que se encontra na string disponibilizada. Usufruí da livraria ["ply.lex"](https://www.dabeaz.com/ply/ply.html#ply_nn3).

## Utilização

### [Input](https://github.com/AndrePereira123/PL2025-A104275/blob/main/TPC4/texto_exemplo.txt)
```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
```

### Output
```
COMMENT   :        #          Linha: 1   Posição: 0
PALAVRA   :     DBPedia       Linha: 1   Posição: 2
DPONTOS   :        :          Linha: 1   Posição: 9
PALAVRA   :      obras        Linha: 1   Posição: 11
PALAVRA   :       de          Linha: 1   Posição: 17
PALAVRA   :      Chuck        Linha: 1   Posição: 20
PALAVRA   :      Berry        Linha: 1   Posição: 26
PALAVRA   :     select        Linha: 3   Posição: 33
INTERRO   :        ?          Linha: 3   Posição: 40
PALAVRA   :      nome         Linha: 3   Posição: 41
INTERRO   :        ?          Linha: 3   Posição: 46
PALAVRA   :      desc         Linha: 3   Posição: 47
PALAVRA   :      where        Linha: 3   Posição: 52
CHAVEESQ  :        {          Linha: 3   Posição: 58
INTERRO   :        ?          Linha: 4   Posição: 64
PALAVRA   :        s          Linha: 4   Posição: 65
PALAVRA   :        a          Linha: 4   Posição: 67
PALAVRA   :       dbo         Linha: 4   Posição: 69
DPONTOS   :        :          Linha: 4   Posição: 72
PALAVRA   :  MusicalArtist    Linha: 4   Posição: 73
PONTO     :        .          Linha: 4   Posição: 86
INTERRO   :        ?          Linha: 5   Posição: 92
PALAVRA   :        s          Linha: 5   Posição: 93
PALAVRA   :      foaf         Linha: 5   Posição: 95
DPONTOS   :        :          Linha: 5   Posição: 99
PALAVRA   :      name         Linha: 5   Posição: 100
ASPA      :        "          Linha: 5   Posição: 105
PALAVRA   :      Chuck        Linha: 5   Posição: 106
PALAVRA   :      Berry        Linha: 5   Posição: 112
ASPA      :        "          Linha: 5   Posição: 117
AT        :        @          Linha: 5   Posição: 118
PALAVRA   :       en          Linha: 5   Posição: 119
PONTO     :        .          Linha: 5   Posição: 122
INTERRO   :        ?          Linha: 6   Posição: 128
PALAVRA   :        w          Linha: 6   Posição: 129
PALAVRA   :       dbo         Linha: 6   Posição: 131
DPONTOS   :        :          Linha: 6   Posição: 134
PALAVRA   :     artist        Linha: 6   Posição: 135
INTERRO   :        ?          Linha: 6   Posição: 142
PALAVRA   :        s          Linha: 6   Posição: 143
PONTO     :        .          Linha: 6   Posição: 144
INTERRO   :        ?          Linha: 7   Posição: 150
PALAVRA   :        w          Linha: 7   Posição: 151
PALAVRA   :      foaf         Linha: 7   Posição: 153
DPONTOS   :        :          Linha: 7   Posição: 157
PALAVRA   :      name         Linha: 7   Posição: 158
INTERRO   :        ?          Linha: 7   Posição: 163
PALAVRA   :      nome         Linha: 7   Posição: 164
PONTO     :        .          Linha: 7   Posição: 168
INTERRO   :        ?          Linha: 8   Posição: 174
PALAVRA   :        w          Linha: 8   Posição: 175
PALAVRA   :       dbo         Linha: 8   Posição: 177
DPONTOS   :        :          Linha: 8   Posição: 180
PALAVRA   :    abstract       Linha: 8   Posição: 181
INTERRO   :        ?          Linha: 8   Posição: 190
PALAVRA   :      desc         Linha: 8   Posição: 191
CHAVEDIR  :        }          Linha: 9   Posição: 196
PALAVRA   :      LIMIT        Linha: 9   Posição: 198
NUMBER    :      1000         Linha: 9   Posição: 204

|| 1 COMMENT || 32 PALAVRA || 6 DPONTOS || 10 INTERRO || 1 CHAVEESQ || 4 PONTO || 2 ASPA || 1 AT || 1 CHAVEDIR || 1 NUMBER ||
```

