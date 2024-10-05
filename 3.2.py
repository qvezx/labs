def user_input():
    text = input()

    with open ("input.txt", "a") as file:
        file.write(text)

print("Введите текст который хотите добавить в файл") 
user_input()