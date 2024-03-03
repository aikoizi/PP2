import os
file_path = "c:/Users/Asus/PP2/pp2/lab6/dir-and-files/del.txt"

if not os.path.exists(file_path):
        print("File does not exist.")
else:
        os.remove(file_path)
        print("File deleted successfully.")

