'''
generator function - uma função
capaz de "pausar"
yield - o comando de "pausar"
'''

# def generator(n=0):
#     yield 1
#     print('Continuando')
#     yield 2
#     print(':)')

#     return 'Fim'


# gen = generator(n=0)

# print(next(gen))
# print(next(gen))
# print(next(gen))


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return


gen = generator(n=0)

for n in gen:
    print(n)
