T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N = int(input())

    ans = [[0 for i in range(N + 2)] for j in range(N + 2)]
    for i in range(N + 2):
        for j in range(N + 2):
            if i <= 0 or j <= 0 or i >= N + 1 or j >= N + 1:
                ans[j][i] = True

    cnt = 1
    pos = [1, 1]
    i = 0

    while cnt < N ** 2:
        ans[pos[0]][pos[1]] = cnt
        ny = pos[0] + dy[i]
        nx = pos[1] + dx[i]
        if ans[ny][nx]:
            i = (i + 1) % 4
            continue
        else:
            pos[0] = ny
            pos[1] = nx
            cnt += 1
    ans[pos[0]][pos[1]] = cnt

    print(f'#{tc}')
    for i in range(1, N+1):
        for j in range(1, N + 1):
            print(ans[i][j], end=' ')
        print()
