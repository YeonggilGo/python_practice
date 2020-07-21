T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())

    a_num = list(map(int, input().split()))
    b_num = list(map(int, input().split()))
    ans = 0

    if a < b:
        a, b = b, a
        a_num, b_num = b_num, a_num

    for i in range(a-b+1):
        tmp = 0
        for j in range(b):
            tmp += a_num[i + j] * b_num[j]

        ans = max(ans, tmp)

    print(f'#{tc} {ans}')
