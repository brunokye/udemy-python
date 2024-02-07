class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


# p1 = Pessoa("João", 35)

dados = {"nome": "João", "idade": 35}
p1 = Pessoa(**dados)

p1.__dict__["outra"] = "coisa"
p1.__dict__["nome"] = "Bruno"
# p1.nome = 'Teste'

print(p1.__dict__)
print(vars(p1))
