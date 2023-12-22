T = int(input())
all_data = []

for _ in range(T):
    n = int(input())
    student_info_list = []
    for _ in range(n):
        student_info = input().split()
        # 将进步总数和解题总数转换为整数
        student_info[1:] = list(map(int, student_info[1:]))
        student_info_list.append(student_info)
    # 对当前组的学生信息进行排序
    student_info_list.sort(key=lambda x: (-x[1], -x[2], x[0]))
    all_data.append(student_info_list)

# 输出每组数据的排名
for student_info_list in all_data:
    rank = 1
    prev_improvement = -1
    prev_total = -1
    for i, student in enumerate(student_info_list):
        # 只在进步总数或解题总数改变时更新排名
        if student[1] != prev_improvement or student[2] != prev_total:
            rank = i + 1

        print(f"{rank} {student[0]} {student[1]} {student[2]}")
        prev_improvement, prev_total = student[1], student[2]
