def multiplica(*args):
    total = 1

    for num in args:
        total *= num

    return total


def par_impar(num):
    if num % 2 == 0:
        return f'{num} é par.'
    return f'{num} é ímpar.'


resultado01 = multiplica(1, 2, 3, 4, 5)
resultado02 = par_impar(resultado01)

print(resultado02)
