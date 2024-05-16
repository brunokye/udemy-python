"""
1 - Receber um número inteiro
2 - Verificar se o número é múltiplo de 3 e 5:
    Bacon com ovos
3 - Verificar se o número é múltiplo de 3:
    Bacon
4 - Verificar se o número é múltiplo de 5:
    Ovos
5 - Verificar se o número NÃO é múltiplo de 3 e 5:
    Passar fome
"""


def bacon_with_eggs(n):
    assert isinstance(n, int), "n needs to be int"

    if n % 3 == 0 and n % 5 == 0:
        return "Bacon with eggs"
    if n % 3 == 0:
        return "Bacon"
    if n % 5 == 0:
        return "Eggs"

    return "Starve"
