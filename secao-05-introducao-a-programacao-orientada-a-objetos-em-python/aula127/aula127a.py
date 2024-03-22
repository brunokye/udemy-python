import json

CAMINHO_ARQUIVO = "aula127/aula127.json"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("João", 23)
p2 = Pessoa("Helena", 32)
p3 = Pessoa("Gabriel", 52)
bd = [vars(p1), vars(p2), vars(p3)]


def dump():
    with open(CAMINHO_ARQUIVO, "w", encoding="UTF-8") as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    print("Arquivo A é o __main__")
    dump()
