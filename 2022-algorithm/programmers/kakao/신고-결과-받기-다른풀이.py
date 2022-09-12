'''
상하관계가 없는 노드 처리의 인사이트를 차용 

reports= {id:cnt} 의 딕셔너리를 생성하여, 
reports[id] +=1 으로 신고당한 횟수를 카운트 한다. 
reports[id] >= k 인 경우 answer array에 값을 더하여 리턴한다.
'''


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}
    print(reports)
    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
reports = ["muzi frodo", "apeach frodo",
           "frodo neo", "muzi neo", "apeach muzi"]
k = 2
answer = solution(id_list, reports, k)
print(answer)
