for tc in range(1, int(input()) + 1):
    N = int(input())

    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    dots = []
    for i in range(N):
        dots.append([x[i], y[i]])

    dis = []
    for i in range(N):
        for j in range(i + 1, N):
            dis.append([pow((dots[i][0] - dots[j][0]) ** 2 + (dots[i][1] - dots[j][1]) ** 2, 0.5), i, j])

    dis.sort(key=lambda x: x[0])
    env_var = float(input())

    # connect : set of connected dots
    connect = []
    ans = 0
    for li in dis:
        a = li[1]
        b = li[2]
        a_idx = -1
        b_idx = -1

        # find group which has a and b separately
        for i in range(len(connect)):
            if a in connect[i]:
                a_idx = i
            if b in connect[i]:
                b_idx = i
            if a_idx != -1 and b_idx != -1:
                break

        # append dots in each group by index
        if a_idx == -1 and b_idx == -1:
            connect.append({a, b})
        elif a_idx != -1 and b_idx == -1:
            connect[a_idx].add(b)
        elif a_idx == -1 and b_idx != -1:
            connect[b_idx].add(a)
        elif a_idx != b_idx:
            connect[a_idx] = connect[a_idx].union(connect[b_idx])
            connect.pop(b_idx)
        else:
            continue

        ans += li[0] ** 2
        # end condition
        if len(connect[0]) == N:
            break
    print(f'#{tc} {round(env_var * ans)}')
