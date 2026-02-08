
def crisis_handler(filename: str, routine: bool) -> None:
    if routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()

        if content == "":
            content = "Empty archive"

        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        if routine:
            print("STATUS: Normal operations resumed")
        else:
            print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        if routine:
            print("STATUS: Normal operations resumed")
        else:
            print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        if routine:
            print("STATUS: Normal operations resumed")
        else:
            print("STATUS: Crisis handled, system stable")


def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    crisis_handler("lost_archive.txt", routine=False)
    crisis_handler("classified_vault.txt", routine=False)
    crisis_handler("standard_archive.txt", routine=True)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    try:
        ft_crisis_response()
    except Exception as error:
        print(f"ERROR: {error}")
