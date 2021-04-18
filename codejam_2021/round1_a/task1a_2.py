import math

test_cases = int(input())

MIN_PRIME_NUMBER = 2
MAX_PRIME_NUMBER = 499

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499]


def is_valid_score_candidate(candidate: int, deck: dict) -> bool:
    # factorize with primes in range [MIN_PRIME_NUMBER, MAX_PRIME_NUMBER]
    deck_l = deck.copy()
    cur_number = candidate
    up_bound = min(MAX_PRIME_NUMBER, math.ceil(math.sqrt(candidate)))
    for prime_factor in PRIMES:
        if cur_number == 1 or prime_factor > up_bound:
            break
        while cur_number % prime_factor == 0:
            if prime_factor not in deck_l or deck_l[prime_factor] == 0:
                return False

            deck_l[prime_factor] -= 1
            cur_number //= prime_factor

    if cur_number != 1 and cur_number > MAX_PRIME_NUMBER:
        return False
    elif cur_number != 1 and cur_number <= MAX_PRIME_NUMBER:
        if cur_number not in deck_l:
            return False
        deck_l[cur_number] -= 1

    # check first group sum
    firs_group_sum = 0
    for prime, remaining_count in deck_l.items():
        firs_group_sum += prime * remaining_count

    if firs_group_sum != candidate:
        return False

    return True


for case in range(1, test_cases + 1):
    M = int(input())

    deck = {}
    total_sum = 0
    total_len = 0

    for _ in range(M):
        P_i, N_i = map(int, input().split())
        deck[P_i] = N_i
        total_sum += P_i * N_i
        total_len += N_i

    max_cards_in_sec_group = math.ceil(math.log2(total_sum))
    max_sum_in_sec_group = MAX_PRIME_NUMBER * max_cards_in_sec_group

    max_score = 0
    lower_score_bound = max(1, total_sum - max_sum_in_sec_group)
    for score_candidate in range(lower_score_bound, total_sum):
        if is_valid_score_candidate(score_candidate, deck):
            max_score = score_candidate

    print(f"Case #{case}: {max_score}")
