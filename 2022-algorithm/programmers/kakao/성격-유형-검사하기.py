def solution(survey, choices):
    mbtis = [{"name": "R", "score": 0}, {"name": "T", "score":  0}, {"name": "C",  "score": 0}, {"name": "F",  "score": 0},
             {"name": "J", "score":  0}, {"name": "M",  "score": 0}, {"name": "A", "score":  0}, {"name": "N", "score": 0}]
    answers = [0, 3, 2, 1, 0, -1, -2, -3]

    answer = ''
    for i in range(len(survey)):
        for mbti in mbtis:
            if mbti["name"] == survey[i][0]:
                mbti["score"] += answers[choices[i]]

    for i in range(len(mbtis)):
        if i % 2 == 0:
            prev = mbtis[i]["score"]
            next = mbtis[i+1]["score"]
            if prev >= next:
                answer += mbtis[i]["name"]
            else:
                answer += mbtis[i+1]["name"]

    return answer


if __name__ == '__main__':
    survey = ["AN", "CF", "MJ", "RT", "NA"]
    choices = [5, 3, 2, 7, 5]
    answer = solution(survey, choices)
    print(answer)
