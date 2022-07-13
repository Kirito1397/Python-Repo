def SampleDecorator(func):
    def inner():
        print('This is a Before Function execution')
        func()
        print('This is a After Function execution')
    return inner

@SampleDecorator
def SampleFunction():
    print('This is a Function')


def the_square(func):
    def inner(a)-> int:
        print(a**2)
        return func(a)
    return inner

@the_square
def enter_num(num):
    print(num)
    return num

if __name__ == '__main__':
    # SampleFunction()
    enter_num(2)


################################################################################################################3

'''Decorator example for Class'''

class TheDecorator():
    def __init__(self,func):
        self.func = func
        
    def __call__(self):
        print('This is the Decorator Ending')
        self.func()
        print('This is the Decorator Ending')

@TheDecorator
class MyFunc():
    def __init__(self):
        print("This is My Function")

Sample  = MyFunc()
