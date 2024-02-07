"""
os.path trabalha com caminhos em Windows, Linux e Mac
Doc: https://docs.python.org/3/library/os.path.html#module-os.path

os.path é um módulo que fornece funções para trabalhar com caminhos de
arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
entre esses sistemas.

Exemplos do os.path:
os.path.join: junta strings em um único caminho. Desse modo,
os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
'pasta1BARRApasta2BARRAarquivo.txt' no Windows. (BARRA = / ao contrário)
os.path.split: divide um caminho uma tupla (diretório, arquivo).

Por exemplo, os.path.split('/home/user/arquivo.txt')
retornaria ('/home/user', 'arquivo.txt').
os.path.exists: verifica se um caminho especificado existe.
os.path só trabalha com caminhos de arquivos e não faz nenhuma
operação de entrada/saída (I/O) com arquivos em si.
"""

import os


caminho = os.path.join("\\home\\users", "Desktop", "curso", "arquivo.txt")
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao = os.path.splitext(arquivo)

print(caminho)
print(arquivo)
print(nome_arquivo)

print(f"\n{20 * '-'}\n")

print(os.path.exists("C:\\Users\\conta\\Desktop\\²\\Python"))
print(os.path.abspath("."))

print(f"\n{20 * '-'}\n")

print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))
