from collections import deque


def dfs(cnt, pos):
    global ans
    if cnt > ans:
        ans = cnt

    visited.append(pos)
    for path in info[pos]:
        if path not in visited:
            dfs(cnt + 1, path)
    visited.pop()


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    info = {i: [] for i in range(1, N + 1)}
    for i in range(M):
        tmp = list(map(int, input().split()))
        info[tmp[0]].append(tmp[1])
        info[tmp[1]].append(tmp[0])

    ans = 1
    visited = []
    for start in info:
        dfs(1, start)

    print(f'#{tc} {ans}')
