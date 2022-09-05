

from collections import defaultdict


def solution2(survey, choices):
    answer = ''
    a = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i, j in zip(survey, choices):
        if j < 4:
            a[i[0]] += 4-j
        else:
            a[i[1]] += j-4
    t = [i for i in a.keys()]
    for i in range(0, 8, 2):
        if a[t[i]] >= a[t[i+1]]:
            answer += t[i]
        else:
            answer += t[i+1]
    return answer


def solution(survey, choices):
    indicator = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    answer = ''
    personality = defaultdict(int)
    for s, c in zip(survey, choices):
        print(s, c)
        if c < 4:
            personality[s[0]] += (4 - c)
        elif c > 4:
            personality[s[1]] += (c - 4)

    print(personality)
    for i in indicator:
        print(personality[i[0]], personality[i[1]])
        if personality[i[0]] >= personality[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer


if __name__ == '__main__':
    survey = ["AN", "CF", "MJ", "RT", "NA"]
    choices = [5, 3, 2, 7, 5]
    answer = solution(survey, choices)
    print(answer)
