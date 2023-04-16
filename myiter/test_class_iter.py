# -*- coding: utf8 -*-
#!/usr/bin/python

# 自定义类，实现迭代器功能
class MyIterator():
    def __init__(self,step):
        self.step = step

    def next(self):
        """ 返回下一个元素 """
        if self.step == 0:
            raise StopIteration
        self.step -=1
        return self.step
    def __iter__(self):
        """返回迭代器自身"""
        return iter(self.step)


if __name__=="__main__":
    for el in MyIterator(4):
       print(el)