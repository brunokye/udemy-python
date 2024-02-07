import importlib

import aula098a

print(aula098a.variavel)

for i in range(10):
    importlib.reload(aula098a)
    print(i)

print('Fim')
