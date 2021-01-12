from typing import List
"""
[주식가격]
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
input: [1, 2, 3, 2, 3]	
output: [4, 3, 1, 1, 0]
"""


# 이중 for
def solution(prices:List[int]) -> List[int]:
    answer = []
    # answer = [0] * len(prices)
    # Q: answer = [0] * len(prices) 하는 이유가 뭔가요? 그냥 answer = [] 이렇게 풀어도 풀리던데..
    # A: prices값과 동일한 길이의 리스트로 초기화 하기 위해서 초기화 작업하신거 같고 , answer = []로 작업을 하게되면 인덱싱 작업시 에러가 발생합니다. (range()-1 해줘야 하는 이유)

    for i in range(len(prices)-1):
        seconds = 0
        # Q: 이것과 완전히 동일한 코드인데 range()가 아닌 enumerate()를 사용했을 때는 왜 효율성 테스트에서 시간초과가 발생하는걸까요? 정말 미스테리합니다...
        # A: enumerate()는 반복 자료형 내 원소를 하나씩 다 봐야하니까 O(n) 인 반면, range()는 O(1)인 걸로 알고 있습니다.
        for j in range(i+1, len(prices)):
            if j == len(prices)-1 or prices[i] > prices[j]:
                answer.append(seconds+1)
                break
            else:
                seconds += 1
    answer += [0]
    return answer


# stack/queue 사용하기
def solution2():
    pass

if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))

