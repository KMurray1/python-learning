class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length + self.width) * 2

if __name__ == '__main__':
    length = int(input('Length of rectangle: '))
    width = int(input('Width of rectangle: '))

    rect = Rectangle(length, width)

    print(f"Area of rectangle: {rect.calc_area()}")
    print(f"Perimeter of rectangle: {rect.perimeter()}")