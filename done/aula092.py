def gen1():
    print('COMEÇO - GEN1')
    yield 1
    yield 2
    yield 3
    print('FIM - GEN1')


def gen2(gen=None):
    print('COMEÇO - GEN2')

    if gen is not None:
        yield from gen

    yield 4
    yield 5
    yield 6
    print('FIM - GEN2')


def gen3():
    print('COMEÇO - GEN3')
    yield 10
    yield 20
    yield 30
    print('FIM - GEN3')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)

print(f'\n{20 * "-"}\n')

for numero in g2:
    print(numero)

print(f'\n{20 * "-"}\n')

for numero in g3:
    print(numero)
