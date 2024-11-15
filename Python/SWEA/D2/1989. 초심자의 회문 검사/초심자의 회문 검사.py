# 회문 체크
def palindrome(lst):
    s,e = 0,len(lst)-1

    while s < e:
        if lst[s] != lst[e]:
            return 0
        s += 1
        e -= 1

    return 1

T = int(input())
for test_case in range(1,T+1):
    word = str(input().strip())
    ans = palindrome(word)
    print(f'#{test_case} {ans}')