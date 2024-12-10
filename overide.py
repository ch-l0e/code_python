class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self): #creates string equivalent
        return f"Animal({self.name})"

    def __repr__(self): #make printable
        return self.__str__()
    
    def sound(self):
        return "urf!"

class Dog(Animal):
    def info(self):
        return 'I AM ACTUALLY A DOG!'
    
    def sound(self):
        return "BARK BARK"

a1 = Animal("Seal")
d1 = Dog("Marshall")
print(a1.sound())
print(d1.sound())