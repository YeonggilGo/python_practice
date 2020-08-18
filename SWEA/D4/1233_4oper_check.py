def cal(oper, num1, num2):
    num1, num2 = float(num1), float(num2)
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2
    else:
        return None


def solve(info):
    if info[0].isdigit():
        return info[0]
    else:
        tmp = cal(info[0], solve(tree[int(info[1]) - 1]), solve(tree[int(info[2]) - 1]))
        if tmp is None:
            return None
        else:
            return tmp


for tc in range(1, 11):
    N = int(input())
    tree = []
    for i in range(N):
        tree.append(input().split()[1:])

    res = solve(tree[0])
    if res is None:
        res = 0
    else:
        res = 1
    print(f'#{tc} {res}')
