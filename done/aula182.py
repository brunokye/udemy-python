"""
Realmente aleatório
utilizar random.seed() não funciona
sendo assim é melhor para questões de segurança
"""

import secrets
import string as s
from secrets import SystemRandom as sr

print("".join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([0, 1, 2, 3, 4, 5]))

r_range = random.randrange(10, 20, 2)
# print(r_range)

r_int = random.randint(10, 20)
# print(r_int)

r_uniform = random.uniform(10, 20)
# print(r_uniform)

nomes = ["Luiz", "Maria", "Helena", "Joana"]
random.shuffle(nomes)
# print(nomes)

novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(nomes))
