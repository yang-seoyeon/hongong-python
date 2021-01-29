def mul(*values):
    초깃값 = 1
    for value in values:
        초깃값 =  초깃값 * value
    return 초깃값

# 함수를 호출합니다.
print(mul(5, 7, 9, 10))