from queue import PriorityQueue

def _extract_amount(p_queue, amount, t):
    extracted_amount = 0
    while not p_queue.empty():
        priority, info = p_queue.get()
        ins_time, cur_amount, remaining_time = info
        if t < ins_time + remaining_time:
            extracted_amount += cur_amount
            if extracted_amount >= amount:
                break

    if extracted_amount < amount:
        return None, None, None
    else:
        return remaining_time, ins_time, extracted_amount - amount


def _solve(deliveries, orders, U, times):
    served_orders = 0
    delivery_queue = PriorityQueue(maxsize=len(deliveries))
    for t in times:
        if t in deliveries:
            delivery = deliveries[t]
            delivery_queue.put((delivery[1] + t, (t, delivery[0], delivery[1])))
        if t in orders:
            remaining_time, ins_time, remaining_items = _extract_amount(delivery_queue, U, t)
            if remaining_time is None:
                break

            served_orders += 1
            if remaining_items > 0:
                delivery_queue.put((ins_time + remaining_time, (t, remaining_items, ins_time + remaining_time - t)))

    return served_orders


def solve(deliveries, D, N, U, orders):
    orders = set(orders)
    times = sorted(list(set(orders).union(deliveries.keys())))
    return _solve(deliveries, orders, U, times)

if __name__ == '__main__':
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        D, N, U = list(map(int, input().split()))

        deliveries = {}
        for _ in range(D):
            delivery = list(map(int, input().split()))
            deliveries[delivery[0]] = (delivery[1], delivery[2])
        orders = list(map(int, input().split()))
        res = solve(deliveries, D, N, U, orders)
        print(f"Case #{case}: {res}")
