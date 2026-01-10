class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self._height: int = height
        self._age: int = age

    def get_info(self) -> str:
        return f"""{self.name} ({self.__class__.__name__}): {self._height}cm,\
 {self._age} days"""


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        print(f"{self.name}  is blooming beautifully!")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, value: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diametr: int = value

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.trunk_diameter}cm diameter"

    def produce_shade(self) -> None:
        shade_area: float = self.trunk_diameter * 1.57
        print(f"{self.name} provides {int(shade_area)} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str,
                 height: int, age: int, season: str, nutrition: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutrition: str = nutrition

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.harvest_season} harvest"

    def nutritional_value(self) -> None:
        print(f"{self.name} is rich in {self.nutrition}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose: Flower = Flower("Rose", 25, 30, "red")
    lily: Flower = Flower("Lily", 35, 20, "white")

    oak: Tree = Tree("Oak", 500, 1825, 50)
    pine: Tree = Tree("Pine", 400, 1460, 40)

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot: Vegetable = Vegetable("Carrot", 20, 75, "autumn", "vitamin A")

    print(rose.get_info())
    rose.bloom()
    print("")
    print(oak.get_info())
    oak.produce_shade()
    print("")
    print(tomato.get_info())
    tomato.nutritional_value()
