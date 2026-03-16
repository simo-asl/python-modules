from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    calls = 0

    def increment() -> int:
        nonlocal calls
        calls += 1
        return calls

    return increment


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    current = initial_power

    def add_power(value: int) -> int:
        nonlocal current
        current = current + value
        return current

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item: str) -> str:
        prefix = enchantment_type
        return f"{prefix} {item}"

    return enchant


def memory_vault() -> Dict[str, Callable]:
    storage: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        if key in storage:
            return storage[key]
        return "Memory not found"

    actions: Dict[str, Callable] = {}
    actions["store"] = store
    actions["recall"] = recall

    return actions


if __name__ == "__main__":
    print("Testing mage counter...")

    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())

    print("\nTesting enchantment factory...")

    fire = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")

    print(fire("Sword"))
    print(ice("Shield"))
