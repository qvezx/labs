def read(var):
  if var == 1:
    with open ("example.txt") as example:
      content = example.read()
      return content

  elif var == 2:
    result = ""
    with open ("example.txt") as example:
      for line in example:
        result += line
      return result

a = int(input("Выбирете каким способом хотите открыть файл(цифра 1 - первый способ, цифра 2 - второй способ): "))

if (a == 1):
  print(read(1))

elif (a == 2):
  print(read(2))

else:
  print("такого варианта не существует")