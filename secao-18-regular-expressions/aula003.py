# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

import re

text = """
    João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
    Maria era o nome dela.

    Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos
    atualmente. Maria, hoje sua esposa, ainda faz aquele café com pão de
    queijo nas tardes de domingo. Também né! Sendo a boa mineira que é,
    nunca esquece seu famoso pão de queijo.

    Não canso de ouvir a Maria:
    "Joooooooooãooooooo, o café tá prontinho aqui. Veeemm vem"!
"""

print(re.findall(r"jo+ão+", text, flags=re.I))
print(re.findall(r"ve{3}m{1,2}", text, flags=re.I))
# print(re.sub(r"jo+ão+", "Bruno", text, flags=re.I))
# print(re.sub(r"jo*ão+", "Bruno", text, flags=re.I))
# print(re.sub(r"jo?ão+", "Bruno", text, flags=re.I))
print(re.sub(r"jo{1,}ão{1,}", "Bruno", text, flags=re.I))

test = "João ama ser amado."

print(re.findall(r"ama[do]*", test, flags=re.I))
print(re.findall(r"ama[do]{0,2}", test, flags=re.I))
