# https://regex101.com/r/wjfSus/1/

import re

string = """
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1

Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
"""


def is_float(string):
    return bool(re.search(r"^[+-]?\d+(?:\.\d+)?$", string))


def is_int(string):
    return bool(re.search(r"^[+-]?\d+$", string))


while True:
    number = input("Type a number: ")

    if is_int(number):
        number = int(number)
        print(f"The number {number} was converted to int.")
        continue

    if is_float(number):
        number = float(number)
        print(f"The number {number} was converted to float.")
        continue
