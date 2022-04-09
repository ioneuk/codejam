import itertools

import numpy as np

def floyd_warshall(graph):
    nodes = len(graph)

    dists = np.copy(graph)
    for k in range(nodes):
        cur_dists = np.zeros_like(dists)
        for i in range(nodes):
            for j in range(nodes):
                cur_dists[i, j] = min(dists[i, j], dists[i, k] + dists[k, j])
                cur_dists[j, i] = cur_dists[i, j]
        dists = cur_dists
    return dists


def solve(graph, N):
    all_pairs_dists = floyd_warshall(graph)
    min_cost = np.inf
    for perm in itertools.permutations(list(range(N)), N):
        cur_cost = 0
        for i in range(N-1):
            cur_cost += all_pairs_dists[perm[i]][perm[i+1]]
        if cur_cost < min_cost:
            min_cost = cur_cost

    return int(min_cost)


if __name__ == '__main__':
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        N = int(input())
        graph = np.ones((N, N)) * np.inf
        for _ in range(N-1):
            A, B, C = list(map(int, input().split()))
            graph[A-1][B-1] = C
            graph[B-1][A-1] = C
        np.fill_diagonal(graph, 0)

        res = solve(graph, N)
        print(f"Case #{case}: {res}")


