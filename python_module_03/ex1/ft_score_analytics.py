import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    print("=== Player Score Analytics ===")

    if args:
        try:
            scores = [int(x) for x in args]
        except ValueError:
            print("Error: All scores must be valid integers.")
            print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
            sys.exit(1)
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
        score_range = maximum - minimum
        print(f"Score range: {score_range}")
    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ...")
