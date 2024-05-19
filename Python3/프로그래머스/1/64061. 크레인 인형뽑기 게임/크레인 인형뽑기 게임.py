def solution(board, moves):
    answer = 0
    height = {} # 위치에 대한 높이
    visited = [False for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if visited[j]:
                continue
            if board[i][j] != 0:
                height[j + 1] = len(board) - i
                visited[j] = True
    
    result = []
    for move in moves:
        # 인형이 없는 경우
        if height[move] == 0:
            continue
        # 인형을 바구니에 추가하고 제거
        result.append(board[len(board) - height[move]][move - 1])
        height[move] -= 1
        
        # 인형이 두개이상 쌓였을 때
        if len(result) > 1:
            # 끝에 있는 두개가 동일하면
            if result[-1] == result[-2]:
                # 인형이 터지니까 +2
                result.pop(-1)
                result.pop(-1)
                answer += 2
    
    return answer