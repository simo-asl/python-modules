import sys


def parse_token(token: str) -> tuple[str, int] | None:
    if ":" not in token:
        return None
    name, qty_str = token.split(":", 1)
    name = name.strip()
    qty_str = qty_str.strip()
    if name == "":
        return None
    try:
        qty = int(qty_str)
    except ValueError:
        return None
    if qty < 0:
        return None
    return (name, qty)


def item_meta(name: str) -> dict[str, str | int]:
    meta_map: dict[str, dict[str, str | int]] = {
        "potion": {"type": "consumable", "value": 10},
        "sword": {"type": "weapon", "value": 120},
        "shield": {"type": "armor", "value": 90},
        "armor": {"type": "armor", "value": 200},
        "helmet": {"type": "armor", "value": 60},
    }
    base = meta_map.get(name, {"type": "misc", "value": 0})
    return {"name": name, "type": str(base["type"]), "value": int(base["value"])}


def build_inventory(argv: list[str]) -> dict[str, dict[str, str | int]]:
    inv: dict[str, dict[str, str | int]] = {}

    for tok in argv:
        parsed = parse_token(tok)
        if parsed is None:
            print(f"Skipping invalid token: {tok}")
            continue

        name, qty = parsed

        current = inv.get(name)
        if current is None:
            meta = item_meta(name)
            inv[name] = {}
            inv[name].update(meta)
            inv[name].update({"quantity": qty})
        else:
            current_qty = int(current.get("quantity", 0))
            current.update({"quantity": current_qty + qty})

    return inv


def total_quantity(inv: dict[str, dict[str, str | int]]) -> int:
    total = 0
    for _, info in inv.items():
        total += int(info.get("quantity", 0))
    return total


def unique_types(inv: dict[str, dict[str, str | int]]) -> int:
    types: set[str] = set()
    for _, info in inv.items():
        types.add(str(info.get("type", "misc")))
    return len(types)


def most_least_abundant(inv: dict[str, dict[str, str | int]]) -> tuple[str, int, str, int] | None:
    if len(inv) == 0:
        return None

    most_name = ""
    most_qty = -1
    least_name = ""
    least_qty = 10**18

    for name, info in inv.items():
        q = int(info.get("quantity", 0))
        if q > most_qty:
            most_qty = q
            most_name = name
        if q < least_qty:
            least_qty = q
            least_name = name

    return (most_name, most_qty, least_name, least_qty)


def categorize(inv: dict[str, dict[str, str | int]]) -> dict[str, dict[str, int]]:
    cats: dict[str, dict[str, int]] = {"Abundant": {}, "Moderate": {}, "Scarce": {}}

    for name, info in inv.items():
        q = int(info.get("quantity", 0))
        if q >= 8:
            cats["Abundant"][name] = q
        elif q >= 4:
            cats["Moderate"][name] = q
        else:
            cats["Scarce"][name] = q

    return cats


def restock_list(inv: dict[str, dict[str, str | int]]) -> list[str]:
    out: list[str] = []
    for name, info in inv.items():
        if int(info.get("quantity", 0)) <= 1:
            out.append(name)
    return out


def print_report(inv: dict[str, dict[str, str | int]]) -> None:
    print("=== Inventory System Analysis ===")

    total = total_quantity(inv)
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {unique_types(inv)}")

    print("=== Current Inventory ===")
    if total == 0 or len(inv) == 0:
        print("(empty)")
    else:
        sorted_items = sorted(inv.items(), key=lambda kv: int(kv[1].get("quantity", 0)), reverse=True)
        for name, info in sorted_items:
            q = int(info.get("quantity", 0))
            pct = (q / total) * 100.0 if total > 0 else 0.0
            print(f"{name}: {q} units ({pct:.1f}%)")

    print("=== Inventory Statistics ===")
    mm = most_least_abundant(inv)
    if mm is None:
        print("Most abundant: (none)")
        print("Least abundant: (none)")
    else:
        most_name, most_qty, least_name, least_qty = mm
        print(f"Most abundant: {most_name} ({most_qty} units)")
        print(f"Least abundant: {least_name} ({least_qty} units)")

    print("=== Item Categories ===")
    cats = categorize(inv)
    print(f"Abundant: {cats['Abundant']}")
    print(f"Moderate: {cats['Moderate']}")
    print(f"Scarce: {cats['Scarce']}")

    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock_list(inv)}")

    print("=== Dictionary Properties Demo ===")
    qty_dict: dict[str, int] = {}
    for name, info in inv.items():
        qty_dict[name] = int(info.get("quantity", 0))

    print(f"Dictionary keys: {list(qty_dict.keys())}")
    print(f"Dictionary values: {list(qty_dict.values())}")
    print(f"Dictionary items sample: {list(qty_dict.items())[:3]}")
    print(f"Sample lookup - 'sword' in inventory: {qty_dict.get('sword', 0) > 0}")


def main() -> None:
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python3 ft_inventory_system.py item:qty item:qty ...")
        print("Example: python3 ft_inventory_system.py sword:1 potion:5 shield:2")
        return

    inv = build_inventory(args)
    print_report(inv)


if __name__ == "__main__":
    main()
