# cook your dish here
for _ in range(int(input())):
    values = list(map(int,input().split()))
    N = values[0]
    p = values[1]
    k = values[2]
    mod_list = []
    for j in range(k):
        for i in range(N):
            if i%k == j:
                mod_list.append((i,i%k))
    for x in range(len(mod_list)):
        if mod_list[x][0] == p:
            print(x+1)
    print(mod_list)