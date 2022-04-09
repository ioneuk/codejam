import numpy as np

test_cases = int(input())

def count_i(matrix):
    return np.count_nonzero(matrix=='I')

def solve(N, matrix):
    upper = count_i(matrix[:N, :])
    lower = count_i(matrix[N:, :])
    left = count_i(matrix[:, :N])
    right = count_i(matrix[:, N:])
    min_mod_count = 0
    while upper != lower or left != right:
        if lower != upper and left != right:
            if upper > lower:
                upper -= 1
            elif lower > upper:
                lower -= 1
            if left > right:
                left -= 1
            elif right > left:
                right -= 1
            min_mod_count += 1
            continue

        if upper == lower:
            if left < right:
                right -= 2
            else:
                left -= 2
            upper -= 1
            lower -= 1

        else:
            if upper < lower:
                lower -= 2
            else:
                upper -= 2
            left -= 1
            right -= 1

        min_mod_count += 2
    return min_mod_count

for case in range(1, test_cases+1):
    N = int(input())
    matrix = []
    for _ in range(2*N):
        line = input()
        matrix.append(list(line))

    np_matrix = np.array(matrix)
    res = solve(N, np_matrix)
    print(f"Case #{case}: {res}")