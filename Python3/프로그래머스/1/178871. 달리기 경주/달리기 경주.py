def solution(players, callings):
    # 초기 순위
    players_ranking = {player: int(rank) for rank, player in enumerate(players)}
    
    for call in callings:
        current_rank = players_ranking[call] # 호출된 선수의 현재 순위
        players_ranking[call] -= 1 # 호출된 선수의 순위 감소
        players_ranking[players[current_rank - 1]] += 1 # 앞의 선수 순위 증가
        
        # 선수들의 순위 바꿔주기
        players[current_rank] = players[current_rank - 1] # 뒷 순위에 앞 선수 저장
        players[current_rank - 1] = call # 앞 순위에 호출된 선수 저장

    return players