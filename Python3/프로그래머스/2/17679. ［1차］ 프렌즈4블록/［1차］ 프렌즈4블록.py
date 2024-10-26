def delete(m, n, board):
    dels = set()  # 삭제할 블록의 좌표 저장
    # 2x2 크기의 블록이 모두 같은지 확인
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != '0' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                # 2x2 범위에 해당하는 블록의 좌표를 모두 삭제 대상에 추가
                dels.add((i, j))
                dels.add((i+1, j))
                dels.add((i, j+1))
                dels.add((i+1, j+1))

    # 블록 삭제 진행 (모든 블록을 찾은 후 한꺼번에 삭제 -> 겹칠 수도 있으니까)
    for i, j in dels:
        board[i][j] = '0'  # 블록을 '0'으로 설정하여 삭제

    return len(dels)  # 삭제된 블록의 개수를 반환

def down(m, n, board):
    # 각 열에 대해 블록을 위에서 아래로 떨어뜨리는 과정
    for j in range(n):
        # 각 열에 대해 '0'이 아닌 블록을 아래로 떨어뜨리기
        stack = []
        for i in range(m):
            if board[i][j] != '0':
                stack.append(board[i][j])  # 빈칸이 아닌 블록을 스택에 저장
        for i in range(m-1, -1, -1):  # 아래에서부터 위로 탐색하면서 블록 채우기
            if stack:
                board[i][j] = stack.pop()  # 스택에서 블록을 꺼내서 채움
            else:
                board[i][j] = '0'  # 스택이 비어 있으면 나머지는 '0'으로 채움

def solution(m, n, board):
    # 문자열을 리스트로 변환하여 각 행을 리스트로 다룸
    board = [list(row) for row in board]  
    total_deleted = 0  # 삭제된 총 블록 수

    while True:
        # 삭제된 블록 수 계산
        deleted = delete(m, n, board)
        if deleted == 0:
            return total_deleted  # 더 이상 삭제할 블록이 없으면 종료
        total_deleted += deleted  # 삭제된 블록 수 누적
        down(m, n, board)  # 블록을 아래로 내림