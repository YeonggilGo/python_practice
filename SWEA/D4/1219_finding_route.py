from _collections import deque

for _ in range(10):
    tc, N = map(int, input().split())
    q = deque([0])
    route = dict()
    tmp = list(map(int, input().split()))
    for i in range(N):
        if tmp[i * 2] in route:
            route[tmp[i * 2]].append(tmp[i * 2 + 1])
        else:
            route[tmp[i * 2]] = [tmp[i * 2 + 1]]
    ans = 0
    while q:
        pos = q.popleft()
        if pos == 99:
            ans = 1
            break
        if pos in route:
            for each in route[pos]:
                q.append(each)

    print(f'#{tc} {ans}')
