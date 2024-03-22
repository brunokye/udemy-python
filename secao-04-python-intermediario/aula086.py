produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

# for chave, valor in produto.items():
#     print(chave, valor)

d1 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}
print(d1)

s1 = {i for i in range(10)}
print(s1)
