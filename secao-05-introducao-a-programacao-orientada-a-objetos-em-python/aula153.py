class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(f"{nome} está chamando {self.phone}")
        return "Teste"


c1 = CallMe("4324234234")
teste = c1("Bruno")
print(teste)
