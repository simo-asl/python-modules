class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    pass


class Tree(Plant):
    pass


class Vegetable(Plant):
    pass
