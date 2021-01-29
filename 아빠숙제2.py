#-*- coding: utf-8 -*-

# def gugu():
#     for number in range (1, 9 +1):
#         answer = number * (number + 1)
#         print(answer)


with open("아빠숙제2.txt", "w", encoding = "utf-8") as file:
    for i in range (1, 9+ 1):
        for j in range (1, 9 + 1):
            print("{} X {} = {}".format(i, j, i*j))
            file.write("{} X {} = {}\n".format(i, j, i*j))