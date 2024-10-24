class circle:
    
    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        print (f"Радиус: {self.radius}")

a = int(input("Введите значение радиуса: "))
circ = circle(a)
circ.get_radius()

b = int(input("Введите новое значение радиуса: "))
circ.set_radius(b)
circ.get_radius()