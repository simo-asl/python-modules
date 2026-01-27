from typing import Dict, List, Set


def make_sets(players: Dict[str, List[str]]) -> Dict[str, Set[str]]:
    res: Dict[str, Set[str]] = {}
    for name, achievements in players.items():
        res[name] = set(achievements)
    return res


def fmt_set_ordered(s: Set[str], order: List[str]) -> str:
    items = [f"'{x}'" for x in order if x in s]
    return "{" + ", ".join(items) + "}"


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

    order = [
        "first_kill", "level_10", "treasure_hunter",
        "speed_demon", "boss_slayer", "collector", "perfectionist"
    ]

    ps = make_sets(players)

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {fmt_set_ordered(ps['alice'], order)}")
    print(f"Player bob achievements: {fmt_set_ordered(ps['bob'], order)}")
    print(
        f"Player charlie achievements: {fmt_set_ordered(ps['charlie'], order)}"
        )

    print("\n=== Achievement Analytics ===")

    all_unique: Set[str] = set()
    for s in ps.values():
        all_unique |= s

    print(f"All unique achievements: {fmt_set_ordered(all_unique, order)}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    common = ps["alice"] & ps["bob"] & ps["charlie"]
    print(f"Common to all players: {fmt_set_ordered(common, order)}")

    counts: Dict[str, int] = {}
    for s in ps.values():
        for ach in s:
            counts[ach] = counts.get(ach, 0) + 1

    rare = {ach for ach, c in counts.items() if c == 1}
    print(f"Rare achievements (1 player): {fmt_set_ordered(rare, order)}")
    print()
    alice_bob_common = ps["alice"] & ps["bob"]
    print(f"Alice vs Bob common: {fmt_set_ordered(alice_bob_common, order)}")

    alice_unique = ps["alice"] - ps["bob"]
    bob_unique = ps["bob"] - ps["alice"]

    print(f"Alice unique: {fmt_set_ordered(alice_unique, order)}")
    print(f"Bob unique: {fmt_set_ordered(bob_unique, order)}")


if __name__ == "__main__":
    main()
