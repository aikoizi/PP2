list = ['Adam', 'Marsel', 'Lev', 'Elias']

path = "C:/Users/Asus/PP2/pp2/lab6/dir-and-files/m.txt"
with open(path, 'w') as file:
        for item in list:
            file.write(str(item) + '\n')
print("List has been successfully written to the file.")