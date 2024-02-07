# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente01 = adiciona_clientes("Bruno")
adiciona_clientes("Joana", cliente01)
cliente01.append("Eduardo")
print(cliente01)

cliente02 = adiciona_clientes("Helena")
adiciona_clientes("Maria", cliente02)
cliente02.append("Gabriel")
print(cliente02)
