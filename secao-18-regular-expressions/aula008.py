# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n

import re

text = """
131.768.460-53 ABC
055.123.060-50 DEF
955.123.060-90
"""

print(re.findall(r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$", text, flags=re.M))

test = "O João gosta de folia \n E adora ser amado"
print(re.findall(r"^o.*o$", test, flags=re.I | re.S))
