import itertools

# 순열: 순서 있음
arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

# 조합: 순서 무관 ((A,B) == (B,A))
arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))
