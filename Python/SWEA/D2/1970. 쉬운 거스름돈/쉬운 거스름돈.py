def solve(cost):
    n = 8
    coins = [50000,10000,5000,1000,500,100,50,10]
    lst = [0] * n

    for i in range(n):
        # print(lst, cost, i)
        if cost == 0:
            break
        if cost // coins[i] > 0:
            lst[i] = cost // coins[i]
            cost %= coins[i]
    return lst

T = int(input())
for test_case in range(1,T+1):
    cost = int(input())
    ans = solve(cost)
    print(f'#{test_case}')
    print(*ans)