from itertools import zip_longest


def list_sum01(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i] + l2[i]) for i in range(intervalo)]


l1 = [10, 2, 3, 4, 5]
l2 = [12, 2, 3, 6, 50, 60, 70]

list_sum02 = [x + y for x, y in zip(l1, l2)]
list_sum03 = [x + y for x, y in zip_longest(l1, l2, fillvalue=0)]

print(list_sum01(l1, l2))
print(list_sum02)
print(list_sum03)
