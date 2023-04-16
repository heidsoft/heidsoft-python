# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm

"""
python 单例类型
"""

class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        print("this is a singleton")
        """
         static method
        """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("this class is a singleton")
        else:
            Singleton.__instance = self


s = Singleton()
print(s)
s1 = Singleton.getInstance()
print(s1)
print(s is s1)

