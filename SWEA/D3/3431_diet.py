for tc in range(1, int(input()) + 1):
    L, U, X = map(int, input().split())
    if X < L:
        ans = L-X
    elif X > U:
        ans = -1
    else:
        ans = 0
    print(f'#{tc} {ans}')
