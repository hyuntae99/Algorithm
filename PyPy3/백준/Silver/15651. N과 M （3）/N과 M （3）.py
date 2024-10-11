N, M = map(int, input().split())
lst = []

def dfs():
    # print('dfs() called')
    # print('current lst:', lst)
    if len(lst) == M: # lst의 길이가 M일때
        print(*lst,end=" ") # lst의 모든 값 출력
        print()
    else:
        for i in range(1, N+1):
            # print('i =', i)
 
            # print('append', i)
            lst.append(i)
            dfs()
            pop = lst.pop() # 맨뒤의 값 삭제
            # print('popped', pop)
    # print('dfs() exited')
    
dfs()