test_cases = int(input())




for case in range(1, test_cases + 1):
    M, N, P = map(int, input().split())
    vertices = M+N

    adj_martix = []
    for _ in range(vertices):
        adj_martix.append(input())

    queries = []
    for _ in range(P):
        first, second = map(int, input().split())
        queries.append((first, second))

    ans = []
    for i in range(1, P+1):
        src, dest = queries[i - 1]
        ans.append(bidirectional_search(adj_martix, src, dest))

    print(f"")
