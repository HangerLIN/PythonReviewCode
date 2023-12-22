input_str = input()

# l = list(input().split())

# 读取两个字符，以空格分隔
char1, char2 = input().split()

# 倒序遍历字符串并查找字符的索引
for i in range(len(input_str) - 1, -1, -1):
    if input_str[i] == char1:
        print(i, char1)
    if input_str[i] == char2:
        print(i, char2)