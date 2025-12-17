class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            ...
        else:
            self.__height = height

    def get_height(self):
        return self.__height

    def set_age(self, age):
        if age < 0:
            ...
        else:
            self.__age = age

    def get_age(self):
        return self.__age
