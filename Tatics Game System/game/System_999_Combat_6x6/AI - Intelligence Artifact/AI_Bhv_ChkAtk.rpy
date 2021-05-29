
#///////////////////////  ATTACKER SLOT 1
#====================================
label AI_Bhv_A_S1_ChkAtk:
#====================================
#-------------------------------------------------------
    while A_S1_CanAct == 1:
#-------------------------------------------------------
        call BS_A_S1_Chk_Tgt
#-------------------------------------------------------
        if A_S1_ChgPos_Count >= 2:
            $ A_S1_CanAct = 0
            $ A_S1_ChgTtc_Count = 0
            $ A_S1_ChgPos_Count = 0
        elif A_S1_ChgTtc_Count >= 2:
            $ A_S1_ChgPos_Count += 1
            call AI_Bhv_A_S1_Chg_Pos_Atk
        elif A_S1_Tgt_Total == 0:
            call AI_Bhv_A_S1_Chg_Ttc
        elif A_S1_Tgt_Total >= 1:
            call BS_Bhv_A_S1_Atk
#-------------------------------------------------------
        call BS_A_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 2
#====================================
label AI_Bhv_A_S2_ChkAtk:
#====================================
#-------------------------------------------------------
    while A_S2_CanAct == 1:
#-------------------------------------------------------
        call BS_A_S2_Chk_Tgt
#-------------------------------------------------------
        if A_S2_ChgPos_Count >= 2:
            $ A_S2_CanAct = 0
            $ A_S2_ChgTtc_Count = 0
            $ A_S2_ChgPos_Count = 0
        elif A_S2_ChgTtc_Count >= 2:
            $ A_S2_ChgPos_Count += 1
            call AI_Bhv_A_S2_Chg_Pos_Atk
        elif A_S2_Tgt_Total == 0:
            call AI_Bhv_A_S2_Chg_Ttc
        elif A_S2_Tgt_Total >= 1:
            call BS_Bhv_A_S2_Atk
#-------------------------------------------------------
        call BS_A_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 3
#====================================
label AI_Bhv_A_S3_ChkAtk:
#====================================
#-------------------------------------------------------
    while A_S3_CanAct == 1:
#-------------------------------------------------------
        call BS_A_S3_Chk_Tgt
#-------------------------------------------------------
        if A_S3_ChgPos_Count >= 2:
            $ A_S3_CanAct = 0
            $ A_S3_ChgTtc_Count = 0
            $ A_S3_ChgPos_Count = 0
        elif A_S3_ChgTtc_Count >= 2:
            $ A_S3_ChgPos_Count += 1
            call AI_Bhv_A_S3_Chg_Pos_Atk
        elif A_S3_Tgt_Total == 0:
            call AI_Bhv_A_S3_Chg_Ttc
        elif A_S3_Tgt_Total >= 1:
            call BS_Bhv_A_S3_Atk
#-------------------------------------------------------
        call BS_A_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 4
#====================================
label AI_Bhv_A_S4_ChkAtk:
#====================================
#-------------------------------------------------------
    while A_S4_CanAct == 1:
#-------------------------------------------------------
        call BS_A_S4_Chk_Tgt
#-------------------------------------------------------
        if A_S4_ChgPos_Count >= 2:
            $ A_S4_CanAct = 0
            $ A_S4_ChgTtc_Count = 0
            $ A_S4_ChgPos_Count = 0
        elif A_S4_ChgTtc_Count >= 2:
            $ A_S4_ChgPos_Count += 1
            call AI_Bhv_A_S4_Chg_Pos_Atk
        elif A_S4_Tgt_Total == 0:
            call AI_Bhv_A_S4_Chg_Ttc
        elif A_S4_Tgt_Total >= 1:
            call BS_Bhv_A_S4_Atk
#-------------------------------------------------------
        call BS_A_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 5
#====================================
label AI_Bhv_A_S5_ChkAtk:
#====================================
#-------------------------------------------------------
    while A_S5_CanAct == 1:
#-------------------------------------------------------
        call BS_A_S5_Chk_Tgt
#-------------------------------------------------------
        if A_S5_ChgPos_Count >= 2:
            $ A_S5_CanAct = 0
            $ A_S5_ChgTtc_Count = 0
            $ A_S5_ChgPos_Count = 0
        elif A_S5_ChgTtc_Count >= 2:
            $ A_S5_ChgPos_Count += 1
            call AI_Bhv_A_S5_Chg_Pos_Atk
        elif A_S5_Tgt_Total == 0:
            call AI_Bhv_A_S5_Chg_Ttc
        elif A_S5_Tgt_Total >= 1:
            call BS_Bhv_A_S5_Atk
#-------------------------------------------------------
        call BS_A_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 6
#====================================
label AI_Bhv_A_S6_ChkAtk:
#====================================
#-------------------------------------------------------
    while A_S6_CanAct == 1:
#-------------------------------------------------------
        call BS_A_S6_Chk_Tgt
#-------------------------------------------------------
        if A_S6_ChgPos_Count >= 2:
            $ A_S6_CanAct = 0
            $ A_S6_ChgTtc_Count = 0
            $ A_S6_ChgPos_Count = 0
        elif A_S6_ChgTtc_Count >= 2:
            $ A_S6_ChgPos_Count += 1
            call AI_Bhv_A_S6_Chg_Pos_Atk
        elif A_S6_Tgt_Total == 0:
            call AI_Bhv_A_S6_Chg_Ttc
        elif A_S6_Tgt_Total >= 1:
            call BS_Bhv_A_S6_Atk
#-------------------------------------------------------
        call BS_A_S2_Rst_Tgt
#-------------------------------------------------------
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#====================================
label AI_Bhv_D_S1_ChkAtk:
#====================================
#-------------------------------------------------------
    while D_S1_CanAct == 1:
#-------------------------------------------------------
        call BS_D_S1_Chk_Tgt
#-------------------------------------------------------
        if D_S1_ChgPos_Count >= 2:
            $ D_S1_CanAct = 0
            $ D_S1_ChgTtc_Count = 0
            $ D_S1_ChgPos_Count = 0
        elif D_S1_ChgTtc_Count >= 2:
            $ D_S1_ChgPos_Count += 1
            call AI_Bhv_D_S1_Chg_Pos_Atk
        elif D_S1_Tgt_Total == 0:
            call AI_Bhv_D_S1_Chg_Ttc
        elif D_S1_Tgt_Total >= 1:
            call BS_Bhv_D_S1_Atk
#-------------------------------------------------------
        call BS_D_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 2
#====================================
label AI_Bhv_D_S2_ChkAtk:
#====================================
#-------------------------------------------------------
    while D_S2_CanAct == 1:
#-------------------------------------------------------
        call BS_D_S2_Chk_Tgt
#-------------------------------------------------------
        if D_S2_ChgPos_Count >= 2:
            $ D_S2_CanAct = 0
            $ D_S2_ChgTtc_Count = 0
            $ D_S2_ChgPos_Count = 0
        elif D_S2_ChgTtc_Count >= 2:
            $ D_S2_ChgPos_Count += 1
            call AI_Bhv_D_S2_Chg_Pos_Atk
        elif D_S2_Tgt_Total == 0:
            call AI_Bhv_D_S2_Chg_Ttc
        elif D_S2_Tgt_Total >= 1:
            call BS_Bhv_D_S2_Atk
#-------------------------------------------------------
        call BS_D_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 3
#====================================
label AI_Bhv_D_S3_ChkAtk:
#====================================
#-------------------------------------------------------
    while D_S3_CanAct == 1:
#-------------------------------------------------------
        call BS_D_S3_Chk_Tgt
#-------------------------------------------------------
        if D_S3_ChgPos_Count >= 2:
            $ D_S3_CanAct = 0
            $ D_S3_ChgTtc_Count = 0
            $ D_S3_ChgPos_Count = 0
        elif D_S3_ChgTtc_Count >= 2:
            $ D_S3_ChgPos_Count += 1
            call AI_Bhv_D_S3_Chg_Pos_Atk
        elif D_S3_Tgt_Total == 0:
            call AI_Bhv_D_S3_Chg_Ttc
        elif D_S3_Tgt_Total >= 1:
            call BS_Bhv_D_S3_Atk
#-------------------------------------------------------
        call BS_D_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 4
#====================================
label AI_Bhv_D_S4_ChkAtk:
#====================================
#-------------------------------------------------------
    while D_S4_CanAct == 1:
#-------------------------------------------------------
        call BS_D_S4_Chk_Tgt
#-------------------------------------------------------
        if D_S4_ChgPos_Count >= 2:
            $ D_S4_CanAct = 0
            $ D_S4_ChgTtc_Count = 0
            $ D_S4_ChgPos_Count = 0
        elif D_S4_ChgTtc_Count >= 2:
            $ D_S4_ChgPos_Count += 1
            call AI_Bhv_D_S4_Chg_Pos_Atk
        elif D_S4_Tgt_Total == 0:
            call AI_Bhv_D_S4_Chg_Ttc
        elif D_S4_Tgt_Total >= 1:
            call BS_Bhv_D_S4_Atk
#-------------------------------------------------------
        call BS_D_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 5
#====================================
label AI_Bhv_D_S5_ChkAtk:
#====================================
#-------------------------------------------------------
    while D_S5_CanAct == 1:
#-------------------------------------------------------
        call BS_D_S5_Chk_Tgt
#-------------------------------------------------------
        if D_S5_ChgPos_Count >= 2:
            $ D_S5_CanAct = 0
            $ D_S5_ChgTtc_Count = 0
            $ D_S5_ChgPos_Count = 0
        elif D_S5_ChgTtc_Count >= 2:
            $ D_S5_ChgPos_Count += 1
            call AI_Bhv_D_S5_Chg_Pos_Atk
        elif D_S5_Tgt_Total == 0:
            call AI_Bhv_D_S5_Chg_Ttc
        elif D_S5_Tgt_Total >= 1:
            call BS_Bhv_D_S5_Atk
#-------------------------------------------------------
        call BS_D_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 6
#====================================
label AI_Bhv_D_S6_ChkAtk:
#====================================
#-------------------------------------------------------
    while D_S6_CanAct == 1:
#-------------------------------------------------------
        call BS_D_S6_Chk_Tgt
#-------------------------------------------------------
        if D_S6_ChgPos_Count >= 2:
            $ D_S6_CanAct = 0
            $ D_S6_ChgTtc_Count = 0
            $ D_S6_ChgPos_Count = 0
        elif D_S6_ChgTtc_Count >= 2:
            $ D_S6_ChgPos_Count += 1
            call AI_Bhv_D_S6_Chg_Pos_Atk
        elif D_S6_Tgt_Total == 0:
            call AI_Bhv_D_S6_Chg_Ttc
        elif D_S6_Tgt_Total >= 1:
            call BS_Bhv_D_S6_Atk
#-------------------------------------------------------
        call BS_D_S2_Rst_Tgt
#-------------------------------------------------------
    return
