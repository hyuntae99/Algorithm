def solution(bandage, health, attacks):
    max_hp = health
    cnt = 0
    attack_idx = 0 
    attack_time = [time[0] for time in attacks] # 공격 시작 시간
    last_attack = attack_time[-1] # 마지막 공격 시간
    
    for i in range(1, last_attack + 1):
        # 공격을 받을 때
        if i == attack_time[attack_idx]:
            damage = attacks[attack_idx][1]
            attack_idx += 1
            health -= damage
            cnt = 0
            # 게임 오버
            if health <= 0:
                return -1
        # 공격을 받지 않을 때
        else:
            health += bandage[1]
            cnt += 1
        # 대성공 보너스
        if cnt == bandage[0]:
            health += bandage[2]
            cnt = 0
        # 최대 체력을 넘을 수 없음
        if health > max_hp:
            health = max_hp
        
    return health