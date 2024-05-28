class StringReprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__} | {self.__dict__} | {params}"

    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {"x": 10, "y": 20}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, first_name=None, last_name=None):
        if first_name is not None:
            self.first_name = first_name

        if last_name is not None:
            self.last_name = last_name


if __name__ == "__main__":
    m1 = MonoStateSimple("Bruno")
    # print(m1)

    m2 = MonoStateSimple(last_name="Ferreira")

    m1.x = "Test"  # type: ignore
    m2.y = "?"  # type: ignore

    print(m1)
    print(m2)
