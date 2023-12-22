# # for j in list:
# #     if 3 in list:
# #         list.remove(3)
# # print(list)
# # list = [1, 2, 3, 4, 5, 6]
# # list *= 3
# # list.remove(3)
# # print(list)
# x = [3,5,3,7]
# print([x.index(i) for i in x if i==3])
#
# x = [8, 55, 111]
# x.sort(key=lambda x: len(str(x)))
# print(x)
#
# print(list(range(6))[::2])
#
x = range(1,5)
y = range(4,8)
zip(x,y)
print(sum(i * j for i, j in zip(x, y)))
#
# print(list('[1, 2, 3]'))
#
# print(list(map(lambda x: x+5, [1, 2, 3, 4, 5])))
#
# print(sorted([111, 2, 33], key=lambda x: -len(str(x))))
#
# x = [1,2,3,4,5]
# x[1::2] = sorted(x[1::2], reverse=True)
# print(x)
#
# vec = [[1,2,3], [3,4,5]]
# print([[row[i] for row in vec] for i in range(len(vec[0]))])
#
# x = [1, 2]
# print(list(enumerate(x)))
#
# x = [1, 2, 3, 2, 3]
# x.remove(2)
# print(x)
#
# x = [3, 5, 7]
# x[len(x):] = [1, 2]
# print(x)
#
# x = [2,4,6,8]
# x.insert(1, 3)
# print(x)