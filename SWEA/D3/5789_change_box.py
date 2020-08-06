T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    coms = []
    for _ in range(Q):
        coms.append(list(map(int, input().split())))

    boxes = [0] * N
    for i, (L, R) in enumerate(coms):
        for j in range(L - 1, R):
            boxes[j] = i + 1

    ans = ' '.join(map(str,boxes))
    print(f'#{tc} {ans}')

