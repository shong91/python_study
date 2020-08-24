def plus(*args):
    result = 0 
    for number in args:
        result += number
    print(result)


plus(1,2,3,4,5,10)