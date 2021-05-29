
#///////////////////////  ATTACKER SLOT 1
label BS_Update_A_S1_ChkTgt_Cls04_Ttc02:

    if A_S1_HP > 0 and A_S1_HP < A_S1_MHP:
        $ A_S1_Tgt_01 = 1
        $ A_S1_DmgRcvType = "Heal"
    if A_S2_HP > 0 and A_S2_HP < A_S2_MHP:
        $ A_S1_Tgt_02 = 1
        $ A_S2_DmgRcvType = "Heal"
    if A_S3_HP > 0 and A_S3_HP < A_S3_MHP:
        $ A_S1_Tgt_03 = 1
        $ A_S3_DmgRcvType = "Heal"
    if A_S4_HP > 0 and A_S4_HP < A_S4_MHP:
        $ A_S1_Tgt_04 = 1
        $ A_S4_DmgRcvType = "Heal"
    if A_S5_HP > 0 and A_S5_HP < A_S5_MHP:
        $ A_S1_Tgt_05 = 1
        $ A_S5_DmgRcvType = "Heal"
    if A_S6_HP > 0 and A_S6_HP < A_S6_MHP:
        $ A_S1_Tgt_06 = 1
        $ A_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  ATTACKER SLOT 2
label BS_Update_A_S2_ChkTgt_Cls04_Ttc02:

    if A_S1_HP > 0 and A_S1_HP < A_S1_MHP:
        $ A_S2_Tgt_01 = 1
        $ A_S1_DmgRcvType = "Heal"
    if A_S2_HP > 0 and A_S2_HP < A_S2_MHP:
        $ A_S2_Tgt_02 = 1
        $ A_S2_DmgRcvType = "Heal"
    if A_S3_HP > 0 and A_S3_HP < A_S3_MHP:
        $ A_S2_Tgt_03 = 1
        $ A_S3_DmgRcvType = "Heal"
    if A_S4_HP > 0 and A_S4_HP < A_S4_MHP:
        $ A_S2_Tgt_04 = 1
        $ A_S4_DmgRcvType = "Heal"
    if A_S5_HP > 0 and A_S5_HP < A_S5_MHP:
        $ A_S2_Tgt_05 = 1
        $ A_S5_DmgRcvType = "Heal"
    if A_S6_HP > 0 and A_S6_HP < A_S6_MHP:
        $ A_S2_Tgt_06 = 1
        $ A_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  ATTACKER SLOT 3
label BS_Update_A_S3_ChkTgt_Cls04_Ttc02:

    if A_S1_HP > 0 and A_S1_HP < A_S1_MHP:
        $ A_S3_Tgt_01 = 1
        $ A_S1_DmgRcvType = "Heal"
    if A_S2_HP > 0 and A_S2_HP < A_S2_MHP:
        $ A_S3_Tgt_02 = 1
        $ A_S2_DmgRcvType = "Heal"
    if A_S3_HP > 0 and A_S3_HP < A_S3_MHP:
        $ A_S3_Tgt_03 = 1
        $ A_S3_DmgRcvType = "Heal"
    if A_S4_HP > 0 and A_S4_HP < A_S4_MHP:
        $ A_S3_Tgt_04 = 1
        $ A_S4_DmgRcvType = "Heal"
    if A_S5_HP > 0 and A_S5_HP < A_S5_MHP:
        $ A_S3_Tgt_05 = 1
        $ A_S5_DmgRcvType = "Heal"
    if A_S6_HP > 0 and A_S6_HP < A_S6_MHP:
        $ A_S3_Tgt_06 = 1
        $ A_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  ATTACKER SLOT 4
label BS_Update_A_S4_ChkTgt_Cls04_Ttc02:

    if A_S1_HP > 0 and A_S1_HP < A_S1_MHP:
        $ A_S4_Tgt_01 = 1
        $ A_S1_DmgRcvType = "Heal"
    if A_S2_HP > 0 and A_S2_HP < A_S2_MHP:
        $ A_S4_Tgt_02 = 1
        $ A_S2_DmgRcvType = "Heal"
    if A_S3_HP > 0 and A_S3_HP < A_S3_MHP:
        $ A_S4_Tgt_03 = 1
        $ A_S3_DmgRcvType = "Heal"
    if A_S4_HP > 0 and A_S4_HP < A_S4_MHP:
        $ A_S4_Tgt_04 = 1
        $ A_S4_DmgRcvType = "Heal"
    if A_S5_HP > 0 and A_S5_HP < A_S5_MHP:
        $ A_S4_Tgt_05 = 1
        $ A_S5_DmgRcvType = "Heal"
    if A_S6_HP > 0 and A_S6_HP < A_S6_MHP:
        $ A_S4_Tgt_06 = 1
        $ A_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  ATTACKER SLOT 5
label BS_Update_A_S5_ChkTgt_Cls04_Ttc02:

    if A_S1_HP > 0 and A_S1_HP < A_S1_MHP:
        $ A_S5_Tgt_01 = 1
        $ A_S1_DmgRcvType = "Heal"
    if A_S2_HP > 0 and A_S2_HP < A_S2_MHP:
        $ A_S5_Tgt_02 = 1
        $ A_S2_DmgRcvType = "Heal"
    if A_S3_HP > 0 and A_S3_HP < A_S3_MHP:
        $ A_S5_Tgt_03 = 1
        $ A_S3_DmgRcvType = "Heal"
    if A_S4_HP > 0 and A_S4_HP < A_S4_MHP:
        $ A_S5_Tgt_04 = 1
        $ A_S4_DmgRcvType = "Heal"
    if A_S5_HP > 0 and A_S5_HP < A_S5_MHP:
        $ A_S5_Tgt_05 = 1
        $ A_S5_DmgRcvType = "Heal"
    if A_S6_HP > 0 and A_S6_HP < A_S6_MHP:
        $ A_S5_Tgt_06 = 1
        $ A_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  ATTACKER SLOT 6
label BS_Update_A_S6_ChkTgt_Cls04_Ttc02:

    if A_S1_HP > 0 and A_S1_HP < A_S1_MHP:
        $ A_S6_Tgt_01 = 1
        $ A_S1_DmgRcvType = "Heal"
    if A_S2_HP > 0 and A_S2_HP < A_S2_MHP:
        $ A_S6_Tgt_02 = 1
        $ A_S2_DmgRcvType = "Heal"
    if A_S3_HP > 0 and A_S3_HP < A_S3_MHP:
        $ A_S6_Tgt_03 = 1
        $ A_S3_DmgRcvType = "Heal"
    if A_S4_HP > 0 and A_S4_HP < A_S4_MHP:
        $ A_S6_Tgt_04 = 1
        $ A_S4_DmgRcvType = "Heal"
    if A_S5_HP > 0 and A_S5_HP < A_S5_MHP:
        $ A_S6_Tgt_05 = 1
        $ A_S5_DmgRcvType = "Heal"
    if A_S6_HP > 0 and A_S6_HP < A_S6_MHP:
        $ A_S6_Tgt_06 = 1
        $ A_S6_DmgRcvType = "Heal"
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
label BS_Update_D_S1_ChkTgt_Cls04_Ttc02:

    if D_S1_HP > 0 and D_S1_HP < D_S1_MHP:
        $ D_S1_Tgt_01 = 1
        $ D_S1_DmgRcvType = "Heal"
    if D_S2_HP > 0 and D_S2_HP < D_S2_MHP:
        $ D_S1_Tgt_02 = 1
        $ D_S2_DmgRcvType = "Heal"
    if D_S3_HP > 0 and D_S3_HP < D_S3_MHP:
        $ D_S1_Tgt_03 = 1
        $ D_S3_DmgRcvType = "Heal"
    if D_S4_HP > 0 and D_S4_HP < D_S4_MHP:
        $ D_S1_Tgt_04 = 1
        $ D_S4_DmgRcvType = "Heal"
    if D_S5_HP > 0 and D_S5_HP < D_S5_MHP:
        $ D_S1_Tgt_05 = 1
        $ D_S5_DmgRcvType = "Heal"
    if D_S6_HP > 0 and D_S6_HP < D_S6_MHP:
        $ D_S1_Tgt_06 = 1
        $ D_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  DEFFENDER SLOT 2
label BS_Update_D_S2_ChkTgt_Cls04_Ttc02:

    if D_S1_HP > 0 and D_S1_HP < D_S1_MHP:
        $ D_S2_Tgt_01 = 1
        $ D_S1_DmgRcvType = "Heal"
    if D_S2_HP > 0 and D_S2_HP < D_S2_MHP:
        $ D_S2_Tgt_02 = 1
        $ D_S2_DmgRcvType = "Heal"
    if D_S3_HP > 0 and D_S3_HP < D_S3_MHP:
        $ D_S2_Tgt_03 = 1
        $ D_S3_DmgRcvType = "Heal"
    if D_S4_HP > 0 and D_S4_HP < D_S4_MHP:
        $ D_S2_Tgt_04 = 1
        $ D_S4_DmgRcvType = "Heal"
    if D_S5_HP > 0 and D_S5_HP < D_S5_MHP:
        $ D_S2_Tgt_05 = 1
        $ D_S5_DmgRcvType = "Heal"
    if D_S6_HP > 0 and D_S6_HP < D_S6_MHP:
        $ D_S2_Tgt_06 = 1
        $ D_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  DEFFENDER SLOT 3
label BS_Update_D_S3_ChkTgt_Cls04_Ttc02:

    if D_S1_HP > 0 and D_S1_HP < D_S1_MHP:
        $ D_S3_Tgt_01 = 1
        $ D_S1_DmgRcvType = "Heal"
    if D_S2_HP > 0 and D_S2_HP < D_S2_MHP:
        $ D_S3_Tgt_02 = 1
        $ D_S2_DmgRcvType = "Heal"
    if D_S3_HP > 0 and D_S3_HP < D_S3_MHP:
        $ D_S3_Tgt_03 = 1
        $ D_S3_DmgRcvType = "Heal"
    if D_S4_HP > 0 and D_S4_HP < D_S4_MHP:
        $ D_S3_Tgt_04 = 1
        $ D_S4_DmgRcvType = "Heal"
    if D_S5_HP > 0 and D_S5_HP < D_S5_MHP:
        $ D_S3_Tgt_05 = 1
        $ D_S5_DmgRcvType = "Heal"
    if D_S6_HP > 0 and D_S6_HP < D_S6_MHP:
        $ D_S3_Tgt_06 = 1
        $ D_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  DEFFENDER SLOT 4
label BS_Update_D_S4_ChkTgt_Cls04_Ttc02:

    if D_S1_HP > 0 and D_S1_HP < D_S1_MHP:
        $ D_S4_Tgt_01 = 1
        $ D_S1_DmgRcvType = "Heal"
    if D_S2_HP > 0 and D_S2_HP < D_S2_MHP:
        $ D_S4_Tgt_02 = 1
        $ D_S2_DmgRcvType = "Heal"
    if D_S3_HP > 0 and D_S3_HP < D_S3_MHP:
        $ D_S4_Tgt_03 = 1
        $ D_S3_DmgRcvType = "Heal"
    if D_S4_HP > 0 and D_S4_HP < D_S4_MHP:
        $ D_S4_Tgt_04 = 1
        $ D_S4_DmgRcvType = "Heal"
    if D_S5_HP > 0 and D_S5_HP < D_S5_MHP:
        $ D_S4_Tgt_05 = 1
        $ D_S5_DmgRcvType = "Heal"
    if D_S6_HP > 0 and D_S6_HP < D_S6_MHP:
        $ D_S4_Tgt_06 = 1
        $ D_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  DEFFENDER SLOT 5
label BS_Update_D_S5_ChkTgt_Cls04_Ttc02:

    if D_S1_HP > 0 and D_S1_HP < D_S1_MHP:
        $ D_S5_Tgt_01 = 1
        $ D_S1_DmgRcvType = "Heal"
    if D_S2_HP > 0 and D_S2_HP < D_S2_MHP:
        $ D_S5_Tgt_02 = 1
        $ D_S2_DmgRcvType = "Heal"
    if D_S3_HP > 0 and D_S3_HP < D_S3_MHP:
        $ D_S5_Tgt_03 = 1
        $ D_S3_DmgRcvType = "Heal"
    if D_S4_HP > 0 and D_S4_HP < D_S4_MHP:
        $ D_S5_Tgt_04 = 1
        $ D_S4_DmgRcvType = "Heal"
    if D_S5_HP > 0 and D_S5_HP < D_S5_MHP:
        $ D_S5_Tgt_05 = 1
        $ D_S5_DmgRcvType = "Heal"
    if D_S6_HP > 0 and D_S6_HP < D_S6_MHP:
        $ D_S5_Tgt_06 = 1
        $ D_S6_DmgRcvType = "Heal"
    return
        
#///////////////////////  DEFFENDER SLOT 6
label BS_Update_D_S6_ChkTgt_Cls04_Ttc02:

    if D_S1_HP > 0 and D_S1_HP < D_S1_MHP:
        $ D_S6_Tgt_01 = 1
        $ D_S1_DmgRcvType = "Heal"
    if D_S2_HP > 0 and D_S2_HP < D_S2_MHP:
        $ D_S6_Tgt_02 = 1
        $ D_S2_DmgRcvType = "Heal"
    if D_S3_HP > 0 and D_S3_HP < D_S3_MHP:
        $ D_S6_Tgt_03 = 1
        $ D_S3_DmgRcvType = "Heal"
    if D_S4_HP > 0 and D_S4_HP < D_S4_MHP:
        $ D_S6_Tgt_04 = 1
        $ D_S4_DmgRcvType = "Heal"
    if D_S5_HP > 0 and D_S5_HP < D_S5_MHP:
        $ D_S6_Tgt_05 = 1
        $ D_S5_DmgRcvType = "Heal"
    if D_S6_HP > 0 and D_S6_HP < D_S6_MHP:
        $ D_S6_Tgt_06 = 1
        $ D_S6_DmgRcvType = "Heal"
    return
