letras = set()

while True:
    letra = input('Digite uma letra: ').lower()
    letras.add(letra)

    if 's' in letras:
        print('Parabéns, você encontrou a letra secreta.')
        break

    print(letras)
