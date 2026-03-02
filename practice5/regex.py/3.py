import re

pattern = r"^[a-z]+_[a-z]+$"

strings = ["hello_world", "Hello_world", "test_case_example"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")