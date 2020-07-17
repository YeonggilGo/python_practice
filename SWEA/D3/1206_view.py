for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    ans = 0

    for i in range(len(building)):
        tmp = []
        for j in range(-2, 3):
            if i+j < 0 or i+j >= len(building) or j == 0:
                continue
            else:
                tmp.append(building[i+j])

        if max(tmp) < building[i]:
            ans += building[i]-max(tmp)

    print(f'#{tc} {ans}')


