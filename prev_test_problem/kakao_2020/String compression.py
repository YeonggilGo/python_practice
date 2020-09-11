# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = N = len(s)
    for i in range(1, N // 2 + 1):
        new_s = ''
        idx = 0
        while idx <= N - 2 * i:
            cnt = 1
            tmp = s[idx:idx + i]
            while s[idx + i: idx + 2 * i] == tmp:
                idx += i
                cnt += 1

            if cnt > 1:
                new_s += str(cnt) + tmp
                idx += i
            else:
                new_s += tmp
                idx += i
        new_s += s[idx:]
        answer = min(answer, len(new_s))
    return answer


# beeeeeetter code
def compress(text, tok_len):
    words = [text[i:i + tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text) / 2) + 1)) + [len(text)])
