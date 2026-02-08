import sys


def ft_score_analytics() -> None:
    args = sys.argv[1:]
    print("=== Player Score Analytics ===")

    if not args:
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores: list[int] = []
    i = 0
    while i < len(args):
        try:
            n = int(args[i])
        except ValueError:
            print("Error: All scores must be valid integers.")
            print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
            return
        scores.append(n)
        i += 1

    print(f"Scores processed: {scores}")
    length = len(scores)
    print(f"Total players: {length}")

    total_sum = sum(scores)
    print(f"Total score: {total_sum}")
    average = total_sum / length
    print(f"Average score: {average:.1f}")

    maximum = max(scores)
    print(f"High score: {maximum}")
    minimum = min(scores)
    print(f"Low score: {minimum}")
    print(f"Score range: {maximum - minimum}")


if __name__ == "__main__":
    """Python has no built-in main() like C/C++/Rust;
      this block runs only when the file is executed directly."""
    try:
        ft_score_analytics()
    except Exception as error:
        print(f"ERROR: {error}")
