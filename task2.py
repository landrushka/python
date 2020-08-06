class Road(object):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate(self, mass, depth):
        return self.__length * self.__width * mass * depth


road = Road(20, 5000)

result = road.calculate(25, 5)
print(result)
