T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    routes = []
    for _ in range(N):
        routes.append(list(map(int, input().split())))

    P = int(input())
    c = []
    for _ in range(P):
        c.append(int(input()))

    bus_stop = [0] * 5001

    for route in routes:
        for i in range(route[0], route[1] + 1):
            bus_stop[i] += 1
    res = [bus_stop[i] for i in c]
    print(f'#{tc}', *res)