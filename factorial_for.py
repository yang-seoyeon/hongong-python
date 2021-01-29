def factorial1(n):
    ret = 1
    for i in range(1, n + 1, 1):
        ret = ret * i
        print(i, ret)


    return ret


print("답1은: ", factorial1(40))


def factorial2(n):
    if n == 1:
        return 1
    
    return n * factorial2(n - 1)

print("답2은: ", factorial2(40))
