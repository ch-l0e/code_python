class Circle:
    def __init__(self, radius, diameter):
        self.__radius = radius
        self.__diameter = diameter
    
    def info(self):
        return f"circle(radius: {self.__radius} diameter: {self.__diameter})"

    @property
    def radius(self):
        return self.__radius
    
    @property
    def diameter(self):
        return self.__diameter

    def get_circumference(self):
        return self.__diameter * 3.14

c1 = Circle(5, 10)
print(c1.info())
print(c1.radius)
print(c1.diameter)
print(c1.get_circumference)