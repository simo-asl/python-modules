from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 8, 10)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 6)

    print("Registering Tournament Cards...")
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"{dragon.name} registered with ID: {dragon_id}")
    print(f"{wizard.name} registered with ID: {wizard_id}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nLeaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card_stats in enumerate(leaderboard, 1):
        print(
            f"{i}. {card_stats['card_name']} - Rating: "
            f"{card_stats['current_rating']} "
            f"({card_stats['total_wins']}-{card_stats['total_losses']})"
        )

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
