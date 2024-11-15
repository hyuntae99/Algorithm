from collections import deque

def solve(q):
    idx = 0
    while q:
        c = q.popleft()

        if c-(idx+1) <= 0:
            q.append(0)
            break

        q.append(c-(idx+1))
        idx = (idx+1) % 5

    return q

T = 10
for _ in range(T):
    test_case = int(input())
    arr = list(map(int, input().split()))
    q = deque(arr)

    ans = solve(q)
    print(f'#{test_case}', end = ' ')
    print(*ans)