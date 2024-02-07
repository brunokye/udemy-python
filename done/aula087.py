lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, str):
        print(f'str: {item.upper()}')
    elif isinstance(item, (int, float)):
        print(f'num: {item, item * 2}')
    elif isinstance(item, set):
        print(f'set: {item}')
    else:
        print(f'outros: {item}')
