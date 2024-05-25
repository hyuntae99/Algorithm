import collections
def solution(n, results):
    # 승리와 패배 관계를 저장할 그래프 초기화
    win_graph = collections.defaultdict(set)
    lose_graph = collections.defaultdict(set)
    
    # 주어진 경기 결과를 바탕으로 그래프 구축
    for winner, loser in results:
        win_graph[winner].add(loser)  # winner가 이긴 선수 목록
        lose_graph[loser].add(winner)  # loser가 패배한 선수 목록
    
    # 각 선수에 대해 승리와 패배 관계 업데이트
    for player in range(1, n + 1):
        # 현재 선수를 패배시킨 선수들에게 현재 선수가 이긴 선수들을 추가
        for winner in lose_graph[player]:
            win_graph[winner].update(win_graph[player])
        # 현재 선수에게 패배한 선수들에게 현재 선수를 패배시킨 선수들을 추가
        for loser in win_graph[player]:
            lose_graph[loser].update(lose_graph[player])
    
    # 순위를 확정지을 수 있는 선수의 수 계산
    answer = 0
    for player in range(1, n + 1):
        # 각 선수의 승리, 패배 관계 합이 n-1이면 모든 선수와의 관계를 알고 있는 것
        if len(win_graph[player]) + len(lose_graph[player]) == n - 1:
            answer += 1
    
    return answer