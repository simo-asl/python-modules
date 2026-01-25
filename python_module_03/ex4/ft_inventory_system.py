import sys


def parse_token(token: str) -> tuple[str, int] | None:
    if ":" not in token:
        return None
    name, qty_str = token.split(":", 1)
    name = name.strip()
    qty_str = qty_str.strip()

    if not name:
        return None

    try:
        qty = int(qty_str)
    except ValueError:
        return None

    if qty < 0:
        return None

    return name, qty


def build_inventory(args: list[str]) -> dict[str, int] | None:
    inventory: dict[str, int] = {}

    for tok in args:
        parsed = parse_token(tok)
        if parsed is None:
            return None
        name, qty = parsed
        inventory[name] = inventory.get(name, 0) + qty

    return inventory


def total_quantity(inventory: dict[str, int]) -> int:
    return sum(inventory.values())


def most_least_abundant(
        inventory: dict[str, int]) -> tuple[str, int, str, int] | None:
    if not inventory:
        return None

    most_name, most_qty = max(inventory.items(), key=lambda kv: kv[1])
    least_name, least_qty = min(inventory.items(), key=lambda kv: kv[1])
    return most_name, most_qty, least_name, least_qty


def categorize(inventory: dict[str, int]) -> dict[str, dict[str, int]]:
    cats: dict[str, dict[str, int]] = {
        "abundant": {}, "moderate": {}, "scarce": {}}

    for name, qty in inventory.items():
        if qty >= 4:
            cats["abundant"][name] = qty
        elif qty >= 2:
            cats["moderate"][name] = qty
        else:
            cats["scarce"][name] = qty

    return cats


def restock_list(inventory: dict[str, int]) -> list[str]:
    return [name for name, qty in inventory.items() if qty <= 1]


def print_report(inventory: dict[str, int]) -> None:
    print("=== Inventory System Analysis ===")

    total = total_quantity(inventory)
    print(f"Total items in inventory: {total}")
    print(f"Unique items: {len(inventory)}")

    print("=== Current Inventory ===")
    if not inventory:
        print("(empty)")
    else:
        sorted_items = sorted(
            inventory.items(), key=lambda kv: kv[1], reverse=True)
        for name, qty in sorted_items:
            pct = (qty / total) * 100.0 if total > 0 else 0.0
            print(f"{name}: {qty} units ({pct:.1f}%)")

    print("=== Inventory Statistics ===")
    mm = most_least_abundant(inventory)
    if mm is None:
        print("Most abundant: (none)")
        print("Least abundant: (none)")
    else:
        most_name, most_qty, least_name, least_qty = mm
        print(f"Most abundant: {most_name} ({most_qty} units)")
        print(f"Least abundant: {least_name} ({least_qty} units)")

    print("=== Item Categories ===")
    cats = categorize(inventory)
    print(f"abundant: {cats['abundant']}")
    print(f"moderate: {cats['moderate']}")
    print(f"scarce: {cats['scarce']}")

    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock_list(inventory)}")

    print("=== Dictionary Properties Demo ===")
    # keys(), values(), items(), get(), update() demo
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Dictionary items sample: {list(inventory.items())[:3]}")
    print(f"Sample lookup - 'sword' in inventory: {inventory.get('sword', 0)}")

    demo_update: dict[str, int] = {}
    demo_update.update(inventory)
    print(f"Update demo (copied dict size): {len(demo_update)}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 ft_inventory_system.py item:qty item:qty ...")
        print(
            "Example: python3 ft_inventory_system.py sword:1 potion:5 shield:2"
            )
        return

    inventory = build_inventory(args)
    if inventory is None:
        print(
            "Error: invalid token format. Expected item:qty "
            "with qty as a non-negative integer."
        )
        return

    print_report(inventory)


if __name__ == "__main__":
    main()
