'''
enumerate -> enumera iteráveis
ao "gastar" todos os elementos, a lista fica "vazia"

'''

nomes = ['Maria', 'Helena', 'Luiz']
nomes.append('João')

# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# lista_enumerada = list(enumerate(nomes))

# for nome in lista_enumerada:
#     print(nome)

for i, nome in enumerate(nomes):
    print(i, nome)
