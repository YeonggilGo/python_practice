import math
T = int(input())

for tc in range(1, T + 1):
    N, A, B = map(int, input().split())

    ans = 10**8

    for R in range(1, N):
        for C in range(1, N//R+1):
            weight = A * abs(R - C) + B * (N - (R * C))
            ans = ans if ans < weight else weight

    print(f'#{tc} {ans}')
