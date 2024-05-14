from calculator import new_sum

print(new_sum(1, 2))
print(new_sum(-10, 5))

try:
    print(new_sum("6", 3))
except AssertionError as e:
    print(f"Número inválido: {e}")

try:
    print(new_sum(6, "3"))
except AssertionError as e:
    print(f"Número inválido: {e}")
