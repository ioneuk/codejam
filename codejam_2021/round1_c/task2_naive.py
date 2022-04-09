# test_cases = int(input())


def is_roaring(year):
    max_prefix_len = len(year) // 2 + 1

    for prefix in range(1, max_prefix_len + 1):
        valid_prefix = False
        cur_number = int(year[:prefix])
        cur_pos = prefix
        while cur_pos < len(year):
            next_number = int(year[cur_pos: cur_pos + len(str(cur_number+1))])
            if next_number != cur_number + 1:
                valid_prefix = False
                break
            else:
                valid_prefix = True
            cur_pos += len(str(cur_number+1))
            cur_number = next_number

        if valid_prefix:
            return True

    return False


def find_roaring(year):
    in_year = int(year)
    cur_year = in_year + 1

    while not is_roaring(str(cur_year)):
        cur_year += 1
    return cur_year


# for case in range(1, test_cases + 1):
#     year = input()
#     answer = find_roaring(year)
#
#     print(f"Case #{case}: {answer}")
