import sys

input = sys.stdin.readline

UNKNOWN = 100
LOWER = -99
UPPER = 99


def main() -> None:
    n = int(input())
    pyramid = [list(map(int, input().split())) for _ in range(n)]

    changed = True
    while changed:
        changed = False

        for r in range(n):
            for c in range(r + 1):
                if pyramid[r][c] != UNKNOWN:
                    continue

                candidates = []

                if r + 1 < n:
                    left = pyramid[r + 1][c]
                    right = pyramid[r + 1][c + 1]
                    if left != UNKNOWN and right != UNKNOWN:
                        candidates.append(left + right)

                if r > 0 and c > 0:
                    parent = pyramid[r - 1][c - 1]
                    sibling = pyramid[r][c - 1]
                    if parent != UNKNOWN and sibling != UNKNOWN:
                        candidates.append(parent - sibling)

                if r > 0 and c < r:
                    parent = pyramid[r - 1][c]
                    sibling = pyramid[r][c + 1]
                    if parent != UNKNOWN and sibling != UNKNOWN:
                        candidates.append(parent - sibling)

                if not candidates:
                    continue

                first = candidates[0]
                for value in candidates[1:]:
                    if value != first:
                        print("no solution")
                        return

                if first < LOWER or first > UPPER:
                    print("no solution")
                    return

                pyramid[r][c] = first
                changed = True

    for r in range(n - 1):
        for c in range(r + 1):
            parent = pyramid[r][c]
            left = pyramid[r + 1][c]
            right = pyramid[r + 1][c + 1]
            if parent != UNKNOWN and left != UNKNOWN and right != UNKNOWN:
                if parent != left + right:
                    print("no solution")
                    return

    if any(UNKNOWN in row for row in pyramid):
        print("ambiguous")
        return

    print("solvable")
    for row in pyramid:
        print(*row)


if __name__ == "__main__":
    main()
