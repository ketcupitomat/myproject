
with open("sample.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is Practice 6\n")
    f.write("File handling in Python\n")

print("File created and data written.")

with open("sample.txt", "a") as f:
    f.write("Appending a new line\n")
    f.write("Python is easy!\n")

print("New lines appended.")