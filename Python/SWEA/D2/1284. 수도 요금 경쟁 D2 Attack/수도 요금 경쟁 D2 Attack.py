def solveA():
    return W * P

def solveB():
    if W < R:
        return Q
    else:
        return Q + (W-R)*S


T = int(input())
for test_case in range(1,T+1):
    # A사 L당 P, B사 R이하 Q / L당 S, 총 수도량 W
    P,Q,R,S,W = map(int,input().split())

    ans = min(solveA(),solveB())
    print(f'#{test_case} {ans}')
