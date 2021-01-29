# 숫자는 무작위로 입력해도 상관없습니다.
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
     character[key_list[i]] = value_list[i]



# while len(key_list) and len(value_list) > 0:
#     character[key_list[0]] = value_list[0]
#     del key_list[0]
#     del value_list[0]


# i = 0
# while i < len(key_list):
#     character[key_list[i]] = value_list[i]
#     i += 1

# i = 0
# while len(key_list) and len(value_list) > 0:
#     character = {key_list[0] : value_list[0]}
#     del key_list[0]
#     del value_list[0]
#     i += 1
#     print(character)



# i = 0
# while len(key_list) and len(value_list) > 0:
#     character = {key_list[i] : value_list[i]}
#     del key_list[i]
#     del value_list[i]
#     i += 1



# 최종 출력
print(character)

