def water_plants(plant_list: list, plant: list) -> None:
    print("Opening watering system")
    try:
        for data in plant:
            if data not in plant_list: 
                print("Error: Cannot water None - invalid plant!")
                return
            print(f"Watering {data}")
    except TypeError:
        print("Error: Invalid plant list!")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    plant_list: list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list, plant_list)

    print("Testing with error...")
    search_list: list = ["tomato", "khyar"]

    water_plants(plant_list, search_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
