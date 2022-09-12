'''
부르트포스
: 문자열을 하나씩, 두개씩, 세개씩,.. 쪼개는 경우를 완전탐색한다. 
https://pearlluck.tistory.com/589
'''


def solution(s):
    answer = len(s)
    if len(s) == 1:
        return 1
    # 최대 절반까지의 범위이므로 len(s) 가 아닌 절반만 돌려도 됨
    for i in range(1, (len(s)//2)+1):
        chunk_str = ''
        cnt = 1
        # 문자열 추출
        temp = s[:i]

        for j in range(i, len(s), i):
            # 이전 문자열과 같으면 cnt++
            if temp == s[j:i+j]:
                cnt += 1
            else:
                # 이전 문자열과 다른 문자가 중복하여 나왔음
                if cnt != 1:
                    chunk_str += str(cnt)+temp
                else:
                    chunk_str += temp
                # temp, cnt 값 초기화
                temp = s[j:i+j]
                cnt = 1

        # 남아있는 문자열 처리
        if cnt != 1:
            chunk_str += str(cnt) + temp
        else:
            chunk_str += temp

        answer = min(answer, len(chunk_str))
    return answer


answer = solution("abcabcabcabcdededededede")
print(answer)
