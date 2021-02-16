if __name__ == '__main__':
    # nums = int(input())
    # # convert str to int and set list
    # scores = list(map(float, input().split()))
    # new_scores = []
    # for score in scores:
    #     score = score / max(scores) * 100
    #     new_scores.append(score)
    #
    # print(sum(new_scores) / nums)

    n, *l = map(int, open(0).read().split())
    print(sum(l) * 100 / max(l) / n)

    # print(sum(b := [*map(int, [*open(0)][1].split())]) * 100 / max(b) / len(b))

