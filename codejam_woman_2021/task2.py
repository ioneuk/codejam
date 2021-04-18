alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

test_cases = int(input())


def is_even(n: int) -> bool:
    return n % 2 == 0


for case in range(1, test_cases + 1):
    blocks_count = int(input())
    lens = list(map(int, input().split()))

    res = ["A"]

    start_pos = 1
    for i in range(1, blocks_count + 1):
        if is_even(i):
            res.extend(list(reversed(alphabet[0:start_pos+1])))
            start_pos = 1
        else:
            cur_l = lens[i - 1]
            res.extend(alphabet[start_pos: start_pos + cur_l - 1])
            start_pos += cur_l - 1

            next_l = lens[i] if i < blocks_count else -1
            if next_l > start_pos:
                start_pos = next_l - 1
                res.append(alphabet[next_l])
            else:
                res.append(alphabet[start_pos])
                start_pos = next_l - 1

    res = "".join(res)
    print(f"Case #{case}: {res}")
