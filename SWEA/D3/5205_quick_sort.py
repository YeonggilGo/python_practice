def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        pivot = partition(low, high)
        sort(low, pivot - 1)
        sort(pivot + 1, high)

    def partition(l, r):
        pivot = arr[l]
        i, j = l, r

        while i < j:
            while arr[i] <= pivot and i < r:
                i += 1
            while arr[j] >= pivot and j > l:
                j -= 1
            if i < j :
                arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[j] = arr[j], arr[l]
        return j

    return sort(0, len(arr) - 1)

for tc in range(int(input())):
    N = int(input())
    res = list(map(int,input().split()))
    quick_sort(res)
    print('#{} {}'.format(tc + 1, res[N//2]))
