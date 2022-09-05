'''
list로 pop(0)을 하면 시간복잡도가 O(1)일거라고 생각하였으나,
맨 앞 원소 삭제는 앞으로 원소들이 당겨지기 때문에 O(n)이다.

deque.append(a) : 맨 오른쪽(뒷쪽)에 원소 추가
deque.appendleft(a): 맨 왼쪽(앞쪽)에 원소 추가
deque.pop() : 맨 오른쪽(뒷쪽) 원소 pop
deque.popleft() : 맨 왼쪽(앞쪽) 원소 pop

-> 모두 시간복잡도 O(1)
'''

'''
testcase11, 28
'''




from collections import deque
def solution2(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    value = [i for i in queue1+queue2 if i > (sum1+sum2)/2]
    if value:
        return -1

    while sum1 != sum2:
        sum1 = sum(queue1)
        sum2 = sum(queue2)

        if sum1 > sum2:
            value = queue1.pop(0)
            queue2.append(value)
            answer += 1
            continue
        elif sum1 < sum2:
            value = queue2.pop(0)
            queue1.append(value)
            answer += 1
            continue
    return answer


def solution(queue1, queue2):
    answer = 0
    nqueue1, nqueue2 = deque(queue1), deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    value = [i for i in queue1+queue2 if i > (sum1+sum2)/2]
    if value:
        return -1

    while sum1 != sum2:

        if sum1 > sum2:
            value = nqueue1.popleft()
            nqueue2.append(value)
            answer += 1
            sum1 -= value
            sum2 += value
            continue
        elif sum1 < sum2:
            value = nqueue2.popleft()
            nqueue1.append(value)
            answer += 1
            sum1 += value
            sum2 -= value
            continue
    return answer


if __name__ == '__main__':
    # queue1 = [3, 2, 7, 2]
    # queue2 = [4, 6, 5, 1]
    queue1 = [1, 1]
    queue2 = [1, 5]
    answer = solution(queue1, queue2)
    print(answer)
