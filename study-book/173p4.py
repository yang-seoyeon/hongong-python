# 딕셔너리를 선언합니다.

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
        },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

# for 반복문을 사용합니다.
for key in character:
    value = character[key]
    if type(value) is dict:
        for k in value:
            print (k, ":", value[k])
    elif type(value) is list:
        for l in value:
            print(key, ":", l)
    else:
        print(key, ":", value)

# for 반복문을 사용합니다.
for key in character:
    # value = character[key]
    if type(character[key]) is dict:
        for k in character[key]:
            print (k, ":", character[key][k])
    elif type(character[key]) is list:
        for l in character[key]:
            print(key, ":", l)
    else:
        print(key, ":", character[key])