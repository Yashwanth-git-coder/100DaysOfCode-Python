with open("file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode= "a") as file:
    file.write("\n New file.")