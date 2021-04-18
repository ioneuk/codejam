import math

test_cases, n, max_queries = map(int, input().split())
queries = 0

cache = {}


def ask_median(first, second, third):
    global queries
    entry = sorted([first, second, third])
    cache_entry = (entry[0], entry[1], entry[2])
    if cache_entry in cache:
        return cache[cache_entry]
    else:
        queries += 1
        if queries > max_queries:
            raise Exception("max queries exceeded")
        print(f"{first} {second} {third}", flush=True)
        result = int(input())
        if result == -1:
            raise RuntimeError("wrong answer")
        cache[cache_entry] = result
        return result


def sort_arr_according_to_the_median(arr, median):
    if arr[1] == median:
        pass
    elif arr[0] == median:
        arr[0], arr[1] = arr[1], arr[0]
    else:
        arr[1], arr[2] = arr[2], arr[1]

    return arr


def insert_el_into_arr(el, arr):
    left = 0
    right = len(arr)
    inserted = False

    while right - left > 1:
        mid = (right + left) // 2
        mid_1 = mid - 1
        mid_2 = mid
        median = ask_median(arr[mid_1], arr[mid_2], el)
        if median == el:
            arr.insert(mid_2, el)
            inserted = True
            break
        elif median == arr[mid_1]:
            right = mid_2
        else:
            if mid_2 + 1 > len(arr) - 1:
                break
            median = ask_median(arr[mid_2], arr[mid_2 + 1], el)
            if median == el:
                arr.insert(mid_2 + 1, el)
                inserted = True
                break
            else:
                left = mid_2 + 1

    if inserted == False:
        mid = (left + right) // 2
        if mid == 0:
            arr.insert(0, el)
        elif mid == len(arr) or mid == len(arr) - 1:
            arr.append(el)


def merge(left, right):
    for el in right:
        insert_el_into_arr(el, left)

    return left


def guess_order(arr):
    if len(arr) == 2:
        return arr
    elif len(arr) == 3:
        median = ask_median(arr[0], arr[1], arr[2])
        arr = sort_arr_according_to_the_median(arr, median)
        return arr

    else:
        mid = int(math.ceil(len(arr) / 2))
        left = guess_order(arr[:mid])
        right = guess_order(arr[mid:])
        return merge(left, right)


for case in range(test_cases):
    cache = {}
    try:
        res = guess_order([i + 1 for i in range(n)])
        print(*res, sep=' ', flush=True)
        answer = int(input())
    except RuntimeError:
        pass
    except Exception:
        break