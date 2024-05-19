from collections import Counter
def solution(board, h, w):
    
    color = board[h][w]
    height = len(board) # 높이
    width = len(board[0]) # 넓이

    count = 0
    # 왼쪽 확인
    if w != 0:
        if board[h][w - 1] == color: 
            count += 1
    # 오른쪽 확인
    if w + 1 < width:
        if board[h][w + 1] == color: 
            count += 1
    # 위쪽 확인
    if h != 0:
        if board[h - 1][w] == color: 
            count += 1
    # 아래쪽 확인
    if h + 1 < height:
        if board[h + 1][w] == color: 
            count += 1

    return count