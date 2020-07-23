T = int(input())

for tc in range(1, T + 1):
    t, N = input().split()

    num_dic = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
               'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    num = input().split()
    num.sort(key=lambda x: num_dic[x])

    print(t)
    for i in range(len(num)):
        print(num[i], end=' ')
