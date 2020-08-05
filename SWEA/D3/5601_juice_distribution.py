T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = ['1/{}'.format(N)] * N
    ans = ' '.join(ans)
    print('#{} {}'.format(tc, ans))
