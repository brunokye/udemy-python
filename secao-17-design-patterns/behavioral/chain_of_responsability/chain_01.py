"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

# Implementing using functions


def handler_ABC(letter: str) -> str:
    letters = ["a", "b", "c"]

    if letter.lower() in letters:
        return f"handler_ABC: Letter {letter} was found!"

    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ["d", "e", "f"]

    if letter.lower() in letters:
        return f"handler_DEF: Letter {letter} was found!"

    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f"handler_unsolved: Letter {letter} was not found!"


if __name__ == "__main__":
    print(handler_ABC("A"))
    print(handler_ABC("B"))
    print(handler_ABC("D"))
    print(handler_ABC("G"))
