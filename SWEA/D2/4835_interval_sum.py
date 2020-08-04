T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_ = 0
    min_ = 10000 * M
    for i in range(N - M + 1):
        sum_ = sum(numbers[i:i + M])
        if sum_ > max_:
            max_ = sum_
        if sum_ < min_:
            min_ = sum_

    print('#{} {}'.format(tc, max_ - min_))
