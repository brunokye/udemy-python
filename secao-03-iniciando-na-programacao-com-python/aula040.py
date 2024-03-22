while True:
    num01 = input('Digite o primeiro número: ')
    num02 = input('Digite o segundo número: ')
    operador = input('Digite o operador aritmético (+-*/): ')

    try:
        num01 = float(num01)
        num02 = float(num02)
    except Exception:
        print('Digite apenas números.')
        continue

    operadores = '+-*/'

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    if operador not in operadores:
        print('Digite um operador válido.')
        continue

    resultado = 'O resultado do seu cálculo é:'

    if operador == '+':
        print(f'{resultado} {num01 + num02}')
    if operador == '-':
        print(f'{resultado} {num01 - num02}')
    if operador == '*':
        print(f'{resultado} {num01 * num02}')
    if operador == '/':
        print(f'{resultado} {num01 / num02}')

    sair = input('Quer sair? [S] ou [N]: ')
    sair = sair.upper().startswith('S')

    if sair:
        break

print('Fim do Programa')
