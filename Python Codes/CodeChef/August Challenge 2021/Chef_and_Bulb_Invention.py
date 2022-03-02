# # cook your dish here
# for _ in range(int(input())):
#     values = list(map(int,input().split()))
#     N = values[0]
#     p = values[1]
#     k = values[2]
#     mod_list = []
#     for j in range(k):
#         for i in range(N):
#             if i%k == j:
#                 mod_list.append((i,i%k))
#     for x in range(len(mod_list)):
#         if mod_list[x][0] == p:
#             print(x+1)
#     print(mod_list)






# Second Better Solution:

# ========================



# cook your dish here
# for _ in range(int(input())):
#     values = list(map(int,input().split()))
#     n = values[0]
#     p = values[1]
#     k = values[2]
#     num,count = 0,0
    
#     for i in range(n):
#         if i%k == (p%k):
#             count += 1
#             if i == p:
#                 print (((p%k)*round(n/k))+count)
#                 break


# Third Solution:
# ===============

for _ in range(int(input())):
    values = list(map(int,input().split()))
    n = values[0]
    p = values[1]
    k = values[2]
    day_num = 0
    gas = p%k
    while True:
        day_num += 1
        # print ("gas==>",gas)
        if gas == p:
            print(((p%k)*round(n/k))+day_num)
            break
        else:
            gas += k
            
# k = odd = wrong
# K = even = right