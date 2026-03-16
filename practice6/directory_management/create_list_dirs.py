import os


os.makedirs("parent/child/grandchild", exist_ok=True)

print("Nested directories created!")


items = os.listdir()

print("Files and folders:")
for item in items:
    print(item)



extension = ".txt"

for file in os.listdir():
    if file.endswith(extension):
        print("Found:", file)