

## Somador on/off
## 1. Somar sequencias de digitos encontradas num texto
## 2. Off em qualquer formato (Caps ou n) desativa o comportamento
## 3. On ativa o comportamente
## 4. Sempre que encontra '=' o resultado é colocado na saida

##dado que as letras "on" aprecem facilmente em texto decidi aceitar a troca
## apenas quando o on ou o off se encontravam entre characteres de espaco " "
## ou , por exemplo, no inicio do texto onde nao ha char a esquerda e ha um epaco
## a esquerda  "OfF O senhor de 79 anos ..."

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
                         print(f"{verde}Soma ativa{reset}",end = "\n") 
                     else: 
                         print(f"{vermelho}Soma inativa{reset}",end = "\n")
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
    print("\nOs ficheiros de texto vao ser lidos\n")
    f = open("PL2025-A104275/TPC1/texto_teste_1.txt", "r")
    somador(f)

    
main()