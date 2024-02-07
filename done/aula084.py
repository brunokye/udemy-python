import pprint


def p(v):
    pprint.pprint(v)


# print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)

# print(lista)


lista = [numero * 2 for numero in range(10)]
print(lista)

print(f'\n{20 * "-"}\n')

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] >= 30
]

p(novos_produtos)

print(f'\n{20 * "-"}\n')

lista = [numero for numero in range(10) if numero < 5]
print(lista)
