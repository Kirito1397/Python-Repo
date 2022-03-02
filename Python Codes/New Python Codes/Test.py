# # cook your dish here
x = ""
for i in range(10):
    x = x + f"{i}\n"

with open("file_test_2.txt", "w+") as f:
    f.write("Hello World!!! .... \n{}".format(x))

filee = open('file_test_2.txt','r')
print(filee.read())
