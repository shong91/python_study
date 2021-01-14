def solution(answers):
    answer = []
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    stu1 = stu1 * int(len(answers) / len(stu1)) + stu1[:len(answers) % len(stu1)]
    stu2 = stu2 * int(len(answers) / len(stu2)) + stu2[:len(answers) % len(stu2)]
    stu3 = stu3 * int(len(answers) / len(stu3)) + stu3[:len(answers) % len(stu3)]
    score = [0, 0, 0]

    for i in range(len(answers)):
        if stu1[i] == answers[i]:
            score[0] += 1
        if stu2[i] == answers[i]:
            score[1] += 1
        if stu3[i] == answers[i]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx + 1)

    return answer


if __name__ == '__main__':
    print(solution([1,3,2,4,2]))