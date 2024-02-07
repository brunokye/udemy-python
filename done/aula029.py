numero_str = input('Digite um número: ')

try:
    numero_int = int(numero_str)
    print(f'O dobro de {numero_int} é {numero_int * 2}')
except:
    print('Isso não é um número')
