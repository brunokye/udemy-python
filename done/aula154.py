# class Multiplicar:
#     def __init__(self, func):
#         self.func = func
#         self._multiplicador = 10

#     def __call__(self, *args, **kwargs):
#         return self.func(*args, **kwargs) * self._multiplicador


# @Multiplicar
# def soma(x, y):
#     return x + y


class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador

        return interna


@Multiplicar(2)
def soma(x, y):
    return x + y


print(soma(2, 2))
