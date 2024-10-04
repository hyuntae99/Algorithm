def solution(lottos, win_nums):
    # 당첨 내용과 순위
    result = {
        6 : 1,
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        1 : 6,
        0 : 6
    }
    
    correct = 0
    for num in win_nums:
        if num in lottos:
            correct += 1
    
    answer = [result[correct + lottos.count(0)], result[correct]]
    
    return answer