# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()


# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")

def print_say():
    print("say")

# 조합하기
call_10_times(print_hello)
call_10_times(print_say)


def f(x):
    return (x % 2) == 0

def fc(x):
    return x%2 == 0:

list_a = list(range(1, 101))
print(list_a)

list_b = filter(f, list_a)

list_c = filter(lambda x: x % 3 ==0, list_a)
print(list_b)

print(list(list_b))
print(list(list_c))


