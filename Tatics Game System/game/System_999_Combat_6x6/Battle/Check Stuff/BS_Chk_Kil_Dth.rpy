
#///////////////////////  ATTACKER SLOT 1 - KILL
label BS_A_S1_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if D_S1_CanEvd == 0:
        if A_S1_Dmg_01 >= D_S1_HP:
            $ A_S1_Kill +=  D_S1_HP
            $ D_S1_Killed +=  D_S1_HP
            $ D_S1_Dmg_Rcv +=  D_S1_HP
            $ A_S1_Exp += D_S1_HP * D_S1_Level
            $ A_S1_Dmg_01 = 0
        elif A_S1_Dmg_01 < D_S1_HP and D_S1_Dmg_Rcv >= D_S1_HP:
            $ A_S1_Kill +=  A_S1_Dmg_01
            $ D_S1_Killed += A_S1_Dmg_01
            $ D_S1_HP -= A_S1_Dmg_01
            $ A_S1_Exp += A_S1_Dmg_01 * D_S1_Level
            $ A_S1_Dmg_01 = 0
        elif A_S1_Dmg_01 < D_S1_HP:
            $ A_S1_Kill += A_S1_Dmg_01
            $ A_S1_Exp += A_S1_Dmg_01 * D_S1_Level
#---------------------------------------------------------------------------------------------------
    if D_S2_CanEvd == 0:
        if A_S1_Dmg_02 >= D_S2_HP:
            $ A_S1_Kill +=  D_S2_HP
            $ D_S2_Killed +=  D_S2_HP
            $ D_S2_Dmg_Rcv +=  D_S2_HP
            $ A_S1_Exp += D_S2_HP * D_S2_Level
            $ A_S1_Dmg_02 = 0
        elif A_S1_Dmg_02 < D_S2_HP and D_S2_Dmg_Rcv >= D_S2_HP:
            $ A_S1_Kill +=  A_S1_Dmg_02
            $ D_S2_Killed += A_S1_Dmg_02
            $ D_S2_HP -= A_S1_Dmg_02
            $ A_S1_Exp += A_S1_Dmg_02 * D_S2_Level
            $ A_S1_Dmg_02 = 0
        elif A_S1_Dmg_02 < D_S2_HP:
            $ A_S1_Kill += A_S1_Dmg_02
            $ A_S1_Exp += A_S1_Dmg_02 * D_S2_Level
#---------------------------------------------------------------------------------------------------
    if D_S3_CanEvd == 0:
        if A_S1_Dmg_03 >= D_S3_HP:
            $ A_S1_Kill +=  D_S3_HP
            $ D_S3_Killed +=  D_S3_HP
            $ D_S3_Dmg_Rcv +=  D_S3_HP
            $ A_S1_Exp += D_S3_HP * D_S3_Level
            $ A_S1_Dmg_03 = 0
        elif A_S1_Dmg_03 < D_S3_HP and D_S3_Dmg_Rcv >= D_S3_HP:
            $ A_S1_Kill +=  A_S1_Dmg_03
            $ D_S3_Killed += A_S1_Dmg_03
            $ D_S3_HP -= A_S1_Dmg_03
            $ A_S1_Exp += A_S1_Dmg_03 * D_S3_Level
            $ A_S1_Dmg_03 = 0
        elif A_S1_Dmg_03 < D_S3_HP:
            $ A_S1_Kill += A_S1_Dmg_03
            $ A_S1_Exp += A_S1_Dmg_03 * D_S3_Level
#---------------------------------------------------------------------------------------------------
    if D_S4_CanEvd == 0:
        if A_S1_Dmg_04 >= D_S4_HP:
            $ A_S1_Kill +=  D_S4_HP
            $ D_S4_Killed +=  D_S4_HP
            $ D_S4_Dmg_Rcv +=  D_S4_HP
            $ A_S1_Exp += D_S4_HP * D_S4_Level
            $ A_S1_Dmg_04 = 0
        elif A_S1_Dmg_04 < D_S4_HP and D_S4_Dmg_Rcv >= D_S4_HP:
            $ A_S1_Kill +=  A_S1_Dmg_04
            $ D_S4_Killed += A_S1_Dmg_04
            $ D_S4_HP -= A_S1_Dmg_04
            $ A_S1_Exp += A_S1_Dmg_04 * D_S4_Level
            $ A_S1_Dmg_04 = 0
        elif A_S1_Dmg_04 < D_S4_HP:
            $ A_S1_Kill += A_S1_Dmg_04
            $ A_S1_Exp += A_S1_Dmg_04 * D_S4_Level
#---------------------------------------------------------------------------------------------------
    if D_S5_CanEvd == 0:
        if A_S1_Dmg_05 >= D_S5_HP:
            $ A_S1_Kill +=  D_S5_HP
            $ D_S5_Killed +=  D_S5_HP
            $ D_S5_Dmg_Rcv +=  D_S5_HP
            $ A_S1_Exp += D_S5_HP * D_S5_Level
            $ A_S1_Dmg_05 = 0
        elif A_S1_Dmg_05 < D_S5_HP and D_S5_Dmg_Rcv >= D_S5_HP:
            $ A_S1_Kill +=  A_S1_Dmg_05
            $ D_S5_Killed += A_S1_Dmg_05
            $ D_S5_HP -= A_S1_Dmg_05
            $ A_S1_Exp += A_S1_Dmg_05 * D_S5_Level
            $ A_S1_Dmg_05 = 0
        elif A_S1_Dmg_05 < D_S5_HP:
            $ A_S1_Kill += A_S1_Dmg_05
            $ A_S1_Exp += A_S1_Dmg_05 * D_S5_Level
#---------------------------------------------------------------------------------------------------
    if D_S6_CanEvd == 0:
        if A_S1_Dmg_06 >= D_S6_HP:
            $ A_S1_Kill +=  D_S6_HP
            $ D_S6_Killed +=  D_S6_HP
            $ D_S6_Dmg_Rcv +=  D_S6_HP
            $ A_S1_Exp += D_S6_HP * D_S6_Level
            $ A_S1_Dmg_06 = 0
        elif A_S1_Dmg_06 < D_S6_HP and D_S6_Dmg_Rcv >= D_S6_HP:
            $ A_S1_Kill +=  A_S1_Dmg_06
            $ D_S6_Killed += A_S1_Dmg_06
            $ D_S6_HP -= A_S1_Dmg_06
            $ A_S1_Exp += A_S1_Dmg_06 * D_S6_Level
            $ A_S1_Dmg_06 = 0
        elif A_S1_Dmg_06 < D_S6_HP:
            $ A_S1_Kill += A_S1_Dmg_06
            $ A_S1_Exp += A_S1_Dmg_06 * D_S6_Level

return

#///////////////////////  ATTACKER SLOT 2 - KILL
label BS_A_S2_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if D_S1_CanEvd == 0:
        if A_S2_Dmg_01 >= D_S1_HP:
            $ A_S2_Kill +=  D_S1_HP
            $ D_S1_Killed +=  D_S1_HP
            $ D_S1_Dmg_Rcv +=  D_S1_HP
            $ A_S2_Exp += D_S1_HP * D_S1_Level
            $ A_S2_Dmg_01 = 0
        elif A_S2_Dmg_01 < D_S1_HP and D_S1_Dmg_Rcv >= D_S1_HP:
            $ A_S2_Kill +=  A_S2_Dmg_01
            $ D_S1_Killed += A_S2_Dmg_01
            $ D_S1_HP -= A_S2_Dmg_01
            $ A_S2_Exp += A_S2_Dmg_01 * D_S1_Level
            $ A_S2_Dmg_01 = 0
        elif A_S2_Dmg_01 < D_S1_HP:
            $ A_S2_Kill += A_S2_Dmg_01
            $ A_S2_Exp += A_S2_Dmg_01 * D_S1_Level
#---------------------------------------------------------------------------------------------------
    if D_S2_CanEvd == 0:
        if A_S2_Dmg_02 >= D_S2_HP:
            $ A_S2_Kill +=  D_S2_HP
            $ D_S2_Killed +=  D_S2_HP
            $ D_S2_Dmg_Rcv +=  D_S2_HP
            $ A_S2_Exp += D_S2_HP * D_S2_Level
            $ A_S2_Dmg_02 = 0
        elif A_S2_Dmg_02 < D_S2_HP and D_S2_Dmg_Rcv >= D_S2_HP:
            $ A_S2_Kill +=  A_S2_Dmg_02
            $ D_S2_Killed += A_S2_Dmg_02
            $ D_S2_HP -= A_S2_Dmg_02
            $ A_S2_Exp += A_S2_Dmg_02 * D_S2_Level
            $ A_S2_Dmg_02 = 0
        elif A_S2_Dmg_02 < D_S2_HP:
            $ A_S2_Kill += A_S2_Dmg_02
            $ A_S2_Exp += A_S2_Dmg_02 * D_S2_Level
#---------------------------------------------------------------------------------------------------
    if D_S3_CanEvd == 0:
        if A_S2_Dmg_03 >= D_S3_HP:
            $ A_S2_Kill +=  D_S3_HP
            $ D_S3_Killed +=  D_S3_HP
            $ D_S3_Dmg_Rcv +=  D_S3_HP
            $ A_S2_Exp += D_S3_HP * D_S3_Level
            $ A_S2_Dmg_03 = 0
        elif A_S2_Dmg_03 < D_S3_HP and D_S3_Dmg_Rcv >= D_S3_HP:
            $ A_S2_Kill +=  A_S2_Dmg_03
            $ D_S3_Killed += A_S2_Dmg_03
            $ D_S3_HP -= A_S2_Dmg_03
            $ A_S2_Exp += A_S2_Dmg_03 * D_S3_Level
            $ A_S2_Dmg_03 = 0
        elif A_S2_Dmg_03 < D_S3_HP:
            $ A_S2_Kill += A_S2_Dmg_03
            $ A_S2_Exp += A_S2_Dmg_03 * D_S3_Level
#---------------------------------------------------------------------------------------------------
    if D_S4_CanEvd == 0:
        if A_S2_Dmg_04 >= D_S4_HP:
            $ A_S2_Kill +=  D_S4_HP
            $ D_S4_Killed +=  D_S4_HP
            $ D_S4_Dmg_Rcv +=  D_S4_HP
            $ A_S2_Exp += D_S4_HP * D_S4_Level
            $ A_S2_Dmg_04 = 0
        elif A_S2_Dmg_04 < D_S4_HP and D_S4_Dmg_Rcv >= D_S4_HP:
            $ A_S2_Kill +=  A_S2_Dmg_04
            $ D_S4_Killed += A_S2_Dmg_04
            $ D_S4_HP -= A_S2_Dmg_04
            $ A_S2_Exp += A_S2_Dmg_04 * D_S4_Level
            $ A_S2_Dmg_04 = 0
        elif A_S2_Dmg_04 < D_S4_HP:
            $ A_S2_Kill += A_S2_Dmg_04
            $ A_S2_Exp += A_S2_Dmg_04 * D_S4_Level
#---------------------------------------------------------------------------------------------------
    if D_S5_CanEvd == 0:
        if A_S2_Dmg_05 >= D_S5_HP:
            $ A_S2_Kill +=  D_S5_HP
            $ D_S5_Killed +=  D_S5_HP
            $ D_S5_Dmg_Rcv +=  D_S5_HP
            $ A_S2_Exp += D_S5_HP * D_S5_Level
            $ A_S2_Dmg_05 = 0
        elif A_S2_Dmg_05 < D_S5_HP and D_S5_Dmg_Rcv >= D_S5_HP:
            $ A_S2_Kill +=  A_S2_Dmg_05
            $ D_S5_Killed += A_S2_Dmg_05
            $ D_S5_HP -= A_S2_Dmg_05
            $ A_S2_Exp += A_S2_Dmg_05 * D_S5_Level
            $ A_S2_Dmg_05 = 0
        elif A_S2_Dmg_05 < D_S5_HP:
            $ A_S2_Kill += A_S2_Dmg_05
            $ A_S2_Exp += A_S2_Dmg_05 * D_S5_Level
#---------------------------------------------------------------------------------------------------
    if D_S6_CanEvd == 0:
        if A_S2_Dmg_06 >= D_S6_HP:
            $ A_S2_Kill +=  D_S6_HP
            $ D_S6_Killed +=  D_S6_HP
            $ D_S6_Dmg_Rcv +=  D_S6_HP
            $ A_S2_Exp += D_S6_HP * D_S6_Level
            $ A_S2_Dmg_06 = 0
        elif A_S2_Dmg_06 < D_S6_HP and D_S6_Dmg_Rcv >= D_S6_HP:
            $ A_S2_Kill +=  A_S2_Dmg_06
            $ D_S6_Killed += A_S2_Dmg_06
            $ D_S6_HP -= A_S2_Dmg_06
            $ A_S2_Exp += A_S2_Dmg_06 * D_S6_Level
            $ A_S2_Dmg_06 = 0
        elif A_S2_Dmg_06 < D_S6_HP:
            $ A_S2_Kill += A_S2_Dmg_06
            $ A_S2_Exp += A_S2_Dmg_06 * D_S6_Level

return

#///////////////////////  ATTACKER SLOT 3 - KILL
label BS_A_S3_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if D_S1_CanEvd == 0:
        if A_S3_Dmg_01 >= D_S1_HP:
            $ A_S3_Kill +=  D_S1_HP
            $ D_S1_Killed +=  D_S1_HP
            $ D_S1_Dmg_Rcv +=  D_S1_HP
            $ A_S3_Exp += D_S1_HP * D_S1_Level
            $ A_S3_Dmg_01 = 0
        elif A_S3_Dmg_01 < D_S1_HP and D_S1_Dmg_Rcv >= D_S1_HP:
            $ A_S3_Kill +=  A_S3_Dmg_01
            $ D_S1_Killed += A_S3_Dmg_01
            $ D_S1_HP -= A_S3_Dmg_01
            $ A_S3_Exp += A_S3_Dmg_01 * D_S1_Level
            $ A_S3_Dmg_01 = 0
        elif A_S3_Dmg_01 < D_S1_HP:
            $ A_S3_Kill += A_S3_Dmg_01
            $ A_S3_Exp += A_S3_Dmg_01 * D_S1_Level
#---------------------------------------------------------------------------------------------------
    if D_S2_CanEvd == 0:
        if A_S3_Dmg_02 >= D_S2_HP:
            $ A_S3_Kill +=  D_S2_HP
            $ D_S2_Killed +=  D_S2_HP
            $ D_S2_Dmg_Rcv +=  D_S2_HP
            $ A_S3_Exp += D_S2_HP * D_S2_Level
            $ A_S3_Dmg_02 = 0
        elif A_S3_Dmg_02 < D_S2_HP and D_S2_Dmg_Rcv >= D_S2_HP:
            $ A_S3_Kill +=  A_S3_Dmg_02
            $ D_S2_Killed += A_S3_Dmg_02
            $ D_S2_HP -= A_S3_Dmg_02
            $ A_S3_Exp += A_S3_Dmg_02 * D_S2_Level
            $ A_S3_Dmg_02 = 0
        elif A_S3_Dmg_02 < D_S2_HP:
            $ A_S3_Kill += A_S3_Dmg_02
            $ A_S3_Exp += A_S3_Dmg_02 * D_S2_Level
#---------------------------------------------------------------------------------------------------
    if D_S3_CanEvd == 0:
        if A_S3_Dmg_03 >= D_S3_HP:
            $ A_S3_Kill +=  D_S3_HP
            $ D_S3_Killed +=  D_S3_HP
            $ D_S3_Dmg_Rcv +=  D_S3_HP
            $ A_S3_Exp += D_S3_HP * D_S3_Level
            $ A_S3_Dmg_03 = 0
        elif A_S3_Dmg_03 < D_S3_HP and D_S3_Dmg_Rcv >= D_S3_HP:
            $ A_S3_Kill +=  A_S3_Dmg_03
            $ D_S3_Killed += A_S3_Dmg_03
            $ D_S3_HP -= A_S3_Dmg_03
            $ A_S3_Exp += A_S3_Dmg_03 * D_S3_Level
            $ A_S3_Dmg_03 = 0
        elif A_S3_Dmg_03 < D_S3_HP:
            $ A_S3_Kill += A_S3_Dmg_03
            $ A_S3_Exp += A_S3_Dmg_03 * D_S3_Level
#---------------------------------------------------------------------------------------------------
    if D_S4_CanEvd == 0:
        if A_S3_Dmg_04 >= D_S4_HP:
            $ A_S3_Kill +=  D_S4_HP
            $ D_S4_Killed +=  D_S4_HP
            $ D_S4_Dmg_Rcv +=  D_S4_HP
            $ A_S3_Exp += D_S4_HP * D_S4_Level
            $ A_S3_Dmg_04 = 0
        elif A_S3_Dmg_04 < D_S4_HP and D_S4_Dmg_Rcv >= D_S4_HP:
            $ A_S3_Kill +=  A_S3_Dmg_04
            $ D_S4_Killed += A_S3_Dmg_04
            $ D_S4_HP -= A_S3_Dmg_04
            $ A_S3_Exp += A_S3_Dmg_04 * D_S4_Level
            $ A_S3_Dmg_04 = 0
        elif A_S3_Dmg_04 < D_S4_HP:
            $ A_S3_Kill += A_S3_Dmg_04
            $ A_S3_Exp += A_S3_Dmg_04 * D_S4_Level
#---------------------------------------------------------------------------------------------------
    if D_S5_CanEvd == 0:
        if A_S3_Dmg_05 >= D_S5_HP:
            $ A_S3_Kill +=  D_S5_HP
            $ D_S5_Killed +=  D_S5_HP
            $ D_S5_Dmg_Rcv +=  D_S5_HP
            $ A_S3_Exp += D_S5_HP * D_S5_Level
            $ A_S3_Dmg_05 = 0
        elif A_S3_Dmg_05 < D_S5_HP and D_S5_Dmg_Rcv >= D_S5_HP:
            $ A_S3_Kill +=  A_S3_Dmg_05
            $ D_S5_Killed += A_S3_Dmg_05
            $ D_S5_HP -= A_S3_Dmg_05
            $ A_S3_Exp += A_S3_Dmg_05 * D_S5_Level
            $ A_S3_Dmg_05 = 0
        elif A_S3_Dmg_05 < D_S5_HP:
            $ A_S3_Kill += A_S3_Dmg_05
            $ A_S3_Exp += A_S3_Dmg_05 * D_S5_Level
#---------------------------------------------------------------------------------------------------
    if D_S6_CanEvd == 0:
        if A_S3_Dmg_06 >= D_S6_HP:
            $ A_S3_Kill +=  D_S6_HP
            $ D_S6_Killed +=  D_S6_HP
            $ D_S6_Dmg_Rcv +=  D_S6_HP
            $ A_S3_Exp += D_S6_HP * D_S6_Level
            $ A_S3_Dmg_06 = 0
        elif A_S3_Dmg_06 < D_S6_HP and D_S6_Dmg_Rcv >= D_S6_HP:
            $ A_S3_Kill +=  A_S3_Dmg_06
            $ D_S6_Killed += A_S3_Dmg_06
            $ D_S6_HP -= A_S3_Dmg_06
            $ A_S3_Exp += A_S3_Dmg_06 * D_S6_Level
            $ A_S3_Dmg_06 = 0
        elif A_S3_Dmg_06 < D_S6_HP:
            $ A_S3_Kill += A_S3_Dmg_06
            $ A_S3_Exp += A_S3_Dmg_06 * D_S6_Level

return

#///////////////////////  ATTACKER SLOT 4 - KILL
label BS_A_S4_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if D_S1_CanEvd == 0:
        if A_S4_Dmg_01 >= D_S1_HP:
            $ A_S4_Kill +=  D_S1_HP
            $ D_S1_Killed +=  D_S1_HP
            $ D_S1_Dmg_Rcv +=  D_S1_HP
            $ A_S4_Exp += D_S1_HP * D_S1_Level
            $ A_S4_Dmg_01 = 0
        elif A_S4_Dmg_01 < D_S1_HP and D_S1_Dmg_Rcv >= D_S1_HP:
            $ A_S4_Kill +=  A_S4_Dmg_01
            $ D_S1_Killed += A_S4_Dmg_01
            $ D_S1_HP -= A_S4_Dmg_01
            $ A_S4_Exp += A_S4_Dmg_01 * D_S1_Level
            $ A_S4_Dmg_01 = 0
        elif A_S4_Dmg_01 < D_S1_HP:
            $ A_S4_Kill += A_S4_Dmg_01
            $ A_S4_Exp += A_S4_Dmg_01 * D_S1_Level
#---------------------------------------------------------------------------------------------------
    if D_S2_CanEvd == 0:
        if A_S4_Dmg_02 >= D_S2_HP:
            $ A_S4_Kill +=  D_S2_HP
            $ D_S2_Killed +=  D_S2_HP
            $ D_S2_Dmg_Rcv +=  D_S2_HP
            $ A_S4_Exp += D_S2_HP * D_S2_Level
            $ A_S4_Dmg_02 = 0
        elif A_S4_Dmg_02 < D_S2_HP and D_S2_Dmg_Rcv >= D_S2_HP:
            $ A_S4_Kill +=  A_S4_Dmg_02
            $ D_S2_Killed += A_S4_Dmg_02
            $ D_S2_HP -= A_S4_Dmg_02
            $ A_S4_Exp += A_S4_Dmg_02 * D_S2_Level
            $ A_S4_Dmg_02 = 0
        elif A_S4_Dmg_02 < D_S2_HP:
            $ A_S4_Kill += A_S4_Dmg_02
            $ A_S4_Exp += A_S4_Dmg_02 * D_S2_Level
#---------------------------------------------------------------------------------------------------
    if D_S3_CanEvd == 0:
        if A_S4_Dmg_03 >= D_S3_HP:
            $ A_S4_Kill +=  D_S3_HP
            $ D_S3_Killed +=  D_S3_HP
            $ D_S3_Dmg_Rcv +=  D_S3_HP
            $ A_S4_Exp += D_S3_HP * D_S3_Level
            $ A_S4_Dmg_03 = 0
        elif A_S4_Dmg_03 < D_S3_HP and D_S3_Dmg_Rcv >= D_S3_HP:
            $ A_S4_Kill +=  A_S4_Dmg_03
            $ D_S3_Killed += A_S4_Dmg_03
            $ D_S3_HP -= A_S4_Dmg_03
            $ A_S4_Exp += A_S4_Dmg_03 * D_S3_Level
            $ A_S4_Dmg_03 = 0
        elif A_S4_Dmg_03 < D_S3_HP:
            $ A_S4_Kill += A_S4_Dmg_03
            $ A_S4_Exp += A_S4_Dmg_03 * D_S3_Level
#---------------------------------------------------------------------------------------------------
    if D_S4_CanEvd == 0:
        if A_S4_Dmg_04 >= D_S4_HP:
            $ A_S4_Kill +=  D_S4_HP
            $ D_S4_Killed +=  D_S4_HP
            $ D_S4_Dmg_Rcv +=  D_S4_HP
            $ A_S4_Exp += D_S4_HP * D_S4_Level
            $ A_S4_Dmg_04 = 0
        elif A_S4_Dmg_04 < D_S4_HP and D_S4_Dmg_Rcv >= D_S4_HP:
            $ A_S4_Kill +=  A_S4_Dmg_04
            $ D_S4_Killed += A_S4_Dmg_04
            $ D_S4_HP -= A_S4_Dmg_04
            $ A_S4_Exp += A_S4_Dmg_04 * D_S4_Level
            $ A_S4_Dmg_04 = 0
        elif A_S4_Dmg_04 < D_S4_HP:
            $ A_S4_Kill += A_S4_Dmg_04
            $ A_S4_Exp += A_S4_Dmg_04 * D_S4_Level
#---------------------------------------------------------------------------------------------------
    if D_S5_CanEvd == 0:
        if A_S4_Dmg_05 >= D_S5_HP:
            $ A_S4_Kill +=  D_S5_HP
            $ D_S5_Killed +=  D_S5_HP
            $ D_S5_Dmg_Rcv +=  D_S5_HP
            $ A_S4_Exp += D_S5_HP * D_S5_Level
            $ A_S4_Dmg_05 = 0
        elif A_S4_Dmg_05 < D_S5_HP and D_S5_Dmg_Rcv >= D_S5_HP:
            $ A_S4_Kill +=  A_S4_Dmg_05
            $ D_S5_Killed += A_S4_Dmg_05
            $ D_S5_HP -= A_S4_Dmg_05
            $ A_S4_Exp += A_S4_Dmg_05 * D_S5_Level
            $ A_S4_Dmg_05 = 0
        elif A_S4_Dmg_05 < D_S5_HP:
            $ A_S4_Kill += A_S4_Dmg_05
            $ A_S4_Exp += A_S4_Dmg_05 * D_S5_Level
#---------------------------------------------------------------------------------------------------
    if D_S6_CanEvd == 0:
        if A_S4_Dmg_06 >= D_S6_HP:
            $ A_S4_Kill +=  D_S6_HP
            $ D_S6_Killed +=  D_S6_HP
            $ D_S6_Dmg_Rcv +=  D_S6_HP
            $ A_S4_Exp += D_S6_HP * D_S6_Level
            $ A_S4_Dmg_06 = 0
        elif A_S4_Dmg_06 < D_S6_HP and D_S6_Dmg_Rcv >= D_S6_HP:
            $ A_S4_Kill +=  A_S4_Dmg_06
            $ D_S6_Killed += A_S4_Dmg_06
            $ D_S6_HP -= A_S4_Dmg_06
            $ A_S4_Exp += A_S4_Dmg_06 * D_S6_Level
            $ A_S4_Dmg_06 = 0
        elif A_S4_Dmg_06 < D_S6_HP:
            $ A_S4_Kill += A_S4_Dmg_06
            $ A_S4_Exp += A_S4_Dmg_06 * D_S6_Level

return

#///////////////////////  ATTACKER SLOT 5 - KILL
label BS_A_S5_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if D_S1_CanEvd == 0:
        if A_S5_Dmg_01 >= D_S1_HP:
            $ A_S5_Kill +=  D_S1_HP
            $ D_S1_Killed +=  D_S1_HP
            $ D_S1_Dmg_Rcv +=  D_S1_HP
            $ A_S5_Exp += D_S1_HP * D_S1_Level
            $ A_S5_Dmg_01 = 0
        elif A_S5_Dmg_01 < D_S1_HP and D_S1_Dmg_Rcv >= D_S1_HP:
            $ A_S5_Kill +=  A_S5_Dmg_01
            $ D_S1_Killed += A_S5_Dmg_01
            $ D_S1_HP -= A_S5_Dmg_01
            $ A_S5_Exp += A_S5_Dmg_01 * D_S1_Level
            $ A_S5_Dmg_01 = 0
        elif A_S5_Dmg_01 < D_S1_HP:
            $ A_S5_Kill += A_S5_Dmg_01
            $ A_S5_Exp += A_S5_Dmg_01 * D_S1_Level
#---------------------------------------------------------------------------------------------------
    if D_S2_CanEvd == 0:
        if A_S5_Dmg_02 >= D_S2_HP:
            $ A_S5_Kill +=  D_S2_HP
            $ D_S2_Killed +=  D_S2_HP
            $ D_S2_Dmg_Rcv +=  D_S2_HP
            $ A_S5_Exp += D_S2_HP * D_S2_Level
            $ A_S5_Dmg_02 = 0
        elif A_S5_Dmg_02 < D_S2_HP and D_S2_Dmg_Rcv >= D_S2_HP:
            $ A_S5_Kill +=  A_S5_Dmg_02
            $ D_S2_Killed += A_S5_Dmg_02
            $ D_S2_HP -= A_S5_Dmg_02
            $ A_S5_Exp += A_S5_Dmg_02 * D_S2_Level
            $ A_S5_Dmg_02 = 0
        elif A_S5_Dmg_02 < D_S2_HP:
            $ A_S5_Kill += A_S5_Dmg_02
            $ A_S5_Exp += A_S5_Dmg_02 * D_S2_Level
#---------------------------------------------------------------------------------------------------
    if D_S3_CanEvd == 0:
        if A_S5_Dmg_03 >= D_S3_HP:
            $ A_S5_Kill +=  D_S3_HP
            $ D_S3_Killed +=  D_S3_HP
            $ D_S3_Dmg_Rcv +=  D_S3_HP
            $ A_S5_Exp += D_S3_HP * D_S3_Level
            $ A_S5_Dmg_03 = 0
        elif A_S5_Dmg_03 < D_S3_HP and D_S3_Dmg_Rcv >= D_S3_HP:
            $ A_S5_Kill +=  A_S5_Dmg_03
            $ D_S3_Killed += A_S5_Dmg_03
            $ D_S3_HP -= A_S5_Dmg_03
            $ A_S5_Exp += A_S5_Dmg_03 * D_S3_Level
            $ A_S5_Dmg_03 = 0
        elif A_S5_Dmg_03 < D_S3_HP:
            $ A_S5_Kill += A_S5_Dmg_03
            $ A_S5_Exp += A_S5_Dmg_03 * D_S3_Level
#---------------------------------------------------------------------------------------------------
    if D_S4_CanEvd == 0:
        if A_S5_Dmg_04 >= D_S4_HP:
            $ A_S5_Kill +=  D_S4_HP
            $ D_S4_Killed +=  D_S4_HP
            $ D_S4_Dmg_Rcv +=  D_S4_HP
            $ A_S5_Exp += D_S4_HP * D_S4_Level
            $ A_S5_Dmg_04 = 0
        elif A_S5_Dmg_04 < D_S4_HP and D_S4_Dmg_Rcv >= D_S4_HP:
            $ A_S5_Kill +=  A_S5_Dmg_04
            $ D_S4_Killed += A_S5_Dmg_04
            $ D_S4_HP -= A_S5_Dmg_04
            $ A_S5_Exp += A_S5_Dmg_04 * D_S4_Level
            $ A_S5_Dmg_04 = 0
        elif A_S5_Dmg_04 < D_S4_HP:
            $ A_S5_Kill += A_S5_Dmg_04
            $ A_S5_Exp += A_S5_Dmg_04 * D_S4_Level
#---------------------------------------------------------------------------------------------------
    if D_S5_CanEvd == 0:
        if A_S5_Dmg_05 >= D_S5_HP:
            $ A_S5_Kill +=  D_S5_HP
            $ D_S5_Killed +=  D_S5_HP
            $ D_S5_Dmg_Rcv +=  D_S5_HP
            $ A_S5_Exp += D_S5_HP * D_S5_Level
            $ A_S5_Dmg_05 = 0
        elif A_S5_Dmg_05 < D_S5_HP and D_S5_Dmg_Rcv >= D_S5_HP:
            $ A_S5_Kill +=  A_S5_Dmg_05
            $ D_S5_Killed += A_S5_Dmg_05
            $ D_S5_HP -= A_S5_Dmg_05
            $ A_S5_Exp += A_S5_Dmg_05 * D_S5_Level
            $ A_S5_Dmg_05 = 0
        elif A_S5_Dmg_05 < D_S5_HP:
            $ A_S5_Kill += A_S5_Dmg_05
            $ A_S5_Exp += A_S5_Dmg_05 * D_S5_Level
#---------------------------------------------------------------------------------------------------
    if D_S6_CanEvd == 0:
        if A_S5_Dmg_06 >= D_S6_HP:
            $ A_S5_Kill +=  D_S6_HP
            $ D_S6_Killed +=  D_S6_HP
            $ D_S6_Dmg_Rcv +=  D_S6_HP
            $ A_S5_Exp += D_S6_HP * D_S6_Level
            $ A_S5_Dmg_06 = 0
        elif A_S5_Dmg_06 < D_S6_HP and D_S6_Dmg_Rcv >= D_S6_HP:
            $ A_S5_Kill +=  A_S5_Dmg_06
            $ D_S6_Killed += A_S5_Dmg_06
            $ D_S6_HP -= A_S5_Dmg_06
            $ A_S5_Exp += A_S5_Dmg_06 * D_S6_Level
            $ A_S5_Dmg_06 = 0
        elif A_S5_Dmg_06 < D_S6_HP:
            $ A_S5_Kill += A_S5_Dmg_06
            $ A_S5_Exp += A_S5_Dmg_06 * D_S6_Level

return

#///////////////////////  ATTACKER SLOT 6 - KILL
label BS_A_S6_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if D_S1_CanEvd == 0:
        if A_S6_Dmg_01 >= D_S1_HP:
            $ A_S6_Kill +=  D_S1_HP
            $ D_S1_Killed +=  D_S1_HP
            $ D_S1_Dmg_Rcv +=  D_S1_HP
            $ A_S6_Exp += D_S1_HP * D_S1_Level
            $ A_S6_Dmg_01 = 0
        elif A_S6_Dmg_01 < D_S1_HP and D_S1_Dmg_Rcv >= D_S1_HP:
            $ A_S6_Kill +=  A_S6_Dmg_01
            $ D_S1_Killed += A_S6_Dmg_01
            $ D_S1_HP -= A_S6_Dmg_01
            $ A_S6_Exp += A_S6_Dmg_01 * D_S1_Level
            $ A_S6_Dmg_01 = 0
        elif A_S6_Dmg_01 < D_S1_HP:
            $ A_S6_Kill += A_S6_Dmg_01
            $ A_S6_Exp += A_S6_Dmg_01 * D_S1_Level
#---------------------------------------------------------------------------------------------------
    if D_S2_CanEvd == 0:
        if A_S6_Dmg_02 >= D_S2_HP:
            $ A_S6_Kill +=  D_S2_HP
            $ D_S2_Killed +=  D_S2_HP
            $ D_S2_Dmg_Rcv +=  D_S2_HP
            $ A_S6_Exp += D_S2_HP * D_S2_Level
            $ A_S6_Dmg_02 = 0
        elif A_S6_Dmg_02 < D_S2_HP and D_S2_Dmg_Rcv >= D_S2_HP:
            $ A_S6_Kill +=  A_S6_Dmg_02
            $ D_S2_Killed += A_S6_Dmg_02
            $ D_S2_HP -= A_S6_Dmg_02
            $ A_S6_Exp += A_S6_Dmg_02 * D_S2_Level
            $ A_S6_Dmg_02 = 0
        elif A_S6_Dmg_02 < D_S2_HP:
            $ A_S6_Kill += A_S6_Dmg_02
            $ A_S6_Exp += A_S6_Dmg_02 * D_S2_Level
#---------------------------------------------------------------------------------------------------
    if D_S3_CanEvd == 0:
        if A_S6_Dmg_03 >= D_S3_HP:
            $ A_S6_Kill +=  D_S3_HP
            $ D_S3_Killed +=  D_S3_HP
            $ D_S3_Dmg_Rcv +=  D_S3_HP
            $ A_S6_Exp += D_S3_HP * D_S3_Level
            $ A_S6_Dmg_03 = 0
        elif A_S6_Dmg_03 < D_S3_HP and D_S3_Dmg_Rcv >= D_S3_HP:
            $ A_S6_Kill +=  A_S6_Dmg_03
            $ D_S3_Killed += A_S6_Dmg_03
            $ D_S3_HP -= A_S6_Dmg_03
            $ A_S6_Exp += A_S6_Dmg_03 * D_S3_Level
            $ A_S6_Dmg_03 = 0
        elif A_S6_Dmg_03 < D_S3_HP:
            $ A_S6_Kill += A_S6_Dmg_03
            $ A_S6_Exp += A_S6_Dmg_03 * D_S3_Level
#---------------------------------------------------------------------------------------------------
    if D_S4_CanEvd == 0:
        if A_S6_Dmg_04 >= D_S4_HP:
            $ A_S6_Kill +=  D_S4_HP
            $ D_S4_Killed +=  D_S4_HP
            $ D_S4_Dmg_Rcv +=  D_S4_HP
            $ A_S6_Exp += D_S4_HP * D_S4_Level
            $ A_S6_Dmg_04 = 0
        elif A_S6_Dmg_04 < D_S4_HP and D_S4_Dmg_Rcv >= D_S4_HP:
            $ A_S6_Kill +=  A_S6_Dmg_04
            $ D_S4_Killed += A_S6_Dmg_04
            $ D_S4_HP -= A_S6_Dmg_04
            $ A_S6_Exp += A_S6_Dmg_04 * D_S4_Level
            $ A_S6_Dmg_04 = 0
        elif A_S6_Dmg_04 < D_S4_HP:
            $ A_S6_Kill += A_S6_Dmg_04
            $ A_S6_Exp += A_S6_Dmg_04 * D_S4_Level
#---------------------------------------------------------------------------------------------------
    if D_S5_CanEvd == 0:
        if A_S6_Dmg_05 >= D_S5_HP:
            $ A_S6_Kill +=  D_S5_HP
            $ D_S5_Killed +=  D_S5_HP
            $ D_S5_Dmg_Rcv +=  D_S5_HP
            $ A_S6_Exp += D_S5_HP * D_S5_Level
            $ A_S6_Dmg_05 = 0
        elif A_S6_Dmg_05 < D_S5_HP and D_S5_Dmg_Rcv >= D_S5_HP:
            $ A_S6_Kill +=  A_S6_Dmg_05
            $ D_S5_Killed += A_S6_Dmg_05
            $ D_S5_HP -= A_S6_Dmg_05
            $ A_S6_Exp += A_S6_Dmg_05 * D_S5_Level
            $ A_S6_Dmg_05 = 0
        elif A_S6_Dmg_05 < D_S5_HP:
            $ A_S6_Kill += A_S6_Dmg_05
            $ A_S6_Exp += A_S6_Dmg_05 * D_S5_Level
#---------------------------------------------------------------------------------------------------
    if D_S6_CanEvd == 0:
        if A_S6_Dmg_06 >= D_S6_HP:
            $ A_S6_Kill +=  D_S6_HP
            $ D_S6_Killed +=  D_S6_HP
            $ D_S6_Dmg_Rcv +=  D_S6_HP
            $ A_S6_Exp += D_S6_HP * D_S6_Level
            $ A_S6_Dmg_06 = 0
        elif A_S6_Dmg_06 < D_S6_HP and D_S6_Dmg_Rcv >= D_S6_HP:
            $ A_S6_Kill +=  A_S6_Dmg_06
            $ D_S6_Killed += A_S6_Dmg_06
            $ D_S6_HP -= A_S6_Dmg_06
            $ A_S6_Exp += A_S6_Dmg_06 * D_S6_Level
            $ A_S6_Dmg_06 = 0
        elif A_S6_Dmg_06 < D_S6_HP:
            $ A_S6_Kill += A_S6_Dmg_06
            $ A_S6_Exp += A_S6_Dmg_06 * D_S6_Level

return

#================================================================
#================================================================
#================================================================    
#================================================================  
#================================================================
#================================================================
#================================================================    
#================================================================  

#///////////////////////  DEFFENDER SLOT 1 - KILL
label BS_D_S1_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if A_S1_CanEvd == 0:
        if D_S1_Dmg_01 >= A_S1_HP:
            $ D_S1_Kill +=  A_S1_HP
            $ A_S1_Killed +=  A_S1_HP
            $ A_S1_Dmg_Rcv +=  A_S1_HP
            $ D_S1_Exp += A_S1_HP * A_S1_Level
            $ D_S1_Dmg_01 = 0
        elif D_S1_Dmg_01 < A_S1_HP and A_S1_Dmg_Rcv >= A_S1_HP:
            $ D_S1_Kill +=  D_S1_Dmg_01
            $ A_S1_Killed += D_S1_Dmg_01
            $ A_S1_HP -= D_S1_Dmg_01
            $ D_S1_Exp += D_S1_Dmg_01 * A_S1_Level
            $ D_S1_Dmg_01 = 0
        elif D_S1_Dmg_01 < A_S1_HP:
            $ D_S1_Kill += D_S1_Dmg_01
            $ D_S1_Exp += D_S1_Dmg_01 * A_S1_Level
#---------------------------------------------------------------------------------------------------
    if A_S2_CanEvd == 0:
        if D_S1_Dmg_02 >= A_S2_HP:
            $ D_S1_Kill +=  A_S2_HP
            $ A_S2_Killed +=  A_S2_HP
            $ A_S2_Dmg_Rcv +=  A_S2_HP
            $ D_S1_Exp += A_S2_HP * A_S2_Level
            $ D_S1_Dmg_02 = 0
        elif D_S1_Dmg_02 < A_S2_HP and A_S2_Dmg_Rcv >= A_S2_HP:
            $ D_S1_Kill +=  D_S1_Dmg_02
            $ A_S2_Killed += D_S1_Dmg_02
            $ A_S2_HP -= D_S1_Dmg_02
            $ D_S1_Exp += D_S1_Dmg_02 * A_S2_Level
            $ D_S1_Dmg_02 = 0
        elif D_S1_Dmg_02 < A_S2_HP:
            $ D_S1_Kill += D_S1_Dmg_02
            $ D_S1_Exp += D_S1_Dmg_02 * A_S2_Level
#---------------------------------------------------------------------------------------------------
    if A_S3_CanEvd == 0:
        if D_S1_Dmg_03 >= A_S3_HP:
            $ D_S1_Kill +=  A_S3_HP
            $ A_S3_Killed +=  A_S3_HP
            $ A_S3_Dmg_Rcv +=  A_S3_HP
            $ D_S1_Exp += A_S3_HP * A_S3_Level
            $ D_S1_Dmg_03 = 0
        elif D_S1_Dmg_03 < A_S3_HP and A_S3_Dmg_Rcv >= A_S3_HP:
            $ D_S1_Kill +=  D_S1_Dmg_03
            $ A_S3_Killed += D_S1_Dmg_03
            $ A_S3_HP -= D_S1_Dmg_03
            $ D_S1_Exp += D_S1_Dmg_03 * A_S3_Level
            $ D_S1_Dmg_03 = 0
        elif D_S1_Dmg_03 < A_S3_HP:
            $ D_S1_Kill += D_S1_Dmg_03
            $ D_S1_Exp += D_S1_Dmg_03 * A_S3_Level
#---------------------------------------------------------------------------------------------------
    if A_S4_CanEvd == 0:
        if D_S1_Dmg_04 >= A_S4_HP:
            $ D_S1_Kill +=  A_S4_HP
            $ A_S4_Killed +=  A_S4_HP
            $ A_S4_Dmg_Rcv +=  A_S4_HP
            $ D_S1_Exp += A_S4_HP * A_S4_Level
            $ D_S1_Dmg_04 = 0
        elif D_S1_Dmg_04 < A_S4_HP and A_S4_Dmg_Rcv >= A_S4_HP:
            $ D_S1_Kill +=  D_S1_Dmg_04
            $ A_S4_Killed += D_S1_Dmg_04
            $ A_S4_HP -= D_S1_Dmg_04
            $ D_S1_Exp += D_S1_Dmg_04 * A_S4_Level
            $ D_S1_Dmg_04 = 0
        elif D_S1_Dmg_04 < A_S4_HP:
            $ D_S1_Kill += D_S1_Dmg_04
            $ D_S1_Exp += D_S1_Dmg_04 * A_S4_Level
#---------------------------------------------------------------------------------------------------
    if A_S5_CanEvd == 0:
        if D_S1_Dmg_05 >= A_S5_HP:
            $ D_S1_Kill +=  A_S5_HP
            $ A_S5_Killed +=  A_S5_HP
            $ A_S5_Dmg_Rcv +=  A_S5_HP
            $ D_S1_Exp += A_S5_HP * A_S5_Level
            $ D_S1_Dmg_05 = 0
        elif D_S1_Dmg_05 < A_S5_HP and A_S5_Dmg_Rcv >= A_S5_HP:
            $ D_S1_Kill +=  D_S1_Dmg_05
            $ A_S5_Killed += D_S1_Dmg_05
            $ A_S5_HP -= D_S1_Dmg_05
            $ D_S1_Exp += D_S1_Dmg_05 * A_S5_Level
            $ D_S1_Dmg_05 = 0
        elif D_S1_Dmg_05 < A_S5_HP:
            $ D_S1_Kill += D_S1_Dmg_05
            $ D_S1_Exp += D_S1_Dmg_05 * A_S5_Level
#---------------------------------------------------------------------------------------------------
    if A_S6_CanEvd == 0:
        if D_S1_Dmg_06 >= A_S6_HP:
            $ D_S1_Kill +=  A_S6_HP
            $ A_S6_Killed +=  A_S6_HP
            $ A_S6_Dmg_Rcv +=  A_S6_HP
            $ D_S1_Exp += A_S6_HP * A_S6_Level
            $ D_S1_Dmg_06 = 0
        elif D_S1_Dmg_06 < A_S6_HP and A_S6_Dmg_Rcv >= A_S6_HP:
            $ D_S1_Kill +=  D_S1_Dmg_06
            $ A_S6_Killed += D_S1_Dmg_06
            $ A_S6_HP -= D_S1_Dmg_06
            $ D_S1_Exp += D_S1_Dmg_06 * A_S6_Level
            $ D_S1_Dmg_06 = 0
        elif D_S1_Dmg_06 < A_S6_HP:
            $ D_S1_Kill += D_S1_Dmg_06
            $ D_S1_Exp += D_S1_Dmg_06 * A_S6_Level

return

#///////////////////////  DEFFENDER SLOT 2 - KILL
label BS_D_S2_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if A_S1_CanEvd == 0:
        if D_S2_Dmg_01 >= A_S1_HP:
            $ D_S2_Kill +=  A_S1_HP
            $ A_S1_Killed +=  A_S1_HP
            $ A_S1_Dmg_Rcv +=  A_S1_HP
            $ D_S2_Exp += A_S1_HP * A_S1_Level
            $ D_S2_Dmg_01 = 0
        elif D_S2_Dmg_01 < A_S1_HP and A_S1_Dmg_Rcv >= A_S1_HP:
            $ D_S2_Kill +=  D_S2_Dmg_01
            $ A_S1_Killed += D_S2_Dmg_01
            $ A_S1_HP -= D_S2_Dmg_01
            $ D_S2_Exp += D_S2_Dmg_01 * A_S1_Level
            $ D_S2_Dmg_01 = 0
        elif D_S2_Dmg_01 < A_S1_HP:
            $ D_S2_Kill += D_S2_Dmg_01
            $ D_S2_Exp += D_S2_Dmg_01 * A_S1_Level
#---------------------------------------------------------------------------------------------------
    if A_S2_CanEvd == 0:
        if D_S2_Dmg_02 >= A_S2_HP:
            $ D_S2_Kill +=  A_S2_HP
            $ A_S2_Killed +=  A_S2_HP
            $ A_S2_Dmg_Rcv +=  A_S2_HP
            $ D_S2_Exp += A_S2_HP * A_S2_Level
            $ D_S2_Dmg_02 = 0
        elif D_S2_Dmg_02 < A_S2_HP and A_S2_Dmg_Rcv >= A_S2_HP:
            $ D_S2_Kill +=  D_S2_Dmg_02
            $ A_S2_Killed += D_S2_Dmg_02
            $ A_S2_HP -= D_S2_Dmg_02
            $ D_S2_Exp += D_S2_Dmg_02 * A_S2_Level
            $ D_S2_Dmg_02 = 0
        elif D_S2_Dmg_02 < A_S2_HP:
            $ D_S2_Kill += D_S2_Dmg_02
            $ D_S2_Exp += D_S2_Dmg_02 * A_S2_Level
#---------------------------------------------------------------------------------------------------
    if A_S3_CanEvd == 0:
        if D_S2_Dmg_03 >= A_S3_HP:
            $ D_S2_Kill +=  A_S3_HP
            $ A_S3_Killed +=  A_S3_HP
            $ A_S3_Dmg_Rcv +=  A_S3_HP
            $ D_S2_Exp += A_S3_HP * A_S3_Level
            $ D_S2_Dmg_03 = 0
        elif D_S2_Dmg_03 < A_S3_HP and A_S3_Dmg_Rcv >= A_S3_HP:
            $ D_S2_Kill +=  D_S2_Dmg_03
            $ A_S3_Killed += D_S2_Dmg_03
            $ A_S3_HP -= D_S2_Dmg_03
            $ D_S2_Exp += D_S2_Dmg_03 * A_S3_Level
            $ D_S2_Dmg_03 = 0
        elif D_S2_Dmg_03 < A_S3_HP:
            $ D_S2_Kill += D_S2_Dmg_03
            $ D_S2_Exp += D_S2_Dmg_03 * A_S3_Level
#---------------------------------------------------------------------------------------------------
    if A_S4_CanEvd == 0:
        if D_S2_Dmg_04 >= A_S4_HP:
            $ D_S2_Kill +=  A_S4_HP
            $ A_S4_Killed +=  A_S4_HP
            $ A_S4_Dmg_Rcv +=  A_S4_HP
            $ D_S2_Exp += A_S4_HP * A_S4_Level
            $ D_S2_Dmg_04 = 0
        elif D_S2_Dmg_04 < A_S4_HP and A_S4_Dmg_Rcv >= A_S4_HP:
            $ D_S2_Kill +=  D_S2_Dmg_04
            $ A_S4_Killed += D_S2_Dmg_04
            $ A_S4_HP -= D_S2_Dmg_04
            $ D_S2_Exp += D_S2_Dmg_04 * A_S4_Level
            $ D_S2_Dmg_04 = 0
        elif D_S2_Dmg_04 < A_S4_HP:
            $ D_S2_Kill += D_S2_Dmg_04
            $ D_S2_Exp += D_S2_Dmg_04 * A_S4_Level
#---------------------------------------------------------------------------------------------------
    if A_S5_CanEvd == 0:
        if D_S2_Dmg_05 >= A_S5_HP:
            $ D_S2_Kill +=  A_S5_HP
            $ A_S5_Killed +=  A_S5_HP
            $ A_S5_Dmg_Rcv +=  A_S5_HP
            $ D_S2_Exp += A_S5_HP * A_S5_Level
            $ D_S2_Dmg_05 = 0
        elif D_S2_Dmg_05 < A_S5_HP and A_S5_Dmg_Rcv >= A_S5_HP:
            $ D_S2_Kill +=  D_S2_Dmg_05
            $ A_S5_Killed += D_S2_Dmg_05
            $ A_S5_HP -= D_S2_Dmg_05
            $ D_S2_Exp += D_S2_Dmg_05 * A_S5_Level
            $ D_S2_Dmg_05 = 0
        elif D_S2_Dmg_05 < A_S5_HP:
            $ D_S2_Kill += D_S2_Dmg_05
            $ D_S2_Exp += D_S2_Dmg_05 * A_S5_Level
#---------------------------------------------------------------------------------------------------
    if A_S6_CanEvd == 0:
        if D_S2_Dmg_06 >= A_S6_HP:
            $ D_S2_Kill +=  A_S6_HP
            $ A_S6_Killed +=  A_S6_HP
            $ A_S6_Dmg_Rcv +=  A_S6_HP
            $ D_S2_Exp += A_S6_HP * A_S6_Level
            $ D_S2_Dmg_06 = 0
        elif D_S2_Dmg_06 < A_S6_HP and A_S6_Dmg_Rcv >= A_S6_HP:
            $ D_S2_Kill +=  D_S2_Dmg_06
            $ A_S6_Killed += D_S2_Dmg_06
            $ A_S6_HP -= D_S2_Dmg_06
            $ D_S2_Exp += D_S2_Dmg_06 * A_S6_Level
            $ D_S2_Dmg_06 = 0
        elif D_S2_Dmg_06 < A_S6_HP:
            $ D_S2_Kill += D_S2_Dmg_06
            $ D_S2_Exp += D_S2_Dmg_06 * A_S6_Level

return

#///////////////////////  DEFFENDER SLOT 3 - KILL
label BS_D_S3_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if A_S1_CanEvd == 0:
        if D_S3_Dmg_01 >= A_S1_HP:
            $ D_S3_Kill +=  A_S1_HP
            $ A_S1_Killed +=  A_S1_HP
            $ A_S1_Dmg_Rcv +=  A_S1_HP
            $ D_S3_Exp += A_S1_HP * A_S1_Level
            $ D_S3_Dmg_01 = 0
        elif D_S3_Dmg_01 < A_S1_HP and A_S1_Dmg_Rcv >= A_S1_HP:
            $ D_S3_Kill +=  D_S3_Dmg_01
            $ A_S1_Killed += D_S3_Dmg_01
            $ A_S1_HP -= D_S3_Dmg_01
            $ D_S3_Exp += D_S3_Dmg_01 * A_S1_Level
            $ D_S3_Dmg_01 = 0
        elif D_S3_Dmg_01 < A_S1_HP:
            $ D_S3_Kill += D_S3_Dmg_01
            $ D_S3_Exp += D_S3_Dmg_01 * A_S1_Level
#---------------------------------------------------------------------------------------------------
    if A_S2_CanEvd == 0:
        if D_S3_Dmg_02 >= A_S2_HP:
            $ D_S3_Kill +=  A_S2_HP
            $ A_S2_Killed +=  A_S2_HP
            $ A_S2_Dmg_Rcv +=  A_S2_HP
            $ D_S3_Exp += A_S2_HP * A_S2_Level
            $ D_S3_Dmg_02 = 0
        elif D_S3_Dmg_02 < A_S2_HP and A_S2_Dmg_Rcv >= A_S2_HP:
            $ D_S3_Kill +=  D_S3_Dmg_02
            $ A_S2_Killed += D_S3_Dmg_02
            $ A_S2_HP -= D_S3_Dmg_02
            $ D_S3_Exp += D_S3_Dmg_02 * A_S2_Level
            $ D_S3_Dmg_02 = 0
        elif D_S3_Dmg_02 < A_S2_HP:
            $ D_S3_Kill += D_S3_Dmg_02
            $ D_S3_Exp += D_S3_Dmg_02 * A_S2_Level
#---------------------------------------------------------------------------------------------------
    if A_S3_CanEvd == 0:
        if D_S3_Dmg_03 >= A_S3_HP:
            $ D_S3_Kill +=  A_S3_HP
            $ A_S3_Killed +=  A_S3_HP
            $ A_S3_Dmg_Rcv +=  A_S3_HP
            $ D_S3_Exp += A_S3_HP * A_S3_Level
            $ D_S3_Dmg_03 = 0
        elif D_S3_Dmg_03 < A_S3_HP and A_S3_Dmg_Rcv >= A_S3_HP:
            $ D_S3_Kill +=  D_S3_Dmg_03
            $ A_S3_Killed += D_S3_Dmg_03
            $ A_S3_HP -= D_S3_Dmg_03
            $ D_S3_Exp += D_S3_Dmg_03 * A_S3_Level
            $ D_S3_Dmg_03 = 0
        elif D_S3_Dmg_03 < A_S3_HP:
            $ D_S3_Kill += D_S3_Dmg_03
            $ D_S3_Exp += D_S3_Dmg_03 * A_S3_Level
#---------------------------------------------------------------------------------------------------
    if A_S4_CanEvd == 0:
        if D_S3_Dmg_04 >= A_S4_HP:
            $ D_S3_Kill +=  A_S4_HP
            $ A_S4_Killed +=  A_S4_HP
            $ A_S4_Dmg_Rcv +=  A_S4_HP
            $ D_S3_Exp += A_S4_HP * A_S4_Level
            $ D_S3_Dmg_04 = 0
        elif D_S3_Dmg_04 < A_S4_HP and A_S4_Dmg_Rcv >= A_S4_HP:
            $ D_S3_Kill +=  D_S3_Dmg_04
            $ A_S4_Killed += D_S3_Dmg_04
            $ A_S4_HP -= D_S3_Dmg_04
            $ D_S3_Exp += D_S3_Dmg_04 * A_S4_Level
            $ D_S3_Dmg_04 = 0
        elif D_S3_Dmg_04 < A_S4_HP:
            $ D_S3_Kill += D_S3_Dmg_04
            $ D_S3_Exp += D_S3_Dmg_04 * A_S4_Level
#---------------------------------------------------------------------------------------------------
    if A_S5_CanEvd == 0:
        if D_S3_Dmg_05 >= A_S5_HP:
            $ D_S3_Kill +=  A_S5_HP
            $ A_S5_Killed +=  A_S5_HP
            $ A_S5_Dmg_Rcv +=  A_S5_HP
            $ D_S3_Exp += A_S5_HP * A_S5_Level
            $ D_S3_Dmg_05 = 0
        elif D_S3_Dmg_05 < A_S5_HP and A_S5_Dmg_Rcv >= A_S5_HP:
            $ D_S3_Kill +=  D_S3_Dmg_05
            $ A_S5_Killed += D_S3_Dmg_05
            $ A_S5_HP -= D_S3_Dmg_05
            $ D_S3_Exp += D_S3_Dmg_05 * A_S5_Level
            $ D_S3_Dmg_05 = 0
        elif D_S3_Dmg_05 < A_S5_HP:
            $ D_S3_Kill += D_S3_Dmg_05
            $ D_S3_Exp += D_S3_Dmg_05 * A_S5_Level
#---------------------------------------------------------------------------------------------------
    if A_S6_CanEvd == 0:
        if D_S3_Dmg_06 >= A_S6_HP:
            $ D_S3_Kill +=  A_S6_HP
            $ A_S6_Killed +=  A_S6_HP
            $ A_S6_Dmg_Rcv +=  A_S6_HP
            $ D_S3_Exp += A_S6_HP * A_S6_Level
            $ D_S3_Dmg_06 = 0
        elif D_S3_Dmg_06 < A_S6_HP and A_S6_Dmg_Rcv >= A_S6_HP:
            $ D_S3_Kill +=  D_S3_Dmg_06
            $ A_S6_Killed += D_S3_Dmg_06
            $ A_S6_HP -= D_S3_Dmg_06
            $ D_S3_Exp += D_S3_Dmg_06 * A_S6_Level
            $ D_S3_Dmg_06 = 0
        elif D_S3_Dmg_06 < A_S6_HP:
            $ D_S3_Kill += D_S3_Dmg_06
            $ D_S3_Exp += D_S3_Dmg_06 * A_S6_Level

return

#///////////////////////  DEFFENDER SLOT 4 - KILL
label BS_D_S4_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if A_S1_CanEvd == 0:
        if D_S4_Dmg_01 >= A_S1_HP:
            $ D_S4_Kill +=  A_S1_HP
            $ A_S1_Killed +=  A_S1_HP
            $ A_S1_Dmg_Rcv +=  A_S1_HP
            $ D_S4_Exp += A_S1_HP * A_S1_Level
            $ D_S4_Dmg_01 = 0
        elif D_S4_Dmg_01 < A_S1_HP and A_S1_Dmg_Rcv >= A_S1_HP:
            $ D_S4_Kill +=  D_S4_Dmg_01
            $ A_S1_Killed += D_S4_Dmg_01
            $ A_S1_HP -= D_S4_Dmg_01
            $ D_S4_Exp += D_S4_Dmg_01 * A_S1_Level
            $ D_S4_Dmg_01 = 0
        elif D_S4_Dmg_01 < A_S1_HP:
            $ D_S4_Kill += D_S4_Dmg_01
            $ D_S4_Exp += D_S4_Dmg_01 * A_S1_Level
#---------------------------------------------------------------------------------------------------
    if A_S2_CanEvd == 0:
        if D_S4_Dmg_02 >= A_S2_HP:
            $ D_S4_Kill +=  A_S2_HP
            $ A_S2_Killed +=  A_S2_HP
            $ A_S2_Dmg_Rcv +=  A_S2_HP
            $ D_S4_Exp += A_S2_HP * A_S2_Level
            $ D_S4_Dmg_02 = 0
        elif D_S4_Dmg_02 < A_S2_HP and A_S2_Dmg_Rcv >= A_S2_HP:
            $ D_S4_Kill +=  D_S4_Dmg_02
            $ A_S2_Killed += D_S4_Dmg_02
            $ A_S2_HP -= D_S4_Dmg_02
            $ D_S4_Exp += D_S4_Dmg_02 * A_S2_Level
            $ D_S4_Dmg_02 = 0
        elif D_S4_Dmg_02 < A_S2_HP:
            $ D_S4_Kill += D_S4_Dmg_02
            $ D_S4_Exp += D_S4_Dmg_02 * A_S2_Level
#---------------------------------------------------------------------------------------------------
    if A_S3_CanEvd == 0:
        if D_S4_Dmg_03 >= A_S3_HP:
            $ D_S4_Kill +=  A_S3_HP
            $ A_S3_Killed +=  A_S3_HP
            $ A_S3_Dmg_Rcv +=  A_S3_HP
            $ D_S4_Exp += A_S3_HP * A_S3_Level
            $ D_S4_Dmg_03 = 0
        elif D_S4_Dmg_03 < A_S3_HP and A_S3_Dmg_Rcv >= A_S3_HP:
            $ D_S4_Kill +=  D_S4_Dmg_03
            $ A_S3_Killed += D_S4_Dmg_03
            $ A_S3_HP -= D_S4_Dmg_03
            $ D_S4_Exp += D_S4_Dmg_03 * A_S3_Level
            $ D_S4_Dmg_03 = 0
        elif D_S4_Dmg_03 < A_S3_HP:
            $ D_S4_Kill += D_S4_Dmg_03
            $ D_S4_Exp += D_S4_Dmg_03 * A_S3_Level
#---------------------------------------------------------------------------------------------------
    if A_S4_CanEvd == 0:
        if D_S4_Dmg_04 >= A_S4_HP:
            $ D_S4_Kill +=  A_S4_HP
            $ A_S4_Killed +=  A_S4_HP
            $ A_S4_Dmg_Rcv +=  A_S4_HP
            $ D_S4_Exp += A_S4_HP * A_S4_Level
            $ D_S4_Dmg_04 = 0
        elif D_S4_Dmg_04 < A_S4_HP and A_S4_Dmg_Rcv >= A_S4_HP:
            $ D_S4_Kill +=  D_S4_Dmg_04
            $ A_S4_Killed += D_S4_Dmg_04
            $ A_S4_HP -= D_S4_Dmg_04
            $ D_S4_Exp += D_S4_Dmg_04 * A_S4_Level
            $ D_S4_Dmg_04 = 0
        elif D_S4_Dmg_04 < A_S4_HP:
            $ D_S4_Kill += D_S4_Dmg_04
            $ D_S4_Exp += D_S4_Dmg_04 * A_S4_Level
#---------------------------------------------------------------------------------------------------
    if A_S5_CanEvd == 0:
        if D_S4_Dmg_05 >= A_S5_HP:
            $ D_S4_Kill +=  A_S5_HP
            $ A_S5_Killed +=  A_S5_HP
            $ A_S5_Dmg_Rcv +=  A_S5_HP
            $ D_S4_Exp += A_S5_HP * A_S5_Level
            $ D_S4_Dmg_05 = 0
        elif D_S4_Dmg_05 < A_S5_HP and A_S5_Dmg_Rcv >= A_S5_HP:
            $ D_S4_Kill +=  D_S4_Dmg_05
            $ A_S5_Killed += D_S4_Dmg_05
            $ A_S5_HP -= D_S4_Dmg_05
            $ D_S4_Exp += D_S4_Dmg_05 * A_S5_Level
            $ D_S4_Dmg_05 = 0
        elif D_S4_Dmg_05 < A_S5_HP:
            $ D_S4_Kill += D_S4_Dmg_05
            $ D_S4_Exp += D_S4_Dmg_05 * A_S5_Level
#---------------------------------------------------------------------------------------------------
    if A_S6_CanEvd == 0:
        if D_S4_Dmg_06 >= A_S6_HP:
            $ D_S4_Kill +=  A_S6_HP
            $ A_S6_Killed +=  A_S6_HP
            $ A_S6_Dmg_Rcv +=  A_S6_HP
            $ D_S4_Exp += A_S6_HP * A_S6_Level
            $ D_S4_Dmg_06 = 0
        elif D_S4_Dmg_06 < A_S6_HP and A_S6_Dmg_Rcv >= A_S6_HP:
            $ D_S4_Kill +=  D_S4_Dmg_06
            $ A_S6_Killed += D_S4_Dmg_06
            $ A_S6_HP -= D_S4_Dmg_06
            $ D_S4_Exp += D_S4_Dmg_06 * A_S6_Level
            $ D_S4_Dmg_06 = 0
        elif D_S4_Dmg_06 < A_S6_HP:
            $ D_S4_Kill += D_S4_Dmg_06
            $ D_S4_Exp += D_S4_Dmg_06 * A_S6_Level

return

#///////////////////////  DEFFENDER SLOT 5 - KILL
label BS_D_S5_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if A_S1_CanEvd == 0:
        if D_S5_Dmg_01 >= A_S1_HP:
            $ D_S5_Kill +=  A_S1_HP
            $ A_S1_Killed +=  A_S1_HP
            $ A_S1_Dmg_Rcv +=  A_S1_HP
            $ D_S5_Exp += A_S1_HP * A_S1_Level
            $ D_S5_Dmg_01 = 0
        elif D_S5_Dmg_01 < A_S1_HP and A_S1_Dmg_Rcv >= A_S1_HP:
            $ D_S5_Kill +=  D_S5_Dmg_01
            $ A_S1_Killed += D_S5_Dmg_01
            $ A_S1_HP -= D_S5_Dmg_01
            $ D_S5_Exp += D_S5_Dmg_01 * A_S1_Level
            $ D_S5_Dmg_01 = 0
        elif D_S5_Dmg_01 < A_S1_HP:
            $ D_S5_Kill += D_S5_Dmg_01
            $ D_S5_Exp += D_S5_Dmg_01 * A_S1_Level
#---------------------------------------------------------------------------------------------------
    if A_S2_CanEvd == 0:
        if D_S5_Dmg_02 >= A_S2_HP:
            $ D_S5_Kill +=  A_S2_HP
            $ A_S2_Killed +=  A_S2_HP
            $ A_S2_Dmg_Rcv +=  A_S2_HP
            $ D_S5_Exp += A_S2_HP * A_S2_Level
            $ D_S5_Dmg_02 = 0
        elif D_S5_Dmg_02 < A_S2_HP and A_S2_Dmg_Rcv >= A_S2_HP:
            $ D_S5_Kill +=  D_S5_Dmg_02
            $ A_S2_Killed += D_S5_Dmg_02
            $ A_S2_HP -= D_S5_Dmg_02
            $ D_S5_Exp += D_S5_Dmg_02 * A_S2_Level
            $ D_S5_Dmg_02 = 0
        elif D_S5_Dmg_02 < A_S2_HP:
            $ D_S5_Kill += D_S5_Dmg_02
            $ D_S5_Exp += D_S5_Dmg_02 * A_S2_Level
#---------------------------------------------------------------------------------------------------
    if A_S3_CanEvd == 0:
        if D_S5_Dmg_03 >= A_S3_HP:
            $ D_S5_Kill +=  A_S3_HP
            $ A_S3_Killed +=  A_S3_HP
            $ A_S3_Dmg_Rcv +=  A_S3_HP
            $ D_S5_Exp += A_S3_HP * A_S3_Level
            $ D_S5_Dmg_03 = 0
        elif D_S5_Dmg_03 < A_S3_HP and A_S3_Dmg_Rcv >= A_S3_HP:
            $ D_S5_Kill +=  D_S5_Dmg_03
            $ A_S3_Killed += D_S5_Dmg_03
            $ A_S3_HP -= D_S5_Dmg_03
            $ D_S5_Exp += D_S5_Dmg_03 * A_S3_Level
            $ D_S5_Dmg_03 = 0
        elif D_S5_Dmg_03 < A_S3_HP:
            $ D_S5_Kill += D_S5_Dmg_03
            $ D_S5_Exp += D_S5_Dmg_03 * A_S3_Level
#---------------------------------------------------------------------------------------------------
    if A_S4_CanEvd == 0:
        if D_S5_Dmg_04 >= A_S4_HP:
            $ D_S5_Kill +=  A_S4_HP
            $ A_S4_Killed +=  A_S4_HP
            $ A_S4_Dmg_Rcv +=  A_S4_HP
            $ D_S5_Exp += A_S4_HP * A_S4_Level
            $ D_S5_Dmg_04 = 0
        elif D_S5_Dmg_04 < A_S4_HP and A_S4_Dmg_Rcv >= A_S4_HP:
            $ D_S5_Kill +=  D_S5_Dmg_04
            $ A_S4_Killed += D_S5_Dmg_04
            $ A_S4_HP -= D_S5_Dmg_04
            $ D_S5_Exp += D_S5_Dmg_04 * A_S4_Level
            $ D_S5_Dmg_04 = 0
        elif D_S5_Dmg_04 < A_S4_HP:
            $ D_S5_Kill += D_S5_Dmg_04
            $ D_S5_Exp += D_S5_Dmg_04 * A_S4_Level
#---------------------------------------------------------------------------------------------------
    if A_S5_CanEvd == 0:
        if D_S5_Dmg_05 >= A_S5_HP:
            $ D_S5_Kill +=  A_S5_HP
            $ A_S5_Killed +=  A_S5_HP
            $ A_S5_Dmg_Rcv +=  A_S5_HP
            $ D_S5_Exp += A_S5_HP * A_S5_Level
            $ D_S5_Dmg_05 = 0
        elif D_S5_Dmg_05 < A_S5_HP and A_S5_Dmg_Rcv >= A_S5_HP:
            $ D_S5_Kill +=  D_S5_Dmg_05
            $ A_S5_Killed += D_S5_Dmg_05
            $ A_S5_HP -= D_S5_Dmg_05
            $ D_S5_Exp += D_S5_Dmg_05 * A_S5_Level
            $ D_S5_Dmg_05 = 0
        elif D_S5_Dmg_05 < A_S5_HP:
            $ D_S5_Kill += D_S5_Dmg_05
            $ D_S5_Exp += D_S5_Dmg_05 * A_S5_Level
#---------------------------------------------------------------------------------------------------
    if A_S6_CanEvd == 0:
        if D_S5_Dmg_06 >= A_S6_HP:
            $ D_S5_Kill +=  A_S6_HP
            $ A_S6_Killed +=  A_S6_HP
            $ A_S6_Dmg_Rcv +=  A_S6_HP
            $ D_S5_Exp += A_S6_HP * A_S6_Level
            $ D_S5_Dmg_06 = 0
        elif D_S5_Dmg_06 < A_S6_HP and A_S6_Dmg_Rcv >= A_S6_HP:
            $ D_S5_Kill +=  D_S5_Dmg_06
            $ A_S6_Killed += D_S5_Dmg_06
            $ A_S6_HP -= D_S5_Dmg_06
            $ D_S5_Exp += D_S5_Dmg_06 * A_S6_Level
            $ D_S5_Dmg_06 = 0
        elif D_S5_Dmg_06 < A_S6_HP:
            $ D_S5_Kill += D_S5_Dmg_06
            $ D_S5_Exp += D_S5_Dmg_06 * A_S6_Level

return

#///////////////////////  DEFFENDER SLOT 6 - KILL
label BS_D_S6_Chk_Kil:

#---------------------------------------------------------------------------------------------------
    if A_S1_CanEvd == 0:
        if D_S6_Dmg_01 >= A_S1_HP:
            $ D_S6_Kill +=  A_S1_HP
            $ A_S1_Killed +=  A_S1_HP
            $ A_S1_Dmg_Rcv +=  A_S1_HP
            $ D_S6_Exp += A_S1_HP * A_S1_Level
            $ D_S6_Dmg_01 = 0
        elif D_S6_Dmg_01 < A_S1_HP and A_S1_Dmg_Rcv >= A_S1_HP:
            $ D_S6_Kill +=  D_S6_Dmg_01
            $ A_S1_Killed += D_S6_Dmg_01
            $ A_S1_HP -= D_S6_Dmg_01
            $ D_S6_Exp += D_S6_Dmg_01 * A_S1_Level
            $ D_S6_Dmg_01 = 0
        elif D_S6_Dmg_01 < A_S1_HP:
            $ D_S6_Kill += D_S6_Dmg_01
            $ D_S6_Exp += D_S6_Dmg_01 * A_S1_Level
#---------------------------------------------------------------------------------------------------
    if A_S2_CanEvd == 0:
        if D_S6_Dmg_02 >= A_S2_HP:
            $ D_S6_Kill +=  A_S2_HP
            $ A_S2_Killed +=  A_S2_HP
            $ A_S2_Dmg_Rcv +=  A_S2_HP
            $ D_S6_Exp += A_S2_HP * A_S2_Level
            $ D_S6_Dmg_02 = 0
        elif D_S6_Dmg_02 < A_S2_HP and A_S2_Dmg_Rcv >= A_S2_HP:
            $ D_S6_Kill +=  D_S6_Dmg_02
            $ A_S2_Killed += D_S6_Dmg_02
            $ A_S2_HP -= D_S6_Dmg_02
            $ D_S6_Exp += D_S6_Dmg_02 * A_S2_Level
            $ D_S6_Dmg_02 = 0
        elif D_S6_Dmg_02 < A_S2_HP:
            $ D_S6_Kill += D_S6_Dmg_02
            $ D_S6_Exp += D_S6_Dmg_02 * A_S2_Level
#---------------------------------------------------------------------------------------------------
    if A_S3_CanEvd == 0:
        if D_S6_Dmg_03 >= A_S3_HP:
            $ D_S6_Kill +=  A_S3_HP
            $ A_S3_Killed +=  A_S3_HP
            $ A_S3_Dmg_Rcv +=  A_S3_HP
            $ D_S6_Exp += A_S3_HP * A_S3_Level
            $ D_S6_Dmg_03 = 0
        elif D_S6_Dmg_03 < A_S3_HP and A_S3_Dmg_Rcv >= A_S3_HP:
            $ D_S6_Kill +=  D_S6_Dmg_03
            $ A_S3_Killed += D_S6_Dmg_03
            $ A_S3_HP -= D_S6_Dmg_03
            $ D_S6_Exp += D_S6_Dmg_03 * A_S3_Level
            $ D_S6_Dmg_03 = 0
        elif D_S6_Dmg_03 < A_S3_HP:
            $ D_S6_Kill += D_S6_Dmg_03
            $ D_S6_Exp += D_S6_Dmg_03 * A_S3_Level
#---------------------------------------------------------------------------------------------------
    if A_S4_CanEvd == 0:
        if D_S6_Dmg_04 >= A_S4_HP:
            $ D_S6_Kill +=  A_S4_HP
            $ A_S4_Killed +=  A_S4_HP
            $ A_S4_Dmg_Rcv +=  A_S4_HP
            $ D_S6_Exp += A_S4_HP * A_S4_Level
            $ D_S6_Dmg_04 = 0
        elif D_S6_Dmg_04 < A_S4_HP and A_S4_Dmg_Rcv >= A_S4_HP:
            $ D_S6_Kill +=  D_S6_Dmg_04
            $ A_S4_Killed += D_S6_Dmg_04
            $ A_S4_HP -= D_S6_Dmg_04
            $ D_S6_Exp += D_S6_Dmg_04 * A_S4_Level
            $ D_S6_Dmg_04 = 0
        elif D_S6_Dmg_04 < A_S4_HP:
            $ D_S6_Kill += D_S6_Dmg_04
            $ D_S6_Exp += D_S6_Dmg_04 * A_S4_Level
#---------------------------------------------------------------------------------------------------
    if A_S5_CanEvd == 0:
        if D_S6_Dmg_05 >= A_S5_HP:
            $ D_S6_Kill +=  A_S5_HP
            $ A_S5_Killed +=  A_S5_HP
            $ A_S5_Dmg_Rcv +=  A_S5_HP
            $ D_S6_Exp += A_S5_HP * A_S5_Level
            $ D_S6_Dmg_05 = 0
        elif D_S6_Dmg_05 < A_S5_HP and A_S5_Dmg_Rcv >= A_S5_HP:
            $ D_S6_Kill +=  D_S6_Dmg_05
            $ A_S5_Killed += D_S6_Dmg_05
            $ A_S5_HP -= D_S6_Dmg_05
            $ D_S6_Exp += D_S6_Dmg_05 * A_S5_Level
            $ D_S6_Dmg_05 = 0
        elif D_S6_Dmg_05 < A_S5_HP:
            $ D_S6_Kill += D_S6_Dmg_05
            $ D_S6_Exp += D_S6_Dmg_05 * A_S5_Level
#---------------------------------------------------------------------------------------------------
    if A_S6_CanEvd == 0:
        if D_S6_Dmg_06 >= A_S6_HP:
            $ D_S6_Kill +=  A_S6_HP
            $ A_S6_Killed +=  A_S6_HP
            $ A_S6_Dmg_Rcv +=  A_S6_HP
            $ D_S6_Exp += A_S6_HP * A_S6_Level
            $ D_S6_Dmg_06 = 0
        elif D_S6_Dmg_06 < A_S6_HP and A_S6_Dmg_Rcv >= A_S6_HP:
            $ D_S6_Kill +=  D_S6_Dmg_06
            $ A_S6_Killed += D_S6_Dmg_06
            $ A_S6_HP -= D_S6_Dmg_06
            $ D_S6_Exp += D_S6_Dmg_06 * A_S6_Level
            $ D_S6_Dmg_06 = 0
        elif D_S6_Dmg_06 < A_S6_HP:
            $ D_S6_Kill += D_S6_Dmg_06
            $ D_S6_Exp += D_S6_Dmg_06 * A_S6_Level

return

#================================================================
#================================================================
#================================================================    
#================================================================  
#================================================================
#================================================================
#================================================================    
#================================================================  

#                               ALL SLOTS - KILLED

label BS_A_S1_Chk_Kld:
    if A_S1_Dmg_Rcv >= A_S1_HP:
        pass
    else:
        $ A_S1_Killed += A_S1_Dmg_Rcv
    return

label BS_A_S2_Chk_Kld:
    if A_S2_Dmg_Rcv >= A_S2_HP:
        pass
    else:
        $ A_S2_Killed += A_S2_Dmg_Rcv
    return

label BS_A_S3_Chk_Kld:
    if A_S3_Dmg_Rcv    >= A_S3_HP:
        pass
    else:
        $ A_S3_Killed += A_S3_Dmg_Rcv
    return

label BS_A_S4_Chk_Kld:
    if A_S4_Dmg_Rcv    >= A_S4_HP:
        pass
    else:
        $ A_S4_Killed += A_S4_Dmg_Rcv
    return

label BS_A_S5_Chk_Kld:
    if A_S5_Dmg_Rcv    >= A_S5_HP:
        pass
    else:
        $ A_S5_Killed += A_S5_Dmg_Rcv
    return

label BS_A_S6_Chk_Kld:
    if A_S6_Dmg_Rcv    >= A_S6_HP:
        pass
    else:
        $ A_S6_Killed += A_S6_Dmg_Rcv
    return

#================================================================
#================================================================
#================================================================    
#================================================================  
#================================================================
#================================================================
#================================================================    
#================================================================  

label BS_D_S1_Chk_Kld:
    if D_S1_Dmg_Rcv >= D_S1_HP:
        pass
    else:
        $ D_S1_Killed += D_S1_Dmg_Rcv
    return

label BS_D_S2_Chk_Kld:
    if D_S2_Dmg_Rcv >= D_S2_HP:
        pass
    else:
        $ D_S2_Killed += D_S2_Dmg_Rcv
    return

label BS_D_S3_Chk_Kld:
    if D_S3_Dmg_Rcv    >= D_S3_HP:
        pass
    else:
        $ D_S3_Killed += D_S3_Dmg_Rcv
    return

label BS_D_S4_Chk_Kld:
    if D_S4_Dmg_Rcv    >= D_S4_HP:
        pass
    else:
        $ D_S4_Killed += D_S4_Dmg_Rcv
    return

label BS_D_S5_Chk_Kld:
    if D_S5_Dmg_Rcv    >= D_S5_HP:
        pass
    else:
        $ D_S5_Killed += D_S5_Dmg_Rcv
    return

label BS_D_S6_Chk_Kld:
    if D_S6_Dmg_Rcv    >= D_S6_HP:
        pass
    else:
        $ D_S6_Killed += D_S6_Dmg_Rcv
    return
