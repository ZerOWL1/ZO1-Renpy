label BS_Chk_Over:

    if (A_S1_HP == 0) and (
    A_S2_HP == 0) and (
    A_S3_HP == 0) and (
    A_S4_HP == 0) and (
    A_S5_HP == 0) and (
    A_S6_HP == 0):
        e "Attacker Lose"
        $ BS_BattleEnd = True
    elif (D_S1_HP == 0) and (
    D_S2_HP == 0) and (
    D_S3_HP == 0) and (
    D_S4_HP == 0) and (
    D_S5_HP == 0) and (
    D_S6_HP == 0):
        e "Defender Lose"
        $ BS_BattleEnd = True
    elif BS_Turns == BS_TurnsMax:
        e "Battle Draw"
        $ BS_BattleEnd = True
    return