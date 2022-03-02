n = int(input())
item = []
for i in range(n):
    num = int(input())
    item.append(num)
item.sort()
new_item = [0]
for k in range(n):
    if item[k]*(n-k) > new_item[0]:
        new_item[0] = item[k]*(n-k)
print(new_item[0])