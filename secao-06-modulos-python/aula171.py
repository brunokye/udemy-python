"""
os.walk para navegar de caminhos de forma recursiva

os.walk é uma função que permite percorrer uma estrutura de diretórios de
maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
e uma lista dos arquivos do diretório atual (files).
"""

import os
from itertools import count

caminho = os.path.abspath(".")
counter = count()
limit = 0

for root, dir, file in os.walk(caminho):
    the_counter = next(counter)
    print(f"{the_counter} Root: {root}")

    for dir_ in dir:
        print(" ", f"{the_counter} Dir: {dir_}")

    for file_ in file:
        caminho_completo = os.path.join(root, file_)
        print(" ", f"{the_counter} File: {file_}")

    limit += 1

    if limit >= 2:
        break
