'''
We've learned that while functions can take in different arguments, methods belong to the objects they act on. 
In Python, polymorphism refers to the way in which different object classes can share the same method name, and
those methods can be called from the same place even though a variety of different objects might be passed in.
'''

# The literal meaning of polymorphism is the condition of occurrence in different forms.
# Polymorphism is a very important concept in programming. It refers to the use of a single type 
# entity (method, operator or object) to represent different types in different scenarios.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

if __name__ == "__main__":

    cat1 = Cat("Kitty", 2.5)
    dog1 = Dog("Fluffy", 4)

    for animal in (cat1, dog1):
        animal.make_sound()
        animal.info()
        animal.make_sound()
