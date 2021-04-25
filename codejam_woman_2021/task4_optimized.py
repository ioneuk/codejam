test_cases = int(input())


def calculate_winner_score(setting):
    olga_decides = False

    while len(setting) > 0:
        if len(setting) == 1:
            if olga_decides:
                return ("O", 1) if setting[0] == "O" else ("I", 2)
            else:
                return ("I", 1) if setting[0] == "I" else ("O", 2)
        if not olga_decides and (setting[0] == setting[-1] == "O"):
            return "O", len(setting) + 1
        elif not olga_decides and (setting[0] == setting[-1] == "I"):
            break
        elif not olga_decides and (setting[0] != setting[-1]):
            olga_decides = True
            if setting[0] == "I":
                setting = setting[1:]
            else:
                setting = setting[:-1]
        elif olga_decides and (setting[0] == setting[-1] == "I"):
            return "I", len(setting) + 1
        elif olga_decides and (setting[0] == setting[-1] == "O"):
            break
        elif olga_decides and (setting[0] != setting[-1]):
            olga_decides = False
            if setting[0] == "O":
                setting = setting[1:]
            else:
                setting = setting[:-1]

    cur_player = "O" if olga_decides else "I"
    ld_nearest = -1
    rd_nearest = -1

    for i in range(1, len(setting)):
        if setting[i - 1] == "I" and setting[i] == "I":
            ld_nearest = i - 1
            break
        elif setting[i - 1] == "O" and setting[i] == "O":
            ld_nearest = i - 1
            break
        else:
            continue

    if ld_nearest == -1:
        if len(setting) % 2 != 0:
            winner = cur_player
        else:
            winner = "I" if olga_decides else "O"
        return winner, 1

    for i in range(len(setting) - 2, -1, -1):
        if setting[i] == "I" and setting[i + 1] == "I":
            rd_nearest = i + 1
            break
        elif setting[i] == "O" and setting[i + 1] == "O":
            rd_nearest = i + 1
            break
        else:
            continue

    if olga_decides and (setting[ld_nearest] == "O" or setting[rd_nearest] == "O"):
        winner = "O"
    elif setting[ld_nearest] == "I" or setting[rd_nearest] == "I":
        winner = "I"
    else:
        winner = "O"


    if setting[ld_nearest] != setting[rd_nearest]:
        min_dist = ld_nearest+1 if setting[ld_nearest] == winner else len(setting) - rd_nearest
        score = len(setting) - min_dist + 1
    elif setting[ld_nearest] == setting[rd_nearest] == cur_player:
        score = len(setting) - min(ld_nearest+1, len(setting) - rd_nearest) + 1
    elif (setting[ld_nearest] == setting[rd_nearest]) and (setting[ld_nearest] != cur_player):
        score = len(setting) - (ld_nearest + 1) -  (len(setting) - rd_nearest) + 1

    return winner, score

for case in range(1, test_cases + 1):
    game_setting = input()

    winner, score = calculate_winner_score(game_setting)
    print(f"Case #{case}: {winner} {score}")
