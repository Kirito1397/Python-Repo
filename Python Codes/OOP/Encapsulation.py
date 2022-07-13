'''Encapsulation in Python using public members'''

# illustrating public members & public access modifier 
class PubMod:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def age(self): 
        # accessing public data member 
        print("Age: ", self.age)
# creating object 
obj = PubMod("Jason", 35)
# accessing public data member 
print("Name: ", obj.name)  
# calling public member function of the class 
obj.age()


#############################################################################################################################

'''Encapsulation in Python using private members'''

# illustrating private members & private access modifier 
class Rectangle:
  __length = 0 #private variable
  __breadth = 0#private variable
  def __init__(self): 
    #constructor
    self.__length = 5
    self.__breadth = 3
    #printing values of the private variable within the class
    print(self.__length)
    print(self.__breadth)
 
rect = Rectangle() #object created 
#printing values of the private variable outside the class 
print(rect.length)
print(rect.breadth)


#############################################################################################################################

'''Encapsulation in Python using protected members'''



# illustrating protected members & protected access modifier 
class Details:
    _name="Jason"
    _age=35
    _job="Developer"
class ProtectedMod(Details):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)
 
# creating object of the class 
obj = ProtectedMod()
# direct access of protected member
print("Name:",obj.name)
print("Age:",obj.age)
