import numpy as np

import codejam_woman_2021.task4 as correct
import codejam_woman_2021.task4_optimized as actual

if __name__ == "__main__":
    while True:
        arr = np.random.randint(2, size=20)
        arr_str = []
        for el in arr:
            arr_str.append("I" if el == 1 else "O")

        arr_str = "".join(arr_str)
        expected_score = correct.calculate_winner_score(correct.serialize(arr))
        winner = "I" if expected_score > 0 else "O"
        score = abs(expected_score)

        actual_winner, actual_score = actual.calculate_winner_score(arr_str)
        if winner != actual_winner or score != actual_score:
            print(f"Setting: {arr_str}")
            print(f"Expected result: {winner} {score}")
            print(f"Acttual result: {actual_winner} {actual_score}")
            raise Exception("Ex")