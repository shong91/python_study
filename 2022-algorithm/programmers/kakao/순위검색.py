from itertools import combinations
from bisect import bisect_left

'''
이분탐색 사용
'''


def solution2(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        # key들로 만들 수 있는 모든 조합 생성
        # { 'javabackendjuniorpizza' : [150...] , 'java' : [100...] , ... }
        for j in range(5):
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(myval)]

    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]
            print(qu_key, scores, qu_val)
            if scores:  # score리스트에 값이 존재하면
                # 정렬된 a에 x를 삽입할 위치를 리턴해준다.  x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환한다.
                enter = bisect_left(scores, int(qu_val))
                print(enter)

                answer.append(len(scores) - enter)
        else:
            answer.append(0)
    return answer


'''
정확성 o
효율성 x (시간초과)
'''


def solution(info, query):
    answer = []

    for q in query:
        new_query = q.replace(' and', '').split()
        answer_cnt = 0
        for i in info:
            cnt = 0
            new_info = i.split()
            for index, value in enumerate(new_info):
                if index == 4 and int(new_query[index]) <= int(value):
                    if cnt == 4:
                        answer_cnt += 1
                        break
                if new_query[index] != '-' and new_query[index] != value:
                    break
                if new_query[index] == '-' or new_query[index] == value:
                    cnt += 1

        answer.append(answer_cnt)
    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

answer = solution2(info, query)
print(answer)
