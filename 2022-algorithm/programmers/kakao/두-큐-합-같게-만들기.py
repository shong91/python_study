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


'''
반복문 탈출 조건을 찾는 것은 쉽지 않았다. 결국 내가 제출한 해법이 최적의 조건인지 확인은 하지 못했다. 
내가 생각한 방법은 단순했다. queue1과 queue2의 모든 원소를 바꾸면 queue1 길이의 2배만큼 횟수가 필요하고 다시 모든 원소를 바꿔 원래의 모습으로 만들면 queue1 길이의 2배만큼 필요해 총 len(queue1) * 4 만큼 횟수가 필요하다.

원래의 모습으로 돌아왔다면 동일한 패턴으로 반복될 수 있기 때문에 최대 횟수라고 판단해서 반복문을 탈출하는 조건으로 선택했다.
(정답을 제출하며 테스트해본 결과 len(queue1) * 3으로 해도 통과는 된다.)
https://a-littlecoding.tistory.com/123
'''




from collections import deque
def solution_다른사람의_풀이(queue1, queue2):
    qu_1 = deque(queue1)
    qu_2 = deque(queue2)
    sum_1 = sum(qu_1)
    sum_2 = sum(qu_2)

    for i in range(len(queue1) * 3):
        if sum_1 == sum_2:
            return i
        if sum_1 > sum_2:
            num = qu_1.popleft()
            qu_2.append(num)
            sum_1 -= num
            sum_2 += num
        else:
            num = qu_2.popleft()
            qu_1.append(num)
            sum_2 -= num
            sum_1 += num
    return -1


def solution(queue1, queue2):
    answer = 0
    nqueue1, nqueue2 = deque(queue1), deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # value = [i for i in queue1+queue2 if i > (sum1+sum2)/2]
    # if value:
    #     return -1

    # if (sum1+sum2) % 2 != 0:
    #     return -1

    while sum1 != sum2:
        if sum1 > sum2:
            value = nqueue1.popleft()
            nqueue2.append(value)
            answer += 1
            sum1 -= value
            sum2 += value
            # continue
        elif sum1 < sum2:
            value = nqueue2.popleft()
            nqueue1.append(value)
            answer += 1
            sum1 += value
            sum2 -= value
            # continue
        if value > (sum1+sum2)/2:
            return -1
    return answer


if __name__ == '__main__':
    # queue1 = [3, 2, 7, 2]
    # queue2 = [4, 6, 5, 1]
    queue1 = [1, 1]
    queue2 = [1, 2]
    answer = solution(queue1, queue2)
    print(answer)
