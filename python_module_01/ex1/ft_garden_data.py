class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def ft_print(self):
        print(
            self.name,
            ": ",
            self.height,
            "cm, ",
            self.age,
            " days old",
            sep="")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Ma3dnouss", 10, 17)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.ft_print()