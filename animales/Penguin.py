from Animal import Animal


class Penguin(Animal):
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_color(self):
        return self.color

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight

    def set_color(self, color):
        self.color = color

    def make_sound(self):
        print("wa wa wa waaa")

    def walk(self):
        print("Penguin is walking")
