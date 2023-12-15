# In Factory pattern, we create object without exposing the creation logic to the client
# and refer to newly created object using a common interface.


class Car:
    def __init__(self, size):
        self.size = size

    def print_info(self):
        print("Car's size: " + self.size)


class CarFactory:
    def __init__(self):
        pass

    def createSmallCar(self):
        size = "small"
        return Car(size)

    def createMediumCar(self):
        size = "medium"
        return Car(size)

    def createBigCar(self):
        size = "big"
        return Car(size)


if __name__ == "__main__":
    carFactory = CarFactory()
    carFactory.createSmallCar().print_info()
    carFactory.createMediumCar().print_info()
    carFactory.createBigCar().print_info()
