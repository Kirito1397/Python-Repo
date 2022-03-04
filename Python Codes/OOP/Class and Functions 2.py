class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius 
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
'''
In the __init__ method above, in order to calculate the area attribute, we had to call Circle.pi.
This is because the object does not yet have its own .pi attribute, so we call the Class Object 
Attribute pi instead.
In the setRadius method, however, we'll be working with an existing Circle object that does have 
its own pi attribute. Here we can use either Circle.pi or self.pi.
'''