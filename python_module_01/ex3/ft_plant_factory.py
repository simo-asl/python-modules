class Plant:
    total = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.total += 1

    def print_plant(self):
        print(
            "Created: ",
            self.name,
            "(",
            self.height,
            "cm, ",
            self.age,
            " days)",
            sep=""
        )


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for plant in plants:
        plant.print_plant()
    print("Total plants created:", Plant.total)
