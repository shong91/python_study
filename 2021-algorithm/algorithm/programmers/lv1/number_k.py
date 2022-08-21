def solution(array, commands):
    answer = []
    for command in commands:
        target = array[command[0]-1:command[1]]
        answer.append(sorted(target)[command[2]-1])
    return answer


if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))