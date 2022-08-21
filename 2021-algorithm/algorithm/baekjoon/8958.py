if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        case = str(input())
        score = 0
        _count = 0
        # list('1111') = ['1','1','1','1']
        for j in list(case):
            if j == "O":
                _count += 1
                score += _count
                continue
            _count = 0
        print(score)
