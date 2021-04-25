from queue import Queue

test_cases = int(input())


def get_neighbors(adj_matrix, src):
    neighbors = []
    for idx, vertex in enumerate(adj_matrix[src]):
        if vertex == "Y":
            neighbors.append(idx)

    return neighbors


def find_shortest_path_len(adj_matrix, src, dest, M, N) -> int:
    vertices_count = len(adj_matrix)
    visited = [False] * vertices_count

    queue = Queue()
    queue.put((src, 1))
    visited[src] = True

    while not queue.empty():
        current, dist = queue.get()
        if current == dest:
            return dist
        neighbors = get_neighbors(adj_matrix, current)
        for neighbor in neighbors:
            if visited[neighbor] == False and neighbor <= M - 1:
                queue.put((neighbor, dist + 1))
            if neighbor == dest:
                return dist + 1
        visited[current] = True

    return -1


def find_shortest_time(adj_martix, src, dest, M, N):
    sp_len = find_shortest_path_len(adj_martix, src, dest, M, N)
    if sp_len == -1:
        return sp_len
    elif sp_len < 3:
        return 0
    elif sp_len == 3:
        return 1

    cur_path_len = sp_len
    res = 0
    while cur_path_len > 3:
        triplets = cur_path_len // 3
        cur_path_len -= triplets
        res += 1

    return res + 1


for case in range(1, test_cases + 1):
    M, N, P = map(int, input().split())
    vertices = M + N

    adj_martix = []
    for _ in range(vertices):
        adj_martix.append(input())

    queries = []
    for _ in range(P):
        first, second = map(int, input().split())
        queries.append((first, second))

    ans = []
    for i in range(1, P + 1):
        src, dest = queries[i - 1]
        ans.append(find_shortest_time(adj_martix, src - 1, dest - 1, M, N))

    ans = " ".join(list(map(str, ans)))
    print(f"Case #{case}: {ans}")
