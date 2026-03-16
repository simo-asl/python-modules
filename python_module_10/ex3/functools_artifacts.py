import functools
import operator
from typing import List, Callable, Dict, Any


def spell_reducer(values: List[int], mode: str) -> int:
    if not values:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if mode not in operations:
        raise ValueError(f"Unknown operation: {mode}")

    func = operations[mode]
    return functools.reduce(func, values)


def partial_enchanter(base: Callable) -> Dict[str, Callable]:
    fire = functools.partial(base, power=50, element="fire")
    ice = functools.partial(base, power=50, element="ice")
    lightning = functools.partial(base, power=50, element="lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def dispatch(value: Any) -> str:
        return "Unknown magic type"

    @dispatch.register(int)
    def _(value: int) -> str:
        return f"Damage spell with {value} power"

    @dispatch.register(str)
    def _(value: str) -> str:
        return f"Casting enchantment: {value}"

    @dispatch.register(list)
    def _(value: list) -> str:
        size = len(value)
        return f"Multi-cast of {size} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")

    numbers = [10, 20, 30, 40]

    print("Sum:", spell_reducer(numbers, "add"))
    print("Product:", spell_reducer(numbers, "multiply"))
    print("Max:", spell_reducer(numbers, "max"))

    print("\nTesting memoized fibonacci...")

    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
