T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    stop = [False] * (N + 1)

    for i in range(len(charge)):
        stop[charge[i]] = True

    cnt, now = 0, 0

    while now < N - K:
        can_go = False
        for i in range(now + K, now, -1):
            if stop[i]:
                can_go = True
                now = i
                cnt += 1
                break

        if not can_go:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
