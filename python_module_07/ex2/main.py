from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")

    elite = EliteCard(
        "Arcane Warrior",
        4,
        "Epic",
        attack_power=5,
        health=8,
        mana_pool=4,
    )

    print("EliteCard capabilities:")
    print("- Card:", ["play", "get_card_info", "is_playable"])
    print("- Combatable:", ["attack", "defend", "get_combat_stats"])
    print("- Magical:", ["cast_spell", "channel_mana", "get_magic_stats"])

    print("Playing Arcane Warrior (Elite Card):")

    print("Combat phase:")
    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(2))

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

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
