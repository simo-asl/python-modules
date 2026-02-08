import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    print(
        f"[STANDARD] Archive status from {archivist_id}: {status}",
        file=sys.stdout,
    )
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr,
    )
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("Three-channel communication test successful.", file=sys.stdout)


if __name__ == "__main__":
    try:
        ft_stream_management()
    except Exception as error:
        print(f"ERROR: {error}")
