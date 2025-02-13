
verde = "\033[32m"
vermelho = "\033[31m"
amarelo = "\033[33m"
bold = "\033[1m"
reset = "\033[0m"  

def On_off(switch,estado):  ##deteta se ha uma string on ou off 
    if estado:
        if switch[0] == " " and switch[1] == "o" and switch[2] == "f" and switch[3] == "f" and switch[4] == " ":
            return True
    else: 
        if switch[1] == " " and switch[2] == "o" and switch[3] == "n" and switch[4] == " ":
            return True
    return False

def somador(f):
    
    digitos = []
    Soma_total = 0
    contador_prints = 0
    estado = True ## se estamos a contar ou nao
    switch = [" "," "," "," "," "] ## verifica On e Off

    while True:
        char = f.read(1)
        if estado and char in ["0","1","2","3","4","5","6","7","8","9"]:
            digitos.append(char)
            switch = [" "," "," "," "," "]
        else:
             valor = intrepretador_digitos(digitos)
             if valor != 0: print (f"|| Valor {valor} encontrado",end = "||\n")
             Soma_total += valor
             digitos = []
             if char == "=":
                 contador_prints += 1
                 print(f"Resultado nº{contador_prints}: {amarelo}{Soma_total}{reset}") 
                 switch = [" "," "," "," "," "]
             else:
                 del switch[0]
                 switch.append(char.lower())
                 if (On_off(switch,estado)):
                     estado = not estado
                     if (estado):
                         print(f"{verde}Soma ativada{reset}",end = "\n") 
                     else: 
                         print(f"{vermelho}Soma desativada{reset}",end = "\n")
             if not char:
                 return

def intrepretador_digitos(digitos):
    if digitos != []:
        d = 0
        res = 0
        while d < len(digitos):
            res = res * 10 + int(digitos[d])
            d+=1
        return res
    return 0

def main():
    print("\nInsira o nome do ficheiro de texto a ler: (default = texto1.txt)\n")
    nome_ficheiro = input()
    if (len(nome_ficheiro) == 0):
        f = open("texto1.txt", "r")
    else:
        try:
            f = open(nome_ficheiro,"r")
        except FileNotFoundError:
            print(f"O ficheiro não foi encontrado")
            return
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return
    somador(f)

    
main()