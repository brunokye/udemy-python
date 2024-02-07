'''
Funções decoradoras e decoradores
Decorar = Adicionar/Remover/Restringir/Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
usar as funções decoradoras em outras funções.
Decoradores são "Syntax Sugar"
'''


def create_function(func):
    def inside(*args, **kwargs):
        for arg in args:
            is_string(arg)

        return func(*args, **kwargs)

    return inside


@create_function
def reserve_string(string):
    print(reserve_string.__name__)
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


reversed = reserve_string('123')

print(reversed)
