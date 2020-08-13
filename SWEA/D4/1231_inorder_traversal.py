# class node만들고 그러는게 깔끔하긴 한데 너무 어렵고
# 파이썬 특성상 배열로 이진 트리를 만들면 순회하기 진짜ㅏㅏㅏㅏㅏ편하다.

def in_order_traversal(idx):
    if idx >= N:
        pass
    else:
        in_order_traversal(idx * 2 + 1)
        res.append(idx)
        in_order_traversal(idx * 2 + 2)


for tc in range(1, 11):
    N = int(input())
    s = ''
    for i in range(N):
        s += input().split()[1]
    res = []
    in_order_traversal(0)
    ans = ''
    for i in range(N):
        ans += s[res[i]]
    print(f'#{tc} {ans}')