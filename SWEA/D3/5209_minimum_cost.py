def sol(idx, total_cost):
    global ans
    # backtracking
    if total_cost > ans:
        return

    # end condition
    if idx == N:
        ans = total_cost
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            sol(idx+1, total_cost + cost[idx][i])
            visited[i] = 0


for tc in range(int(input())):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    ans = N * 99
    visited = [0] * N
    sol(0, 0)
    print('#{} {}'.format(tc+1, ans))