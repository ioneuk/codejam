test_cases = int(input())


def get_max_possible_cost_for_n(n):
    return sum(range(2, n + 1))


def _memoization(func):
    def _func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    cache = {}
    return _func


def get_list_recursively(n, c):
    if n == 2 and c == 1:
        return [1, 2]
    elif n == 2 and c == 2:
        return [2, 1]
    else:
        position = -1
        max_cost_1 = get_max_possible_cost_for_n(n - 1)
        array = [0] * n
        for j in range(n - 1, -1, -1):
            new_cost = c - j - 1
            if n - 2 <= new_cost <= max_cost_1:
                position = j
                break

        array[position] = 1
        # Fill everything in range [position; end)
        if position < n - 1:
            array[position + 1:] = list(range(position + 2, n + 1))

        if position > 0:
            skipped_positions = n - 1 - position
            left_arr = list(reversed(get_list_recursively(position, c - position - skipped_positions - 1)))
            left_arr = [x + 1 for x in left_arr]
            array[:position] = left_arr
        return array


get_list_recursively = _memoization(get_list_recursively)

for case in range(1, test_cases + 1):
    n, cost = map(int, input().split())

    max_cost_n_1 = get_max_possible_cost_for_n(n - 1)
    max_cost = n + max_cost_n_1

    if cost < n - 1 or cost > max_cost:
        print(f"Case #{case}: IMPOSSIBLE")
        continue

    array = get_list_recursively(n, cost)
    array_str = " ".join(map(str, array))
    print(f"Case #{case}: {array_str}")
