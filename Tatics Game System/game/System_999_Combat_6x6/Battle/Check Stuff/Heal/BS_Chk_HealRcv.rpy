#///////////////////////  ATTACKER SLOT 1
label BS_A_S1_Chk_HealRcv:
    if A_S1_Dmg_Rcv >= (A_S1_MHP - A_S1_HP):
        $ A_S1_Dmg_Rcv = A_S1_MHP - A_S1_HP
    return

#///////////////////////  ATTACKER SLOT 2
label BS_A_S2_Chk_HealRcv:
    if A_S2_Dmg_Rcv >= (A_S2_MHP - A_S2_HP):
        $ A_S2_Dmg_Rcv = A_S2_MHP - A_S2_HP
    return

#///////////////////////  ATTACKER SLOT 3
label BS_A_S3_Chk_HealRcv:
    if A_S3_Dmg_Rcv >= (A_S3_MHP - A_S3_HP):
        $ A_S3_Dmg_Rcv = A_S3_MHP - A_S3_HP
    return

#///////////////////////  ATTACKER SLOT 4
label BS_A_S4_Chk_HealRcv:
    if A_S4_Dmg_Rcv >= (A_S4_MHP - A_S4_HP):
        $ A_S4_Dmg_Rcv = A_S4_MHP - A_S4_HP
    return

#///////////////////////  ATTACKER SLOT 5
label BS_A_S5_Chk_HealRcv:
    if A_S5_Dmg_Rcv >= (A_S5_MHP - A_S5_HP):
        $ A_S5_Dmg_Rcv = A_S5_MHP - A_S5_HP
    return

#///////////////////////  ATTACKER SLOT 6
label BS_A_S6_Chk_HealRcv:
    if A_S6_Dmg_Rcv >= (A_S6_MHP - A_S6_HP):
        $ A_S6_Dmg_Rcv = A_S6_MHP - A_S6_HP
    return
 
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
label BS_D_S1_Chk_HealRcv:
    if D_S1_Dmg_Rcv >= (D_S1_MHP - D_S1_HP):
        $ D_S1_Dmg_Rcv = D_S1_MHP - D_S1_HP
    return

#///////////////////////  DEFFENDER SLOT 2
label BS_D_S2_Chk_HealRcv:
    if D_S2_Dmg_Rcv >= (D_S2_MHP - D_S2_HP):
        $ D_S2_Dmg_Rcv = D_S2_MHP - D_S2_HP
    return

#///////////////////////  DEFFENDER SLOT 3
label BS_D_S3_Chk_HealRcv:
    if D_S3_Dmg_Rcv >= (D_S3_MHP - D_S3_HP):
        $ D_S3_Dmg_Rcv = D_S3_MHP - D_S3_HP
    return

#///////////////////////  DEFFENDER SLOT 4
label BS_D_S4_Chk_HealRcv:
    if D_S4_Dmg_Rcv >= (D_S4_MHP - D_S4_HP):
        $ D_S4_Dmg_Rcv = D_S4_MHP - D_S4_HP
    return

#///////////////////////  DEFFENDER SLOT 5
label BS_D_S5_Chk_HealRcv:
    if D_S5_Dmg_Rcv >= (D_S5_MHP - D_S5_HP):
        $ D_S5_Dmg_Rcv = D_S5_MHP - D_S5_HP
    return

#///////////////////////  DEFFENDER SLOT 6
label BS_D_S6_Chk_HealRcv:
    if D_S6_Dmg_Rcv >= (D_S6_MHP - D_S6_HP):
        $ D_S6_Dmg_Rcv = D_S6_MHP - D_S6_HP

    return