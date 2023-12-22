# 获取用户输入
a_class_str = input()
b_class_str = input()
acm_str = input()
english_str = input()
transfer_student = input()

# 将字符串转换为集合
a_class = set(a_class_str)
b_class = set(b_class_str.split())
acm = set(acm_str.split())
english = set(english_str.split())

# 计算总人数
total_students = a_class.union(b_class)

# 既没有参加ACM，也没有参加English的学生
not_in_race = total_students - (acm.union(english))

# 参加了任何一种竞赛的学生
all_racers = acm.union(english)

# 同时参加了ACM和English的学生
acm_and_english = acm.intersection(english)

# 只参加了ACM的学生
only_acm = acm - english

# 只参加了English的学生
only_english = english - acm

# 只参加了ACM或只参加了English的学生
acm_or_english = (acm - english).union(english - acm)

# 输出结果
print(f"Total: {len(total_students)}")
print(f"Not in race: {sorted(not_in_race)}, num: {len(not_in_race)}")
print(f"All racers: {sorted(all_racers)}, num: {len(all_racers)}")
print(f"ACM + English: {sorted(acm_and_english)}, num: {len(acm_and_english)}")
print(f"Only ACM: {sorted(only_acm)}")
print(f"Only English: {sorted(only_english)}")
print(f"ACM Or English: {sorted(acm_or_english)}")

# 处理转学的学生
if transfer_student in a_class:
    a_class.remove(transfer_student)
elif transfer_student in b_class:
    b_class.remove(transfer_student)

# 输出更新后的班级名单
updated_class = a_class.union(b_class)
print(sorted({x for x in updated_class if x.isalpha()}))
