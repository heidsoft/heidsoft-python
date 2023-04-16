from enum import Enum


class MyEnum(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(MyEnum.BLUE)
print(type(MyEnum))
