frase = 'O Python é uma linguagem de programação multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

i = 0
counter = 0
letra = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_vezes = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_vezes > counter:
        letra = letra_atual
        counter = qtd_vezes

    i += 1

print(f'A letra "{letra}" apareceu {counter} vezes.')
