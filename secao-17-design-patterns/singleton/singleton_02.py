def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        print("Test")
        self.theme = "O tema claro"
        self.font = "18px"


@singleton
class Test:
    def __init__(self):
        print("Test")


if __name__ == "__main__":
    as1 = AppSettings()
    as1.theme = "O tema escuro"
    as1.font = "16px"

    as2 = AppSettings()

    print(as1.theme)
    print(as2.theme)
    print(as1.font)
    print(as2.font)
    print(as1 == as2)

    t1 = Test()
    t2 = Test()
