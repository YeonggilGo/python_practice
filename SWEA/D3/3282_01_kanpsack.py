# combination쓰면 시간 초과 걸린다.

# from itertools import combinations as comb
# T = int(input())

# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     stuff = []
#     for _ in range(N):
#         stuff.append(list(map(int, input().split())))
#     stuff.sort(key=lambda x: x[0])

#     ans = 0
#     for i in range(1, len(stuff)):
#         if sum([v[0] for v in stuff[:i]]) > K:
#             break

#         for com in comb(stuff, i):
#             if sum([v[0] for v in com]) > K:
#                 continue
#             if sum([v[1] for v in com]) > ans:
#                 ans = sum([v[1] for v in com])

#     print(f'#{tc} {ans}')


# dfs도 시간초과다 젠장

# def dfs(weight, value, N, K):
#     if dp[weight-1] <= value:
#         dp[weight-1] = value
#     else:
#         return
#     for i in range(N):
#         if visited[i]:
#             continue
#         if weight + stuff[i][0] <= K:
#             visited[i] = 1
#             dfs(weight + stuff[i][0], value + stuff[i][1], N, K)
#             visited[i] = 0


# T = int(input())

# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     stuff = []
#     for _ in range(N):
#         stuff.append(list(map(int, input().split())))
#     dp = [0] * K
#     visited = [0] * N

#     dfs(0, 0, N, K)
#     print(f'#{tc} {max(dp)}')


# 예상대로 당연히 재귀도 안된다.

# def knapsack(capacity, n):
#     if capacity == 0 or n == 0:
#         return 0
#     if size[n - 1] > capacity:
#         return knapsack(capacity, n - 1)
#     else:
#         return max(value[n-1] + knapsack(capacity-size[n-1], n-1), knapsack(capacity, n-1))


# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     info = []
#     for i in range(N):
#         info.append(list(map(int, input().split())))

#     size = []
#     value = []
#     for i in range(N):
#         size.append(info[i][0])
#         value.append(info[i][1])
#     print(f'#{tc} {knapsack(K,N)}')


# dp(dynamic programing)의 기본문제다


# N : stuff개수, K : 부피 한도, volume, value: 각 stuff의 부피, 가치
def knapsack(N, K):
    # dp : dp를 저장할 공간
    dp = [[0 for i in range(K + 1)] for j in range(N + 1)]

    # j : j번 째 stuff를 넣어 본다
    for j in range(N + 1):
        # i : 무게를 i까지 늘어 났을 때 최대 value
        for i in range(K + 1):

            # 첫번째줄, 무게 0 인 부분은 모두 0
            if j == 0 or i == 0:
                dp[j][i] = 0
            elif volume[j] <= i:
                dp[j][i] = max(dp[j - 1][i], value[j] +
                               dp[j - 1][i - volume[j]])
            else:
                dp[j][i] = dp[j - 1][i]
    return dp[-1][-1]


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    info = []
    for i in range(N):
        info.append(list(map(int, input().split())))
    info.sort(key=lambda x: x[0])

    volume = [0]
    value = [0]
    for i in range(N):
        volume.append(info[i][0])
        value.append(info[i][1])

    print(f'#{tc} {knapsack(N, K)}')
