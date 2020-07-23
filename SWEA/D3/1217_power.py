def power(N, M):
    if M == 0:
        return 1
    else:
        return power(N, M - 1) * N


for _ in range(10):
    t = int(input())
    N, M = map(int, input().split())

    print(f'#{t} {power(N,M)}')
