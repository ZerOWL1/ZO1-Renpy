
#///////////////////////  ATTACKER SLOT 1
#==========================================
label BS_A_S1_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_A_S1_Rst_Tgt
#-----------------------------------
    if A_S1_Cls == 1:
#-----------------------------------
        if A_S1_Ttc == 1:
            call BS_Update_A_S1_ChkTgt_Cls01_Ttc01
        elif A_S1_Ttc == 2:
            call BS_Update_A_S1_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif A_S1_Cls == 2:
#-----------------------------------
        if A_S1_Ttc == 1:
            call BS_Update_A_S1_ChkTgt_Cls02_Ttc01
        elif A_S1_Ttc == 2:
            call BS_Update_A_S1_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif A_S1_Cls == 3:
#-----------------------------------
        if A_S1_Ttc == 1:
            call BS_Update_A_S1_ChkTgt_Cls03_Ttc01
        elif A_S1_Ttc == 2:
            call BS_Update_A_S1_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ A_S1_Tgt_Total = (
    A_S1_Tgt_01) + (
    A_S1_Tgt_02) + (
    A_S1_Tgt_03) + (
    A_S1_Tgt_04) + (
    A_S1_Tgt_05) + (
    A_S1_Tgt_06)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 2
#==========================================
label BS_A_S2_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_A_S2_Rst_Tgt
#-----------------------------------
    if A_S2_Cls == 1:
#-----------------------------------
        if A_S2_Ttc == 1:
            call BS_Update_A_S2_ChkTgt_Cls01_Ttc01
        elif A_S2_Ttc == 2:
            call BS_Update_A_S2_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif A_S2_Cls == 2:
#-----------------------------------
        if A_S2_Ttc == 1:
            call BS_Update_A_S2_ChkTgt_Cls02_Ttc01
        elif A_S2_Ttc == 2:
            call BS_Update_A_S2_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif A_S2_Cls == 3:
#-----------------------------------
        if A_S2_Ttc == 1:
            call BS_Update_A_S2_ChkTgt_Cls03_Ttc01
        elif A_S2_Ttc == 2:
            call BS_Update_A_S2_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ A_S2_Tgt_Total = (
    A_S2_Tgt_01) + (
    A_S2_Tgt_02) + (
    A_S2_Tgt_03) + (
    A_S2_Tgt_04) + (
    A_S2_Tgt_05) + (
    A_S2_Tgt_06)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 3
#==========================================
label BS_A_S3_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_A_S3_Rst_Tgt
#-----------------------------------
    if A_S3_Cls == 1:
#-----------------------------------
        if A_S3_Ttc == 1:
            call BS_Update_A_S3_ChkTgt_Cls01_Ttc01
        elif A_S3_Ttc == 2:
            call BS_Update_A_S3_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif A_S3_Cls == 2:
#-----------------------------------
        if A_S3_Ttc == 1:
            call BS_Update_A_S3_ChkTgt_Cls02_Ttc01
        elif A_S3_Ttc == 2:
            call BS_Update_A_S3_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif A_S3_Cls == 3:
#-----------------------------------
        if A_S3_Ttc == 1:
            call BS_Update_A_S3_ChkTgt_Cls03_Ttc01
        elif A_S3_Ttc == 2:
            call BS_Update_A_S3_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ A_S3_Tgt_Total = (
    A_S3_Tgt_01) + (
    A_S3_Tgt_02) + (
    A_S3_Tgt_03) + (
    A_S3_Tgt_04) + (
    A_S3_Tgt_05) + (
    A_S3_Tgt_06)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 4
#==========================================
label BS_A_S4_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_A_S4_Rst_Tgt
#-----------------------------------
    if A_S4_Cls == 1:
#-----------------------------------
        if A_S4_Ttc == 1:
            call BS_Update_A_S4_ChkTgt_Cls01_Ttc01
        elif A_S4_Ttc == 2:
            call BS_Update_A_S4_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif A_S4_Cls == 2:
#-----------------------------------
        if A_S4_Ttc == 1:
            call BS_Update_A_S4_ChkTgt_Cls02_Ttc01
        elif A_S4_Ttc == 2:
            call BS_Update_A_S4_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif A_S4_Cls == 3:
#-----------------------------------
        if A_S4_Ttc == 1:
            call BS_Update_A_S4_ChkTgt_Cls03_Ttc01
        elif A_S4_Ttc == 2:
            call BS_Update_A_S4_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ A_S4_Tgt_Total = (
    A_S4_Tgt_01) + (
    A_S4_Tgt_02) + (
    A_S4_Tgt_03) + (
    A_S4_Tgt_04) + (
    A_S4_Tgt_05) + (
    A_S4_Tgt_06)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 5
#==========================================
label BS_A_S5_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_A_S5_Rst_Tgt
#-----------------------------------
    if A_S5_Cls == 1:
#-----------------------------------
        if A_S5_Ttc == 1:
            call BS_Update_A_S5_ChkTgt_Cls01_Ttc01
        elif A_S5_Ttc == 2:
            call BS_Update_A_S5_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif A_S5_Cls == 2:
#-----------------------------------
        if A_S5_Ttc == 1:
            call BS_Update_A_S5_ChkTgt_Cls02_Ttc01
        elif A_S5_Ttc == 2:
            call BS_Update_A_S5_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif A_S5_Cls == 3:
#-----------------------------------
        if A_S5_Ttc == 1:
            call BS_Update_A_S5_ChkTgt_Cls03_Ttc01
        elif A_S5_Ttc == 2:
            call BS_Update_A_S5_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ A_S5_Tgt_Total = (
    A_S5_Tgt_01) + (
    A_S5_Tgt_02) + (
    A_S5_Tgt_03) + (
    A_S5_Tgt_04) + (
    A_S5_Tgt_05) + (
    A_S5_Tgt_06)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 6
#==========================================
label BS_A_S6_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_A_S6_Rst_Tgt
#-----------------------------------
    if A_S6_Cls == 1:
#-----------------------------------
        if A_S6_Ttc == 1:
            call BS_Update_A_S6_ChkTgt_Cls01_Ttc01
        elif A_S6_Ttc == 2:
            call BS_Update_A_S6_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif A_S6_Cls == 2:
#-----------------------------------
        if A_S6_Ttc == 1:
            call BS_Update_A_S6_ChkTgt_Cls02_Ttc01
        elif A_S6_Ttc == 2:
            call BS_Update_A_S6_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif A_S6_Cls == 3:
#-----------------------------------
        if A_S6_Ttc == 1:
            call BS_Update_A_S6_ChkTgt_Cls03_Ttc01
        elif A_S6_Ttc == 2:
            call BS_Update_A_S6_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ A_S6_Tgt_Total = (
    A_S6_Tgt_01) + (
    A_S6_Tgt_02) + (
    A_S6_Tgt_03) + (
    A_S6_Tgt_04) + (
    A_S6_Tgt_05) + (
    A_S6_Tgt_06)
#-----------------------------------
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#==========================================
label BS_D_S1_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_D_S1_Rst_Tgt
#-----------------------------------
    if D_S1_Cls == 1:
#-----------------------------------
        if D_S1_Ttc == 1:
            call BS_Update_D_S1_ChkTgt_Cls01_Ttc01
        elif D_S1_Ttc == 2:
            call BS_Update_D_S1_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif D_S1_Cls == 2:
#-----------------------------------
        if D_S1_Ttc == 1:
            call BS_Update_D_S1_ChkTgt_Cls02_Ttc01
        elif D_S1_Ttc == 2:
            call BS_Update_D_S1_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif D_S1_Cls == 3:
#-----------------------------------
        if D_S1_Ttc == 1:
            call BS_Update_D_S1_ChkTgt_Cls03_Ttc01
        elif D_S1_Ttc == 2:
            call BS_Update_D_S1_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ D_S1_Tgt_Total = (
    D_S1_Tgt_01) + (
    D_S1_Tgt_02) + (
    D_S1_Tgt_03) + (
    D_S1_Tgt_04) + (
    D_S1_Tgt_05) + (
    D_S1_Tgt_06)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 2
#==========================================
label BS_D_S2_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_D_S2_Rst_Tgt
#-----------------------------------
    if D_S2_Cls == 1:
#-----------------------------------
        if D_S2_Ttc == 1:
            call BS_Update_D_S2_ChkTgt_Cls01_Ttc01
        elif D_S2_Ttc == 2:
            call BS_Update_D_S2_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif D_S2_Cls == 2:
#-----------------------------------
        if D_S2_Ttc == 1:
            call BS_Update_D_S2_ChkTgt_Cls02_Ttc01
        elif D_S2_Ttc == 2:
            call BS_Update_D_S2_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif D_S2_Cls == 3:
#-----------------------------------
        if D_S2_Ttc == 1:
            call BS_Update_D_S2_ChkTgt_Cls03_Ttc01
        elif D_S2_Ttc == 2:
            call BS_Update_D_S2_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ D_S2_Tgt_Total = (
    D_S2_Tgt_01) + (
    D_S2_Tgt_02) + (
    D_S2_Tgt_03) + (
    D_S2_Tgt_04) + (
    D_S2_Tgt_05) + (
    D_S2_Tgt_06)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 3
#==========================================
label BS_D_S3_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_D_S3_Rst_Tgt
#-----------------------------------
    if D_S3_Cls == 1:
#-----------------------------------
        if D_S3_Ttc == 1:
            call BS_Update_D_S3_ChkTgt_Cls01_Ttc01
        elif D_S3_Ttc == 2:
            call BS_Update_D_S3_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif D_S3_Cls == 2:
#-----------------------------------
        if D_S3_Ttc == 1:
            call BS_Update_D_S3_ChkTgt_Cls02_Ttc01
        elif D_S3_Ttc == 2:
            call BS_Update_D_S3_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif D_S3_Cls == 3:
#-----------------------------------
        if D_S3_Ttc == 1:
            call BS_Update_D_S3_ChkTgt_Cls03_Ttc01
        elif D_S3_Ttc == 2:
            call BS_Update_D_S3_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ D_S3_Tgt_Total = (
    D_S3_Tgt_01) + (
    D_S3_Tgt_02) + (
    D_S3_Tgt_03) + (
    D_S3_Tgt_04) + (
    D_S3_Tgt_05) + (
    D_S3_Tgt_06)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 4
#==========================================
label BS_D_S4_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_D_S4_Rst_Tgt
#-----------------------------------
    if D_S4_Cls == 1:
#-----------------------------------
        if D_S4_Ttc == 1:
            call BS_Update_D_S4_ChkTgt_Cls01_Ttc01
        elif D_S4_Ttc == 2:
            call BS_Update_D_S4_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif D_S4_Cls == 2:
#-----------------------------------
        if D_S4_Ttc == 1:
            call BS_Update_D_S4_ChkTgt_Cls02_Ttc01
        elif D_S4_Ttc == 2:
            call BS_Update_D_S4_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif D_S4_Cls == 3:
#-----------------------------------
        if D_S4_Ttc == 1:
            call BS_Update_D_S4_ChkTgt_Cls03_Ttc01
        elif D_S4_Ttc == 2:
            call BS_Update_D_S4_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ D_S4_Tgt_Total = (
    D_S4_Tgt_01) + (
    D_S4_Tgt_02) + (
    D_S4_Tgt_03) + (
    D_S4_Tgt_04) + (
    D_S4_Tgt_05) + (
    D_S4_Tgt_06)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 5
#==========================================
label BS_D_S5_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_D_S5_Rst_Tgt
#-----------------------------------
    if D_S5_Cls == 1:
#-----------------------------------
        if D_S5_Ttc == 1:
            call BS_Update_D_S5_ChkTgt_Cls01_Ttc01
        elif D_S5_Ttc == 2:
            call BS_Update_D_S5_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif D_S5_Cls == 2:
#-----------------------------------
        if D_S5_Ttc == 1:
            call BS_Update_D_S5_ChkTgt_Cls02_Ttc01
        elif D_S5_Ttc == 2:
            call BS_Update_D_S5_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif D_S5_Cls == 3:
#-----------------------------------
        if D_S5_Ttc == 1:
            call BS_Update_D_S5_ChkTgt_Cls03_Ttc01
        elif D_S5_Ttc == 2:
            call BS_Update_D_S5_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ D_S5_Tgt_Total = (
    D_S5_Tgt_01) + (
    D_S5_Tgt_02) + (
    D_S5_Tgt_03) + (
    D_S5_Tgt_04) + (
    D_S5_Tgt_05) + (
    D_S5_Tgt_06)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 6
#==========================================
label BS_D_S6_Chk_Tgt:
#==========================================
#-----------------------------------
    call BS_D_S6_Rst_Tgt
#-----------------------------------
    if D_S6_Cls == 1:
#-----------------------------------
        if D_S6_Ttc == 1:
            call BS_Update_D_S6_ChkTgt_Cls01_Ttc01
        elif D_S6_Ttc == 2:
            call BS_Update_D_S6_ChkTgt_Cls01_Ttc02
#-----------------------------------
    elif D_S6_Cls == 2:
#-----------------------------------
        if D_S6_Ttc == 1:
            call BS_Update_D_S6_ChkTgt_Cls02_Ttc01
        elif D_S6_Ttc == 2:
            call BS_Update_D_S6_ChkTgt_Cls02_Ttc02
#-----------------------------------
    elif D_S6_Cls == 3:
#-----------------------------------
        if D_S6_Ttc == 1:
            call BS_Update_D_S6_ChkTgt_Cls03_Ttc01
        elif D_S6_Ttc == 2:
            call BS_Update_D_S6_ChkTgt_Cls03_Ttc02
#-----------------------------------
    $ D_S6_Tgt_Total = (
    D_S6_Tgt_01) + (
    D_S6_Tgt_02) + (
    D_S6_Tgt_03) + (
    D_S6_Tgt_04) + (
    D_S6_Tgt_05) + (
    D_S6_Tgt_06)
#-----------------------------------
    return
