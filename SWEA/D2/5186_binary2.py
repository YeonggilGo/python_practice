for tc in range(1, int(input()) + 1):
    N = float(input())
    ans = ''
    i = -1
    while N and i >= -12:
        if N >= 2 ** i:
            N -= 2 ** i
            ans += '1'
        else:
            ans += '0'
        i -= 1
    if N:
        ans = 'overflow'
    print('#{} {}'.format(tc, ans))
