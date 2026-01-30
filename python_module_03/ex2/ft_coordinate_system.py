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
    parts = s.split(",")
    if len(parts) != 3:
        raise ValueError("Expected 3 comma-separated values")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def main() -> None:
    print("=== Game Coordinate System ===\n")

    origin = create_position(0, 0, 0)
    pos = create_position(10, 20, 5)
    print(f"Position created: {pos}")
    d1 = calculate_distance(origin, pos)
    print(f"Distance between {origin} and {pos}: {d1:.2f}")
    print()

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    parsed = parse_coordinates(coord_str)
    print(f"Parsed position: {parsed}")
    d2 = calculate_distance(origin, parsed)
    print(f"Distance between {origin} and {parsed}: {d2}")
    print()

    bad = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad}"')
    try:
        _ = parse_coordinates(bad)
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
    main()
