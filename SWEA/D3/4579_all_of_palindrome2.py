def is_palin(s):
    for i in range(len(s) // 2):
        if s[i] == '*' or s[-i - 1] == '*':
            return True
        if s[i] != s[-i - 1]:
            return False
    return True

T = int(input())
for tc in range(1, T + 1):
    s = input()
    is_palin(s)
    ans = 'Exist' if is_palin(s) else 'Not exist'
    print(f'#{tc} {ans}')
