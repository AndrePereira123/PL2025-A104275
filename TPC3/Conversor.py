import re

def main():
    f = open("Original.md", "r",encoding = "utf-8")
    print(f"\nDados do ficheiro \"{f.name}\" serão processados agora\n")

    html = f.read()

    pagHTML = "<!DOCTYPE html>  <html> <head> <style> body { background-color: #121212; color: #ffffff; text-align:center;font-size:2rem;} </style> </head>"


    html = re.sub(r"^(#+)(\s+.+)", lambda m: f"<h{len(m.group(1))}>{m.group(2).strip()}</h{len(m.group(1))}>", html, flags=re.M)
    #titulos
    html = re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",html)
    #negrito
    html = re.sub(r"\*(.+?)\*",r"<i>\1</i>",html)
    #italico
    
    padrao_listas = r"((?:\d+\.\s[^\n]+\n)+)"
    
    listas = re.findall(padrao_listas,html,flags=re.DOTALL)

    listas_em_html = []
    for lista in listas:
        lista_html = ""
        for linha in lista.split("\n"):
            if len(linha) > 3:
                lista_html += ("<li>" + linha[3:] + "</li>\n")
        listas_em_html.append("<ol>\n" + lista_html + "</ol>\n")

    for original in listas:
        html = html.replace(original, listas_em_html.pop())
        #listas

    html = re.sub(r"\!\[(.+?)\]\((.+?)\)(\n?)" ,r'<img src="\2" alt="\1" width="100"/>\3\3',html)
    #links
    html = re.sub(r"\[(.+?)\]\((.+?)\)(\n?)",r'<a href="\2">\1</a>\3\3',html)
    #imagens


    pagHTML += html

    with open("output.html", "w", encoding="utf-8") as html_file:
        html_file.write(pagHTML)
    
    print("Processamento completo!\n")




main()