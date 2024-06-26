# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

text = """
    João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
    Maria era o nome dela.

    Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos
    atualmente. Maria, hoje sua esposa, ainda faz aquele café com pão de
    queijo nas tardes de domingo. Também né! Sendo a boa mineira que é,
    nunca esquece seu famoso pão de queijo.

    Não canso de ouvir a Maria:
    "Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
"""

print(re.findall(r"João|Maria|ad..tos", text))
print(re.findall(r"[Jj]oão|Maria", text))
print(re.findall(r"[A-Za-z]aria", text))
print(re.findall(r"jOãO|MaRiA", text, flags=re.I))
