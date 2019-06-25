class Circle():

    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius
    
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(60)

print(my_circle.get_circumference())