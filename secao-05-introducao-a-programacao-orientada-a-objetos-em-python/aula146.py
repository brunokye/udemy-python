"""
Para criar uma Exception em Python, você só
precisa herdar de alguma exceção da linguagem.
A recomendação da doc é herdar de Exception.

Criando exceções (comum colocar Error ao final)
Levantando (raise) / Lançando (throw) exceções
Relançando exceções
Adicionando notas em exceções (3.11.0)
"""


class MeuError(Exception):
    ...


class OutroErro(Exception):
    ...


def levantar():
    exception = MeuError("a", "b", "c")
    exception.add_note("Olha a nota 01")
    exception.add_note("01 - Nota um")
    raise exception


try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(f"Erro lançado: {error}")

    exception = OutroErro("Vou lançar de novo.")
    exception.__notes__ = error.__notes__.copy()
    exception.add_note("02 - Nota dois")
    raise exception
