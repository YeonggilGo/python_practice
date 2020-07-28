T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    b = N - M
    a = 2*M - N
    print(f'#{tc} {a} {b}')
