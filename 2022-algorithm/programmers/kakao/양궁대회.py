'''
https://velog.io/@hygge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-BFS
'''
from collections import deque


def bfs(n, info):
    res = []
    # [(focus, arrow)]
    queue = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    max_gap = 0

    while queue:
        focus, arrow = queue.popleft()
        # 화살을 다 쏜 경우
        if sum(arrow) == n:
            apeach, ryan = 0, 0
            for i in range(11):
                # 점수 따기
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10-i
                    else:
                        ryan += 10 - i

            # 점수 비교
            if apeach < ryan:
                gap = ryan - apeach
                if max_gap > gap:
                    continue
                if max_gap < gap:
                    # 최대 점수차 갱신
                    max_gap = gap
                    res.clear()
                # 최대 점수차를 내는 화살 상황 저장
                res.append(arrow)
        # 주어진 화살보다 더 쏜 경우
        elif sum(arrow) > n:
            continue
        # 화살을 덜 쏜 경우 (마지막 과녁에 왔으면 남은 화살을 모두 사용한다)
        elif focus == 10:
            temp = arrow.copy()
            temp[focus] = n-sum(temp)
            queue.append((-1, temp))  # focus 는 의미없는 값으로 대체한다.
        # 화살 쏘기
        # 어피치를 이기려면 target 과녁에 어피치보다 1개 더 많이 쏘아 점수를 얻거나,
        # target 과녁은 버리고 다른 과녁에서 이겨서 점수를 쌓아야 한다.
        else:
            temp = arrow.copy()
            temp[focus] = info[focus]+1
            queue.append((focus+1, temp))  # 어피치보다 1발 많이 쏘기
            temp2 = arrow.copy()
            temp2[focus] = 0
            queue.append((focus+1, temp2))  # 0발 쏘기
    return res


def solution(n, info):
    winList = bfs(n, info)

    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]


if __name__ == '__main__':
    n = 5
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    answer = solution(n, info)
    print(answer)
