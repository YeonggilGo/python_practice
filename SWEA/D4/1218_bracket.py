for tc in range(1, 11):
    N = int(input())
    brackets = input()
    stack = []
    match = {'[': ']', '{': '}', '<': '>', '(': ')'}
    ans = 1
    for bracket in brackets:
        if bracket in '[{<(':
            stack.append(bracket)
        else:
            if bracket == match[stack[-1]]:
                stack.pop()
            else:
                ans = 0
                break
    print(f'#{tc} {ans}')
