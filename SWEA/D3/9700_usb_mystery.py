T = int(input())
for tc in range(1, T + 1):
    p, q = map(float, input().split())
    ans = 'YES' if p * (1 - q) > (1 - p) else 'No'
    print(f'#{tc} {ans}')
