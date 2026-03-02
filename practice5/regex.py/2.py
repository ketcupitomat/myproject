import re

pattern = r"ab{2,3}"

strings = ["ab", "abb", "abbb", "abbbb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")