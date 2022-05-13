from animals.Cat import Cat
from animals.Penguin import Penguin


class AnimalFactory:

    def create_animal(self, kk, n, age, weight, color):

        animals = {
            "cat": Cat,
            "pingui": Penguin
        }

        return animals[kk](n, age, weight, color)
