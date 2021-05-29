#=====================================================
label BS_Chk_PosChg:
#=====================================================
#----------------------------------------------
    if (A_S1_HP == 0) and (
    A_S2_HP == 0) and (
    A_S3_HP == 0):
#----------------------------------------------
        call BS_Chg_A_Pos01_04
        call BS_Chg_A_Pos02_05
        call BS_Chg_A_Pos03_06

        $ A_S4_HP           = 0
        $ A_S4_MHP           = 0
        $ A_S5_HP           = 0
        $ A_S5_MHP           = 0
        $ A_S6_HP           = 0
        $ A_S6_MHP           = 0
        $ Led_A_S4_HP = 0
        $ Led_A_S4_MHP = 0
        $ Led_A_S5_HP = 0
        $ Led_A_S5_MHP = 0
        $ Led_A_S6_HP = 0
        $ Led_A_S6_MHP = 0

        call BS_Chk_A_S4_UntEvt
        call BS_Chk_A_S4_LedEvt
        call BS_Chk_A_S5_UntEvt
        call BS_Chk_A_S5_LedEvt
        call BS_Chk_A_S6_UntEvt
        call BS_Chk_A_S6_LedEvt
#----------------------------------------------
    elif (D_S1_HP == 0) and (
    D_S2_HP == 0) and (
    D_S3_HP == 0):
#----------------------------------------------
        call BS_Chg_D_Pos01_04
        call BS_Chg_D_Pos02_05
        call BS_Chg_D_Pos03_06

        $ D_S4_HP           = 0
        $ D_S4_MHP           = 0
        $ D_S5_HP           = 0
        $ D_S5_MHP           = 0
        $ D_S6_HP           = 0
        $ D_S6_MHP           = 0
        $ Led_D_S4_HP = 0
        $ Led_D_S4_MHP = 0
        $ Led_D_S5_HP = 0
        $ Led_D_S5_MHP = 0
        $ Led_D_S6_HP = 0
        $ Led_D_S6_MHP = 0

        call BS_Chk_D_S4_UntEvt
        call BS_Chk_D_S4_LedEvt
        call BS_Chk_D_S5_UntEvt
        call BS_Chk_D_S5_LedEvt
        call BS_Chk_D_S6_UntEvt
        call BS_Chk_D_S6_LedEvt
#----------------------------------------------
    $ renpy.pause(SecWait_ChgPOS, hard = True)
#----------------------------------------------
    return