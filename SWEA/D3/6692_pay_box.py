import decimal
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = 0
    for _ in range(N):
        boxes = input().split()
        ans += decimal.Decimal(boxes[0]) * decimal.Decimal(boxes[1])
    print(f'#{tc} {ans}')