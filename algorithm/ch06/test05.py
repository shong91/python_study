import collections
from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # 존재하지 않는 키일 경우 keyerror가 나는 것을 방지하기 위해 defaultdict() 로 선언한다.
    anagrams = collections.defaultdict(list)
    for word in strs:
        # 정렬한 값을 키로 하여 딕셔너리에 추가한다. 정렬된 데이터를 key 로 사용하기 위해, 리스트로 리턴된 값을 문자열로 join() 해준다.
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()