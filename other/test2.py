class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14159 * self.__radius ** 2

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

class Table:
    def __init__(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

# (1) 创建半径为2的圆和高度为4的桌子的实例，并输出它们的面积和高度
circle = Circle(2)
table = Table(4)
print(f"Circle Area: {circle.get_area()}")  # 输出圆的面积
print(f"Table Height: {table.get_height()}")  # 输出桌子的高度

# (2) 将圆的半径和桌子的高度分别改为4和8，然后再次输出
circle.set_radius(4)
table.set_height(8)
print(f"Updated Circle Area: {circle.get_area()}")  # 输出更新后的圆的面积
print(f"Updated Table Height: {table.get_height()}")  # 输出更新后的桌子的高度
