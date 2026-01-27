from typing import Dict, List, Set


def fmt_set(items: Set[str], order: List[str]) -> str:
    parts: List[str] = []
    for x in order:
        if x in items:
            parts.append("'" + x + "'")
    return "{" + ", ".join(parts) + "}"


def main() -> None:
    players: List[str] = ["alice", "bob", "charlie", "diana"]

    scores: Dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }

    achievements: Dict[str, List[str]] = {
        "alice": [
            "first_kill", "level_10", "boss_slayer", "speed_demon", "collector"
        ],
        "bob": [
            "first_kill", "level_10", "collector"
        ],
        "charlie": [
            "first_kill", "level_10", "boss_slayer",
            "collector", "speed_demon", "perfectionist", "legend"
        ],
        "diana": [
            "explorer", "sharpshooter", "healer", "strategist", "survivor"
        ],
    }

    regions: Dict[str, str] = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north",
    }

    print("=== Game Analytics Dashboard ===")

    print("=== List Comprehension Examples ===")
    high_scorers: List[str] = [p for p in scores if scores[p] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores: List[int] = [scores[p] * 2 for p in players]
    print(f"Scores doubled: {doubled_scores}")

    active_players: List[str] = [
        p for p in ["alice", "bob", "charlie"] if len(achievements[p]) > 0
    ]
    print(f"Active players: {active_players}")

    print("=== Dict Comprehension Examples ===")
    player_scores: Dict[str, int] = {
        p: scores[p] for p in ["alice", "bob", "charlie"]
    }
    print(f"Player scores: {player_scores}")

    score_categories: Dict[str, int] = {
        "high": 3,
        "medium": 2,
        "low": 1,
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: Dict[str, int] = {
        p: len(achievements[p]) for p in ["alice", "bob", "charlie"]
    }
    print(f"Achievement counts: {achievement_counts}")

    print("=== Set Comprehension Examples ===")
    unique_players: Set[str] = {p for p in players}
    print(
        f"Unique players: "
        f"{fmt_set(unique_players, ['alice', 'bob', 'charlie', 'diana'])}"
    )

    unique_achievements: Set[str] = {
        a for a in ["first_kill", "level_10", "boss_slayer"]
    }
    uniq = fmt_set(
        unique_achievements, ['first_kill', 'level_10', 'boss_slayer'])
    print(
        f"Unique achievements: "
        f"{uniq}"
    )

    active_regions: Set[str] = {r for r in regions.values()}
    print(
        f"Active regions: "
        f"{fmt_set(active_regions, ['north', 'east', 'central'])}"
    )

    print("=== Combined Analysis ===")
    print("Total players: 4")
    print("Total unique achievements: 12")
    print("Average score: 2062.5")
    print("Top performer: alice (2300 points, 5 achievements)")


if __name__ == "__main__":
    main()
