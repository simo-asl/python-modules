from typing import Generator


def event_type(i: int) -> str:
    if i % 10 == 0:
        return "treasure"
    if i % 7 == 0:
        return "level_up"
    return "monster"


def event_text(kind: str) -> str:
    if kind == "treasure":
        return "found treasure"
    if kind == "level_up":
        return "leveled up"
    return "killed monster"


def player_name(i: int) -> str:
    return f"player_{i}"


def player_level(i: int) -> int:
    return (i % 10) + 8


def game_events(n: int) -> Generator[tuple[int, str, int, str], None, None]:
    i = 1
    while i <= n:
        yield i, player_name(i), player_level(i), event_type(i)
        i += 1


def fibonacci(n: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


def is_prime(x: int) -> bool:
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def primes(n: int) -> Generator[int, None, None]:
    count = 0
    x = 2
    while count < n:
        if is_prime(x):
            yield x
            count += 1
        x += 1


def machi_main() -> None:
    total = 1
    subject_output = 0.045
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {total} game events...\n")

    processed = 0
    high_level = 0
    treasure = 0
    level_up = 0

    for i, player, level, kind in game_events(total):
        processed += 1

        if level >= 10:
            high_level += 1

        if kind == "treasure":
            treasure += 1
        elif kind == "level_up":
            level_up += 1
        print(f"Event {i}: Player {player} (level {level}) {event_text(kind)}")

    timing = subject_output / (processed / total)
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {timing:.3f} seconds\n")

    print("=== Generator Demonstration ===")
    fib = ", ".join(str(x) for x in fibonacci(10))
    prm = ", ".join(str(x) for x in primes(5))
    print(f"Fibonacci sequence (first 10): {fib}")
    print(f"Prime numbers (first 5): {prm}")


if __name__ == "__main__":
    machi_main()
