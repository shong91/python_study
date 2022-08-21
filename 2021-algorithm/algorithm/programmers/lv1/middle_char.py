"""
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
"""

# 홀짝 구분하여 슬라이싱 (삼항연산자)
def get_middle_char(word:str) -> str:
    answer = word[(len(word)//2 -1):len(word)//2 +1] if (len(word) % 2 == 0) else word[len(word)//2]
    return answer


# 홀짝 구분을 안하고 슬라이싱도 가능하다.
def get_middle_char(str):
    return str[(len(str)-1)//2:len(str)//2+1]


if __name__ == '__main__':
    print(get_middle_char('qwerty'))