import copy

T = int(input())
for tc in range(1, T + 1):
    bi = list(map(int, input()))
    ti = list(map(int, input()))
    answer = None
    for j in range(len(bi)):
        t_bi = copy.deepcopy(bi)
        t_bi[j] = 0 if bi[j] else 1

        for i in range(len(ti)):
            t_ti = copy.deepcopy(ti)
            for k in [0, 1, 2]:
                if ti[i] == k:
                    continue
                t_ti[i] = k
                s_bi = sum([t_bi[-l - 1] * (2 ** l) for l in range(len(t_bi))])
                s_ti = sum([t_ti[-l - 1] * (3 ** l) for l in range(len(t_ti))])
                if s_bi == s_ti:
                    answer = s_bi
                    break
            if answer is not None:
                break
        if answer is not None:
            break
    print('#{} {}'.format(tc, answer))
