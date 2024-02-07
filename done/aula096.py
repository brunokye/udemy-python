'''
inteiro - import nome_modulo
Vantagens: você tem o namespace do módulo
Desvantagens: nomes grandes
'''

# import sys

# print(sys.platform)
# sys.exit()


'''
partes - from nome_modulo import objeto1, objeto2
Vantagens: nomes pequenos
Desvantagens: Sem o namespace do módulo
'''

# from sys import exit, platform

# print(platform)
# exit()


'''
alias 1 - import nome_modulo as apelido
alias 2 - from nome_modulo import objeto as apelido
Vantagens: você pode reservar nomes para seu código
Desvantagens: pode ficar fora do padrão da linguagem
'''

# import sys as s

# print(s.platform)

# from sys import exit as ex
# from sys import platform as pf

# print(pf)
# ex()


'''
má prática - from nome_modulo import *
Vantagens: importa tudo de um módulo
Desvantagens: importa tudo de um módulo
'''

# from sys import *

# print(platform)
# exit()
