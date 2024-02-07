cpf = '51868434826'
valores = cpf[:9]
contador = 10
resultado = 0

for numero in valores:
    resultado += int(numero) * contador
    contador -= 1

digito01 = (resultado * 10) % 11
digito01 = digito01 if digito01 <= 9 else 0

print(digito01)
