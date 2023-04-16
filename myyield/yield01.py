#https://pyzh.readthedocs.io/en/latest/the-python-yield-keyword-explained.html

"""
当你建立了一个列表，你可以逐项地读取这个列表，这叫做一个可迭代对象:

"""
mylist = [1, 2, 3]


def test1():
    print("\ntest1---------------------")
    for i in mylist:
        print(i)


test1()

"""
mylist 是一个可迭代的对象。当你使用一个列表生成式来建立一个列表的时候，就建立了一个可迭代的对象:
"""
mylist2 = [x * x for x in range(3)]


def test2():
    print("\ntest2---------------------")
    for i in mylist2:
        print(i)


test2()


"""
生成器

看起来除了把 [] 换成 () 外没什么不同。
但是，你不可以再次使用 for i in mygenerator , 
因为生成器只能被迭代一次：先计算出0，然后继续计算1，然后计算4，一个跟一个的…
"""
mygenerator = (x*x for x in range(3))

def test3():
    print("\ntest3---------------------")
    for i in mygenerator:
        print(i)
test3()

def createGenerator():
    mylist = range(3)
    print(mylist)
    for i in mylist:
        print("yield test {!r}".format(i));
        yield i*i

mygenerator = createGenerator()
print(mygenerator)
for i in mygenerator:
    print(i)