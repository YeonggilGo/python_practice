if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        ans = 0
        row = [0]*N

        dfs(0, N)
        print(f'#{tc} {ans}')


def adjacent(cnt):
    for i in range(cnt):
        if row[i] == row[cnt] or abs(row[i] - row[cnt]) == cnt - i:
            return False
    return True


def dfs(cnt, N):
    global ans
    if cnt == N:
        ans += 1
        return
    for i in range(N):
        row[cnt] = i
        if adjacent(cnt):
            dfs(cnt + 1, N)
