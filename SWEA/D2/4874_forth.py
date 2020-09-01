T = int(input())
for tc in range(1, T + 1):
    opers = input().split()
    stack = []
    ans = 0
    for i in range(len(opers)):
        if opers[i].isdigit():
            stack.append(opers[i])
        else:
            if opers[i] == '.':
                if len(stack) == 1:
                    ans = stack.pop()
                else:
                    ans = 'error'
            else:
                if len(stack) >= 2:
                    num2 = int(stack.pop())
                    num1 = int(stack.pop())
                    if opers[i] == '+':
                        stack.append(num1 + num2)
                    elif opers[i] == '-':
                        stack.append(num1 - num2)
                    elif opers[i] == '*':
                        stack.append(num1 * num2)
                    elif opers[i] == '/':
                        stack.append(num1 // num2)
                else:
                    ans = 'error'
                    break
    print(f'#{tc} {ans}')
