from typing import Dict, List, Set


def ft_achievement_tracker() -> None:
    players: Dict[str, List[str]] = {
        "alice": [
            "first_kill", "level_10", "treasure_hunter",
            "speed_demon", "first_kill"
        ],
        "bob": [
            "first_kill", "level_10", "boss_slayer",
            "collector", "collector"
        ],
        "charlie": [
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist", "perfectionist"
        ],
    }

    try:
        alice_list = players["alice"]
    except KeyError:
        alice_list = []

    try:
        bob_list = players["bob"]
    except KeyError:
        bob_list = []

    try:
        charlie_list = players["charlie"]
    except KeyError:
        charlie_list = []

    alice_set = set(alice_list)
    bob_set = set(bob_list)
    charlie_set = set(charlie_list)

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice_set}")
    print(f"Player bob achievements: {bob_set}")
    print(f"Player charlie achievements: {charlie_set}")

    print("\n=== Achievement Analytics ===")

    all_unique: Set[str] = alice_set.union(bob_set, charlie_set)

    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    common = bob_set & alice_set & charlie_set
    print(f"Common to all players: {common}")

    rare = (
        alice_set.difference(charlie_set, bob_set)
        | charlie_set.difference(alice_set, bob_set)
        | bob_set.difference(alice_set, charlie_set)
    )
    print(f"Rare achievements (1 player): {rare}")
    print()

    alice_bob_common = alice_set & bob_set
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice_set - bob_set
    bob_unique = bob_set - alice_set

    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    """Python has no built-in main() like C/C++/Rust;
      this block runs only when the file is executed directly."""
    try:
        ft_achievement_tracker()
    except Exception as error:
        print(f"ERROR: {error}")
