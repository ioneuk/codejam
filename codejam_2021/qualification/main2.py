def get_char_at_idx(s, idx):
    if idx < 0 or idx > len(s) - 1:
        return None
    return s[idx]


def get_reverse_char(c):
    if c == "C":
        return "J"
    else:
        return "C"


def find_first_defined_char(s):
    for char in s:
        if char != "?":
            return char

    return None


test_cases = int(input())

for case in range(1, test_cases + 1):
    cj, jc, str_art = input().split()

    cj = int(cj)
    jc = int(jc)
    str_art = list(str_art)

    cost = 0

    if cj >= 0 and jc >= 0:
        preferable_char = "C" if cj < jc else "J"
        for idx, char in enumerate(str_art):
            if char != "?":
                prev_char = get_char_at_idx(str_art, idx - 1)
                if prev_char is not None and prev_char != char:
                    cost += cj if prev_char == "C" and char == "J" else jc
                continue

            # First character
            if idx == 0:
                ch = find_first_defined_char(str_art)
                res = ch if ch is not None else preferable_char
            # Last character
            elif idx == len(str_art) - 1:
                res = str_art[idx - 1]

            # Somewhere in the middle
            else:
                if str_art[idx - 1] == str_art[idx + 1]:
                    res = str_art[idx - 1]
                else:
                    res = str_art[idx - 1]
                    prev_char = get_char_at_idx(str_art, idx - 1)
                    if prev_char is not None and prev_char != res:
                        cost += cj if prev_char == "C" and res == "J" else jc

            str_art[idx] = res

    else:
        preferable_char = "C" if cj < jc else "J"
        for idx, char in enumerate(str_art):
            if char != "?":
                prev_char = get_char_at_idx(str_art, idx - 1)
                if prev_char != char:
                    cost += cj if prev_char == "C" and char == "J" else jc
                continue

            # First character
            if idx == 0:
                if str_art[idx + 1] != "?":
                    if str_art[idx + 1] == "C":
                        res = "J" if jc < 0 else "C"
                    else:
                        res = "C" if cj < 0 else "J"
                else:
                    if cj + jc >= 0:
                        res = find_first_defined_char(str_art)
                    else:
                        res = preferable_char

            # Last character
            elif idx == len(str_art) - 1:
                if str_art[idx - 1] == "J":
                    res = "C" if jc < 0 else "J"
                else:
                    res = "J" if cj < 0 else "C"

            # Somewhere in the middle
            else:
                if str_art[idx - 1] == str_art[idx + 1]:
                    res = get_reverse_char(str_art[idx - 1]) if cj + jc < 0 else str_art[idx - 1]
                else:
                    next_char = str_art[idx + 1]
                    if next_char == "?":
                        if cj + jc < 0:
                            res = get_reverse_char(str_art[idx-1])
                        else:
                            res = str_art[idx-1]
                    else:
                        res = preferable_char
                prev_char = get_char_at_idx(str_art, idx - 1)
                if prev_char != res:
                    cost += cj if prev_char == "C" and res == "J" else jc

            str_art[idx] = res

    print(f"Case #{case}: {cost}")
