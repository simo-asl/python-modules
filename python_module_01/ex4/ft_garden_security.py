class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant Created: {self.name}")

    def set_height(self, cm):
        if cm < 0:
            print(f"\nInvalid operation attempted: height {cm}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = cm
            print(f"Height updated: {cm}cm [OK]")

    def get_height(self):
        return self.__height

    def set_age(self, age):
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    age = rose.get_age()
    height = rose.get_height()
    print(f"Current plant: {rose.name} ({height}cm, {age} days)")
