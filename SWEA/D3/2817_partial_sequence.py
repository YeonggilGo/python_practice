from itertools import combinations as comb

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    ans = 0
    for i in range(len(numbers)):
        for com in comb(numbers, i):
            if sum(com) == K:
                ans += 1

    print(f'#{tc} {ans}')
