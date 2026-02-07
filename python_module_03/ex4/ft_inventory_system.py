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

        new_qty = inventory.get(name, 0) + qty
        inventory.update({name: new_qty})

    return inventory


def total_quantity(inventory: dict[str, int]) -> int:
    total = 0
    for qty in inventory.values():
        total += qty
    return total


def most_least_abundant(
        inventory: dict[str, int]) -> tuple[str, int, str, int] | None:
    if not inventory:
        return None

    most_name = ""
    most_qty = -1

    least_name = ""
    least_qty = None

    for name, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_name = name

        if least_qty is None or qty < least_qty:
            least_qty = qty
            least_name = name

    return most_name, most_qty, least_name, least_qty


def unit_word(qty: int) -> str:
    return "unit" if qty == 1 else "units"


def categorize_subject(inventory: dict[str, int]) -> dict[str, dict[str, int]]:
    categories: dict[str, dict[str, int]] = {
        "abundant": {},
        "moderate": {},
        "scarce": {},
    }

    for name, qty in inventory.items():
        if qty <= 1:
            categories["scarce"].update({name: qty})
        elif qty <= 4:
            categories["moderate"].update({name: qty})
        else:
            categories["abundant"].update({name: qty})

    return categories


def restock_list(inventory: dict[str, int]) -> list[str]:
    out: list[str] = []
    for name, qty in inventory.items():
        if qty <= 1:
            out.append(name)
    return out


def print_inventory_desc(inventory: dict[str, int], total: int) -> None:
    printed: dict[str, int] = {}
    printed_count = 0

    while printed_count < len(inventory):
        best_name = ""
        best_qty = -1

        for name, qty in inventory.items():
            if name in printed:
                continue
            if qty > best_qty:
                best_qty = qty
                best_name = name

        printed.update({best_name: 1})
        printed_count += 1

        pct = (best_qty / total) * 100.0 if total > 0 else 0.0
        print(f"{best_name}: {best_qty} {unit_word(best_qty)} ({pct:.1f}%)")


def print_report(inventory: dict[str, int]) -> None:
    print("=== Inventory System Analysis ===")

    total = total_quantity(inventory)
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")
    if not inventory:
        print("(empty)")
    else:
        print_inventory_desc(inventory, total)

    print("\n=== Inventory Statistics ===")
    mm = most_least_abundant(inventory)
    if mm is None:
        print("Most abundant: (none)")
        print("Least abundant: (none)")
    else:
        most_name, most_qty, least_name, least_qty = mm
        print(f"Most abundant: {most_name} ({most_qty} units)")
        print(f"Least abundant: {least_name} "
              f"({least_qty} {unit_word(least_qty)})\n")

    print("=== Item Categories (Nested Dicts) ===")
    categories = categorize_subject(inventory)

    abundant = categories.get("abundant", {})
    moderate = categories.get("moderate", {})
    scarce = categories.get("scarce", {})

    print(f"Abundant: {abundant}")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}\n")

    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock_list(inventory)}\n")

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Dictionary items: {inventory.items()}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def ft_inventory_system() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 ft_inventory_system.py item:qty item:qty ...")
        print("Example: ", end="")
        print("python3 ft_inventory_system.py sword:1 potion:5 shield:2")
        return

    inventory = build_inventory(args)
    if inventory is None:
        print("Error: invalid token format. Expected item:qty "
              "with qty as a non-negative integer.")
        return

    print_report(inventory)


if __name__ == "__main__":
    """Python has no built-in main() like C/C++/Rust;
      this block runs only when the file is executed directly."""
    ft_inventory_system()
