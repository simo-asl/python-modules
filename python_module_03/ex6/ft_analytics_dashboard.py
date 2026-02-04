def format_set(values: set[str]) -> str:
    items = [f"'{x}'" for x in sorted(values)]
    return "{" + ", ".join(items) + "}"


def machi_main() -> None:
    players: list[str] = [
        "alice",
        "bob",
        "charlie",
        "diana",
    ]

    scores: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050,
    }

    achievements: dict[str, list[str]] = {
        "alice": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "speed_demon",
            "collector",
        ],
        "bob": [
            "first_kill",
            "level_10",
            "collector",
        ],
        "charlie": [
            "first_kill",
            "level_10",
            "boss_slayer",
            "collector",
            "speed_demon",
            "perfectionist",
            "legend",
        ],
        "diana": [
            "explorer",
            "sharpshooter",
            "healer",
            "strategist",
            "survivor",
        ],
    }

    regions: dict[str, str] = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north",
    }

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    high_scorers: list[str] = [
        player
        for player, score in scores.items()
        if score > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores: list[int] = [
        scores[player] * 2
        for player in players
    ]
    print(f"Scores doubled: {doubled_scores}")

    active_players: list[str] = [
        player
        for player in players
        if len(achievements[player]) > 0
    ]
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")
    selected_players: list[str] = [
        "alice",
        "bob",
        "charlie",
    ]
    player_scores: dict[str, int] = {
        player: scores[player]
        for player in selected_players
    }
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        "high": len([
            player
            for player, score in scores.items()
            if score >= 2200
        ]),
        "medium": len([
            player
            for player, score in scores.items()
            if 2000 <= score < 2200
        ]),
        "low": len([
            player
            for player, score in scores.items()
            if score < 2000
        ]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {
        player: len(achievements[player])
        for player in selected_players
    }
    print(f"Achievement counts: {achievement_counts}\n")

    print("=== Set Comprehension Examples ===")
    unique_players: set[str] = {
        player
        for player in players
    }
    print(f"Unique players: {format_set(unique_players)}")

    unique_achievements: set[str] = {
        achievement
        for achievement in [
            "first_kill",
            "level_10",
            "boss_slayer",
        ]
    }
    print(f"Unique achievements: {format_set(unique_achievements)}")

    active_regions: set[str] = {
        region
        for region in regions.values()
    }
    print(f"Active regions: {format_set(active_regions)}\n")

    print("=== Combined Analysis ===")
    total_players: int = len(players)

    all_achievements: set[str] = {
        achievement
        for achievement_list in achievements.values()
        for achievement in achievement_list
    }
    total_unique_achievements: int = len(all_achievements)

    average_score: float = sum(scores.values()) / len(scores)

    top_player: str = max(scores, key=lambda player: scores[player])
    top_score: int = scores[top_player]
    top_achievements: int = len(achievements[top_player])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_player} ({top_score} points, "
        f"{top_achievements} achievements)"
    )


if __name__ == "__main__":
    machi_main()
