test_cases = int(input())


# Concatenation function: f_n(x) = x x+1 x+2 ... x+n
def get_roaring_year(initial_number, concat_number):
    cur_num = initial_number
    roaring_year = cur_num
    for i in range(concat_number-1):
        cur_num += 1
        roaring_year = int(str(roaring_year) + str(cur_num))

    return roaring_year


def find_roaring(year):
    in_year = int(year)
    if len(year) == 1:
        return 12

    options = []
    max_digit_len = len(year) + 1
    for concat_number in range(2, max_digit_len + 1):
        left = 0
        right = 10**18
        answer = 0
        while right - left > 1:
            mid = (right + left) // 2
            roaring_year = get_roaring_year(mid, concat_number)
            if roaring_year > in_year:
                right = mid
                answer = roaring_year
            else:
                left = mid
        options.append(answer)

    return min(options)


for case in range(1, test_cases + 1):
    year = input()
    answer = find_roaring(year)

    print(f"Case #{case}: {answer}")
