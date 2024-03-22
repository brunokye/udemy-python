string = 'Bruno'
metodo = 'upper'

try:
    if hasattr(string, 'upper'):
        print(getattr(string, metodo)())
except Exception:
    print(f'Não existe o método {metodo}')
