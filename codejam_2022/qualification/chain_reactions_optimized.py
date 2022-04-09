from collections import defaultdict
from typing import Tuple

import numpy as np


def _dfs_get_leaves(subtree_root, rev_graph) -> list:
    stack = [subtree_root]
    initiators = []
    while len(stack) > 0:
        cur_node = stack.pop()
        childs = rev_graph[cur_node]
        if len(childs) == 0:
            initiators.append(cur_node)
        else:
            stack.extend(childs)

    return initiators


def _get_remained_subtrees(root, initiator, rev_graph, graph, funs) -> Tuple[int, list]:
    cur_node = initiator
    remained_subtrees = []
    max_val = funs[cur_node]
    while cur_node is not None:
        prev_node = cur_node
        cur_node = graph[prev_node]
        if cur_node is not None:
            max_val = max(max_val, funs[cur_node])
        childs = rev_graph[cur_node]
        for ch in childs:
            if ch != prev_node:
                remained_subtrees.append(ch)
        if cur_node == root:
            break
    return max_val, remained_subtrees


def _compute_fun(root, N, funs, graph, rev_graph):
    compute_fun_cache = np.full(N, -1)
    subtree_initiators_cache = defaultdict(list)
    remained_subtrees_cache = defaultdict(lambda: (None, []))

    stack = [root]
    while len(stack) > 0:
        cur_node = stack.pop()
        if len(rev_graph[cur_node]) == 0:
            compute_fun_cache[cur_node] = funs[cur_node]
            continue

        subtree_initiators = subtree_initiators_cache[cur_node]
        if len(subtree_initiators) == 0:
            subtree_initiators = _dfs_get_leaves(cur_node, rev_graph)
            subtree_initiators_cache[cur_node] = subtree_initiators
        all_options = []

        found_dependencies = False
        for cur_initiator in subtree_initiators:
            cur_max, remained_subtrees = remained_subtrees_cache[(cur_node, cur_initiator)]
            if cur_max is None or len(remained_subtrees) == 0:
                cur_max, remained_subtrees = _get_remained_subtrees(cur_node, cur_initiator, rev_graph, graph, funs)
                remained_subtrees_cache[(cur_node, cur_initiator)] = (cur_max, remained_subtrees)

            if len(remained_subtrees) > 0 and -1 in compute_fun_cache[remained_subtrees]:
                stack.append(cur_node)
                for rem in remained_subtrees:
                    if compute_fun_cache[rem] == -1:
                        stack.append(rem)
                found_dependencies = True
                break
            assert cur_max is not None
            result = cur_max
            if len(remained_subtrees) > 0:
                result += sum(compute_fun_cache[remained_subtrees])
            all_options.append(result)
        if found_dependencies:
            continue

        compute_fun_cache[cur_node] = max(all_options)

    return compute_fun_cache[root]


def solve(pointers, funs, N):
    graph = defaultdict(lambda: None)
    rev_graph = defaultdict(list)
    initiators = np.full((N), True)
    roots = []
    for idx, p in enumerate(pointers):
        if p == 0:
            roots.append(idx)
            continue
        initiators[p - 1] = False
        graph[idx] = p - 1
        rev_graph[p - 1].append(idx)

    total_fun = 0
    for _r in roots:
        total_fun += _compute_fun(_r, N, funs, graph, rev_graph)
    return total_fun


if __name__ == '__main__':
    test_cases = int(input())

    for case in range(1, test_cases + 1):
        N = int(input())
        funs = list(map(int, input().split()))
        pointers = list(map(int, input().split()))

        res = solve(pointers, funs, N)
        print(f"Case #{case}: {res}")
