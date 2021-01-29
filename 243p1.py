def flatten(data):
    a = []
    for i in data:
        print(i, type(i))
        if type(i) == type([]):
            print('list')
            a = a + flatten(i)
        else:
            a.append(i)
    return a



example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# example = [[1, 2, 3]]
print("원본:", example)
print("변환:", flatten(example))