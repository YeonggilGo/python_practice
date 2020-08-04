T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    max_ = 0
    min_ = 10000000
    num = list(map(int, input().split()))
    for i in range(N):
        max_ = num[i] if num[i] > max_ else max_
        min_ = num[i] if num[i] < min_ else min_

    print('#{} {}'.format(tc, max_ - min_))
