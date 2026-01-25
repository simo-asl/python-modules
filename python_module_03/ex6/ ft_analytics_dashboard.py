import sys


def parse_event(token: str) -> tuple[str, int, int] | None:
    parts = token.split(":")
    if len(parts) != 3:
        return None

    player = parts[0].strip()
    if player == "":
        return None

    try:
        score = int(parts[1].strip())
        damage = int(parts[2].strip())
    except ValueError:
        return None

    if score < 0 or damage < 0:
        return None

    return player, score, damage


def read_events(args: list[str]) -> list[tuple[str, int, int]] | None:
    events: list[tuple[str, int, int]] = []

    for tok in args:
        ev = parse_event(tok)
        if ev is None:
            return None
        events.append(ev)

    return events


def get_players(events: list[tuple[str, int, int]]) -> set[str]:
    return {player for player, _, _ in events}


def get_total_events(events: list[tuple[str, int, int]]) -> int:
    return len(events)


def get_total_score(events: list[tuple[str, int, int]]) -> int:
    scores = [score for _, score, _ in events]
    return sum(scores)


def get_total_damage(events: list[tuple[str, int, int]]) -> int:
    damages = [damage for _, _, damage in events]
    return sum(damages)


def score_by_player(
        events: list[tuple[str, int, int]],
        players: set[str]) -> dict[str, int]:
    return {
        p: sum(score for player, score, _ in events if player == p)
        for p in players
    }


def damage_by_player(
        events: list[tuple[str, int, int]],
        players: set[str]) -> dict[str, int]:
    return {
        p: sum(dmg for player, _, dmg in events if player == p)
        for p in players
    }


def count_by_player(
        events: list[tuple[str, int, int]],
        players: set[str]) -> dict[str, int]:
    return {
        p: sum(1 for player, _, _ in events if player == p)
        for p in players
    }


def average_score_by_player(
    totals: dict[str, int],
    counts: dict[str, int],
    players: set[str]
) -> dict[str, float]:
    return {
        p: (totals[p] / counts[p]) for p in players if counts[p] > 0
    }


def high_score_events(
        events: list[tuple[str, int, int]],
        threshold: int) -> list[tuple[str, int, int]]:
    result: list[tuple[str, int, int]] = []

    for event in events:
        player = event[0]
        score = event[1]
        damage = event[2]

        if score >= threshold:
            result.append((player, score, damage))

    return result


def leaderboard(
    players: set[str],
    scores: dict[str, int],
    damages: dict[str, int]
) -> list[tuple[str, int, int]]:
    rows = [(p, scores[p], damages[p]) for p in players]
    return sorted(rows, key=lambda x: x[1], reverse=True)


def print_summary(events: list[tuple[str, int, int]]) -> None:
    players = get_players(events)

    total_events = get_total_events(events)
    total_score = get_total_score(events)
    total_damage = get_total_damage(events)

    avg_score = (total_score / total_events) if total_events > 0 else 0.0
    avg_damage = (total_damage / total_events) if total_events > 0 else 0.0

    scores = score_by_player(events, players)
    damages = damage_by_player(events, players)
    counts = count_by_player(events, players)
    avg_scores = average_score_by_player(scores, counts, players)

    hi_events = high_score_events(events, 50)
    hi_players = {p for p, _, _ in hi_events}

    board = leaderboard(players, scores, damages)

    print("=== Analytics Dashboard ===")
    print("Total events:", total_events)
    print("Unique players:", len(players))
    print("Total score:", total_score)
    print("Total damage:", total_damage)
    print(f"Average score/event: {avg_score:.2f}")
    print(f"Average damage/event: {avg_damage:.2f}")
    print()

    print("=== Players (set comprehension) ===")
    print("Players:", sorted(players))
    print("High scorers (score>=50):", sorted(hi_players))
    print()

    print("=== Per-player totals (dict comprehensions) ===")
    for p in sorted(players):
        print(
            f"{p}: events={counts[p]}, score={scores[p]}, "
            f"damage={damages[p]}, avg_score={avg_scores.get(p, 0.0):.2f}"
        )
    print()

    print("=== Leaderboard (list comprehension + sorted) ===")
    for rank, (p, sc, dmg) in enumerate(board, start=1):
        print(f"{rank}. {p} | score={sc} | damage={dmg}")
    print()

    print("=== High score events (list comprehension) ===")
    if not hi_events:
        print("(none)")
    else:
        for p, sc, dmg in hi_events:
            print(f"{p}: score={sc}, damage={dmg}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage:  ")
        print("python3 ft_analytics_dashboard.py player:score:damage ...")
        print("Example:  ")
        print(
            "python3 ft_analytics_dashboard.py simo:60:3 sara:20:7 simo:10:1")
        return

    events = read_events(args)
    if events is None:
        print("Error: invalid token. Expected player:score:damage (ints >= 0)")
        return

    print_summary(events)


if __name__ == "__main__":
    main()
