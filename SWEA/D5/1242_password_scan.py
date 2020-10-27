import sys

sys.stdin = open('sample_input.txt', 'r')
T = int(input())
dict_pwd = {
    '0001101': '0', '0011001': '1',
    '0010011': '2', '0111101': '3',
    '0100011': '4', '0110001': '5',
    '0101111': '6', '0111011': '7',
    '0110111': '8', '0001011': '9'
}
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = 0
    sig = [input() for _ in range(N)]
    for j in range(1, N):
        i = M - 1
        while i >= 15:
            if sig[j][i] != '0' and sig[j - 1][i] == '0':
                bin_sig = bin(int(sig[j][:i + 1], 16))[2:].rstrip('0')
                is_extended = False
                ext = 1
                for e in range(2, len(bin_sig) // 56 + 2):
                    temp_sig = '0' * (e*56 - len(bin_sig))
                    

                pwd = ''
                for k in range(8):
                    pwd += dict_pwd[bin_pwd[k * 7:(k + 1) * 7]]
                pwd = list(map(int, pwd))
                print(pwd)
                if sum([pwd[k] * 3 if k % 2 == 0 else pwd[k] for k in range(8)]) % 10 == 0:
                    answer += sum(pwd)
            else:
                i -= 1
    print('#{} {}'.format(tc, answer))
