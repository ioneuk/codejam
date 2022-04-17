def solve(s):
    res = []
    counter_for_same_ch = 0
    for i in range(len(s)-1):
        ch_code = ord(s[i])
        next_code = ord(s[i+1])
        if ch_code < next_code:
            res.extend([s[i]] * (2 * (counter_for_same_ch + 1)))
            counter_for_same_ch = 0
        elif ch_code > next_code:
            res.extend([s[i]] * (counter_for_same_ch + 1))
            counter_for_same_ch = 0
        else:
            counter_for_same_ch += 1
    if counter_for_same_ch == 0:
        res.append(s[-1])
    else:
        res.extend([s[-1]] * (counter_for_same_ch + 1))
    return ''.join(res)


if __name__ == '__main__':
    test_cases = int(input())

    for case in range(1, test_cases + 1):
        s = input()
        res = solve(s)
        print(f"Case #{case}: {res}")
