class Person:
    def __init__(self, age):
        self._age = age  # 这是一个内部变量，不直接暴露给外部

    @property
    def age(self):
        """Getter for age."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for age. Includes validation."""
        if isinstance(value, int) and 0 <= value <= 150:
            self._age = value
        else:
            raise ValueError("Invalid age")

    @age.deleter
    def age(self):
        """Deleter for age."""
        del self._age

p = Person(30)
print(p.age)
p.age = 35
print(p.age)
del p.age
print(p.age)  # AttributeError: 'Person' object has no attribute '_age'