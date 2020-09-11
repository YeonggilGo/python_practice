def check_proper(ps):
    stack = []
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True


def algo(w):
    global answer
    # 1
    if not w:
        return

    # 2
    cnt = 0
    for i in range(len(w)):
        if w[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if not cnt:
            break
    u, v = w[:i + 1], w[i + 1:]

    # 3
    if check_proper(u):
        answer += u
        algo(v)
    # 4
    else:
        answer += '('
        algo(v)
        answer += ')'
        for p in u[1:-1]:
            answer += ')' if p == '(' else '('


answer = ''


def solution(p):
    global answer
    algo(p)
    return answer


# beeeeetter code
def solution(p):
    if p == '': return p
    r = True;
    c = 0
    for i in range(len(p)):
        if p[i] == '(':
            c -= 1
        else:
            c += 1
        if c > 0: r = False
        if c == 0:
            if r:
                return p[:i + 1] + solution(p[i + 1:])
            else:
                return '(' + solution(p[i + 1:]) + ')' + ''.join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))
