def dfs(pos, left_bat, cnt):
    global ans
    # backtracking
    if cnt > ans:
        return

    # end condition
    if pos == N - 1:
        ans = cnt
        return

    # don't change at this stop
    if left_bat > 1:
        dfs(pos + 1, left_bat - 1, cnt)

    # change at this stop
    dfs(pos + 1, stops[pos], cnt + 1)


for tc in range(int(input())):
    temp = list(map(int, input().split()))
    N = temp[0]
    stops = temp[1:]
    ans = N - 1
    dfs(1, stops[0], 0)
    print('#{} {}'.format(tc + 1, ans))
