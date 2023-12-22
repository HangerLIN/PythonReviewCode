# 这是一个带参数的装饰器示例

def decorator_with_args(decorator_arg1, decorator_arg2):
    # 这是装饰器工厂，接受装饰器参数
    def decorator(func):
        # 这是实际的装饰器，接受函数作为参数
        def wrapper(*args, **kwargs):
            # 在被装饰函数前执行的代码
            print(f"Decorator arguments: {decorator_arg1}, {decorator_arg2}")
            # 调用原始函数
            result = func(*args, **kwargs)
            # 在被装饰函数后执行的代码
            return result
        # 返回包装后的函数
        return wrapper
    # 返回装饰器
    return decorator

# 使用带参数的装饰器来装饰函数
@decorator_with_args('hello', 'world')
def say_hello(name):
    print(f"Hello {name}")

# 当我们调用 say_hello 时，它已经被装饰器包装了
say_hello("Alice")
