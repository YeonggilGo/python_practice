from itertools import combinations as combs

T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    sum_ = []
    for comb in combs(numbers,3):
        sum_.append(sum(comb))
    sum_ = list(set(sum_))
    sum_.sort(reverse=True)
    print(f'#{tc} {sum_[4]}')
