'''
set - Conjunto em Python (tipo set)
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.

Sets são eficientes para remover valores duplicados
de iteráveis.
- Não aceitam valores mutáveis;
- Seus valores serão sempre únicos;
- não tem índexes;
- não garantem ordem;
- são iteráveis (for, in, not in)

Métodos úteis:
add, update, clear, discard

Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença (-) - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
'''

s1 = set('Luiz')
print(s1)

l1 = [1, 2, 3, 3, 3, 3, 3, 3, 4, 5]
s2 = set(l1)
print(s2)

s1.add('Bruno')
s1.update('2')
print(s1)

s1.discard('Bruno')
print(s1)

print(f'\n{20 * "-"}\n')

s3 = {1, 2, 3}
s4 = {2, 3, 4}

s5 = s3 | s4
print(f'União: {s5}')

s5 = s3 & s4
print(f'Intersecção: {s5}')

s5 = s3 - s4
print(f'Diferença (só tem no 1º): {s5}')

s5 = s4 - s3
print(f'Diferença (só tem no 2º): {s5}')

s5 = s3 ^ s4
print(f'Diferença Simétrica (falta em ambos): {s5}')
