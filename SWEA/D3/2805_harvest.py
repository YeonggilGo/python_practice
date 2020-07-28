T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    field = []
    for i in range(N):
        field.append(list(input()))
    ans = 0
    for j in range(N):
        for i in range(N // 2 - abs(N // 2 - j) + 1):
            if i:
                ans += int(field[j][N // 2 + i]) + int(field[j][N // 2 - i])
            else:
                ans += int(field[j][N // 2])
    print(f'#{tc} {ans}')
