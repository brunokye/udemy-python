"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
"""

#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'

del lista[-1]
lista.append('5')
lista.insert(0, 'teste')

# print(lista)
# print(lista[2], type(lista[2]))

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
lista_b.extend(lista_a)

# print(lista_a)
# print(lista_c)

lista01 = [1, 2, 3, 4]
lista02 = lista01.copy()
lista03 = lista01

lista01.pop()

print(lista02)
print(lista03)
