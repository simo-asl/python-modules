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
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    p4 = Plant("Ma3dnouss", 10, 17)
    print("=== Garden Plant Registry ===")
    p1.ft_print()
    p2.ft_print()
    p3.ft_print()
    p4.ft_print()
