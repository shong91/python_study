import collections
from typing import List
import re


def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # 전처리 (데이터 클렌징)
    # banned 이 아닌 문자에 대하여, re.sub(): 단어문자(\w) 가 아닌(^) 모든 문자를 공백(' ') 으로 치환한다
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]