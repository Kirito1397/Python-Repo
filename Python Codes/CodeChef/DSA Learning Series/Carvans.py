for _ in range(int(input())):
    ncar = int(input())
    lcar = list(map(int,input().split()))
    car_count = 0
    print("List -->",lcar,"lcar =",lcar[0])

    temp = lcar[0]
    for  i in range(ncar):
        if temp >= lcar[i]:
            car_count += 1
            temp = lcar[i]
    print(car_count)