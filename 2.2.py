def describe_person (name, age = 30):
    return "Имя " + name + " Возраст " + str(age)

print (describe_person("Nikita"), describe_person("Nikita", 18))