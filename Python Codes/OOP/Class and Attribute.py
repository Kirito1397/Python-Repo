# An attribute is a characteristic of an object
class Dog():

   # Class Object Attribute
    species = 'mammal'

    # __init__ method is used to initialize the attributes of an object.
    def __init__(self,breed):
        #Here the breed will attribute of 'Dog' class.
        self.breed = breed 

if __name__ == "__main__":
    mydog = Dog("Boxer")

    # Getting Class Object Attribute of 'mydog' instance
    print(mydog.species)

    # Getting attribute of 'mydog' instance
    print(mydog.breed)