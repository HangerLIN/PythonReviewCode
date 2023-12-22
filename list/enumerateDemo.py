numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # 升序排序
print(numbers)
numbers.sort(reverse=True)  # 降序排序
print(numbers)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

for i, value in enumerate(["a", "b", "c"]):
    print(i, value)