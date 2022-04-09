test_cases = int(input())


def find_probability(N, K, tickets):
    tickets = sorted(tickets)
    intervals = []

    intervals.append((1, tickets[0], tickets[0] - 1))
    last_closed_endpoint = tickets[0]
    for ticket in tickets:
        if ticket != last_closed_endpoint:
            left_wins = (ticket - last_closed_endpoint) // 2
            intervals.append((last_closed_endpoint, ticket, left_wins))
            if (ticket - last_closed_endpoint) > 2:
                intervals.append((last_closed_endpoint, ticket, ticket - last_closed_endpoint - 1 - left_wins))
            last_closed_endpoint = ticket

    intervals.append((tickets[-1], K, K - tickets[-1]))

    intervals = sorted(intervals, key=lambda x: x[2], reverse=True)
    win_events = intervals[0][2] + intervals[1][2]
    return win_events / K


for case in range(1, test_cases + 1):
    N, K = map(int, input().split())
    tickets = list(map(int, input().split()))
    prob = find_probability(N, K, tickets)
    print(f"Case #{case}: {prob}")
