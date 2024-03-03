import os
path = "C:/Users/Asus/PP2/pp2/lab6/dir-and-files/kuro.txt"
with open(path, 'r') as file:
            line_count = len(file.readlines())

print("Number of lines in the file:",line_count)



