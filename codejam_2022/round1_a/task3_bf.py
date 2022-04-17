import numpy as np
import math


def _generate_substack_from_spec(spec):
    stack = []
    for weight_type, weight_count in enumerate(spec):
        stack.extend([weight_type + 1] * weight_count)
    return stack


class unique_element:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences


def perm_unique(elements):
    if len(elements) == 0:
        return []
    eset = set(elements)
    listunique = [unique_element(i, elements.count(i)) for i in eset]
    u = len(elements)
    return perm_unique_helper(listunique, [0] * u, u - 1)


def perm_unique_helper(listunique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d] = i.value
                i.occurrences -= 1
                for g in perm_unique_helper(listunique, result_list, d - 1):
                    yield g
                i.occurrences += 1


def solve(E, W, exercises):
    min_weights = exercises.min(axis=0)
    c = int(min_weights.sum())
    exercises = exercises - min_weights


    cur_ex = 0
    while cur_ex < len(exercises) and exercises[cur_ex].sum() == 0:
        cur_ex += 1

    if cur_ex >= len(exercises):
        return 2*c
    first_stack = _generate_substack_from_spec(exercises[cur_ex])
    operations_count = len(first_stack)
    min_operations = math.inf
    try:
        for perm in perm_unique(first_stack):
            stack = [(perm, cur_ex+1, operations_count)]
            while len(stack) > 0:
                stack_structure, cur_ex, cur_operations_count = stack.pop()
                if cur_operations_count >= min_operations:
                    continue
                if cur_ex == E:
                    total_operations_count = cur_operations_count + len(stack_structure)
                    min_operations = min(min_operations, total_operations_count)
                    continue

                next_ex_spec = exercises[cur_ex]

                lowest_rem_item = len(stack_structure)
                for weight_type in range(W):
                    occurrences_in_stack = stack_structure.count(weight_type + 1)
                    rem = occurrences_in_stack - next_ex_spec[weight_type]
                    if rem > 0:
                        indexes = [i for i, j in reversed(list(enumerate(stack_structure))) if j == weight_type + 1]
                        lowest_rem_item = min(lowest_rem_item, indexes[rem - 1])
                min_remove_operations = len(stack_structure) - lowest_rem_item

                for remove_operations in range(min_remove_operations, len(stack_structure) + 1):

                    stack_structure = stack_structure[: len(stack_structure) - remove_operations]

                    weights_to_add = [0] * W
                    for weight_type in range(W):
                        occurrences_in_stack = stack_structure.count(weight_type + 1)
                        rem = occurrences_in_stack - next_ex_spec[weight_type]
                        if rem < 0:
                            weights_to_add[weight_type] = -rem

                    substack = _generate_substack_from_spec(weights_to_add)
                    if len(substack) == 0:
                        stack.append(((stack_structure), cur_ex + 1, cur_operations_count + remove_operations))
                    else:
                        for subperm in perm_unique(substack):
                            stack.append((stack_structure + subperm, cur_ex + 1,
                                          cur_operations_count + remove_operations + len(subperm)))
    except Exception:
        return -1

    return 2*c + min_operations


if __name__ == '__main__':
    test_cases = int(input())

    for case in range(1, test_cases + 1):
        E, W = list(map(int, input().split()))
        exercises = np.zeros((E, W), dtype=np.int32)
        for i in range(E):
            exercises[i] = np.array(list(map(int, input().split())), dtype=np.int32)
        res = solve(E, W, exercises)
        print(f"Case #{case}: {res}")
