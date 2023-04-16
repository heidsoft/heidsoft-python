# -*- coding: utf8 -*-
#!/usr/bin/python

"""
生成器测试，使需要返回一系列元素的函数所需代码更加简单、高效。
"""
def fibonacci():
      a, b = 0, 1
      while True:
        yield b
        a, b = b, a+b

if __name__=="__main__":
    fib = fibonacci()
    print(fib.__next__())
    print(fib.__next__())
    print([fib.__next__() for i in range(10)])