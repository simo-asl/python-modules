from ex2.EliteCard import EliteCard


def main() -> None:
    try:
        print("\n=== DataDeck Ability System ===\n")

        elite = EliteCard(
            "Arcane Warrior",
            4,
            "Epic",
            attack_power=5,
            health=8,
            mana_pool=4
        )

        print("EliteCard capabilities:")
        print("- Card:", ["play", "get_card_info", "is_playable"])
        print("- Combatable:", ["attack", "defend", "get_combat_stats"])
        print("- Magical:", ["cast_spell", "channel_mana", "get_magic_stats"])
        print()
        print("Playing Arcane Warrior (Elite Card):")
        elite.play({})

        print("Combat phase:")
        print("Attack result:", elite.attack("Enemy"))
        print("Defense result:", elite.defend(2))
        print()
        print("Magic phase:")
        print("Spell cast:",
              elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
        print("Mana channel:", elite.channel_mana(3))
        print()
        print("Multiple interface implementation successful!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
