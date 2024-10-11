ans = 0  

def solution(number):
    l = len(number)

    def dfs(n, cnt, num):
        global ans
        if cnt == 3:  # 세 개의 숫자를 선택했을 때
            if num == 0:
                ans += 1
            return
        
        if n >= l:  # 범위를 벗어난 경우
            return
        
        dfs(n + 1, cnt + 1, num + number[n])  # 선택하는 경우
        dfs(n + 1, cnt, num)  # 선택하지 않는 경우

    dfs(0, 0, 0)
    return ans


# import itertools

# def solution(number):
#     answer = 0
#     # n^3 알고리즘, 하지만 13까지이므로 허용
#     arr = list(itertools.combinations(number, 3)) 
    
#     # 각 케이스에 대해서
#     for i in arr:
#         # 합이 0이면 카운트
#         if sum(list(i)) == 0:
#             answer += 1
#     return answer