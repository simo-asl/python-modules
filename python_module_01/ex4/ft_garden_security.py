class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height: int = 0
        self.__age: int = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, cm: int) -> None:
        if cm < 0:
            print(f"Invalid operation attempted: height {cm}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = cm
        print(f"Height updated: {cm}cm [OK]")

    def get_height(self) -> int:
        return self.__height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def get_age(self) -> int:
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)

    age: int = rose.get_age()
    height: int = rose.get_height()

    print()
    print(f"Current plant: {rose.name} ({height}cm, {age} days)")
