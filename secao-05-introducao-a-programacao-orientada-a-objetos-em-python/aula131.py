"""
@property - um getter no modo Pythônico
getter - um método para obter um atributo
cor -> get_cor()

modo pythônico - modo do Python de fazer coisas
@property é uma propriedade do objeto, ela
é um método que se comporta como um atributo.

Geralmente é usada nas seguintes situações:
- como getter
- p/ evitar quebrar código cliente (é o código que usa seu código)
- p/ habilitar setter
- p/ executar ações ao obter um atributo
"""


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    def get_cor(self):
        print("GET cor")
        return self.cor

    @property
    def cor(self):
        print("Property 01")
        return self.cor_tinta

    @property
    def cor_tampa(self):
        print("Property 02")
        return 123456


caneta = Caneta("Azul")
print(caneta.cor)
print(caneta.cor_tampa)
