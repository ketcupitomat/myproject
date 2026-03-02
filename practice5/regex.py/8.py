import re

text = "SplitThisStringAtUppercase"

result = re.findall(r"[A-Z][^A-Z]*", text)
print(result)