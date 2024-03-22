import os
import platform


def limpar():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


lista = []

while True:
    letra = input(
        'Selecione uma Opção \n'
        '[l]istar [i]nserir [a]pagar [s]air: '
    ).lower()

    if letra == 'l':
        if len(lista) == 0:
            limpar()
            print('Nada para listar.')
        else:
            limpar()
            for i, item in enumerate(lista):
                print(i, item)
        continue
    elif letra == 'i':
        limpar()
        item = input('Nome do item: ')
        lista.append(item)
        continue
    elif letra == 'a':
        limpar()
        i = input('Índice do item: ')
        try:
            del lista[int(i)]
        except Exception:
            print('Digite um índice presente na lista.')
        continue
    elif letra == 's':
        limpar()
        print('Fim do Programa.')
        break
    else:
        limpar()
        print('Escolha uma das opções.')
