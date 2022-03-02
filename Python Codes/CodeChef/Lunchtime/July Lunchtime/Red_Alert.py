for t in range(int(input())):
    data = (list(map(int,input().split())))
    rain_vol = (list(map(int,input().split())))
    vol = 0
    vol_list = []
    for i in range(data[0]):
        if rain_vol[i] > 0:
            vol += rain_vol[i]
        elif rain_vol[i] == 0:
            if vol < data[1]:
                vol =0
            else:
                vol -= data[1]
        if vol > data[2]:
           break
    if vol > data[2]:
        print("YES")
    else:
        print("NO")