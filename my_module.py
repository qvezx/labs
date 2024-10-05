def fact(num):
    a = 1
    i = 1

    if (num == 0):
       return 1
    
    else :
      for i in range (num):
        i += 1
        a *= i
      return a