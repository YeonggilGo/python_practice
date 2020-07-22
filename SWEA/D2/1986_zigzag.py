T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    ans = 0
    for i in range(1, N + 1):
        if i % 2:
            ans += i
        else:
            ans -= i

    print(f'#{tc} {ans}')
