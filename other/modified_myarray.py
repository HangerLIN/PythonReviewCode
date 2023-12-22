
class MyArray:
    """All the elements in this array must be numbers"""
    def __IsNumber(self,n):
        return isinstance(n, (int, float, complex))
    def __init__(self,*args):
        if not args:
            self.__value =[]
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print('All elements must be numbers')
                    return
            self.__value = list(args)

    def __mul__(self, other):
        if isinstance(other, MyArray):
            if len(self.__value) != len(other.__value):
                return 'Lengths of arrays must be equal for dot product'
            return sum(a * b for a, b in zip(self.__value, other.__value))
        elif self.__IsNumber(other):
            return MyArray(*[a * other for a in self.__value])
        else:
            return 'Invalid operation'

    def __str__(self):
        return str(self.__value)

ma = MyArray(1,2,3,4,5,6)
ma = ma * 2
mc = MyArray(1,2,3,4,5,6)
result = ma * mc
print(ma)
print(result)