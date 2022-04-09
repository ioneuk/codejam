test_cases = int(input())

TOTAL = 1000000


def solve(cyan, magenta, yellow, black):
    min_c = min(cyan)
    min_m = min(magenta)
    min_y = min(yellow)
    min_b = min(black)

    total_sum = min_c + min_m + min_y + min_b
    if total_sum < TOTAL:
        return None, None, None, None
    elif total_sum == TOTAL:
        return min_c, min_m, min_y, min_b
    else:
        remaining = TOTAL
        res_m = 0
        res_y = 0
        res_b = 0
        res_c = min_c
        remaining -= res_c
        if remaining == 0:
            return res_c, res_m, res_y, res_b

        res_m = min(remaining, min_m)
        remaining -= res_m
        if remaining == 0:
            return res_c, res_m, res_y, res_b

        res_y = min(remaining, min_y)
        remaining -= res_y
        if remaining == 0:
            return res_c, res_m, res_y, res_b

        res_b = min(remaining, min_b)
        remaining -= res_b
        if remaining == 0:
            return res_c, res_m, res_y, res_b

        return None, None, None, None


for case in range(1, test_cases + 1):
    cyan = []
    magenta = []
    yellow = []
    black = []
    for _ in range(3):
        c, m, y, k = list(map(int, input().split()))
        cyan.append(c)
        magenta.append(m)
        yellow.append(y)
        black.append(k)

    c_res, m_res, y_res, k_res = solve(cyan, magenta, yellow, black)
    if c_res is None:
        print(f"Case #{case}: IMPOSSIBLE")
    else:
        print(f"Case #{case}: {c_res} {m_res} {y_res} {k_res}")
