from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def material_consumption(self):
        raise NotImplementedError


class Coat(Clothes):
    def __init__(self, name: str, size):
        super().__init__(name=name)
        self.size = size

    @property
    def material_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name: str, growth):
        super().__init__(name=name)
        self.growth = growth

    @property
    def material_consumption(self):
        return self.growth * 2 + 0.3


coat = Coat(name="Coat", size=6.5)
print(coat.name, coat.material_consumption)

suit = Suit(name="Suit", growth=10)
print(suit.name, suit.material_consumption)
