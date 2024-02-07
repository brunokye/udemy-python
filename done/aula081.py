'''
Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única
expressão.
'''

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)

# print(sorted(lista))
# print(lista)

l1 = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def ordena(item):
    return item['nome']


def exibir(lista):
    for item in lista:
        print(item)


l1.sort(key=ordena)
exibir(l1)

print(f'\n{20 * "-"}\n')

l2 = sorted(l1, key=lambda item: item['sobrenome'])
exibir(l2)
