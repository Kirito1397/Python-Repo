# FYI --> Formula for total number of substrings n*(n+1)/2

def minion_game(string):
    n = len(list(string)) 
    word = list(string)
    the_list = set()
    for i in range(n):
        for j in range(n+1):
            the_list.update(["".join(word[i:j])])

    the_list.remove("")
    kevin_score,stuart_score = 0,0

    for i in  the_list:
            if i[0] in "AEIOU":
                kevin_score = kevin_score + sum(1 for j in range(len(string)) if string.startswith(i, j))
            else:
                stuart_score = stuart_score + sum(1 for j in range(len(string)) if string.startswith(i, j))
    if kevin_score > stuart_score:
        print ("Kevin",kevin_score)
    if kevin_score < stuart_score:
        print ("Stuart",stuart_score)
    else:
        print ("Draw")   

if __name__ == '__main__':
    s = input()
    minion_game(s)

'''The above solution works, unfortunately for only small strings for a big string it provides Memory or RunTime errordue to For Loops.'''


# ALTERNATE:
# ==========

# def minion_game(s):
#     s1=0
#     s2=0
#     vow='AEIOU'
#     for i in range(len(s)):
#         if s[i] not in vow:
#             s1=s1+(len(s)-i)  #Here we deduct the String length with the possible solution number
#         else:
#             s2=s2+(len(s)-i)   
#     if s1>s2:
#         print("Stuart",s1)
#     elif s2>s1:
#         print("Kevin",s2)
#     else:
#         print("Draw")    

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)