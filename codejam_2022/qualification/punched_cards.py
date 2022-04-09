test_cases = int(input())


def _print_header(C):
    out = ['..+']
    for _ in range(C - 1):
        out += ['-+']
    print(''.join(out), flush=True)


def _print_first_line(C):
    out = ['..|']
    for _ in range(C - 1):
        out += ['.|']
    print(''.join(out), flush=True)

    out = ['+']
    for _ in range(C):
        out += ['-+']
    print(''.join(out), flush=True)


def _print_line(C):
    out = ['|']
    for _ in range(C):
        out += ['.|']
    print(''.join(out), flush=True)
    out = ['+']
    for _ in range(C):
        out += ['-+']
    print(''.join(out), flush=True)


def print_ascii_table(R, C):
    _print_header(C)
    _print_first_line(C)

    for _ in range(R - 1):
        _print_line(C)


for case in range(1, test_cases + 1):
    R, C = list(map(int, input().split()))
    print(f"Case #{case}:")
    print_ascii_table(R, C)
