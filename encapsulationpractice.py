class Person:
    def __init__(self, name, wealth):
        self.name = name
        self.__wealth = wealth

    def info(self):
        return f"Person(name: {self.name}, wealth: {self.__wealth})"

    #for encapsulation attributes, if you want to "read" them, create a getter method --> def get_wealth(): works and is fine
    @property #decorator
    def wealth(self):
        return self.__wealth

    #setter --> a controlled way to modify a encapsulated attribute
    @wealth.setter
    def wealth(self, new_value):
        self.__wealth = new_value

p1 = Person("Mr Park", 69)
p2 = Person("Marshall", 1000000)
# print(p1.info())
# p1.name = "francis"
# p1.wealth = 69000000
# print(p1.info())
print(p1.wealth)
#if property did not exist --> print(p1.wealth()) instead of above
p1.wealth = 1234
print(p1.info())