cpf = '51868434826'
valores = cpf[:9]
contador = 10
resultado = 0

for numero in valores:
    resultado += int(numero) * contador
    contador -= 1

digito01 = (resultado * 10) % 11
digito01 = digito01 if digito01 <= 9 else 0

valores = valores + str(digito01)
contador = 11
resultado = 0

for numero in valores:
    resultado += int(numero) * contador
    contador -= 1

digito02 = (resultado * 10) % 11
digito02 = digito02 if digito02 <= 9 else 0

resultado = valores + str(digito02)

if resultado == cpf:
    print('CPF válido.')
else:
    print('CPF inválido.')
