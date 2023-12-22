class MyClass:
    def __init__(self, value):
        self._my_attribute = value

    @property
    def my_attribute(self):
        """Getter for my_attribute."""
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        """Setter for my_attribute."""
        self._my_attribute = value

    @my_attribute.deleter
    def my_attribute(self):
        """Deleter for my_attribute."""
        del self._my_attribute

class Person:
    def __init__(self, age):
        self._age = age  # _age 是一个内部变量，用于存储年龄值

    def get_age(self):
        """Getter method for age."""
        return self._age

    def set_age(self, value):
        """Setter method for age. Checks if the age is a valid integer."""
        if isinstance(value, int) and 0 <= value <= 150:
            self._age = value
        else:
            raise ValueError("Invalid age")

    def del_age(self):
        """Deleter method for age."""
        del self._age

    # 使用 property() 创建 age 属性，链接到相应的 getter、setter 和 deleter
    age = property(get_age, set_age, del_age, "I am the 'age' property.")
