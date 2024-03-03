import os

path = "C:/Users/Asus/PP2/pp2/lab6/dir-and-files/meme.txt"

exists = os.path.exists(path)

if exists:
    print("Path exists.")
    directory, filename = os.path.split(path)
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path does not exist.")