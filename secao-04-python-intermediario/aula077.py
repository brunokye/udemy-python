perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
contador = 0

for pergunta in perguntas:
    print(f'Pergunta: {pergunta["Pergunta"]}')

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')

    usuario = input('Escolha uma opção: ')

    try:
        usuario = int(usuario)
    except Exception:
        print('\nDigite apenas números.\n')
        break

    if pergunta['Opções'][int(usuario)] == pergunta['Resposta']:
        contador += 1
        print('Acertou :)\n')
        continue

    print('Errou :/\n')

print(f'Você acertou {contador} de {len(perguntas)} perguntas.')
