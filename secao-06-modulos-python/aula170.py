"""
os.listdir para navegar em caminhos
/Users/luizotavio/Desktop/EXEMPLO
caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
"""

import os

caminho = os.path.abspath(".")

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo):
        continue

    for arquivo in os.listdir(caminho_completo):
        print(arquivo)
