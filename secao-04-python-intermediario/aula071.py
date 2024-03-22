x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def soma(*args):
    total = 0

    for num in args:
        total += num

    return total


soma01 = soma(1, 2, 3, 4, 5, 6)
print(soma01)

numeros = 1, 2, 3, 4, 5, 6
soma02 = soma(*numeros)
print(soma02)

print(sum(numeros))
