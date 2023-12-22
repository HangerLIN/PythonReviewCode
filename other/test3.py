class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14159 * self.radius ** 2

class Table:
    def __init__(self, height):
        self.height = height

    def get_height(self):
        return self.height

class Roundtable(Circle, Table):
    def __init__(self, radius, height, color):
        Circle.__init__(self, radius)
        Table.__init__(self, height)
        self.color = color

    def get_color(self):
        return self.color

# (1) 创建半径为2，高度为4，颜色为红色的圆桌实例，并输出其面积、高度和颜色信息
round_table = Roundtable(2, 4, "red")
print(f"Roundtable Area: {round_table.get_area()}")  # 输出圆桌的面积
print(f"Roundtable Height: {round_table.get_height()}")  # 输出圆桌的高度
print(f"Roundtable Color: {round_table.get_color()}")  # 输出圆桌的颜色