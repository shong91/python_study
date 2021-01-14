import collections


def solution(participant, completion):
    answers = collections.Counter(participant) - collections.Counter(completion)
    answer = list(answers)[0]
    return answer


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["leo", "kiki"]))

