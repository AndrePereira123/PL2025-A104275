# PL2025-A104275 || André Filipe Soares Pereira || A104275
# TPC-5: Máquina de Vending

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
in
```

### Output
```
out
```

