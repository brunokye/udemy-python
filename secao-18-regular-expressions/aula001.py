# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

import re

string = "This is a regular expression test (test)."
print(re.search(r"test", string))
print(re.findall(r"test", string))
print(re.sub(r"test", "ABCD", string, count=1))

print(f"\n{20 * '-'}\n")

regexp = re.compile(r"test")
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub("ABCD", string, count=1))
