# for _ in range(int(input())):
#     n,m,x = list(map(int,input().split()))
#     players_distance = list(map(int,input().split()))
#     qualified_players = []
#     disqualified_players = []
#     p_range = len(players_distance)
#     count = 0
#     for distance in range(len(players_distance)):
#         if players_distance[distance]>=m:
#             qualified_players.append(str(distance+1))
#         else:
#             disqualified_players.append(players_distance[distance])
        
#     disqualified_players.sort(reverse=True)

#     for distance in disqualified_players:
#         if len(qualified_players)<x:
#             temp = players_distance.index(distance)
#             qualified_players.append(str(temp+1))
        
#     qualified_players.sort()
#     print("Disqualified Player{}".format(disqualified_players))

#     print("Players Distance {}".format(players_distance))
    
#     print("Qualified Players {}".format(qualified_players))
#     print(len(qualified_players)," ".join((qualified_players[:])))


# SOLUTION : B 
# =============

for _ in range(int(input())):
    n,m,x = list(map(int,input().split()))
    players_distance = list(map(int,input().split()))
    qualified_players = []
    data = []

    for index,distance in enumerate(players_distance):
        data.append((index+1,distance))

    data.sort(key = lambda x:x[1],reverse=True)
    # print(data)
    for distance in data:
        if (distance[1] > m or len(qualified_players)<x):
            qualified_players.append(distance[0])

    # print(len(qualified_players)," ".join((qualified_players[:])))
    print(len(qualified_players),*sorted(qualified_players))
 
# Other USer Accepted Solution:
#=============================


a=int(input())
for i in range(a):
    n,m,x=list(map(int,input().split()))
    b=list(map(int,input().split()))
    t=b.copy()
    d=[]
    t.sort(reverse=True)
    count=0
    for j in range(n):
        if t[j]>=m or count<x:
            count+=1
            d.append(b.index(t[j])+1)
    d.sort()
    print(count,*d)