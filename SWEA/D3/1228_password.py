for _ in range(10):
    N = int(input())
    pwd = input().split()
    com_len = input()
    coms = input().strip().split('I')

    for i in range(len(coms)):
        coms[i] = list(map(int, coms[i].split()))

    for com in coms:
        if com:
            for i in range(com[1]):
                pwd.insert(com[0] + i, str(com[2 + i]))

    ans = ' '.join(pwd[:10])

    print(f'#{_+1} {ans}')
