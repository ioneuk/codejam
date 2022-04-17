import math
import numpy as np


def solve(E, exercises):
    intersections = np.zeros((E, E), dtype=np.int32)
    dp = np.zeros((E, E), dtype=np.int32)

    # Build intersections table
    for i in range(E):
        for j in range(i, E):
            if i == j:
                intersections[i, j] = exercises[i].sum()
            else:
                intersections[i, j] = exercises[i:j+1].min(axis=0).sum()

    for prefix_len in range(2, E+1):
        for prefix_start in range(0, E - prefix_len+1):
            l = prefix_start
            r = prefix_start + prefix_len - 1
            optimal = math.inf
            for x in range(l+1, r+1):
                res = dp[l,x-1] + 2 * (intersections[l,x-1] - intersections[l,r]) \
                      + dp[x, r] + 2 * (intersections[x, r] - intersections[l, r])
                optimal = min(optimal, res)
            dp[l, r] = optimal

    return dp[0, E-1] + 2 * intersections[0, E-1]
        

if __name__ == '__main__':
    test_cases = int(input())

    for case in range(1, test_cases + 1):
        E, W = list(map(int, input().split()))
        exercises = np.zeros((E, W), dtype=np.int32)
        for i in range(E):
            exercises[i] = np.array(list(map(int, input().split())), dtype=np.int32)
        res = solve(E, exercises)
        print(f"Case #{case}: {res}")
