"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        print("Test")
        self.theme = "O tema claro"
        self.font = "18px"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.theme = "O tema escuro"
    as1.font = "15px"

    as2 = AppSettings()

    print(as1.theme)
    print(as2.theme)
    print(as1.font)
    print(as2.font)
    print(as1 == as2)
