from typing import Callable, Tuple, Any, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combines two spells to be cast simultaneously on the same targets."""
    def combined(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplifies the numerical return value of a spell."""
    def amplified(*args: Any, **kwargs: Any) -> Any:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Casts a spell only if the condition evaluates to True."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return wrapper


def spell_sequence(spells: List[Callable]) -> Callable:
    """Casts a sequence of spells in order on the same targets."""
    def sequence_wrapper(*args: Any, **kwargs: Any) -> List[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence_wrapper


if __name__ == "__main__":
    def fireball(target: str) -> str: return f"Fireball hits {target}"
    def heal(target: str) -> str: return f"Heals {target}"
    combined = spell_combiner(fireball, heal)
    res = combined("Dragon")
    print("Testing spell combiner...")
    print(f"Combined spell result: {res[0]}, {res[1]}")
    print("\nTesting power amplifier...")
    def raw_power() -> int: return 10
    amplified = power_amplifier(raw_power, 3)
    print(f"Original: {raw_power()}, Amplified: {amplified()}")
