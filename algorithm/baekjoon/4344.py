from collections import Counter
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    nums = int(input())
    for i in range(nums):
        answers = list(map(float, input().split()))
        avg = sum(answers[1:]) / answers[0]
        cnt = 0

        for j in answers[1:]:
            if j > avg:
                cnt += 1

        # round(n, m): 숫자 n을 소수점 m자리까지 표현 (단, 0은 표현하지 않음)
        # 엄격한 출력형식을 위해서는 format() 을 사용
        rate = cnt / answers[0]
        print(format(rate, '.3%'))
        # print(f'{(above/len(scores))*100:.3f}%')


        # n, *l = map(float, input().split())