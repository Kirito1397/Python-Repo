# Methods are functions defined inside the body of a class.
class Dog():
    species = 'mammel'

    def __init__(self,breed):
        self.breed = breed

    # 'Bark' is a method defined here, which takes 1 argument
    def bark(self,level):
        self.level = level
        return "Wooooof" if level=="loud" else "Woof"


if __name__ == "__main__":
    mydog = Dog("Poodle")

    print(mydog.breed)
    print(mydog.bark("loud"))