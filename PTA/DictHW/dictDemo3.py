dict = {}

for _ in range(5):
    # 输入姓名
    if input() == "张富":
        dict["张富"] = 50000
    elif input() == "赵诺":
        dict["赵诺"] = 50000
    else:
        dict[input()] = 30000

for k, v in dict.items():
    print(f"{k}的年终奖为{v}")