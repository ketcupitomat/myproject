import re

pattern = r"a.*b"

strings = ["ab", "axb", "axxxb", "a123b", "ac"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")