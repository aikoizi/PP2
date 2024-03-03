import os

path = r"C:/Users/Asus/PP2/pp2/lab6/dir-and-files"

exists = os.path.exists(path)
readable = os.access(path, os.R_OK)
writable = os.access(path, os.W_OK)
executable = os.access(path, os.X_OK)

print("Path exists:", exists)
if exists:
    print("Readable:", readable)
    print("Writable:", writable)
    print("Executable:", executable)
