import math
import random
import time

test_cases = int(input())
percentage = int(input())
# players = 100
# questions = 10000
#
players = 6
questions = 8

results = []


def solve_case(q_p, p_p, a):
    max_score = 0
    player_with_max_score = 0

    for p in range(players):
        score = 0
        for q in range(questions):
            exp_a = int(p_p[p] > q_p[q])
            score += math.fabs(exp_a - a[p][q])

        if score > max_score:
            max_score = score
            player_with_max_score = p + 1

    return player_with_max_score


start_time = time.time()

for case in range(1, test_cases + 1):
    question_difficulty = [None] * questions
    player_skills = [None] * players
    answers = []

    # if case % 10 == 0:
    #     print(f"iteration: {case}")

    for p in range(players):
        my_list = [0] * 4 + [1] * 4
        random.shuffle(my_list)
        my_list_str = "".join(map(str, my_list))
        answer_str = my_list_str
        correct_answers = answer_str.count("1")
        player_skills[p] = correct_answers / questions

        player_answers = [int(a) for a in answer_str]
        answers.append(player_answers)

    for question_number in range(questions):
        total_correct_answers = sum(row[question_number] for row in answers)
        question_difficulty[question_number] = total_correct_answers / players

    cheater = solve_case(question_difficulty, player_skills, answers)

    results.append(f"Case #{case}: {cheater}")

print(*results, sep="\n", flush=True)

print("--- %s seconds ---" % (time.time() - start_time))
