list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.extend(list_a) # [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.append(10) # [0, 1, 2, 3, 4, 5, 6, 7, 10]
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.insert(3,0) # [0, 1, 2, 0, 3, 4, 5, 6, 7]
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.remove(3) # [0, 1, 2, 4, 5, 6, 7]
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.pop(3) # [0, 1, 2, 4, 5, 6, 7]
print(list_a)

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
list_a.clear() # []
print(list_a)