import math


class Circle:
    Radius = 0

    def __init__(self, R):
        self.Radius = R

    def getArea(self):
        return math.pi * self.Radius * self.Radius


class Table:
    Height = 0

    def __init__(self, H):
        self.Height = H

    def getHeight(self):
        return self.Height

# if __name__ == '__main__':
#     print_hi('PyCharm')
# 第一个问题
Circle1 = Circle(2)
print(Circle1.getArea())

Table1 = Table(4)
print(Table1.getHeight())


# 第二个问题
Circle1.Radius = 4
print(Circle1.getArea())
Table1.Height = 8
print(Table1.getHeight())