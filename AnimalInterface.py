from abc import abstractmethod
from abc import ABCMeta


class AnimalInterface(metaclass=ABCMeta):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def walk(self):
        pass
