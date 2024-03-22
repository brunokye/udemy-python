# kwargs - keyword arguments (argumentos nomeados)

pessoa = {
    'nome': 'Bruno',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

print(f'\n{20 * "-"}\n')


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

lista = [1, 2, 3, 4]

mostro_argumentos_nomeados(*lista, **configuracoes)
