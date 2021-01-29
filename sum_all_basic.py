def sum_all(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

print(sum_all(1, 100))
print(sum_all(50, 100))


def ret_none():
    return

print(ret_none())