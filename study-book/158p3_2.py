numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if len(str(number)) == 3:
        format_a = "{} 는 3 자리수입니다.".format(number)
        print(format_a)
    elif len(str(number)) == 2:
        format_b = "{} 는 2 자리수입니다.".format(number)
        print(format_b)
    else:
        format_c = "{} 는 1 자리수입니다.".format(number)
        print(format_c)