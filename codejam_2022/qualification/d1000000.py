test_cases = int(input())


def solve(N, si):
    si = sorted(si)
    counter = 0
    for num in si:
        if num < counter + 1:
            continue
        counter += 1
    return counter



for case in range(1, test_cases + 1):
    N = int(input())
    si = list(map(int, input().split()))
    res = solve(N, si)
    print(f"Case #{case}: {res}")
