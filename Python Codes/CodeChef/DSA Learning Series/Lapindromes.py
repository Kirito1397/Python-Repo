for _ in range(int(input())):
    string = str(input())
    n= len(string)
    reoccur_1,reoccur_2 = [],[]
    half = int(n/2)
    pre_half = string[:(half)]
    if n%2 == 0:
        next_half = string[half:n]
    else:
        next_half = string[(half+1):n]
    for i in range(len(pre_half)):
        value_1 = next_half.count(pre_half[i])
        reoccur_1.append(value_1)
        value_2 = next_half.count(next_half[i])
        reoccur_2.append(value_2)
    reoccur_1.sort()
    reoccur_2.sort()
    if reoccur_1 != reoccur_2:
        print("NO")
    else:
        print("YES")