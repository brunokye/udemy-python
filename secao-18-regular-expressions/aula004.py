# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1

import re

text = "<p>Frase 1</p> <p>:)</p> <p>Test</p> <div></div>"

print(re.findall(r"<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>", text))  # greedy
print(re.findall(r"<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>", text))  # lazy
