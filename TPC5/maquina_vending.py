
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


saldo = float("0.0")

def adicionar_saldo(moeda):
    global saldo
    if moeda[-1] == "e":  # Moeda em euros
        saldo += float(moeda[:-1])  # Retira o 'e' e converte para float
    else:  # Moeda em centavos
        if len(moeda) > 2:  # Ex: 50c
            saldo += float(moeda[:2]) / float('100')  # Divide por 100
        else:  # Ex: 5c
            saldo += float(moeda[:1]) / float('100')  # Divide por 100


s = open("stock.json","r",encoding = "utf-8") 

produtos = json.load(s)

## print(produtos[0]["cod"])

azul()
print(date.today(),end=" ")
print("Máquina carregada com " + str(len(produtos)) + " produtos")
res = None
while res != "SAIR":  
    amarelo()
    print("Olá. Estou disponível para atender o seu pedido. (AJUDA para lista de comandos)")
    reset()
    res = input()   
    if res == "AJUDA":
        verde()
        print("Comandos Disponiveis:")
        print("LISTAR- Lista produtos disponiveis com codigo quantidade e preco")
        print("SALDO- Ver saldo disponivel")
        print("MOEDA- Este comando seguindo de \"2e\" \"1e\" \"50c\" \"20c\" \"10c\" ou \"5c\", separados por virgulas e ponto no final, permite introduzir moedas na maquina")
        print("SELECIONAR- Este comando seguido de um codigo de produto permite comprá-lo, se o saldo for suficiente")

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
            print(f"Saldo inicial: {saldo:.2f}")
            amarelo()
            for m in moedas:
                str = (m.group()).strip().strip(",").strip(".")
                adicionar_saldo(str)
                print(f"Moeda {str} -> saldo {saldo:.2f}")
            verde()
            print(f"Saldo novo: {saldo:.2f}")
    
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
            if float(produto_pedido["preco"]) > saldo:
                vermelho()
                print(f"Saldo insuficiente para satisfazer o pedido\nSaldo = {saldo:.2f}; Pedido = {produto_pedido["preco"]}")
            else:
                saldo -= float(produto_pedido["preco"])
                vermelho()
                print(f"{produto_pedido["preco"]} gasto")
                azul()
                print(f"Pode retirar o produto dispensado \"{produto_pedido["nome"]}\"")
                print(f"Saldo = {saldo:.2f}")
            

    else:
        vermelho()
        print("Input não suportado, escreva \"AJUDA\" para uma lista de comandos suportados.")
