
#///////////////////////  ATTACKER SLOT 1
#=================================
label BS_A_S1_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if A_S1_Ttc == 1:
#-------------------------------
        if A_S1_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S1_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S1_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S1_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S1_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S1_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    elif A_S1_Ttc == 2:
#-------------------------------
        if A_S1_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S1_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S1_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S1_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S1_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S1_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  ATTACKER SLOT 2
#=================================
label BS_A_S2_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if A_S2_Ttc == 1:
#-------------------------------
        if A_S2_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S2_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S2_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S2_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S2_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S2_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    elif A_S2_Ttc == 2:
#-------------------------------
        if A_S2_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S2_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S2_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S2_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S2_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S2_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  ATTACKER SLOT 3
#=================================
label BS_A_S3_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if A_S3_Ttc == 1:
#-------------------------------
        if A_S3_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S3_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S3_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S3_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S3_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S3_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    elif A_S3_Ttc == 2:
#-------------------------------
        if A_S3_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S3_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S3_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S3_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S3_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S3_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  ATTACKER SLOT 4
#=================================
label BS_A_S4_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if A_S4_Ttc == 1:
#-------------------------------
        if A_S4_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S4_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S4_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S4_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S4_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S4_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    elif A_S4_Ttc == 2:
#-------------------------------
        if A_S4_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S4_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S4_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S4_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S4_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S4_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  ATTACKER SLOT 5
#=================================
label BS_A_S5_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if A_S5_Ttc == 1:
#-------------------------------
        if A_S5_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S5_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S5_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S5_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S5_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S5_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    elif A_S5_Ttc == 2:
#-------------------------------
        if A_S5_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S5_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S5_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S5_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S5_Tgt_05 == 1:
            $ A_S5_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S5_Chk_HealRcv
            call BS_A_S5_Chg_HP_Heal
        if A_S5_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  ATTACKER SLOT 6
#=================================
label BS_A_S6_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if A_S6_Ttc == 1:
#-------------------------------
        if A_S6_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S6_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S6_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S6_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S6_Tgt_05 == 1:
            $ A_S6_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
        if A_S6_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    elif A_S6_Ttc == 2:
#-------------------------------
        if A_S6_Tgt_01 == 1:
            $ A_S1_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S1_Chk_HealRcv
            call BS_A_S1_Chg_HP_Heal
        if A_S6_Tgt_02 == 1:
            $ A_S2_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S2_Chk_HealRcv
            call BS_A_S2_Chg_HP_Heal
        if A_S6_Tgt_03 == 1:
            $ A_S3_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S3_Chk_HealRcv
            call BS_A_S3_Chg_HP_Heal
        if A_S6_Tgt_04 == 1:
            $ A_S4_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S4_Chk_HealRcv
            call BS_A_S4_Chg_HP_Heal
        if A_S6_Tgt_05 == 1:
            $ A_S6_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
        if A_S6_Tgt_06 == 1:
            $ A_S6_Dmg_Rcv = (A_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_A_S6_Chk_HealRcv
            call BS_A_S6_Chg_HP_Heal
#-------------------------------
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#=================================
label BS_D_S1_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if D_S1_Ttc == 1:
#-------------------------------
        if D_S1_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S1_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S1_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S1_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S1_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S1_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    elif D_S1_Ttc == 2:
#-------------------------------
        if D_S1_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S1_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S1_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S1_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S1_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S1_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S1_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  DEFFENDER SLOT 2
#=================================
label BS_D_S2_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if D_S2_Ttc == 1:
#-------------------------------
        if D_S2_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S2_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S2_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S2_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S2_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S2_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    elif D_S2_Ttc == 2:
#-------------------------------
        if D_S2_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S2_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S2_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S2_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S2_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S2_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S2_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  DEFFENDER SLOT 3
#=================================
label BS_D_S3_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if D_S3_Ttc == 1:
#-------------------------------
        if D_S3_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S3_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S3_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S3_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S3_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S3_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    elif D_S3_Ttc == 2:
#-------------------------------
        if D_S3_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S3_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S3_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S3_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S3_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S3_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S3_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  DEFFENDER SLOT 4
#=================================
label BS_D_S4_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if D_S4_Ttc == 1:
#-------------------------------
        if D_S4_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S4_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S4_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S4_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S4_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S4_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    elif D_S4_Ttc == 2:
#-------------------------------
        if D_S4_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S4_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S4_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S4_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S4_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S4_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S4_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  DEFFENDER SLOT 5
#=================================
label BS_D_S5_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if D_S5_Ttc == 1:
#-------------------------------
        if D_S5_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S5_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S5_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S5_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S5_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S5_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    elif D_S5_Ttc == 2:
#-------------------------------
        if D_S5_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S5_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S5_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S5_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S5_Tgt_05 == 1:
            $ D_S5_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S5_Chk_HealRcv
            call BS_D_S5_Chg_HP_Heal
        if D_S5_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S5_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    return

#///////////////////////  DEFFENDER SLOT 6
#=================================
label BS_D_S6_Chk_HealOrg_Ttc02:
#=================================
#-------------------------------
    if D_S6_Ttc == 1:
#-------------------------------
        if D_S6_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S6_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S6_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S6_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S6_Tgt_05 == 1:
            $ D_S6_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
        if D_S6_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    elif D_S6_Ttc == 2:
#-------------------------------
        if D_S6_Tgt_01 == 1:
            $ D_S1_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S1_Chk_HealRcv
            call BS_D_S1_Chg_HP_Heal
        if D_S6_Tgt_02 == 1:
            $ D_S2_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S2_Chk_HealRcv
            call BS_D_S2_Chg_HP_Heal
        if D_S6_Tgt_03 == 1:
            $ D_S3_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S3_Chk_HealRcv
            call BS_D_S3_Chg_HP_Heal
        if D_S6_Tgt_04 == 1:
            $ D_S4_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S4_Chk_HealRcv
            call BS_D_S4_Chg_HP_Heal
        if D_S6_Tgt_05 == 1:
            $ D_S6_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
        if D_S6_Tgt_06 == 1:
            $ D_S6_Dmg_Rcv = (D_S6_Atk * Cls004_Ttc02_HealRate)/ 100
            call BS_D_S6_Chk_HealRcv
            call BS_D_S6_Chg_HP_Heal
#-------------------------------
    return
