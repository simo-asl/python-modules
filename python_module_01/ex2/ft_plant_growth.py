class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def ft_age(self):
        self.age += 1

    def ft_grow(self):
        self.height += 1

    def ft_pass_day(self):
        self.ft_grow()
        self.ft_age()

    def ft_get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.ft_get_info()
    now = rose.height
    for day in range(1, 7):
        rose.ft_pass_day()

    print("=== Day 7 ===")
    rose.ft_get_info()
    print(f"Growth this week: +{rose.height - now}cm")
