class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added: int = 0
            self.total_growth: int = 0
            self.regular_count: int = 0
            self.flowering_count: int = 0
            self.prize_count: int = 0

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list["Plant"] = []
        self.stats: GardenManager.GardenStats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: "Plant") -> None:
        self.plants.append(plant)
        self.stats.plants_added += 1

        if plant.type == "prize":
            self.stats.prize_count += 1
        elif plant.type == "flowering":
            self.stats.flowering_count += 1
        else:
            self.stats.regular_count += 1

        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        print()
        print(
            f"Plants added: {self.stats.plants_added}, "
            f"Total growth: {self.stats.total_growth}cm"
        )
        print(
            f"Plant types: {self.stats.regular_count} regular, "
            f"{self.stats.flowering_count} flowering, "
            f"{self.stats.prize_count} prize flowers\n"
        )

    @classmethod
    def create_garden_network(cls) -> str:
        return f"Total gardens managed: {cls.total_gardens}"

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.type: str = "regular"

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str, is_blooming: bool
                 ) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = is_blooming
        self.type: str = "flowering"

    def get_info(self) -> str:
        status: str = "blooming" if self.is_blooming else "not blooming"
        return f"{super().get_info()}, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        is_blooming: bool,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color, is_blooming)
        self.prize_points: int = prize_points
        self.type: str = "prize"

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.prize_points}"


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    oak_bob = Plant("Oak Tree", 100)
    rose_bob = FloweringPlant("Rose", 25, "red", True)
    sunflower_bob = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print()

    bob.add_plant(oak_bob)
    bob.add_plant(rose_bob)
    bob.add_plant(sunflower_bob)
    print()

    alice.help_plants_grow()
    print()

    bob.help_plants_grow()
    print()

    alice.report()
    bob.report()

    print("Height validation test:", GardenManager.validate_height(oak.height))
    print()

    alice_score: int = 0
    for p in alice.plants:
        alice_score += p.height

    bob_score: int = 0
    for p in bob.plants:
        bob_score += p.height

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(GardenManager.create_garden_network())


if __name__ == "__main__":
    main()
