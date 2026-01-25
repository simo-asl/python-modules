def read_file_content(filename: str) -> str | None:
    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        return None

    content = f.read()
    f.close()
    return content


def main() -> None:
    filename = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")

    content = read_file_content(filename)
    if content is None:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...")
    print("RECOVERED DATA:")

    lines = content.splitlines()
    for line in lines:
        if line.strip() != "":
            print(line)

    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
