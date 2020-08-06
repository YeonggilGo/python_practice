T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    dp = numbers[:]
    for i in range(1,N):
        dp[i] = max(dp[i-1] + numbers[i], numbers[i])
    print(f'#{tc} {max(dp)}')
