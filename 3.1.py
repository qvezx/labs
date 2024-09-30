def first():
    with open ("example.txt") as example:
        content = example.read()
        print(content)

def second():
    result = ""
    with open ("example.txt") as example:
        for line in example:
            result += line

        print(result)

print(first(), second())