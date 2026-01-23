def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    print("Testing temperature: 25")
    check_temperature("25")

    print("\nTesting temperature: abc")
    check_temperature("abc")

    print("\nTesting temperature: 100")
    check_temperature("100")

    print("\nTesting temperature: -50")
    check_temperature("-50")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
