def solution(id_list, report, k):
    answer = []
    users = {user : '' for user in id_list} # 누가 누굴 신고했는지
    count = {user : 0 for user in id_list} # 얼만큼 신고 당했는가
    for r in report:
        a, b = r.split(' ')
        # 같은 사람을 중복 신고한 경우는 제외
        if b not in users[a].split(' '):
            users[a] += b + ' '
            count[b] += 1
    
    # 정지 당한 사람
    ban = []
    for user in id_list:
        if count[user] >= k:
            ban.append(user)

    for i in range(len(id_list)):
        cnt = 0
        # 신고한 사람들중 정지된 사람이 있으면 카운트
        for user in users[id_list[i]].split(' '):
            if user in ban:
                cnt += 1
        answer.append(cnt)

    return answer