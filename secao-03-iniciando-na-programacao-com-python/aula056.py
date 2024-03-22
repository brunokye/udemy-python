"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip (rstrip e lstrip) - remove os espaços
"""

frase = 'Bruno, olha só que coisa interessante'
frases = frase.split(',')
frases_corrigidas = []

for i, frase in enumerate(frases):
    frases_corrigidas.append(frases[i].strip())

frases_unidas = ', '.join(frases_corrigidas)

print(frases)
print(frases_corrigidas)
print(frases_unidas)
