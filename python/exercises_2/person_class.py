class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name} you are {self.age} ya old feck!"
    
person = Person('Billy', 55)
print(person.greet())