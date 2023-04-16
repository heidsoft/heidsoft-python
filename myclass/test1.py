
class Test1(object):
    """
    __init__
    __enter__
    __exit__

    """
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("enter...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit...")


if __name__=="__main__":
    t1 = Test1(name="java")
    t2 = Test1(name="c++")
    t3 = Test1(name="go")
    print(t1)
    print(t2)
    print(t3)
    with open('demo.txt', 'w') as opened_file:
        opened_file.write('Hola!')