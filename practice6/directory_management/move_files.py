import shutil
import os


os.makedirs("backup", exist_ok=True)


shutil.copy("sample.txt", "backup/sample.txt")
print("File copied!")


shutil.move("sample.txt", "backup/sample_moved.txt")
print("File moved!")