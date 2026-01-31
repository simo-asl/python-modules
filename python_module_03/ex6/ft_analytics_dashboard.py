def format_set(values: set[str]) -> str:
    items = [f"'{x}'" for x in sorted(values)]
    return "{" + ", ".join(items) + "}"


def main() -> None:
    players: list[str] = ["alice", "bob", "charlie", "diana"]

    scores: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }

    achievements: dict[str, list[str]] = {
        "alice": ["first_kill", "level_10", "boss_slayer", "speed_demon", "collector"],
        "bob": ["first_kill", "level_10", "collector"],
        "charlie": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "collector",
            "speed_demon",
            "perfectionist",
            "legend",
        ],
        "diana": ["explorer", "sharpshooter", "healer", "strategist", "survivor"],
    }

    regions: dict[str, str] = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north",
    }

    print("=== Game Analytics Dashboard ===")

    print("=== List Comprehension Examples ===")
    high_scorers: list[str] = [p for p, s in scores.items() if s > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores: list[int] = [scores[p] * 2 for p in players]
    print(f"Scores doubled: {doubled_scores}")

    active_players: list[str] = [p for p in players if len(achievements[p]) > 0]
    print(f"Active players: {active_players}")

    print("=== Dict Comprehension Examples ===")
    player_scores: dict[str, int] = {p: scores[p] for p in ["alice", "bob", "charlie"]}
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        "high": len([p for p, s in scores.items() if s >= 2200]),
        "medium": len([p for p, s in scores.items() if 2000 <= s < 2200]),
        "low": len([p for p, s in scores.items() if s < 2000]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {p: len(achievements[p]) for p in ["alice", "bob", "charlie"]}
    print(f"Achievement counts: {achievement_counts}")

    print("=== Set Comprehension Examples ===")
    unique_players: set[str] = {p for p in players}
    print(f"Unique players: {format_set(unique_players)}")

    unique_achievements: set[str] = {a for a in ["first_kill", "level_10", "boss_slayer"]}
    print(f"Unique achievements: {format_set(unique_achievements)}")

    active_regions: set[str] = {r for r in regions.values()}
    print(f"Active regions: {format_set(active_regions)}")

    print("=== Combined Analysis ===")
    total_players: int = len(players)
    all_achievements: set[str] = {a for lst in achievements.values() for a in lst}
    total_unique_achievements: int = len(all_achievements)
    average_score: float = sum(scores.values()) / len(scores)

    top_player: str = max(scores, key=lambda p: scores[p])
    top_score: int = scores[top_player]
    top_achievements: int = len(achievements[top_player])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_player} ({top_score} points, {top_achievements} achievements)")


if __name__ == "__main__":
    main()
