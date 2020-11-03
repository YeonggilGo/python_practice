from math import trunc


def dfs(n, idx, add, sub, mul, div):
    global maxi, mini
    if idx == N:
        if maxi < n:
            maxi = n
        if mini > n:
            mini = n
        return

    if add:
        dfs(n + numbers[idx], idx + 1, add - 1, sub, mul, div)
    if sub:
        dfs(n - numbers[idx], idx + 1, add, sub - 1, mul, div)
    if mul:
        dfs(n * numbers[idx], idx + 1, add, sub, mul - 1, div)
    if div:
        dfs(trunc(n / numbers[idx]), idx + 1, add, sub, mul, div - 1)


T = int(input())
for tc in range(T):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    maxi, mini = -100000000, 100000000
    dfs(numbers[0], 1, add, sub, mul, div)
    print('#{} {}'.format(tc + 1, maxi - mini))
