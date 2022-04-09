import random
from collections import defaultdict

import numpy as np
import networkx as nx
import chain_reactions_bf as bf
import chain_reactions_optimized as opt


def _print_rev_graph(rev_graph, N):
    result = [0] * N
    for i in range(N):
        if i not in rev_graph or len(rev_graph[i]) == 0:
            continue
        result[i] = rev_graph[i][0] + 1
    return result


if __name__ == '__main__':
    while True:
        nodes = 15
        edges = 9
        tree = nx.random_tree(n=nodes, seed=0)
        g = nx.Graph(tree)
        graph = defaultdict(lambda: None)
        rev_graph = defaultdict(list)
        roots = np.full((nodes), True)
        initiators = np.full((nodes), True)
        for edge in g.edges:
            if edge[1] not in rev_graph:
                graph[edge[0]] = edge[1]
                rev_graph[edge[1]].append(edge[0])
                initiators[edge[1]] = False
                roots[edge[0]] = False

        _initiators = np.where(initiators)[0].tolist()
        _roots = np.where(roots)[0].tolist()
        funs = random.sample(range(1, 10 * nodes), nodes)
        graph = [0] * nodes
        for i in range(nodes):
            graph[i] = random.randint(0, i)

        try:
            expected_answer = bf.solve(graph, funs, nodes)
            # actual_answer = opt.solve(graph, rev_graph, funs, _initiators, nodes, _roots)
            actual_answer = opt.solve(graph, funs, nodes)
            print("Done")
            if actual_answer != expected_answer:
                print('Graph adjacency list:')
                print(graph)
                print(f'Funs:')
                print(' '.join(map(str, funs)))
                print('Graph structure:')
                print(' '.join(map(str, graph)))
                print('Graph roots:')
                print(_roots)
                print(f'Expected answer: {expected_answer}')
                print(f'Actual answer: {actual_answer}')
                exit(0)
        except Exception as e:
            print('ERROR!')
            print(e.__traceback__)
            print('Graph adjacency list:')
            print(graph)
            print('Graph structure:')
            print(' '.join(map(str, graph)))
            print(f'Funs:')
            print(' '.join(map(str, funs)))
            print('Graph roots:')
            print(_roots)
            exit(0)
