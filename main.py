from AnimalFactory import AnimalFactory


def main():
    cat = AnimalFactory.create_animal(None, "cat", "Mich", 10, 9, "Gris")

    cat.walk()
    cat.make_sound()


if __name__ == "__main__":
    main()
