T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    if N % 2:
        s1 = (N + 1) * (N // 2) + (N // 2) + 1
        s2 = (N * 2) * (N // 2) + N
        s3 = ((N+1) * 2) * (N // 2) + N + 1
    else:
        s1 = (N + 1) * (N // 2)
        s2 = (N * 2) * (N // 2)
        s3 = (N * 2 + 2) * (N // 2)

    print(f'#{tc} {s1} {s2} {s3}')
