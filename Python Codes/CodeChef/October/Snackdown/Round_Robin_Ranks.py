for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    match_won_normally = (2*(n-k))
    extra_match_that_can_be_won = 2*((k-1)//2)
    print(match_won_normally+extra_match_that_can_be_won)
