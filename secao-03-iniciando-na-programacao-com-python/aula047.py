import os
import random
import platform

lista_palavras = [
    'abacaxi',
    'girassol',
    'computador',
    'cachoeira',
    'lapis',
    'avião'
]

palavra = random.choice(lista_palavras)
acertou = ''
tentativas = 0

print(f'Palavra: {"*" * len(palavra)}')

while True:
    letra = input('Digite uma letra: ').lower()
    tentativas += 1
    resultado = ''

    if len(letra) > 1 or not letra.isalpha():
        print('Digite apenas uma letra.')
        continue

    if letra in palavra:
        acertou += letra

    for letra in palavra:
        if letra in acertou:
            resultado += letra
        else:
            resultado += '*'

    if resultado == palavra:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        print(f'Parabéns, você acertou, a palavra é: {palavra}')
        print(f'Você conseguiu descobrir em {tentativas} tentativas.')

        break

    print(f'Palavra: {resultado}')
