def is_prime (number):
    a = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            a += 1
    if (a > 2): 
        return False
    else:
        return True

b = int(input())

print(is_prime(b))
    