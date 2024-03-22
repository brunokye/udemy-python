"""
Criando arquivos com Python + Context Manager with
Usamos a função open para abrir
um arquivo em Python (ele pode ou não existir)

Modos:
r (leitura), w (escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)
Context manager - with (abre e fecha)

Métodos úteis:
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)

Vamos falar mais sobre o módulo os:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo

Vamos falar mais sobre o módulo json:
json.dump = Gera um arquivo json
json.load
"""

# import os

caminho_arquivo = "aula116/aula116.txt"

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# with open(caminho_arquivo, "w+") as arquivo:
#     arquivo.write("Linha 1\n")
#     arquivo.write("Linha 2\n")
#     arquivo.writelines(("Linha 3\n", "Linha 4\n"))

#     arquivo.seek(0, 0)
#     print("Leitura Comum")
#     print(arquivo.read())

#     arquivo.seek(0, 0)
#     print("Read Line")
#     print(arquivo.readline(), end="")
#     print(arquivo.readline().strip())
#     print(arquivo.readline())

#     arquivo.seek(0, 0)
#     print("Read Lines")
#     for linha in arquivo.readlines():
#         print(linha.strip())


# print(f"\n{'#' * 10}\n")

# with open(caminho_arquivo, "r") as arquivo:
#     print(arquivo.read())

with open(caminho_arquivo, "w", encoding="UTF-8") as arquivo:
    arquivo.write("Atenção\n")
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.writelines(("Linha 3\n", "Linha 4\n"))

# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)

# os.rename(caminho_arquivo, "aula116/aula116a.txt")
