from collections import defaultdict

def solve():
    percents = [0.35, 0.45, 0.20]
    students = defaultdict(float)
    for i in range(N):
        s = 0
        for j in range(3):
            s += (scores[i][j]*percents[j])
        students[i+1] = s/3

    return rank(students)

def rank(students):
    s = defaultdict(str)
    ranks = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    cnt = int(N/10)
    idx = 0
    for i, student in enumerate(sorted(students.items(), key=lambda x: x[1], reverse=True)):
        s[student[0]] = ranks[idx]
        if (i+1) % cnt == 0:
            idx += 1
        # print(s)
    return s[K]

T = int(input())
for test_case in range(1,T+1):
    N,K = map(int,input().split())
    scores = []
    for _ in range(N):
        m,l,a = map(int,input().split()) # 중간 35 / 기말 45 / 과제 20
        scores.append((m,l,a))
    ans = solve()
    print(f'#{test_case} {ans}')

