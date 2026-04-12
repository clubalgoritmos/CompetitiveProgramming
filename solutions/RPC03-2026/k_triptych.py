def count_spotlight_sequences(w, d):
    from collections import defaultdict

    def evolve(length):
        dp = {(0, 0, 0, 0): 1}

        for _ in range(length):
            next_dp = defaultdict(int)
            for (ab, bc, last, run_b), ways in dp.items():
                if last != 1:
                    next_dp[(ab + 1, bc, 1, 0)] += ways

                if run_b < 2:
                    next_dp[(ab - 1, bc + 1, 2, run_b + 1 if last == 2 else 1)] += ways

                if last != 3:
                    next_dp[(ab, bc - 1, 3, 0)] += ways

            dp = next_dp

        return dp

    def balanced(ab, bc):
        return abs(ab) <= d and abs(bc) <= d and abs(ab + bc) <= d

    full_dp = evolve(w)
    total = 0
    for (ab, bc, _, _), ways in full_dp.items():
        if balanced(ab, bc):
            total += ways

    half = w // 2
    half_dp = evolve(half)
    pal = 0

    if w % 2 == 0:
        for (ab, bc, last, run_b), ways in half_dp.items():
            if last == 2 and run_b == 1 and balanced(2 * ab, 2 * bc):
                pal += ways
    else:
        centers = (
            (
                1,
                lambda ab, bc: abs(2 * ab + 1) <= d
                and abs(2 * bc) <= d
                and abs(2 * (ab + bc) + 1) <= d,
            ),
            (
                2,
                lambda ab, bc: abs(2 * ab - 1) <= d
                and abs(2 * bc + 1) <= d
                and abs(2 * (ab + bc)) <= d,
            ),
            (
                3,
                lambda ab, bc: abs(2 * ab) <= d
                and abs(2 * bc - 1) <= d
                and abs(2 * (ab + bc) - 1) <= d,
            ),
        )

        for (ab, bc, last, _), ways in half_dp.items():
            for center, ok in centers:
                if last != center and ok(ab, bc):
                    pal += ways

    return total - pal


w, d = map(int, input().split())
print(count_spotlight_sequences(w, d))
