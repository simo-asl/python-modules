class Plant:
    total = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.total += 1

    def print_p(self):
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
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)
    p1.print_p()
    p2.print_p()
    p3.print_p()
    p4.print_p()
    p5.print_p()
    print("Total plants created:", Plant.total)
