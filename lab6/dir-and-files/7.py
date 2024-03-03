path = "C:/Users/Asus/PP2/pp2/lab6/dir-and-files/lev.txt"
path1 ="C:/Users/Asus/PP2/pp2/lab6/dir-and-files/lev1.txt"
with open(path, 'r') as source_file:
        content = source_file.read()
with open(path1, 'w') as destination_file:
        destination_file.write(content)
print("File content copied successfully.")