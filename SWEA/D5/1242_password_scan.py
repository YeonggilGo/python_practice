def hex_to_bin(hex_num):
    bin_num = ''
    for l in range(M):
        t = bin(int(hex_num[l], 16))[2:]
        bin_num += '0' * (4 - len(t)) + t
    return bin_num


T = int(input())
dict_pwd = {
    '211': 0, '221': 1,
    '122': 2, '411': 3,
    '132': 4, '231': 5,
    '114': 6, '312': 7,
    '213': 8, '112': 9
}
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = 0
    pre_sig = hex_to_bin(input())
    for j in range(1, N):
        cur_sig = hex_to_bin(input())
        i = M * 4 - 1
        while i >= 56:
            if cur_sig[i] != '0' and pre_sig[i] == '0':
                pwd = [0] * 8
                for k in range(8):
                    x, y, z = 0, 0, 0
                    while cur_sig[i] == '1':
                        z += 1
                        i -= 1
                    while cur_sig[i] == '0':
                        y += 1
                        i -= 1
                    while cur_sig[i] == '1':
                        x += 1
                        i -= 1
                    while cur_sig[i] == '0':
                        i -= 1

                    if k == 0:
                        ext = min(x, y, z)

                    pwd[7 - k] = dict_pwd[''.join(map(lambda l: str(l // ext), [x, y, z]))]
                if sum([pwd[k] * 3 if k % 2 == 0 else pwd[k] for k in range(8)]) % 10 == 0:
                    answer += sum(pwd)
            else:
                i -= 1
        pre_sig = cur_sig
    print('#{} {}'.format(tc, answer))
