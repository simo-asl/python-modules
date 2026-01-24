from typing import Dict, List, Set, Tuple


def make_sets(players: Dict[str, List[str]]) -> Dict[str, Set[str]]:
    res: Dict[str, Set[str]] = {}
    for name, lst in players.items():
        res[name] = set(lst)
    return res


def union_all(player_sets: Dict[str, Set[str]]) -> Set[str]:
    all_ach: Set[str] = set()
    for s in player_sets.values():
        all_ach = all_ach | s
    return all_ach


def intersection_all(player_sets: Dict[str, Set[str]]) -> Set[str]:
    names: List[str] = list(player_sets.keys())
    if len(names) == 0:
        return set()
    common: Set[str] = player_sets[names[0]].copy()
    for i in range(1, len(names)):
        common = common & player_sets[names[i]]
    return common


def unique_each(player_sets: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    names: List[str] = list(player_sets.keys())
    res: Dict[str, Set[str]] = {}

    for name in names:
        others: Set[str] = set()
        for other in names:
            if other != name:
                others = others | player_sets[other]
        res[name] = player_sets[name] - others

    return res


def rare(player_sets: Dict[str, Set[str]], owners: int = 1) -> Set[str]:
    counts: Dict[str, int] = {}

    for s in player_sets.values():
        for ach in s:
            counts[ach] = counts.get(ach, 0) + 1

    out: Set[str] = set()
    for ach, c in counts.items():
        if c <= owners:
            out.add(ach)

    return out


def communities(
        player_sets: Dict[str, Set[str]]) -> List[Tuple[str, str, Set[str]]]:
    names: List[str] = list(player_sets.keys())
    links: List[Tuple[str, str, Set[str]]] = []

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a: str = names[i]
            b: str = names[j]
            shared: Set[str] = player_sets[a] & player_sets[b]
            if len(shared) > 0:
                links.append((a, b, shared))

    return links


def main() -> None:
    players: Dict[str, List[str]] = {
        "Alice": [
            "first_kill", "level_10", "treasure_hunter",
            "speed_demon", "first_kill"],
        "Bob": [
            "first_kill", "level_10", "boss_slayer", "collector", "collector"],
        "Charlie": [
            "level_10", "treasure_hunter", "boss_slayer", "speed_demon",
            "perfectionist", "perfectionist"],
    }

    ps: Dict[str, Set[str]] = make_sets(players)

    print("All unique:", union_all(ps))
    print("Common to all:", intersection_all(ps))
    print("Rare (1 owner):", rare(ps, 1))
    print("Unique per player:", unique_each(ps))

    print("Communities:")
    for a, b, shared in communities(ps):
        print(f"- {a} & {b}: {shared}")

    print("\nSet ops:")
    print("A | B = union")
    print("A & B = intersection")
    print("A - B = difference")


if __name__ == "__main__":
    main()
