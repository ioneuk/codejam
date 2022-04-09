import itertools

import numpy as np


def solve(pointers, funs, N):
    graph = dict()
    initiators = np.full((N), True)
    for idx, p in enumerate(pointers):
        if p == 0:
            graph[idx] = None
            continue
        initiators[p - 1] = False
        graph[idx] = p - 1
    initiators = np.where(initiators)[0].tolist()
    max_total_fun = 0
    for perm in itertools.permutations(initiators):
        visited = np.full((N), False)
        total_fun = 0
        for initiator in perm:
            assert visited[initiator] == False, "Initiator can't be visited"
            cur_fun = 0
            node = initiator
            while node is not None and visited[node] == False:
                cur_fun = max(cur_fun, funs[node])
                visited[node] = True
                node = graph[node]

            total_fun += cur_fun
        max_total_fun = max(max_total_fun, total_fun)
    return max_total_fun


if __name__ == '__main__':
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        N = int(input())
        funs = list(map(int, input().split()))
        pointers = list(map(int, input().split()))

        res = solve(pointers, funs, N)
        print(f"Case #{case}: {res}")
