import re

def main():
    f = open("Original.md", "r",encoding = "utf-8")
    print(f"\nDados do ficheiro \"{f.name}\" serão processados agora\n")
    ##procurar 6 instancias de ; antes de fazer split - dado q existe sempre um \n entre instancias podemos faze lo
    html = f.read()

    pagHTML = "<!DOCTYPE html>  <html> <head> <style> body { background-color: #121212; color: #ffffff; text-align:center;font-size:2rem;} </style> </head>"


    html = re.sub(r"#(\s+.+)",r"<h1>\1</h1>",html)
    html = re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",html)
    html = re.sub(r"\*(.+?)\*",r"<i>\1</i>",html)
    
    padrao_listas = r"((?:\d+\.\s[^\n]+\n)+)"
    
    ##html = re.sub(r"(\d+)\.\s(.+)(\d+)\.\s([^\n]+)", r"<ol><li>\2</li></ol>", html ,flags=re.DOTALL)

    # Step 1: Extract matches
    listas = re.findall(padrao_listas,html,flags=re.DOTALL)

    listas_em_html = []
    for lista in listas:
        lista_html = ""
        for linha in lista.split("\n"):
            if len(linha) > 3:
                lista_html += ("<li>" + linha[3:] + "</li>")
        listas_em_html.append("<ol>" + lista_html + "</ol>")

    for original in listas:
        html = html.replace(original, listas_em_html.pop())

    html = re.sub(r"\!\[(.+?)\]\((.+?)\)(\n?)" ,r'<img src="\2" alt="\1" width="100"/>\3\3',html)
    html = re.sub(r"\[(.+?)\]\((.+?)\)(\n?)",r'<a href="\2">\1</a>\3\3',html)

    html = re.sub(r"#(\s+.+)",r"<h1>\1</h1>",html)

    pagHTML += html

    with open("output.html", "w", encoding="utf-8") as html_file:
        html_file.write(pagHTML)
    
    print("Processamento completo!\n")




main()