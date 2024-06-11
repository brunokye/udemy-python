# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação

import re


cpf = "test 147.852.963-12 test"
print(re.findall(r"((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})", cpf))

cpf = "test 147.852.963-12"
print(re.findall(r"^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})", cpf))

cpf = "147.852.963-12 test"
print(re.findall(r"^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})", cpf))

cpf = "test 147.852.963-12 test"
print(re.findall(r"^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$", cpf))

cpf = "147.852.963-12"
print(re.findall(r"[^0-9]+", cpf))
