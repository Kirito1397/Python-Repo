class Solution:
    def palindrome(N) -> int:
        rev = 0
        temp = N
        while(temp > 0):        #The value of temp (eg. 121 should be greater than 0)
            r = temp%10         # This returns the last digit of a number (i.e '1' in case of 121)
            rev = rev*10 + r    # Now we store the last number in a rev variable and add it with itself 
            temp = temp//10     # This provides the remaining digits except the last number (i.e. '12')
        return (N == rev),rev   # Compare reversed number with original number

for _ in range(int(input())):
    N = int(input())
    res = Solution.palindrome(N)
    print(res)