class triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.char=1/2

    def area(self):
        print(f'area of triange with {self.base} and {self.height} is {self.char*self.base * self.height}')
