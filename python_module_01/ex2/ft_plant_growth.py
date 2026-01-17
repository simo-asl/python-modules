class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def ft_age(self) -> None:
        self.age += 1

    def ft_grow(self) -> None:
        self.height += 1

    def ft_pass_day(self) -> None:
        self.ft_grow()
        self.ft_age()

    def ft_get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    print("=== Day 1 ===")
    for p in plants:
        p.ft_get_info()

    start_heights: dict[str, int] = {p.name: p.height for p in plants}

    for day in range(7):
        for p in plants:
            p.ft_pass_day()

    print("=== Day 7 ===")
    for p in plants:
        p.ft_get_info()
        growth: int = p.height - start_heights[p.name]
        print(f"Growth this week: +{growth}cm")
