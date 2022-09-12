from collections import defaultdict, Counter


def solution(id_list, reports, k):
    answer = []
    # 중복 신고 제거
    reports = list(set(reports))
    # user 별 신고한 아이디 저장
    users = defaultdict(set)
    # user 별 신고당한 횟수 저장
    cnt = defaultdict(int)

    # 아이디 별 신고 횟수 계산
    for report in reports:
        reporter, reportee = report.split()
        users[reporter].add(reportee)
        cnt[reportee] += 1

    # 메일 발송
    for id in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for user in users[id]:
            if cnt[user] >= k:
                result += 1
        answer.append(result)
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
reports = ["muzi frodo", "apeach frodo",
           "frodo neo", "muzi neo", "apeach muzi"]
k = 2
answer = solution(id_list, reports, k)
print(answer)
