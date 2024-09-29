def greet(name):
    return "hello " + name

def square(number):
    return "Квадрат числа " + str(number) + " равен " + str(number**2)

def square2 (number):
    return number **2

def max_of_two(x,y):
    return "Максимальное число " + str(max(x,y))

print(greet("Никита"), square2(5), square(4), max_of_two(3,10))