"""
Funções recursivas e recursividade
- funções que podem se chamar de volta
- úteis p/ dividir problemas grandes em partes menores
Toda função recursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pequeno problema
- Um caso base que para a recursão
"""

# import sys

# sys.setrecursionlimit(1004)


# def recursiva(inicio=0, fim=10):
#     print(inicio, fim)

#     if inicio >= fim:
#         return fim

#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0, 1000))


def fatorial(n):
    if n <= 1:
        return 1

    return n * fatorial(n - 1)


print(fatorial(10))
