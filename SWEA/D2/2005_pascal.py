T = int(input())


def pascal(n):
    if n == 1:
        return [1]
    else:
        res = []
        for i in range(n):
            if i == 0 or i == n - 1:
                res.append(1)
            else:
                res.append(pascal(n - 1)[i - 1] + pascal(n - 1)[i])
        return res


for tc in range(1, T + 1):
    N = int(input())

    print(f'#{tc}')
    for i in range(1, N + 1):
        print(' '.join(list(map(str, pascal(i)))))
