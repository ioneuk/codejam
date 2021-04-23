import math
import sys

T, A, B = map(int, input().split())
MAX_EXCHANGES = 300


def exchange(x, y):
    print(f"{x} {y}")
    response = input()
    if response == "WRONG":
        sys.exit(0)

    return response


def lineFromPoints(P, Q, a, b, c):
    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a * (P[0]) + b * (P[1])
    return a, b, c


def perpendicularBisectorFromLine(P, Q, a, b, c):
    mid_point = [(P[0] + Q[0]) // 2, (P[1] + Q[1]) // 2]

    c = -b * (mid_point[0]) + a * (mid_point[1])
    temp = a
    a = -b
    b = temp
    return a, b, c


def lineLineIntersection(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1
    if (determinant == 0):

        return [(10.0) ** 19, (10.0) ** 19]
    else:
        x = (b2 * c1 - b1 * c2) // determinant
        y = (a1 * c2 - a2 * c1) // determinant
        return [x, y]


def findCircumCenter(P, Q, R):
    a, b, c = 0.0, 0.0, 0.0
    a, b, c = lineFromPoints(P, Q, a, b, c)

    e, f, g = 0.0, 0.0, 0.0
    e, f, g = lineFromPoints(Q, R, e, f, g)

    a, b, c = perpendicularBisectorFromLine(P, Q, a, b, c)
    e, f, g = perpendicularBisectorFromLine(Q, R, e, f, g)

    return lineLineIntersection(a, b, c, e, f, g)


def guess_brute_force(x_bottom, x_upper, y_bottom, y_upper):
    for x in range(x_bottom, x_upper + 1):
        for y in range(y_bottom, y_upper + 1):
            response = exchange(x, y)
            if response == "CENTER":
                return


def solve_eq(a, b, c):
    D = b * b - 4 * a * c
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    x = max(x1, x2)
    return int(math.ceil(x))


def calculate_center_coords(x_ul, y_ul, x_br, y_br, radius):
    len1 = x_br - x_ul
    len2 = y_br - y_ul

    mid_x, mid_y = (x_br + x_ul) // 2, (y_ul + y_br) // 2

    if len2 > len1:
        direction = "UP"
        x_o = mid_x
        y_o = mid_y - radius
    else:
        direction = "LEFT"
        x_o = mid_x - radius
        y_o = mid_y

    return x_o, y_o, direction


def smart_guess_bin_search(radius, counter = 0):
    x_ul, y_ul = radius, 2 * (10 ** 9) - radius
    x_br, y_br = y_ul, radius

    while True:
        if counter >= MAX_EXCHANGES:
            sys.exit(0)

        if MAX_EXCHANGES - counter > (x_br - x_ul + 1) * (y_ul - y_br + 1):
            guess_brute_force(x_ul - 10 ** 9, x_br - 10 ** 9, y_br - 10 ** 9, y_ul - 10 ** 9)
            return

        x_c, y_c, loc = calculate_center_coords(x_ul, y_ul, x_br, y_br, radius)
        response = exchange(x_c - 10 ** 9, y_c - 10 ** 9)
        if response == "CENTER":
            return
        elif response == "MISS":
            if loc == "UP":
                width = x_br - x_ul
                root = solve_eq(1, -radius, width * width / 4)
                delta_y = min(root, radius - root)
                y_ul = (y_ul + y_br) // 2 - delta_y
            else:
                width = y_ul - y_br
                root = solve_eq(1, -radius, width * width / 4)
                delta_x = min(root, radius - root)
                x_ul = (x_br + x_ul) // 2 + delta_x

        elif response == "HIT":
            if loc == "UP":
                y_br = (y_ul + y_br) // 2
            else:
                x_br = (x_br + x_ul) // 2
        else:
            sys.exit(0)

        counter += 1


def bin_search_x(left, right, move_to_left_half_on, counter=0):
    _left = left
    _right = right
    _counter = counter
    while math.fabs(_right - _left) > 1:
        mid = (_right + _left) // 2
        response = exchange(mid, 0)
        _counter += 1
        if response == "CENTER":
            return response, ""
        elif response == move_to_left_half_on:
            _right = mid
        else:
            _left = mid

    return _right, _counter


def bin_search_y(left, right, move_to_left_half_on, counter=0):
    _left = left
    _right = right
    _counter = counter
    while math.fabs(_right - _left) > 1:
        mid = (_right + _left) // 2

        response = exchange(0, mid)
        _counter += 1
        if response == "CENTER":
            return response, ""
        elif response == move_to_left_half_on:
            _right = mid
        else:
            _left = mid

    return _right, _counter


def estimate_radius():
    first_x, counter = bin_search_x(-(10 ** 9), int(0.76 * (10 ** 9)), "HIT")
    if first_x == "CENTER":
        return "CENTER", 0
    sec_x, counter = bin_search_x(int(-0.76 * (10 ** 9)), 10 ** 9, "MISS", counter)
    if sec_x == "CENTER":
        return "CENTER", 0
    third_y, counter = bin_search_y(-(10 ** 9), int(0.8 * (10 ** 9)), "HIT", counter)
    if third_y == "CENTER":
        return "CENTER", 0
    first_center = [first_x, 0]
    sec_center = [sec_x, 0]
    third_center = [0, third_y]

    cent = findCircumCenter(first_center, sec_center, third_center)
    response = exchange(cent[0], cent[1])
    counter += 1
    if response == "CENTER":
        return response, 0

    return int(math.sqrt((cent[0] - first_x) ** 2 + (cent[1]) ** 2)), counter


def guess_center():
    if A == B == (10 ** 9) - 5:
        guess_brute_force(-5, 5, -5, 5)
    elif A == B == (10 ** 9) - 50:
        smart_guess_bin_search(min(A, B))
    else:
        radius, counter = estimate_radius()
        if radius == "CENTER":
            return
        smart_guess_bin_search(radius, counter)


for case in range(1, T + 1):
    guess_center()
