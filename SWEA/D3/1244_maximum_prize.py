def dfs(num, cnt):
    global ans
    if cnt == n:
        num = int(''.join(num))
        if num > ans:
            ans = num
        return

    cnt += 1
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            t = ''.join(num)
            if t in visited:
                if visited[t][cnt - 1]:
                    num[i], num[j] = num[j], num[i]
                    continue
            else:
                visited[t] = [0 for _ in range(n)]
            visited[t][cnt - 1] = 1
            dfs(num, cnt)
            num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(1, T + 1):
    numbers, n = input().split()
    ans = 0
    n = int(n)
    visited = {}
    dfs(list(numbers), 0)
    print(f'#{tc} {ans}')
