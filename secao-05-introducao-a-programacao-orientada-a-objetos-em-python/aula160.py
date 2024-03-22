"""
namedtuples - tuplas imutáveis com nomes para valores
Usamos namedtuples para criar classes de objetos que são apenas um
agrupamento de atributos, como classes normais sem métodos, ou registros de
bases de dados, etc. As namedtuples são imutáveis assim como as tuplas.
"""

# from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = "PADRÃO"
    naipe: str = "PADRÃO"


# Carta = namedtuple(
#   "Carta", ["valor", "naipe"], defaults=["PADRÃO", "PADRÃO"]
# )
as_espadas = Carta("A", "Espadas")

print(as_espadas)
print(as_espadas._asdict())
print(as_espadas.valor, as_espadas.naipe)

print(f"\n{20 * '-'}\n")

print(as_espadas._fields)
print(as_espadas._field_defaults)

print(f"\n{20 * '-'}\n")

for valor in as_espadas:
    print(valor)
