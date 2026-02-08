def write_archive(filename: str, entries: list[str]) -> None:
    f = open(filename, "w", encoding="utf-8")
    for line in entries:
        f.write(line + "\n")
    f.close()


def ft_archive_creation() -> None:
    filename = "new_discovery.txt"
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")

    for line in entries:
        print(line)

    write_archive(filename, entries)

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    try:
        ft_archive_creation()
    except Exception as error:
        print(f"ERROR: {error}")
