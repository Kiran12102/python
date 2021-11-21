class circle():
    def __init__(self, radius):
        self.radius = radius
        self.pie = 3.14

    def area(self):
        print(f'area of circle with {self.radius} is {self.pie * self.radius**2}')
