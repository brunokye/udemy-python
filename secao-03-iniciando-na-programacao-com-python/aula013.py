# '...' pode ser utilizado como placeholder -> imc = ...

nome = 'Bruno Ferreira'
altura = 1.7
peso = 70
imc = peso / (altura * altura)

# f-strings

print(f'{nome} tem {altura:.2f} de altura,')
print(f'pesa {peso} quilos e seu IMC é')
print(f'{imc:.2f}')
