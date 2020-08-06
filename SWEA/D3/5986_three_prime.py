from itertools import combinations_with_replacement as combs

check = [1] * 1001
check[0], check[1] = 0, 0
prime = []
for n in range(2, 1000):
    if check[n]:
        prime.append(n)
    for i in range(n, 1000, n):
        check[i] = 0

dict_Vino = {}
for comb in combs(prime, 3):
    if sum(comb) in dict_Vino:
        dict_Vino[sum(comb)] += 1
    else:
        dict_Vino[sum(comb)] = 1

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc} {dict_Vino[int(input())]}')
