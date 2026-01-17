class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self._height: int = height
        self._age: int = age

    def get_info(self) -> str:
        return f"{self.name} ({self.__class__.__name__}): {self._height}cm," +\
            f" {self._age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int
                 ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = diameter

    def produce_shade(self) -> None:
        shade_area: float = self.trunk_diameter * 1.57
        print(f"{self.name} provides {int(shade_area)} square meters of shade")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        season: str,
        nutrition: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutrition: str = nutrition

    def nutritional_value(self) -> None:
        print(f"{self.name} is rich in {self.nutrition}")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.harvest_season} harvest"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose: Flower = Flower("Rose", 25, 30, "red")
    oak: Tree = Tree("Oak", 500, 1825, 50)
    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print(rose.get_info())
    rose.bloom()
    print()

    print(oak.get_info())
    oak.produce_shade()
    print()

    print(tomato.get_info())
    tomato.nutritional_value()
