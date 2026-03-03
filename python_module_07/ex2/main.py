from typing import List, Set, Type

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical


def _methods_defined_on(
    cls: Type[object],
    *,
    exclude: Set[str] | None = None,
) -> List[str]:
    """
    Returns method names defined directly on `cls` (not inherited),
    preserving definition order via cls.__dict__ (insertion-ordered).
    """
    exclude = exclude or set()
    methods: List[str] = []

    for name, value in cls.__dict__.items():
        if name.startswith("__"):
            continue
        if name in exclude:
            continue
        if callable(value):
            methods.append(name)

    return methods


def _capabilities_for_base(
    impl_cls: Type[object],
    base_cls: Type[object],
    *,
    exclude: Set[str] | None = None,
) -> List[str]:
    """
    Uses MRO to ensure `base_cls` is part of the implementation ancestry,
    then returns methods defined on that base interface/class.
    """
    if base_cls not in impl_cls.mro():
        return []
    return _methods_defined_on(base_cls, exclude=exclude)


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    elite = EliteCard(
        "Arcane Warrior",
        4,
        "Epic",
        attack_power=5,
        health=8,
        mana_pool=4,
    )

    print("EliteCard capabilities:")
    print("- Card:", _capabilities_for_base(EliteCard, Card,
          exclude={"__init__"}))
    print("- Combatable:", _capabilities_for_base(EliteCard, Combatable))
    print("- Magical:", _capabilities_for_base(EliteCard, Magical))
    print()
    print("Playing Arcane Warrior (Elite Card):")
    print()
    print("Combat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(2))
    print()
    print("Magic phase:")

    spell_elite = EliteCard(
        "Arcane Warrior",
        4,
        "Epic",
        attack_power=5,
        health=8,
        mana_pool=4,
    )
    print("Spell cast:",
          spell_elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))

    mana_elite = EliteCard(
        "Arcane Warrior",
        4,
        "Epic",
        attack_power=5,
        health=8,
        mana_pool=4,
    )
    print("Mana channel:", mana_elite.channel_mana(3))
    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
