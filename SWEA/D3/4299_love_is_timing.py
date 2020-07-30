T = int(input())

for tc in range(1, T + 1):
    D, H, M = map(int, input().split())
    H += (D - 11) * 24
    M += (H - 11) * 60 - 11
    if M < 0:
        M = -1
    print(f'#{tc} {M}')
