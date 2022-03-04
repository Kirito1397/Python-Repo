def collatz_seq(number):
    if (number%2==0):
        x = number//2
        print(x)
        return x
    else :
        y = 3*number+1
        print(y)
        return (y)


try:
    print()
    user_input=int(input())  #User inputs value 
    while (user_input != 1):  
        """Collatz Sequeunce function is called and it returns the 
            processed output back to the user_input variable"""
        user_input=collatz_seq(user_input)  

except ValueError as ve:   # It provides an Exception statement, if ValueError is encountered.
    print("Enter Valid Integer Value")