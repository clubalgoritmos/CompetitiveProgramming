import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    c = data[0]
    votes = data[1 : 1 + c]

    total_votes = sum(votes)
    majority = total_votes // 2 + 1

    ordered = sorted(votes, reverse=True)
    second_votes = ordered[1]

    # If the second-place candidate already has a majority in round 1,
    # the first-place candidate also has a majority and wins immediately.
    if second_votes >= majority:
        print("IMPOSSIBLE TO WIN")
        return

    other_candidates = sorted(ordered[2:])

    rounds = 0
    current = second_votes
    for v in other_candidates:
        current += v
        rounds += 1
        if current >= majority:
            print(rounds)
            return

    print("IMPOSSIBLE TO WIN")


if __name__ == "__main__":
    main()
