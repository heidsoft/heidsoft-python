# 可变参数
def work(**kwargs):
    print(type(kwargs))
    if isinstance(kwargs,dict):
        for key,value in kwargs.items():
            print(key+"--"+value)
    print(kwargs)

if __name__=="__main__":
    work(name="liubin")