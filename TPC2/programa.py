
import re
import bisect

def guardar_informacao(instancia_em_texto,Lista_Compositores,N_Obras_por_periodo,Obras_por_periodo):
    
    ##Descricao_obra = re.search(r'^.*?;(.*?);\d{4};.*?;.*?;\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    ##Ano_Obra = re.search(r'^.*?;.*?;(\d{4});.*?;.*?;\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    ##Duracao = re.search(r'^.*?;.*?;\d{4};.*?;.*?;(\d\d:\d\d:\d\d);\d*',instancia_em_texto,re.DOTALL).group(1)
    ##_id = re.search(r'^.*?;.*?;\d{4};.*?;.*?;\d\d:\d\d:\d\d;(\d*)',instancia_em_texto,re.DOTALL).group(1)

    Nome_obra = re.search(r'(^.*?);.*?;\d{4};.*?;.*?;\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    Compositor = re.search(r'^.*?;.*?;\d{4};.*?;(.*?);\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    Periodo = re.search(r'^.*?;.*?;\d{4};(.*?);.*?;\d\d:\d\d:\d\d;\d*',instancia_em_texto,re.DOTALL).group(1)
    

    Obras_por_periodo.setdefault(Periodo,[])
    N_Obras_por_periodo.setdefault(Periodo,0)
        
    bisect.insort(Obras_por_periodo[Periodo],Nome_obra)
    N_Obras_por_periodo[Periodo] += 1
    bisect.insort(Lista_Compositores,Compositor)

def main():
    f = open("obras.csv", "r",encoding = "utf-8")
    print(f"\nDados do ficheiro \"{f.name}\" serão processados agora\n")
    Lista_Compositores = []
    N_Obras_por_periodo = {}
    Obras_por_periodo = {}
    ##procurar 6 instancias de ; antes de fazer split - dado q existe sempre um \n entre instancias podemos faze lo
    instancia_em_texto = ""
    numero_de_pontos_virgula = 0
    next(f) ##ignorar primeira linha
    for linha in f:
        instancia_em_texto += linha
        numero_de_pontos_virgula += linha.count(";")
        if (numero_de_pontos_virgula >= 6):
            guardar_informacao(instancia_em_texto,Lista_Compositores,N_Obras_por_periodo,Obras_por_periodo)
            instancia_em_texto = ""
            numero_de_pontos_virgula = 0
    print("Processamento completo!\n")

    continuar = True
    while(continuar):
        i = 0
        print("\n")
        while(i not in [1,2,3,4]):
            print("Selecione uma opção:")
            print("1.Lista ordenada alfabeticamente dos compositores musicais.")
            print("2.Distribuição das obras por período.(número)")
            print("3.Dicionário de obras por período.")
            print("4.Sair.\n")
            i = input(">")
            if i.isdigit():
                i = int(i)
            else:
                i = 0
            print("\n")
        
        if i == 1:
            for compositor in Lista_Compositores:
                print(compositor)
        elif i == 2:
            for (periodo,n_obras) in N_Obras_por_periodo.items():
                print(f"Período: {periodo.ljust(15)} || NºObras: {n_obras}")
        elif i == 3:
            for (periodo,obras) in Obras_por_periodo.items():
                print("\n--------------------------")
                print(f"Período \"{periodo}\":\n")
                switch = True
                for obra in obras:
                    if(switch):
                        print (obra,end = " || ")
                    else:
                        print (obra)
                    switch = not switch
                print("\n--------------------------\n")
        else:
            break


main()