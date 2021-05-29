label BS_Chk_DuelMor:

    if A_S1_CanDuel == "Winner":
        $ A_S1_MorIcr += BS_DuelWin_MorIcr
        call BS_A_S1_Chk_Mor
    elif A_S1_CanDuel == "Loser":
        $ A_S1_MorDcr += BS_DuelLos_MorDcr
        call BS_A_S1_Chk_Mor

    elif A_S2_CanDuel == "Winner":
        $ A_S2_MorIcr += BS_DuelWin_MorIcr
        call BS_A_S2_Chk_Mor
    elif A_S2_CanDuel == "Loser":
        $ A_S2_MorDcr += BS_DuelLos_MorDcr
        call BS_A_S2_Chk_Mor

    elif A_S3_CanDuel == "Winner":
        $ A_S3_MorIcr += BS_DuelWin_MorIcr
        call BS_A_S3_Chk_Mor
    elif A_S3_CanDuel == "Loser":
        $ A_S3_MorDcr += BS_DuelLos_MorDcr
        call BS_A_S3_Chk_Mor

    elif A_S4_CanDuel == "Winner":
        $ A_S4_MorIcr += BS_DuelWin_MorIcr
        call BS_A_S4_Chk_Mor
    elif A_S4_CanDuel == "Loser":
        $ A_S4_MorDcr += BS_DuelLos_MorDcr
        call BS_A_S4_Chk_Mor

    elif A_S5_CanDuel == "Winner":
        $ A_S5_MorIcr += BS_DuelWin_MorIcr
        call BS_A_S5_Chk_Mor
    elif A_S5_CanDuel == "Loser":
        $ A_S5_MorDcr += BS_DuelLos_MorDcr
        call BS_A_S5_Chk_Mor

    elif A_S6_CanDuel == "Winner":
        $ A_S6_MorIcr += BS_DuelWin_MorIcr
        call BS_A_S6_Chk_Mor
    elif A_S6_CanDuel == "Loser":
        $ A_S6_MorDcr += BS_DuelLos_MorDcr
        call BS_A_S6_Chk_Mor

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

    if D_S1_CanDuel == "Winner":
        $ D_S1_MorIcr += BS_DuelWin_MorIcr
        call BS_D_S1_Chk_Mor
    elif D_S1_CanDuel == "Loser":
        $ D_S1_MorDcr += BS_DuelLos_MorDcr
        call BS_D_S1_Chk_Mor

    elif D_S2_CanDuel == "Winner":
        $ D_S2_MorIcr += BS_DuelWin_MorIcr
        call BS_D_S2_Chk_Mor
    elif D_S2_CanDuel == "Loser":
        $ D_S2_MorDcr += BS_DuelLos_MorDcr
        call BS_D_S2_Chk_Mor

    elif D_S3_CanDuel == "Winner":
        $ D_S3_MorIcr += BS_DuelWin_MorIcr
        call BS_D_S3_Chk_Mor
    elif D_S3_CanDuel == "Loser":
        $ D_S3_MorDcr += BS_DuelLos_MorDcr
        call BS_D_S3_Chk_Mor

    elif D_S4_CanDuel == "Winner":
        $ D_S4_MorIcr += BS_DuelWin_MorIcr
        call BS_D_S4_Chk_Mor
    elif D_S4_CanDuel == "Loser":
        $ D_S4_MorDcr += BS_DuelLos_MorDcr
        call BS_D_S4_Chk_Mor

    elif D_S5_CanDuel == "Winner":
        $ D_S5_MorIcr += BS_DuelWin_MorIcr
        call BS_D_S5_Chk_Mor
    elif D_S5_CanDuel == "Loser":
        $ D_S5_MorDcr += BS_DuelLos_MorDcr
        call BS_D_S5_Chk_Mor

    elif D_S6_CanDuel == "Winner":
        $ D_S6_MorIcr += BS_DuelWin_MorIcr
        call BS_D_S6_Chk_Mor
    elif D_S6_CanDuel == "Loser":
        $ D_S6_MorDcr += BS_DuelLos_MorDcr
        call BS_D_S6_Chk_Mor

    return