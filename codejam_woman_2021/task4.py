from typing import Callable

import numpy as np

# test_cases = int(input())


def _memoization(func: Callable):
    def _func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    cache = {}
    return _func


def serialize(arr):
    return np.array2string(arr, separator='')[1:-1]


def invert(arr):
    return np.logical_not(arr).astype(int)


def calculate_winner_score(setting):
    if len(setting) == 0:
        return -1
    if setting[0] != "1" and setting[-1] != "1":
        return -(len(setting) + 1)

    if setting[0] == "1" and setting[-1] == "1":
        first_setting = np.fromstring(setting[1:], 'u1') - ord('0')
        second_setting = np.fromstring(setting[:-1], 'u1') - ord('0')

        return max(-1 * calculate_winner_score(serialize(invert(first_setting))),
                   -1 * calculate_winner_score(serialize(invert(second_setting))))

    if setting[0] == "1":
        new_setting = np.fromstring(setting[1:], 'u1') - ord('0')

    else:
        new_setting = np.fromstring(setting[:-1], 'u1') - ord('0')

    return -calculate_winner_score(serialize(invert(new_setting)))


calculate_winner_score = _memoization(calculate_winner_score)

# for case in range(1, test_cases + 1):
#     game_setting = input()
#
#     setting = np.zeros(len(game_setting), dtype=np.uint8)
#     for i, piece in enumerate(game_setting):
#         setting[i] = 1 if piece == "I" else 0
#
#     s = calculate_winner_score(serialize(setting))
#     winner = "I" if s > 0 else "O"
#     print(f"Case #{case}: {winner} {abs(s)}")
