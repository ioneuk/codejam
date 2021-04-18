from operator import itemgetter

test_cases = int(input())

for case in range(1, test_cases+1):
    arr_len = int(input())
    arr = list(map(int, input().split()))

    cost = 0

    for i in range(arr_len-1):
        j = i + min(enumerate(arr[i:]), key=itemgetter(1))[0]
        cost += j - i + 1
        arr[i:j+1] = arr[i:j+1][::-1]

    print(f"Case #{case}: {cost}")