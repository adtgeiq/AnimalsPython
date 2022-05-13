import unittest

from Animal import Animal
from AnimalFactory import AnimalFactory
from AnimalInterface import AnimalInterface
from animales.Cat import Cat


class AnimalFactoryTest(unittest.TestCase):
    def test_animal_creation(self):
        n = AnimalFactory.create_animal(None, "cat", "Mich", 10, 9, "Gris")
        self.assertEqual(n.get_name(), "Mich")
        self.assertEqual(n.get_age(), 10)
        self.assertEqual(n.get_weight(), 9)
        self.assertEqual(n.get_color(), "Gris")

    def test_is_an_animal(self):
        aaaaaa = AnimalFactory.create_animal(None, "pingui", "Pingu", 16, 15, "Blanco y negro")
        self.assertIsInstance(aaaaaa, Animal)

    def test_e(self):
        sss = AnimalFactory.create_animal(None, "pingui", "Pingu", 16, 15, "Blanco y negro")
        self.assertIsInstance(sss, AnimalInterface)

    def test_gato(self):
        n = AnimalFactory.create_animal(None, "cat", "Mich", 10, 9, "Gris")
        self.assertIsInstance(n, Cat)
