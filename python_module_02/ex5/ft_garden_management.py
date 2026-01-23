class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plants(self, name: str) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants += [name]
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
            self, name: str, water_level: int, sunlight: int) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if sunlight < 2:
            raise GardenError(f"Sunlight hours {sunlight} is too low (min 2)")
        if sunlight > 12:
            raise GardenError(
                f"Sunlight hours {sunlight} is too high (max 12)")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    garden_manager = GardenManager()

    print("Adding plants...")
    try:
        garden_manager.add_plants("tomato")
        garden_manager.add_plants("lettuce")
        garden_manager.add_plants("")
    except GardenError as error:
        print(f"Caught error: {error}")

    print("\nChecking plant health...")
    try:
        garden_manager.check_plant_health("tomato", 5, 8)
        garden_manager.check_plant_health("lettuce", 15, 10)
    except (GardenError, Exception) as error:
        print(f"Caught error: {error}")

    print("\nWatering plants...")
    try:
        garden_manager.water_plants()
    except GardenError as error:
        print(f"Caught error: {error}")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
