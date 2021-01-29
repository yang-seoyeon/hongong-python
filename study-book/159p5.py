numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number-1)%3].append(number)

print(output)

output = [[], [], []]
for number in numbers:
    if (number%3 == 1):
        output[0].append(number)
    elif (number%3 == 2):
        output[1].append(number)
    elif (number%3 == 0):
        output[2].append(number)


print(output)

a = 100
if a=10:
    print("a==10")
else:
    print("a!=0")