def solve_case():
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    with_ids = [(x, i + 1) for i, x in enumerate(a)]
    
    answer = []
    for v, i in sorted(with_ids, reverse=True):
        if len(answer) < k or v >= m:
            answer.append(i)

    print(len(answer), *sorted(answer))

cases = int(input())
for _ in range(cases):
    solve_case()