import math


def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:
    return (x, y, z)


def calculate_distance(p1: tuple[float, float, float],
                       p2: tuple[float, float, float]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def parse_coordinates(s: str) -> tuple[int, int, int]:
    if s is None:
        raise ValueError("Expected 3 comma-separated values")
    parts = s.split(",")
    if len(parts) != 3:
        raise ValueError("Expected 3 comma-separated values")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def put_your_args(first_str: str, second_str: str) -> None:
    print("=== Game Coordinate System ===\n")

    origin = create_position(0, 0, 0)
    pos = create_position(10, 20, 5)
    print(f"Position created: {pos}")
    d1 = calculate_distance(origin, pos)
    print(f"Distance between {origin} and {pos}: {d1:.2f}")
    print()

    print(f'Parsing coordinates: "{first_str}"')
    try:
        parsed = parse_coordinates(first_str)
        print(f"Parsed position: {parsed}")
        d2 = calculate_distance(origin, parsed)
        print(f"Distance between {origin} and {parsed}: {d2}")
        print()
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            f"Error details - Type: {error.__class__.__name__}"
            f", Args: {error.args}"
            )
        return
    print(f'Parsing invalid coordinates: "{second_str}"')
    try:
        parsed = parse_coordinates(second_str)
        print(f"Parsed position: {parsed}")
        d2 = calculate_distance(origin, parsed)
        print(f"Distance between {origin} and {parsed}: {d2}")
        print()
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(
            f"Error details - Type: {error.__class__.__name__}"
            f", Args: {error.args}"
            )
    print()

    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    put_your_args("3,4,0", "abc,def,ghi")
