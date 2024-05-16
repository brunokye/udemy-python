def new_sum(x, y):
    """
    >>> new_sum(10, 30)
    40

    >>> new_sum("10", 30)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float.
    """

    assert isinstance(x, (int, float)), "x precisa ser int ou float."
    assert isinstance(y, (int, float)), "y precisa ser int ou float."
    return x + y


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
