"""
Simple Python Code for Hello World
and taking inputs from the User
"""
# print("Hello World\n")

print("What is your name ?")
name=input()  # User needs to enter the Name

print("It is Nice to meet you " + str(name))

print("What is your current Age ?") 
age=int(input())  # User needs to enter the Age

if age<30:
    print ("So, you are " + str(age) + ". You are quite young and have a great life ahead of you")
elif 30<age<50:
    print ("So, you are " + str(age) + ". It seems you will soon hit mid-life crisis.\nJust Joking")
elif 50<age<90:
    print ("So, you are " + str(age) + ". Better Start on the savings for the retirement man!")
elif 90<age<110:
    print ("Seriously! you are " + str(age) + ".""\nThat is hard to belive ")
elif age>110:
    print ("So, you are " + str(age) + ". Don't fool around and enter a proper age")    