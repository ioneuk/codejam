test_cases = int(input())

for case in range(1, test_cases+1):
    arr_len = int(input())
    arr = list(map(int, input().split()))

    total_appends = 0
    prev_len = len(str(arr[0]))
    prev = arr[0]
    for i in range(1, arr_len):
        if arr[i] > prev:
            prev = arr[i]
            prev_len = len(str(arr[i]))
            continue

        cur_len = len(str(arr[i]))
        diff = prev_len - cur_len
        if diff == 0:
            total_appends += 1
            arr[i] *= 10
            prev = arr[i]
            prev_len = cur_len + 1
        elif (10**diff) * arr[i] <= prev:
            diff_2 = prev - (10**diff) * arr[i]
            check = arr[i] < prev // (10 ** diff)
            check_diff_2 = str(diff_2) == "9" * len(str(diff_2)) and arr[i] == prev // (10 ** diff)
            check_prev = str(prev) == "9" * len(str(prev))

            if check or check_diff_2 or check_prev:
                total_appends += diff + 1

                arr[i] *= 10 ** (diff + 1)
                prev = arr[i]
                prev_len = cur_len + diff + 1
            else:
                total_appends += diff
                arr[i] *= (10 ** diff)
                arr[i] += diff_2 + 1
                prev = arr[i]
                prev_len = cur_len + diff

        else:
            total_appends += diff
            arr[i] *= 10 ** diff
            prev = arr[i]
            prev_len = cur_len + diff

    print(f"Case #{case}: {total_appends}")
