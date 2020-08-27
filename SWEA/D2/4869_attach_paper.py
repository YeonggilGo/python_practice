def dfs(cnt, cnt_big):
    global ans
    if cnt == N:
        ans += 2 ** cnt_big
        return

    # attach 20 x 10 paper
    stack.append(1)
    dfs(cnt + 1, cnt_big)
    stack.pop()

    # attach 20 x 20 paper or attach twice 20 x 10 horizontal
    if cnt <= N - 2:
        stack.extend([1, 1])
        dfs(cnt + 2, cnt_big + 1)
        stack.pop()
        stack.pop()


if __name__ == '__main__':
    for tc in range(1, int(input()) + 1):
        N = int(input()) // 10
        ans = 0
        stack = []
        dfs(0, 0)
        print('#{} {}'.format(tc, ans))