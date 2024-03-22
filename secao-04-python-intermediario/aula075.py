def calculo(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = calculo(2)
triplicar = calculo(3)
quadruplicar = calculo(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))
