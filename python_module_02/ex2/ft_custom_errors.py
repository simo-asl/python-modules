class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_garden_status(issue_type: str) -> None:
    if issue_type == "plant":
        raise PlantError("The tomato plant is wilting!")
    elif issue_type == "water":
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")

    try:
        check_garden_status("plant")
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")

    try:
        check_garden_status("water")
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")
    issues = ["plant", "water"]

    for issue in issues:
        try:
            check_garden_status(issue)
        except GardenError as error:
            print(f"Caught a garden error: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
