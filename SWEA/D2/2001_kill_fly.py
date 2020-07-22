T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    fly = []
    for i in range(N):
        fly.append(list(map(int, input().split())))

    ans = 0

    for i in range(N - M+1):
        for j in range(N - M+1):
            tmp = 0
            for k in range(M):
                tmp += sum(fly[j + k][i: i + M])

            ans = tmp if tmp > ans else ans

    print(f'#{tc} {ans}')
