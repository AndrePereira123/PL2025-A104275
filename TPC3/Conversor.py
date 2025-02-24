import re

Padrao_Regex = '^.*?;.*?;\d{4};.*?;.*?;\d\d:\d\d:\d\d;\d*'



def main():
    f = open("obras.csv", "r",encoding = "utf-8")
    print(f"\nDados do ficheiro \"{f.name}\" serão processados agora\n")
    Lista_Compositores = []
    N_Obras_por_periodo = {}
    Obras_por_periodo = {}
    ##procurar 6 instancias de ; antes de fazer split - dado q existe sempre um \n entre instancias podemos faze lo
    instancia_em_texto = ""
    next(f) ##ignorar primeira linha
    for linha in f:
        instancia_em_texto += linha
        if (re.match(Padrao_Regex,instancia_em_texto,re.DOTALL)):
            guardar_informacao(instancia_em_texto,Lista_Compositores,N_Obras_por_periodo,Obras_por_periodo)
            instancia_em_texto = ""
    print("Processamento completo!\n")




main()