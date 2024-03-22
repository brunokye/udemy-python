# nome = 'Bruno'

# print('r' in nome)
# print('z' in nome)

# print('no' in nome)
# print('zero' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
