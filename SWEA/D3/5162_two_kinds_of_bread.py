T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    ans = C//A if A<B else C//B
    print(f'#{tc} {ans}')