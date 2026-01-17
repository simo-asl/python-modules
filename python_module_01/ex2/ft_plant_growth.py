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
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    rose.ft_get_info()

    start_height: int = rose.height
    for _day in range(1, 7):
        rose.ft_pass_day()

    print("=== Day 7 ===")
    rose.ft_get_info()
    print(f"Growth this week: +{rose.height - start_height}cm")
