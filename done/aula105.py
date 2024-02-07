def decorator_factory(a, b, c):
    print('Fábrica')

    def decorator(func):
        print('Decoradora')

        def nested(*args, **kwargs):
            print('Aninhada')
            return func(*args, **kwargs)

        return nested
    return decorator


@decorator_factory(1, 2, 3)
def sum(x, y):
    return x + y


multiply = decorator_factory(1, 2, 3)(lambda x, y: x * y)

sum01 = sum(10, 5)
mult01 = multiply(10, 5)

print(sum01)
print(mult01)
