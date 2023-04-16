
def generator_function():
    """
    生成器降低程序内存使用，在程序调用时获取迭代的值，而不是一次性直接返回
    :return:
    """
    for i in range(3):
        yield i

if __name__=="__main__":
    a = generator_function()
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print("-----")
    for item in generator_function():
        print(item)