from typing import Callable, Tuple, Any, List


def spell_combiner(first_spell: Callable, second_spell: Callable) -> Callable:
    def cast_both(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        result_one = first_spell(*args, **kwargs)
        result_two = second_spell(*args, **kwargs)
        return result_one, result_two

    return cast_both


def power_amplifier(spell: Callable, multiplier: int) -> Callable:
    def boosted_spell(*args: Any, **kwargs: Any) -> Any:
        base_value = spell(*args, **kwargs)
        return base_value * multiplier

    return boosted_spell


def conditional_caster(check: Callable, spell: Callable) -> Callable:
    def conditional_spell(*args: Any, **kwargs: Any) -> Any:
        allowed = check(*args, **kwargs)

        if not allowed:
            return "Spell fizzled"

        return spell(*args, **kwargs)

    return conditional_spell


def spell_sequence(spell_list: List[Callable]) -> Callable:
    def cast_sequence(*args: Any, **kwargs: Any) -> List[Any]:
        results: List[Any] = []

        for spell in spell_list:
            outcome = spell(*args, **kwargs)
            results.append(outcome)

        return results

    return cast_sequence


if __name__ == "__main__":

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    result = combo("Dragon")
    print(result[0], ",", result[1])

    print("\nTesting power amplifier...")

    def raw_power() -> int:
        return 10

    amplified = power_amplifier(raw_power, 3)
    print(f"Original: {raw_power()}, Amplified: {amplified()}")
