def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        if person1[i%len(person1)] == answers[i]:
            cnt1 += 1
        if person2[i%len(person2)] == answers[i]:
            cnt2 += 1
        if person3[i%len(person3)] == answers[i]:
            cnt3 += 1
            
    max_score = max(cnt1, cnt2, cnt3)
    
    if cnt1 == max_score:
        answer.append(1)
    if cnt2 == max_score:
        answer.append(2)
    if cnt3 == max_score:
        answer.append(3)
    
    return answer