from typing import Dict, List, Set


def main() -> None:
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

    alice_set = set(players.get("alice", {}))
    bob_set = set(players.get("bob", {}))
    charlie_set = set(players.get("charlie", {}))

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

    rare = (alice_set.difference(charlie_set, bob_set)
            | charlie_set.difference(alice_set, bob_set)
            | bob_set.difference(alice_set, charlie_set))
    print(f"Rare achievements (1 player): {rare}")
    print()
    alice_bob_common = alice_set & bob_set
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice_set - bob_set
    bob_unique = bob_set - alice_set

    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
