dimensions = list(map(int,input().split()))
# for row in range(dimensions[0]):

# The Top Part
for column in range(dimensions[1]):
    if column < (((dimensions[0]+1)/2)-1):
        print(
        "-"*((int((dimensions[1]-3)/2))-(3*column))
        +
        ".|."*(1+(column*2))
        +
        ("-"*((int((dimensions[1]-3)/2))-(3*column))).rjust(0)
        )

#The Center Welcome
print(
"-"*(int((dimensions[1]-7)/2))+"WELCOME"+"-"*(int((dimensions[1]-7)/2))
)

#The Lower Part
x9=(int((dimensions[1]-3)/2))
y3= (int((((dimensions[0]+1)/2)-1)))

for column in range(dimensions[1]):
    if column < (((dimensions[0]+1)/2)-1):
        print(
        "-"*(int(x9/y3)+(3*column))
        +
        ".|."*(1+((int((((dimensions[0]+1)/2)-1))) -1 -column) *2 )
        +
        ("-"*(int(x9/y3)+(3*column))).rjust(0)
        )

    # ---------.|.---------
    # ------.|..|..|.------
    # ---.|..|..|..|..|.---
    # -------WELCOME-------
    # ---.|..|..|..|..|.---
    # ------.|..|..|.------
    # ---------.|.---------


# ALTERNATE :
# ===============

# if __name__ == '__main__':
#         N, M = map(int, input().split(" "))

#         for i in range(N):
#                 pattern = ".|."
#                 if i < (N-1)/2:
#                         print((pattern * (2*i+1)).center(M, "-"))
#                 elif i == (N-1)/2:
#                         print("WELCOME".center(M, "-"))
#                 else:
#                         print((pattern * (2*(N-1-i)+1)).center(M, "-"))


# ++++++++++++++++++++++++++++++++++++++OR+++++++++++++++++++++++++++++++++++++++++++++++


# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

