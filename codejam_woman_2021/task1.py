from collections import defaultdict

test_cases = int(input())

for case in range(1, test_cases+1):
    arr_len = int(input())

    arr = list(map(int, input().split()))

    mem = defaultdict(lambda: 0)
    for el in arr:
        mem[el] += 1

    res = 0
    mem = {k: v for k, v in sorted(mem.items(), key=lambda item: item[0])}

    cur = 1
    for v in mem.values():
        res += cur * v
        cur += 1

    print(f"Case #{case}: {res}")