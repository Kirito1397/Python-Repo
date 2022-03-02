# from sys            import setrecursionlimit, stdin, stderr
# from bisect         import bisect_left, bisect_right
# from collections    import defaultdict, deque, Counter
# from itertools      import combinations, permutations, product
# from functools      import lru_cache, cmp_to_key, reduce
# from heapq          import heapify, heappush, heappop, heappushpop, heapreplace
# setrecursionlimit(300005)
# LOGN  = 20
# INF   = 1 << 60
# MOD   = 10 ** 9 + 7
# input = lambda: stdin.readline().rstrip("\r\n")
# dbg   = lambda *A, **M: stderr.write("\033[91m" + \
#         M.get("sep", " ").join(map(str, A)) + M.get("end", "\n") + "\033[0m")
# ============================ START OF MY CODE ============================ #
 
# def solve():
#     A = str(input())
#     bracket_sequence = False
#     bracket_list = []
#     bracket_list[0:0] = A
#     count = 0
#     bracket_list_len = len(bracket_list)
#     while (bracket_sequence == False):
#         for i in range(1,bracket_list_len):
#             if bracket_list[:int(bracket_list_len/2)].count('(') == bracket_list[int(bracket_list_len/2):].count(')'):
#                 bracket_sequence = True
#             elif bracket_list[i-1] == ')' and bracket_list[i] == '(' :
#                 count += 1
#                 bracket_list[i-1],bracket_list[i] = bracket_list[i],bracket_list[i-1]
 
# if __name__ == "__main__":
#     solve()

# for _ in range(int(input())):
#     bags,kids = list(map(int,input().split()))
#     candies = list(map(int,input().split()))
    
#     total_candies = sum(candies)
    
#     remaining_candy = total_candies%kids
#     print(remaining_candy)



def chhotaBheem(n, a):
    a.sort()
    result = 0
    for index in range(1,n+1):
      for ele in list(a):
        if ele >= index:
          result += 1
          a.remove(ele)
          break
        a.remove(ele)
    return result

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = chhotaBheem(n, a)
    print(ans)
    

if __name__=="__main__":
    main()







# def hostelRoom(s):
#     s_list = []
#     s_list[:] = s
#     room_count = s_list.count('R')
#     wc_count = s_list.count("W")
#     room_sections = int((room_count/2))
#     if (room_count%2 == 1) or (room_sections < 2) :
#       return 0
#     elif room_sections == 2:
#       return wc_count
#     else:
#       return ((room_sections * wc_count)%(1000000007))


# def main():
#     s = input()
#     ans = hostelRoom(s)
#     print(ans)

# if __name__=="__main__":
#     main()