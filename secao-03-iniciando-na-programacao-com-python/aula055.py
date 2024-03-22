import decimal

numero01 = 0.7
numero02 = 0.1

numero03 = numero01 + numero02

print(numero03)
print(f'{numero03:.2f}')
print(round(numero03, 2))

'''
usando 'Decimal'
caso seja necessário um cálculo de alta precisão
'''

numero01 = decimal.Decimal(0.7)
numero02 = decimal.Decimal(0.1)

numero03 = numero01 + numero02

print(numero03)
