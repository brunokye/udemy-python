# Meta caracteres: ^ $
# ()     \1
# ()()   \1 \2
# (())() \1 \2 \3

import re
from pprint import pprint

text = "<p>Frase 1</p> <p>:)</p> <p>Test</p> <div></div>"
pprint(re.findall(r"<([pdiv]{1,3})>.*?<\/\1>", text))
pprint(re.findall(r"<([pdiv]{1,3})>(?:.*?)<\/\1>", text))
pprint(re.findall(r"<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>", text))
pprint(re.sub(r"(<(.+?)>)(.+?)(<\/\2>)", r"\1\4", text))

print(f"\n{20 * '-'}\n")

tags = re.findall(r"(<([pdiv]{1,3})>.*?<\/\2>)", text)
pprint(tags)

print(f"\n{20 * '-'}\n")

for tag in tags:
    one, two = tag
    print(f"{one} | {two}")

print(f"\n{20 * '-'}\n")

cpf = "test 147.852.963-12 test"
print(re.findall(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}", cpf))
print(re.findall(r"((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})", cpf))
