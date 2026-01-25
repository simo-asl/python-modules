def safe_read_lines(filename: str) -> list[str]:
    lines: list[str] = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.rstrip("\n")

                if line.strip() == "":
                    continue

                lines.append(line)

    except FileNotFoundError:
        return []

    return lines


def write_secure_note(filename: str, line: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    classified_file = "classified_vault.txt"
    out_file = "secure_protocols.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("SECURE EXTRACTION:")
    lines = safe_read_lines(classified_file)
    if lines:
        for line in lines:
            print(line)
    else:
        print("[CLASSIFIED] Quantum encryption keys recovered")
        print("[CLASSIFIED] Archive integrity: 100%")

    print("SECURE PRESERVATION:")
    write_secure_note(out_file, "[CLASSIFIED] New security protocols archived")
    print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
