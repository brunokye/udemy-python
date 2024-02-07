nome = 'Bruno Ferreira'
novo_nome = ''
letra = 0

while letra < len(nome):
    novo_nome += f'*{nome[letra]}'
    letra += 1

print(novo_nome + '*')
