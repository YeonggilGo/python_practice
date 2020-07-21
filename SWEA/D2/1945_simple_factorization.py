T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ans = [0] * 5
    facto = [2, 3, 5, 7, 11]

    for i in range(len(facto)):
        while N % facto[i] == 0:
            ans[i] += 1
            N //= facto[i]

    ans = ' '.join(list(map(str, ans)))
    print(f'#{tc} {ans}')
