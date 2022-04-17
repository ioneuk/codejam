import bisect

MAX_VAL = 10 ** 9

odd_numbers = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215, 217, 219, 221]


def print_list(l):
    print(' '.join(map(str, l)))


def solve(N):
    first_half = [2**i for i in range(N) if 2 ** i < MAX_VAL]
    if len(first_half) < N:
        for i in range(N-len(first_half)):
            first_half.append(odd_numbers[i])


    print_list(first_half)
    sum_f = sum(first_half)
    inp = input()
    if inp == '-1':
        exit(0)
    sec_half = list(map(int, inp.split()))
    tot_sum = sum_f + sum(sec_half)
    target_sum = tot_sum // 2
    arr = sorted(first_half + sec_half)

    first_idx = bisect.bisect_left(arr, target_sum, lo=0, hi=len(arr))
    if first_idx == len(arr):
        first_idx -= 1

    for i in range(first_idx, 0, -1):
        start_el = arr[i]
        target = target_sum - start_el
        resulting_set = [arr[i]]
        upper = i
        while target != 0 and upper > 0:
            idx = bisect.bisect_left(arr, target, lo=0, hi=upper - 1)
            if arr[idx] > target:
                idx -=1
            el = arr[idx]
            resulting_set.append(el)
            if el == target:
                return resulting_set
            upper = idx
            target -= el

    exit(2)


if __name__ == '__main__':
    test_cases = int(input())

    for case in range(1, test_cases + 1):
        inp = input()
        if inp == '-1':
            exit(0)
        N = int(inp)
        res = solve(N)
        print_list(res)
