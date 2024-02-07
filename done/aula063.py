import re
import sys

entrada = input('Digite o seu CPF [000.000.000-00]: ')

cpf = re.sub(r'[^0-9]', '', entrada)
numero = cpf[0]

if numero * len(cpf) == cpf:
    print('Você enviou números repetidos.')
    sys.exit()

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
