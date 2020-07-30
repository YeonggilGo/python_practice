for tc in range(1, int(input()) + 1):
    N = int(input())
    card = input().split()

    left = card[:N // 2 + N % 2]
    right = card[N // 2 + N % 2:]

    ans = ''

    for i in range(len(right)):
        ans += f'{left[i]} {right[i]} '
    if N % 2:
        ans += left[-1]

    print(f'#{tc} {ans}')
