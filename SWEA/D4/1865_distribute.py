def dfs(cnt, pro):
    global ans
    if pro < ans:
        return

    if cnt == N:
        ans = pro
        return

    for i in range(N):
        if not visited[i] and P[cnt][i]:
            visited[i] = 1
            dfs(cnt + 1, pro * P[cnt][i] / 100)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = {}
    for i in range(N):
        P[i] = list(map(int, input().split()))

    visited = [0 for _ in range(N)]
    ans = 0
    dfs(0, 1)
    ans = round(ans * 100, 6)
    print(f'#{tc} {ans:6f}')
