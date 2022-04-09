import itertools

test_cases = int(input())

REVOLUTION = 360 * 12 * 10 ** 10
HOURS = 12
HOUR_TICKS = 30 * 12 * 10 ** 10
MIN_TICKS = HOUR_TICKS // 60
MIN = 360 / (12 * 60)

DEG = 12 * (10 ** 10)


def find_time(a, b, c):

    perm = list(itertools.permutations([a, b, c]))
    for p in perm:
        full_hours = p[0] * HOURS // REVOLUTION
        remaining_h = p[0] - full_hours * HOUR_TICKS

        full_mins = remaining_h * 60 // HOUR_TICKS
        remaining_m = remaining_h - full_mins * MIN_TICKS

        full_sec = remaining_m * 60 // MIN_TICKS

        if full_mins == p[1] * 60 // REVOLUTION and full_sec == p[2] * 60 // REVOLUTION:
            return full_hours, full_mins, full_sec, 0

        if full_mins == p[2] * 60 // REVOLUTION and full_sec == p[1] * 60 // REVOLUTION:
            return full_hours, full_mins, full_sec, 0

    return -1, -1, -1, -1


def find_time_reliable(a, b, c):
    for delta in range(36000):
        a = (a + delta * DEG//100) % REVOLUTION
        b = (b + delta * DEG//100) % REVOLUTION
        c = (c + delta * DEG//100) % REVOLUTION

        res = find_time(a, b, c)
        if res[0] != -1 and res[1] != -1 and res[2] != -1 and res[3] != -1:
            return res

    return -1, -1, -1, -1


for case in range(1, test_cases + 1):
    A, B, C = map(int, input().split())
    h, m, s, n = find_time_reliable(A, B, C)
    print(f"Case #{case}: {h} {m} {s} {n}")
