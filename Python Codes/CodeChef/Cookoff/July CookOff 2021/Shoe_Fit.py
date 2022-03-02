num = int(input())
l2= []
for i in range(num):
    l1 = list(map(int,input().split()))
    if 0 in l1 and 1 in l1:
        l2.append("1")
    else:
        l2.append("0")
print("\n".join(l2[0:]))