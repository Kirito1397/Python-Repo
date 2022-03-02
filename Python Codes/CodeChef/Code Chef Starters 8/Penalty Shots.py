for _ in range(int(input())):
    shots = list(map(int,input().split()))
    print(shots)
    odd_sum,even_sum = 0,0
    for i in range(len(shots)):
        if (i%2 == 0):  # Will be odd as range starts from "0" in list and in sample testcase it start from "1"
            odd_sum = odd_sum + shots[i]
        else:
            even_sum = even_sum + shots[i]
    if odd_sum>even_sum:
        print(1)
    elif odd_sum<even_sum:
        print(2)
    elif odd_sum == even_sum:
        print(0)