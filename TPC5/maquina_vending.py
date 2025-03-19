
import json,re
from datetime import date
from decimal import Decimal

def amarelo():
    print("\033[33m",end="")  # ANSI code for yellow text
def vermelho():
    print("\033[31m",end="")  # ANSI code for red text
def verde():
    print("\033[32m",end="")  # ANSI code for green text
def azul():
    print("\033[34m",end="")  # ANSI code for blue text
def reset():
    print("\033[0m",end="")  # ANSI code to reset color/style


saldo = 0

def adicionar_saldo(moeda):
    global saldo
    if moeda[-1] == "e":  # Moeda em euros
        saldo += int(moeda[:-1])*100  # Retira o 'e' e converte para float
    else:  # Moeda em centavos
        if len(moeda) > 2:  # Ex: 50c
            saldo += int(moeda[:2])  
        else:  # Ex: 5c
            saldo += int(moeda[:1]) 

def print_dinheiro(saldo):
    print(f"{int(saldo/100)}e{int((saldo%100))}c" )

s = open("stock.json","r",encoding = "utf-8") 

produtos = json.load(s)

## print(produtos[0]["cod"])

azul()
print(date.today(),end=" ")
print("Máquina carregada com " + str(len(produtos)) + " produtos")
res = None
while res != "SAIR":  
    amarelo()
    print("\nOlá. Estou disponível para atender o seu pedido. (AJUDA para lista de comandos)", end = " >")
    reset()
    res = input()   
    if res == "AJUDA":
        verde()
        print("Comandos Disponiveis:")
        print("LISTAR- Lista produtos disponiveis com codigo quantidade e preco")
        print("MOEDA- Este comando seguindo de \"2e\" \"1e\" \"50c\" \"20c\" \"10c\" ou \"5c\", separados por virgulas e ponto no final, permite introduzir moedas na maquina")
        print("SELECIONAR- Este comando seguido de um codigo de produto permite comprá-lo, se o saldo for suficiente")
        print("REPOR- Permite repor o stock de um produto")
        print("SAIR- Terminar o programa e receber troco")
    elif res[:5] == "REPOR":
        codigo = None
        while (codigo == None):
            azul()
            print("Código do produto a repor: >", end = "")
            codigos = []
            produto_pedido = None
            reset()
            codigo_produto = input()
            azul()
            for produto in produtos:
                codigos.append(produto["cod"])
                if produto["cod"] == codigo_produto:
                    produto_pedido = produto
                    codigo = produto_pedido["cod"]

            if codigo == None:
                vermelho()
                print(f"Produto com código {codigo_produto} não existe. Códigos válidos: {codigos}")
            elif produto_pedido["quant"] == 20:
                vermelho()
                print(f"\"{produto_pedido["nome"]}\" já se encontra com o stock máximo de 20.")
                codigo = None
            else: 
                quantidade = None
                while quantidade == None:
                    verde()
                    print(f"\"{produto_pedido["nome"]}\" selecionado. Stock atual = {produto_pedido["quant"]}")
                    azul()
                    print("Qual o número de unidade a inserir? >", end = "")
                    reset()
                    i = int(input())
                    azul()
                    if i in range(1,21 - int(produto_pedido["quant"])):
                        quantidade = i
                        produto_pedido["quant"] += quantidade
                        verde()
                        print(f"{i} unidade de \"{produto_pedido["nome"]}\" foram inseridas. Stock atual = {produto_pedido["quant"]}.")
                    else: 
                        vermelho()
                        print(f"O valor {i} é inválido, o limite de stock é 20.(20 < {int(produto_pedido["quant"])} + {i})")
                        
            

    elif res == "LISTAR":
        amarelo()
        print(f"{'cod':^10} | {'nome':^20} | {'quantidade':^10} | {'preco':^6}")
        print("-------------------------------------------------------------")
        for i,produto in enumerate(produtos):
            verde()
            if i%2==0:
                azul()
            
            print(f"{produto['cod']:^10} | {produto['nome']:^20} | {produto['quant']:^10} | {produto['preco']:^6}")

    elif res[:5] == "MOEDA":
            moedas = re.finditer(r"(2e|1e|50c|20c|10c|5c)(?:,|\s)*", res[5:])
            vermelho()
            print(f"Saldo inicial: ", end = "")
            print_dinheiro(saldo)
            azul()
            for m in moedas:
                str = (m.group()).strip().strip(",").strip(".")
                adicionar_saldo(str)
                azul()
                print(f" + Moeda {str}",end = "")
                verde()
                print(f" => Saldo: ", end = "")
                print_dinheiro(saldo)
            verde()
            print(f"Saldo atual: ", end = "")
            print_dinheiro(saldo)

    elif res[:10] == "SELECIONAR":
        codigo_produto = res[11:14]
        codigos = []
        produto_pedido = None
        for produto in produtos:
            codigos.append(produto["cod"])
            if produto["cod"] == codigo_produto:
                produto_pedido = produto

        if produto_pedido == None:
            vermelho()
            print(f"Produto com código {codigo_produto} não existe. Códigos válidos: {codigos}")
        else:
            if (produto_pedido["quant"]) == 0:   
                vermelho()
                print(f"\"{produto_pedido["nome"]}\" está indisponível (sem stock).")
            else:
                custo = int(float(produto_pedido["preco"])*100)
                if  custo > saldo:
                    vermelho()
                    print(f"Saldo insuficiente para satisfazer o pedido\nSaldo = ",end = "")
                    print_dinheiro(saldo)
                    print(f"Pedido = ",end = "")
                    print_dinheiro(custo)
                else:
                    saldo -= custo
                    produto_pedido["quant"] -= 1
                    vermelho()
                    print("-",end = "")
                    print_dinheiro(custo)
                    print(f"Stock atualizado ({produto_pedido["quant"]})")
                    azul()
                    print(f"Pode retirar o produto dispensado \"{produto_pedido["nome"]}\"")
                    print(f"Saldo = ",end = "")
                    print_dinheiro(saldo)

    elif res[:4] == "SAIR":
            azul()
            lista_moedas = [200,100,50,20,10,5]
            num_moedas = {}
            for x in lista_moedas:
                while saldo >= x :
                    if (num_moedas.get(x) is None) : num_moedas[x] = 1
                    else: num_moedas[x] += 1 
                    saldo -= x

            items = list(num_moedas.items()) 
            if (items): 
                print("\nPode retirar o troco: " , end = "")
                for i, (k, v) in enumerate(items):
                    str_inicio = ""
                    str_final = ", "
                    if i == len(items) - 2 : str_final = ""
                    if i == len(items) - 1 :
                        str_final = "."
                        if len(items) > 1 : str_inicio = " e "

                    if v > 0:
                        if int(k) >= 100:
                            print(f"{str_inicio}{v}x {int(k/100)}e" , end = str_final)
                        else:
                            print(f"{str_inicio}{v}x {k}c",end = str_final)
            verde()

            with open("stock.json", "w", encoding="utf-8") as s:
                json.dump(produtos, s, ensure_ascii=False, indent=4)
            print("\nAté à próxima")
            reset()
                

                    
    else:
        vermelho()
        print("Input não suportado, escreva \"AJUDA\" para uma lista de comandos suportados.")
