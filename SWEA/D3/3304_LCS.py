# Longest Common Sequence

T = int(input())

for tc in range(1, T + 1):
    s1, s2 = input().split()
    dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

    for i in range(len(s2) + 1):
        for j in range(len(s1) + 1):
            if i == 0 or j == 0:
                continue

            if s2[i-1] == s1[j-1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])

    print(f'#{tc} {dp[-1][-1]}')
