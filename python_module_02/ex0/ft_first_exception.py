def check_temperature(temp_str: str) -> int | None:
    temp = int(temp_str)

    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    try:
        print("Testing temperature: 25")
        check_temperature("25")
    except ValueError as error:
        print(error)

    try:
        print("\nTesting temperature: abc")
        check_temperature("abc")
    except ValueError as error:
        print(error)

    try:
        print("\nTesting temperature: 100")
        check_temperature("100")
    except ValueError as error:
        print(error)

    try:
        print("\nTesting temperature: -50")
        check_temperature("-50")
    except ValueError as error:
        print(error)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
