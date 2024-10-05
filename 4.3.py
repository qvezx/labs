from module import module2 as mdl2, module3 as mdl3

a = int(input("Введите 1 чтобы воспользоваться первым модулем и 2 чтобы воспользоваться вторым: "))

if (a == 1):
  b = int(input("Введите желаемый размер стороны квадрата: "))
  print(mdl2.square(b))

elif (a == 2):
  print("Введите текст: ")
  mdl3.user_inp()
  print("Текст добавлен в файл")

else:
  ("ошибка")

