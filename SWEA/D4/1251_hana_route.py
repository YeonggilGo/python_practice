for tc in range(1, int(input()) + 1):
    N = int(input())
    dots = []
    for i in range(N):
        dots.append(list(map(int, input().split())))

    dis = []
    for i in range(N):
        for j in range(i, N):
            dis.append(pow((dots[i][0] - dots[j][0]) ** 2 + (dots[i][1] - dots[j][1]) ** 2, 0.5))

    dis.sort()
