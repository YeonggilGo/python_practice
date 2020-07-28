T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    list1 = input().split()
    list2 = input().split()
    ans = len(set(list1).intersection(set(list2)))
    print(f'#{tc} {ans}')
