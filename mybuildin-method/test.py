import datetime

mydate = datetime.datetime.now()

print("__str__() string: ", mydate.__str__())
print("str() string: ", str(mydate))

print("__repr__() string: ", mydate.__repr__())
print("repr() string: ", repr(mydate))


mydate1 = datetime.datetime.now()
mydate2 = eval(repr(mydate1))

print("mydate1 repr() string: ", repr(mydate1))
print("mydate2 repr() string: ", repr(mydate2))

print("the values of the objects are equal: ", mydate1==mydate2)


class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))