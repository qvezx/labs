def read(var):
    try:
        if var == 1:
            with open ("example.txt") as example:
                content = example.read()
                print(content)

        elif var == 2:
            result = ""
            with open ("example.txt") as example:
                for line in example:
                    result += line

    except FileNotFoundError:
        print("Такого файла не существует")

print(read(1))