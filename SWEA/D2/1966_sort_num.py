T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = sorted(list(map(int, input().split())))
    ans = ' '.join(list(map(str, num)))
    print(f'#{tc} {ans}')
