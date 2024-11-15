N = int(input())

for num in range(1,N+1):
    s = str(num)
    ans = ''
    for a in s:
        if a in ('3', '6', '9'):
            ans += '-'

    if len(ans) == 0:
        print(s, end=' ')
    else:
        print(ans, end=' ')
print()