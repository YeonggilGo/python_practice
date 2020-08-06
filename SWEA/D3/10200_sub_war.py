T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    max_ = min(A, B)
    min_ = A + B - N if A + B > N else 0
    print(f'#{tc} {max_} {min_}')