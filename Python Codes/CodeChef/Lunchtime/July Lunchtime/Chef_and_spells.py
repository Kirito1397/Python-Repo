for i in range(int(input())):
    points = (list(map(int,input().split())))
    points.sort(reverse=True)
    # print(points)
    max_points= points[0]+points[1]
    print(max_points)
