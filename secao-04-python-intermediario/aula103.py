def create_function(func):
    def inside(*args, **kwargs):
        for arg in args:
            is_string(arg)

        return func(*args, **kwargs)

    return inside


def reserve_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


check_param = create_function(reserve_string)
reversed = check_param('123')

print(reversed)
