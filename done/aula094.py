'''
try:
    ...
except:
    ...

try:
    ...
finally:
    ...

try:
    ...
except:
    ...
else:
    ...
'''

try:
    print('Ponto 01')
    print(8 / 0)
except ZeroDivisionError as error:
    print(f'{error.__class__.__name__}: {error}')
finally:
    print('Ponto 02')
