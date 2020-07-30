# Longest Increasing Subsequence
# Dp를 활용한다.
# Dp를 바로 전 인덱스만 참조하는게 아니라
# 앞의 전체 인덱스를 참조해야 제대로 된 결과가 나온다. O(n)
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if dp[j] >= dp[i] and num[j] < num[i]:
                dp[i] = dp[j] + 1

    print(f'#{tc} {max(dp)}')
