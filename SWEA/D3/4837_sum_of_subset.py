import sys

sys.stdin = open('부분집합의 합.txt', 'r')
T = int(input())
numbers = list(range(1, 13))
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1<<12):
        subset = [numbers[j] for j in range(12) if i & (1<<j)]
        if len(subset) == N and sum(subset) == K:
            ans += 1
    print('#{} {}'.format(tc,ans))
