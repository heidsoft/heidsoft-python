# -*- coding: utf8 -*-
#!/usr/bin/python

#通过索引实现
def testByIndex():
    i = 0
    seq = ["one","two","thress"]
    for elements in seq:
        seq[i] = '%d: %s' % (i,seq[i])
        i +=1
    print(seq)


#通过内置函数实现
def testByEnumerate():
    seq = ["one","two","thress"]
    for index,elements in enumerate(seq):
        seq[index] = '%d: %s' % (index,seq[index])
    print(seq)


#私有函数
def _treatment(pos,element):
    """

    :rtype: object
    """
    return '%d: %s' % (pos,element)

#重构为列表推到方式
def testByHightEnumerate():
    seq = ["one","two","thress"]
    print [_treatment(i,el) for i,el in enumerate(seq)]

if __name__=="__main__":
    testByIndex()
    testByEnumerate()
    testByHightEnumerate()