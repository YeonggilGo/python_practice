def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr

    pivot = len(arr) // 2
    low_arr = merge_sort(arr[:pivot])
    high_arr = merge_sort(arr[pivot:])
    if low_arr[-1] > high_arr[-1]:
        cnt += 1

    res = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            res.append(low_arr[l])
            l += 1
        else:
            res.append(high_arr[h])
            h += 1
    res += low_arr[l:] + high_arr[h:]
    return res


T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(numbers)
    print('#{} {} {}'.format(tc + 1, ans[N // 2], cnt))
