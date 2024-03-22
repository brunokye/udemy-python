"""
Implementando o protocolo do Iterator em Python
Essa é apenas uma aula para introduzir os protocolos de collections.abc no
Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
estrutura usada nessa aula.
"""

from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next = 0

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self._index:
            self._next = 0
            raise StopIteration

        value = self._data[self._next]
        self._next += 1

        return value

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1


if __name__ == "__main__":
    lista = MyList()

    lista.append("Rafael", "Pedro")
    lista.append("Julio")
    lista[0] = "Felipe"

    for item in lista:
        print(item)
