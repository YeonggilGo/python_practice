def bi_search(arr, key):
    global ans
    s, e = 0, len(arr)
    pre = ''
    while s <= e:
        m = (s + e) // 2
        if arr[m] == key:
            ans += 1
            return
        elif arr[m] > key:
            if pre == 'l':
                return
            else:
                e = m - 1
                pre = 'l'
        else:
            if pre == 'r':
                return
            else:
                s = m + 1
                pre = 'r'

for tc in range(int(input())):
    N, M = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    keys = list(map(int, input().split()))
    ans = 0
    for tar in keys:
        bi_search(nums, tar)
    print('#{} {}'.format(tc + 1, ans))
