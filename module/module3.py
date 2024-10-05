def user_inp():
    text = input()

    with open ("input2.txt", "a") as file:
        file.write(text)
