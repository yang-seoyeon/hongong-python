print("#1번 문제")
for i in range(1, 100 + 1):
    print (i)
print()


print("#2번 문제")
for i in range(1, 100 + 1):
    if i == 100:
        print (i)
    else:
        print (i, end=",")
print()


print("#3번 문제")
for i in range(1, 100 + 1):
    if i == 100:
        print(i)
    elif i % 10 ==0:
        print (i)
    else:
        print (i, end=",")
print()


print("#4번 문제")
for i in range(1, 100 + 1):
    if i % 10 == 0:
        print (i)
    else:
        print ("%02d" % i, end = ",")