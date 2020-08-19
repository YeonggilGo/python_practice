def find_last_node(idx):
    if idx >= N:
        last_node.add((idx - 1) // 2)
        return
    else:
        find_last_node(idx * 2 + 1)
        find_last_node(idx * 2 + 2)


for tc in range(1, 11):
    N = int(input())
    tree = []
    for i in range(N):
        tree.append(input().split())

    last_node = set()
    find_last_node(0)
    res = 1
    for i in range(N):
        if i in last_node:
            print('마지막', i, tree[i][1])
            if not tree[i][1].isdigit():
                res = 0
                break
        else:
            print(i, tree[i][1])
            if tree[i][1].isdigit():
                res = 0
                break
    print(f'#{tc} {res}')
