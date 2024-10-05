def solution(record):
    answer = [] 
    users = {}
    historys = []
    for r in record:
        history = r.split(' ')
        if history[0] == 'Enter':
            users[history[1]] = history[2]
            historys.append('Enter ' + history[1])
        if history[0] == 'Leave':
            historys.append('Leave ' + history[1])
        if history[0] == 'Change':
            users[history[1]] = history[2]
    
    for history in historys:
        status, userid = history.split(' ')
        if status == 'Enter':
            answer.append(users[userid] + "님이 들어왔습니다.")
        else:
            answer.append(users[userid] + "님이 나갔습니다.")

    
    return answer