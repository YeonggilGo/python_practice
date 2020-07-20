T = int(input())

for T in range(1, T + 1):
    min_ = 100000000
    max_ = 0
    num = list(map(int, input().split()))

    for i in range(N):
        min_ = num[i] if num[i] < min_ else min_
        max_ = num[i] if num[i] > max_ else max_

    print(f'#{tc} {max_-min_}')
