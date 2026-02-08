def read_file_content(filename: str) -> str | None:
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        return None

    content = f.read()
    f.close()
    return content


def ft_ancient_text() -> None:
    filename = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")

    content = read_file_content(filename)
    if content is None:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...\n")
    print("RECOVERED DATA:")

    print(content)

    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    try:
        ft_ancient_text()
    except Exception as error:
        print(f"ERROR: {error}")
