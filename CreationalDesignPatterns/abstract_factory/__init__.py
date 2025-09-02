from abc import ABC, abstractmethod

class InterfaceColor(ABC):
    @abstractmethod
    def set_color(self):
        pass

class ColorBlue(InterfaceColor):
    def set_color(self):
        return "ColorBlue"
    
class ColorGreen(InterfaceColor):
    def set_color(self):
        return "ColorGreen"
    
class Car(ABC):
    @abstractmethod
    def walk(self, color: InterfaceColor):
        pass

class Fiat(Car):
    def walk(self, color: InterfaceColor):
        return f"Car {color.color()} Walking"

class Honda(Car):
    def walk(self, color: InterfaceColor):
        return f"Car {color.color()} Walking"

class CarFactory(ABC):
    @abstractmethod
    def create_car(self) -> 'Car':
        pass

    @abstractmethod
    def set_color(self) -> 'InterfaceColor':
        pass

class FiatFactory(CarFactory):
    def create_car(self) -> 'Car':
        return Fiat()
    
    def set_color(self) -> 'InterfaceColor':
        return ColorBlue()

class HondaFactory(CarFactory):
    def create_car(self) -> 'Car':
        return Honda()

    def set_color(self) -> 'InterfaceColor':
        return ColorGreen()

class Client:
    def __init__(self, factory: CarFactory):
        self._car = factory.create_car()
        self._color = factory.set_color()

    def run(self) -> None:
        print(self._car.walk(self._color))

if __name__ == '__main__':
    print("Creating a Fiat with its compatible color:")
    fiat_app = Client(FiatFactory())
    fiat_app.run()

    print("\nCreating a Honda with its compatible color:")
    honda_app = Client(HondaFactory())
    honda_app.run()