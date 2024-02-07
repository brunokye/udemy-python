x = 1


def escopo():
    x = 10

    def outra_funcao():
        x = 11
        print(f'x da outra função: {x}')

    outra_funcao()
    print(f'x do escopo: {x}')


print(f'x inicial: {x}')
escopo()
print(f'x após as funções: {x}')
