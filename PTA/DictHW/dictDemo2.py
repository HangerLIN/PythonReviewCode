l = list(input().split())
dict = {}

for i in range(len(l)):
    if l[i] in dict:
        dict[l[i]] += 1
    else:
        dict[l[i]] = 1

# 对字典中的项按值进行排序
dict2 = sorted(dict.items(), key=lambda x: -x[1])

# 遍历排序后的列表并打印
for k, v in dict2:
    print(f"{k}:{v}")
