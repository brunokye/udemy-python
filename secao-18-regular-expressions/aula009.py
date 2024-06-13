import re
from pprint import pprint

text = """
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
"""

# pprint(re.findall(r"\w+\s(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)", text))
# pprint(re.findall(r"\w+\s(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)", text))

# print(re.findall(r"(?=.*inactive).+", text))
# print(re.findall(r"(?=.*[^in]active).+", text))

pprint(re.findall(r"\w+(?<=ONLINE)\s(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+", text))
pprint(re.findall(r"\w+(?<!ONLINE)\s(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+", text))
