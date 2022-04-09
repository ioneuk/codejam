def solve_ref(d, n, u, deli, orders):
    # deli = []
    # for _ in range(d):
    #     m, l, e = map(int, input().split())
    #     deli.append((m, l, m + e - 1))

    # orders = list(map(int, input().split()))
    ans = 0
    for order in orders:
        valid_deli = []
        for i in range(d):
            begin, leaf, end = deli[i]
            if begin <= order <= end:
                valid_deli.append((end, i))
        valid_deli.sort()
        rem = u
        yay = False
        for v in valid_deli:
            end, i = v
            de = deli[i]
            take = min(rem, de[1])
            rem -= take
            deli[i] = (de[0], de[1] - take, de[2])
            if rem == 0:
                ans += 1
                yay = True
                break
        if not yay:
            break

    return ans
