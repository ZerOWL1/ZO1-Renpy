
#///////////////////////  ATTACKER SLOT 1
#==========================================
label BS_A_S1_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if A_S1_Cls == 1:
        if A_S1_Ttc == 1:
            call BS_A_S1_Chk_Cls001_Ttc01_Dmg
        elif A_S1_Ttc == 2:
            call BS_A_S1_Chk_Cls001_Ttc02_Dmg
        call BS_A_S1_Cls001_Chk_Act
    elif A_S1_Cls == 2:
        if A_S1_Ttc == 1:
            call BS_A_S1_Chk_Cls002_Ttc01_Dmg
        elif A_S1_Ttc == 2:
            call BS_A_S1_Chk_Cls002_Ttc02_Dmg
        call BS_A_S1_Cls002_Chk_Act
    elif A_S1_Cls == 3:
        if A_S1_Ttc == 1:
            call BS_A_S1_Chk_Cls003_Ttc01_Dmg
        elif A_S1_Ttc == 2:
            call BS_A_S1_Chk_Cls003_Ttc02_Dmg
        call BS_A_S1_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 2
#==========================================
label BS_A_S2_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if A_S2_Cls == 1:
        if A_S2_Ttc == 1:
            call BS_A_S2_Chk_Cls001_Ttc01_Dmg
        elif A_S2_Ttc == 2:
            call BS_A_S2_Chk_Cls001_Ttc02_Dmg
        call BS_A_S2_Cls001_Chk_Act
    elif A_S2_Cls == 2:
        if A_S2_Ttc == 1:
            call BS_A_S2_Chk_Cls002_Ttc01_Dmg
        elif A_S2_Ttc == 2:
            call BS_A_S2_Chk_Cls002_Ttc02_Dmg
        call BS_A_S2_Cls002_Chk_Act
    elif A_S2_Cls == 3:
        if A_S2_Ttc == 1:
            call BS_A_S2_Chk_Cls003_Ttc01_Dmg
        elif A_S2_Ttc == 2:
            call BS_A_S2_Chk_Cls003_Ttc02_Dmg
        call BS_A_S2_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 3
#==========================================
label BS_A_S3_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if A_S3_Cls == 1:
        if A_S3_Ttc == 1:
            call BS_A_S3_Chk_Cls001_Ttc01_Dmg
        elif A_S3_Ttc == 2:
            call BS_A_S3_Chk_Cls001_Ttc02_Dmg
        call BS_A_S3_Cls001_Chk_Act
    elif A_S3_Cls == 2:
        if A_S3_Ttc == 1:
            call BS_A_S3_Chk_Cls002_Ttc01_Dmg
        elif A_S3_Ttc == 2:
            call BS_A_S3_Chk_Cls002_Ttc02_Dmg
        call BS_A_S3_Cls002_Chk_Act
    elif A_S3_Cls == 3:
        if A_S3_Ttc == 1:
            call BS_A_S3_Chk_Cls003_Ttc01_Dmg
        elif A_S3_Ttc == 2:
            call BS_A_S3_Chk_Cls003_Ttc02_Dmg
        call BS_A_S3_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 4
#==========================================
label BS_A_S4_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if A_S4_Cls == 1:
        if A_S4_Ttc == 1:
            call BS_A_S4_Chk_Cls001_Ttc01_Dmg
        elif A_S4_Ttc == 2:
            call BS_A_S4_Chk_Cls001_Ttc02_Dmg
        call BS_A_S4_Cls001_Chk_Act
    elif A_S4_Cls == 2:
        if A_S4_Ttc == 1:
            call BS_A_S4_Chk_Cls002_Ttc01_Dmg
        elif A_S4_Ttc == 2:
            call BS_A_S4_Chk_Cls002_Ttc02_Dmg
        call BS_A_S4_Cls002_Chk_Act
    elif A_S4_Cls == 3:
        if A_S4_Ttc == 1:
            call BS_A_S4_Chk_Cls003_Ttc01_Dmg
        elif A_S4_Ttc == 2:
            call BS_A_S4_Chk_Cls003_Ttc02_Dmg
        call BS_A_S4_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 5
#==========================================
label BS_A_S5_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if A_S5_Cls == 1:
        if A_S5_Ttc == 1:
            call BS_A_S5_Chk_Cls001_Ttc01_Dmg
        elif A_S5_Ttc == 2:
            call BS_A_S5_Chk_Cls001_Ttc02_Dmg
        call BS_A_S5_Cls001_Chk_Act
    elif A_S5_Cls == 2:
        if A_S5_Ttc == 1:
            call BS_A_S5_Chk_Cls002_Ttc01_Dmg
        elif A_S5_Ttc == 2:
            call BS_A_S5_Chk_Cls002_Ttc02_Dmg
        call BS_A_S5_Cls002_Chk_Act
    elif A_S5_Cls == 3:
        if A_S5_Ttc == 1:
            call BS_A_S5_Chk_Cls003_Ttc01_Dmg
        elif A_S5_Ttc == 2:
            call BS_A_S5_Chk_Cls003_Ttc02_Dmg
        call BS_A_S5_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 6
#==========================================
label BS_A_S6_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if A_S6_Cls == 1:
        if A_S6_Ttc == 1:
            call BS_A_S6_Chk_Cls001_Ttc01_Dmg
        elif A_S6_Ttc == 2:
            call BS_A_S6_Chk_Cls001_Ttc02_Dmg
        call BS_A_S6_Cls001_Chk_Act
    elif A_S6_Cls == 2:
        if A_S6_Ttc == 1:
            call BS_A_S6_Chk_Cls002_Ttc01_Dmg
        elif A_S6_Ttc == 2:
            call BS_A_S6_Chk_Cls002_Ttc02_Dmg
        call BS_A_S6_Cls002_Chk_Act
    elif A_S6_Cls == 3:
        if A_S6_Ttc == 1:
            call BS_A_S6_Chk_Cls003_Ttc01_Dmg
        elif A_S6_Ttc == 2:
            call BS_A_S6_Chk_Cls003_Ttc02_Dmg
        call BS_A_S6_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
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
label BS_D_S1_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if D_S1_Cls == 1:
        if D_S1_Ttc == 1:
            call BS_D_S1_Chk_Cls001_Ttc01_Dmg
        elif D_S1_Ttc == 2:
            call BS_D_S1_Chk_Cls001_Ttc02_Dmg
        call BS_D_S1_Cls001_Chk_Act
    elif D_S1_Cls == 2:
        if D_S1_Ttc == 1:
            call BS_D_S1_Chk_Cls002_Ttc01_Dmg
        elif D_S1_Ttc == 2:
            call BS_D_S1_Chk_Cls002_Ttc02_Dmg
        call BS_D_S1_Cls002_Chk_Act
    elif D_S1_Cls == 3:
        if D_S1_Ttc == 1:
            call BS_D_S1_Chk_Cls003_Ttc01_Dmg
        elif D_S1_Ttc == 2:
            call BS_D_S1_Chk_Cls003_Ttc02_Dmg
        call BS_D_S1_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 2
#==========================================
label BS_D_S2_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if D_S2_Cls == 1:
        if D_S2_Ttc == 1:
            call BS_D_S2_Chk_Cls001_Ttc01_Dmg
        elif D_S2_Ttc == 2:
            call BS_D_S2_Chk_Cls001_Ttc02_Dmg
        call BS_D_S2_Cls001_Chk_Act
    elif D_S2_Cls == 2:
        if D_S2_Ttc == 1:
            call BS_D_S2_Chk_Cls002_Ttc01_Dmg
        elif D_S2_Ttc == 2:
            call BS_D_S2_Chk_Cls002_Ttc02_Dmg
        call BS_D_S2_Cls002_Chk_Act
    elif D_S2_Cls == 3:
        if D_S2_Ttc == 1:
            call BS_D_S2_Chk_Cls003_Ttc01_Dmg
        elif D_S2_Ttc == 2:
            call BS_D_S2_Chk_Cls003_Ttc02_Dmg
        call BS_D_S2_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 3
#==========================================
label BS_D_S3_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if D_S3_Cls == 1:
        if D_S3_Ttc == 1:
            call BS_D_S3_Chk_Cls001_Ttc01_Dmg
        elif D_S3_Ttc == 2:
            call BS_D_S3_Chk_Cls001_Ttc02_Dmg
        call BS_D_S3_Cls001_Chk_Act
    elif D_S3_Cls == 2:
        if D_S3_Ttc == 1:
            call BS_D_S3_Chk_Cls002_Ttc01_Dmg
        elif D_S3_Ttc == 2:
            call BS_D_S3_Chk_Cls002_Ttc02_Dmg
        call BS_D_S3_Cls002_Chk_Act
    elif D_S3_Cls == 3:
        if D_S3_Ttc == 1:
            call BS_D_S3_Chk_Cls003_Ttc01_Dmg
        elif D_S3_Ttc == 2:
            call BS_D_S3_Chk_Cls003_Ttc02_Dmg
        call BS_D_S3_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 4
#==========================================
label BS_D_S4_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if D_S4_Cls == 1:
        if D_S4_Ttc == 1:
            call BS_D_S4_Chk_Cls001_Ttc01_Dmg
        elif D_S4_Ttc == 2:
            call BS_D_S4_Chk_Cls001_Ttc02_Dmg
        call BS_D_S4_Cls001_Chk_Act
    elif D_S4_Cls == 2:
        if D_S4_Ttc == 1:
            call BS_D_S4_Chk_Cls002_Ttc01_Dmg
        elif D_S4_Ttc == 2:
            call BS_D_S4_Chk_Cls002_Ttc02_Dmg
        call BS_D_S4_Cls002_Chk_Act
    elif D_S4_Cls == 3:
        if D_S4_Ttc == 1:
            call BS_D_S4_Chk_Cls003_Ttc01_Dmg
        elif D_S4_Ttc == 2:
            call BS_D_S4_Chk_Cls003_Ttc02_Dmg
        call BS_D_S4_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 5
#==========================================
label BS_D_S5_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if D_S5_Cls == 1:
        if D_S5_Ttc == 1:
            call BS_D_S5_Chk_Cls001_Ttc01_Dmg
        elif D_S5_Ttc == 2:
            call BS_D_S5_Chk_Cls001_Ttc02_Dmg
        call BS_D_S5_Cls001_Chk_Act
    elif D_S5_Cls == 2:
        if D_S5_Ttc == 1:
            call BS_D_S5_Chk_Cls002_Ttc01_Dmg
        elif D_S5_Ttc == 2:
            call BS_D_S5_Chk_Cls002_Ttc02_Dmg
        call BS_D_S5_Cls002_Chk_Act
    elif D_S5_Cls == 3:
        if D_S5_Ttc == 1:
            call BS_D_S5_Chk_Cls003_Ttc01_Dmg
        elif D_S5_Ttc == 2:
            call BS_D_S5_Chk_Cls003_Ttc02_Dmg
        call BS_D_S5_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 6
#==========================================
label BS_D_S6_Chk_ActWhat_Atk:
#==========================================
#-----------------------------------
    if D_S6_Cls == 1:
        if D_S6_Ttc == 1:
            call BS_D_S6_Chk_Cls001_Ttc01_Dmg
        elif D_S6_Ttc == 2:
            call BS_D_S6_Chk_Cls001_Ttc02_Dmg
        call BS_D_S6_Cls001_Chk_Act
    elif D_S6_Cls == 2:
        if D_S6_Ttc == 1:
            call BS_D_S6_Chk_Cls002_Ttc01_Dmg
        elif D_S6_Ttc == 2:
            call BS_D_S6_Chk_Cls002_Ttc02_Dmg
        call BS_D_S6_Cls002_Chk_Act
    elif D_S6_Cls == 3:
        if D_S6_Ttc == 1:
            call BS_D_S6_Chk_Cls003_Ttc01_Dmg
        elif D_S6_Ttc == 2:
            call BS_D_S6_Chk_Cls003_Ttc02_Dmg
        call BS_D_S6_Cls003_Chk_Act
#-----------------------------------
    call Update_Scr_Cls_All_Phase_02_On
    call Call_Scr_DmgRcv_Eft_On_Off
#-----------------------------------
    return