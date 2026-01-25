import sys


def fibonacci_stream(n: int):
    a = 0
    b = 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_stream(n: int):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def number_stream(n: int):
    i = 0
    while i < n:
        yield i
        i += 1


def game_event_stream(n: int):
    i = 1
    while i <= n:
        yield {
            "tick": i,
            "score": i * 3,
            "damage": (i * 7) % 10
        }
        i += 1


def batch_stream(stream, size: int):
    batch = []
    for item in stream:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch


def main() -> None:
    k = 10
    n = 100000
    events = 20
    batch_size = 5

    args = sys.argv[1:]
    if len(args) >= 1:
        k = int(args[0])
    if len(args) >= 2:
        n = int(args[1])
    if len(args) >= 3:
        events = int(args[2])
    if len(args) >= 4:
        batch_size = int(args[3])

    print("Fibonacci:")
    for x in fibonacci_stream(k):
        print(x, end=" ")
    print("\n")

    print("Primes:")
    for x in prime_stream(k):
        print(x, end=" ")
    print("\n")

    gen = number_stream(n)
    lst = list(range(n))

    print("Memory demo:")
    print("Generator size:", sys.getsizeof(gen))
    print("List size:", sys.getsizeof(lst))
    print()

    print("Game events (batched):")
    stream = game_event_stream(events)
    for i, batch in enumerate(batch_stream(stream, batch_size), start=1):
        score = 0
        damage = 0
        for ev in batch:
            score += ev["score"]
            damage += ev["damage"]
        print(
            "Batch", i,
            "| size:", len(batch),
            "| score:", score,
            "| damage:", damage
        )


if __name__ == "__main__":
    main()
