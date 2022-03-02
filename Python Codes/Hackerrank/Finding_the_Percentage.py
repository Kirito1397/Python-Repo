num = int(input())
info = []
dict = {}
perc = 0
for x in range(num):
    info = list(map(str,input().split(" "))) #Storing the input into a List format
    # print(info[1])
    dict[info[0]] = [] # Adding Key to dictionary beforehand and not in the below Loop to avoid loop from calling empty dictionary
    for x in range(1,len(info)):
        dict[info[0]].append(info[x]) #Appending the values to the Keys.

# print(dict)
# user_input = str(input())
x = dict[input()]
for i in x:
    perc += float(i)
print("{:.2f}".format(perc/len(x)))    


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()   #------------> This is a GOOOD Approach
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()