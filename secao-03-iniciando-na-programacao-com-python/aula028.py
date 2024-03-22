nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
espaco = ...

print(f'\n{20 * "-"}\n')

if ' ' in nome:
    espaco = 'Seu nome contém espaços'
else:
    espaco = 'Seu nome não contém espaços'

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(espaco)
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A primeira letra do seu nome é {nome[-1]}')
else:
    print('Deculpe, você deixou campos vazios.')
