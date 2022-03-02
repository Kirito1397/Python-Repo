for _ in range(int(input())):
    R = int(input())
    if R >= 2000:
        print(1)
    elif R>=1600 and R<2000:
        print(2)
    elif R < 1600:
        print(3)