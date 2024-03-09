class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    
v1 = Vector(2,3)
v2 = Vector(-1,1)

result = v1 + v2
print(f"Resultant vector: {result.x}, {result.y}")