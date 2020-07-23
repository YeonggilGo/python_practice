T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    pwd = []
    for i in range(N):
        pwd.append(input())

    pos = [0, 0]

    for i in range(len(pwd)):
        if '1' in pwd[i]:
            pos[0] = i
            pos[1] = pwd[i].index('1')
            break

    dict_pwd = {
        '0001101': '0', '0011001': '1',
        '0010011': '2', '0111101': '3',
        '0100011': '4', '0110001': '5',
        '0101111': '6', '0111011': '7',
        '0110111': '8', '0001011': '9'
    }
    while pwd[pos[0]][pos[1]:pos[1] + 7] not in dict_pwd:
        pos[1] -= 1

    pwd = pwd[pos[0]][pos[1]:pos[1]+56]
    res = ''

    for i in range(8):
        res += dict_pwd[pwd[i * 7:(i + 1) * 7]]

    ans = 0
    res = list(map(int, list(res)))
    if (sum([res[i]*2 for i in range(len(res)-1) if i % 2 == 0]) + sum(res)) % 10 == 0:
        ans = sum(res)

    print(f'#{tc} {ans}')
