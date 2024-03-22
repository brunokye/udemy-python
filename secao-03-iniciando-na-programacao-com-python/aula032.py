numero = input('Digite um número inteiro: ')

numero_int = int(numero)

if numero_int % 2 == 0:
    print(f'{numero} é par')
elif numero_int % 2 == 1:
    print(f'{numero} é ímpar')
else:
    print(f'{numero} não é um número inteiro')


hora = input('Digite a hora em números inteiros: ')

hora_int = int(hora)

if hora_int >= 0 and hora_int <= 11:
    print('Bom dia')
elif hora_int >= 12 and hora_int <= 17:
    print('Boa tarde')
elif hora_int >= 18 and hora_int <= 23:
    print('Boa noite')
else:
    print('Digite apenas números inteiros')


nome = input('Digite o seu nome: ')
letras = len(nome)

if letras <= 4:
    print('Seu nome é curto')
elif letras >= 5 and letras <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
