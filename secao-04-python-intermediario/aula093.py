try:
    a = 18
    b = 0
    c = a / b
except ZeroDivisionError as error:
    print(f'Error: {error}')
except NameError as error:
    print(f'Error: {error}')
except (TypeError, IndexError) as error:
    print(f'Error: {error}')
except Exception as error:
    print(f'Unknown Error: {error}')

print('Ponto 01')
