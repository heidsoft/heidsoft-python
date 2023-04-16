# -*- coding: utf8 -*-

"""

协同程序测试
"""

def mytask_1():
    for i in range(3):
        print("task1 %s" % i)
        yield i

def mytask_2():
    for i in range(3):
        print "task2 %s" % i
        yield i


if __name__=="__main__":
    multitask.add(mytask_1())
    multitask.add(mytask_2())
    multitask.run()