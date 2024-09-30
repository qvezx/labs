def user_input():
    text = input()

    with open ("input.txt", "a") as file:
        file.write(text)

user_input()