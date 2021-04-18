import math

test_cases = int(input())
percentage = int(input())
players = 100
questions = 10000
#
# players = 6
# questions = 7

COEF = 10

results = []

def solve_case(q_p, p_p, a):
    max_score = 0
    player_with_max_score = 0

    for p in range(players):
        score = 0
        for q in range(questions):
            exp_a = int(p_p[p] > q_p[q])
            res = math.fabs(exp_a - a[p][q])
            if a[p][q] == 1 and res > 0:
                score += COEF * (q_p[q] - p_p[p])

        if score > max_score:
            max_score = score
            player_with_max_score = p + 1

    return player_with_max_score


for case in range(1, test_cases + 1):
    question_difficulty = [None] * questions
    player_skills = [None] * players
    answers = []

    for p in range(players):
        answer_str = input()
        correct_answers = answer_str.count("1")
        player_skills[p] = correct_answers / questions

        player_answers = [int(a) for a in answer_str]
        answers.append(player_answers)

    for question_number in range(questions):
        total_correct_answers = sum(row[question_number] for row in answers)
        question_difficulty[question_number] = 1 - total_correct_answers / players

    cheater = solve_case(question_difficulty, player_skills, answers)

    results.append(f"Case #{case}: {cheater}")

print(*results, sep="\n", flush=True)