'''
Inheritance is a way to form new classes using classes that have already been defined.
The newly formed classes are called derived classes, the classes that we derive from 
are called base classes. Important benefits of inheritance are code reuse and reduction
of complexity of a program. 
The derived classes (descendants) override or extend the functionality of base classes (ancestors).
'''

class Animal():
    def __init__(self):
        print("Animal Created")

    # The function from Base class can be overwritten/modified
    def whoami(self):
        print("Animal")

    def eat(self):
        print("Eating (Function of Base class)")

class Dog(Animal):
    def __init__(self):

        # invoking the __init__ of the parent class
        Animal.__init__(self)
        print("Dog Created")
    
    def whoami(self):
        print("Dog")

    # Derived class extends the functionality of the base class, by defining a new bark() method.
    def bark(self):
        print("Woof")

if __name__ == "__main__":

    mydog = Dog()

    mydog.whoami()
    mydog.eat()
    mydog.bark()



######################################################################################################################


'''Example of invoking Parent Class __init__ method in Child Class'''

# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class

class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
