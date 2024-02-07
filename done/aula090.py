'''
generator expression:
não guarda todos os valores em memória,
ela age como um loop que gera valores conforme necessário,
"lembra" onde parou internamente
e não precisa armazenar os valores gerados.
'''

import sys

# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable)  # tem __iter__ e __next__
# print(next(iterator))

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# print(generator)
# print(next(generator))

# for n in generator:
#     print(n)
