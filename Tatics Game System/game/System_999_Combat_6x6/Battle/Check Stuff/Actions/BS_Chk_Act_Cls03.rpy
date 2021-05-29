
#///////////////////////  ATTACKER SLOT 1
#==========================================
label BS_A_S1_Cls003_Chk_Act:
#==========================================

    if A_S1_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S1_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif A_S1_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S1_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif A_S1_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $ A_S1_CanAct = "Target Hit"
    return

#///////////////////////  ATTACKER SLOT 2
#==========================================
label BS_A_S2_Cls003_Chk_Act:
#==========================================

    if A_S2_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S2_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif A_S2_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S2_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif A_S2_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $A_S2_CanAct = "Target Hit"
    return

#///////////////////////  ATTACKER SLOT 3
#==========================================
label BS_A_S3_Cls003_Chk_Act:
#==========================================

    if A_S3_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S3_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif A_S3_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S3_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif A_S3_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $A_S3_CanAct = "Target Hit"
    return

#///////////////////////  ATTACKER SLOT 4
#==========================================
label BS_A_S4_Cls003_Chk_Act:
#==========================================

    if A_S4_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S4_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif A_S4_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S4_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif A_S4_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $A_S4_CanAct = "Target Hit"
    return

#///////////////////////  ATTACKER SLOT 5
#==========================================
label BS_A_S5_Cls003_Chk_Act:
#==========================================

    if A_S5_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S5_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif A_S5_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S5_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif A_S5_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $A_S5_CanAct = "Target Hit"
    return

#///////////////////////  ATTACKER SLOT 6
#==========================================
label BS_A_S6_Cls003_Chk_Act:
#==========================================

    if A_S6_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S6_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif A_S6_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if A_S6_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif A_S6_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $A_S6_CanAct = "Target Hit"
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
label BS_D_S1_Cls003_Chk_Act:
#==========================================

    if D_S1_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S1_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif D_S1_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S1_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif D_S1_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $ D_S1_CanAct = "Target Hit"
    return

#///////////////////////  DEFFENDER SLOT 2
#==========================================
label BS_D_S2_Cls003_Chk_Act:
#==========================================

    if D_S2_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S2_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif D_S2_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S2_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif D_S2_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $D_S2_CanAct = "Target Hit"
    return

#///////////////////////  DEFFENDER SLOT 3
#==========================================
label BS_D_S3_Cls003_Chk_Act:
#==========================================

    if D_S3_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S3_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif D_S3_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S3_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif D_S3_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $D_S3_CanAct = "Target Hit"
    return

#///////////////////////  DEFFENDER SLOT 4
#==========================================
label BS_D_S4_Cls003_Chk_Act:
#==========================================

    if D_S4_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S4_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif D_S4_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S4_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif D_S4_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $D_S4_CanAct = "Target Hit"
    return

#///////////////////////  DEFFENDER SLOT 5
#==========================================
label BS_D_S5_Cls003_Chk_Act:
#==========================================

    if D_S5_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S5_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif D_S5_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S5_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif D_S5_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $D_S5_CanAct = "Target Hit"
    return

#///////////////////////  DEFFENDER SLOT 6
#==========================================
label BS_D_S6_Cls003_Chk_Act:
#==========================================

    if D_S6_CanCrt == 1:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S6_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeCrit, hard=True)
        elif D_S6_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeCrit, hard=True)
    else:
        $ renpy.pause(SecWait_Act, hard=True)
        if D_S6_DmgType == "Melee":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_MeleeNormal, hard=True)
        elif D_S6_DmgType == "Range":
            call Call_Scr_Tgt_Ttc_On_Off
            call Update_Scr_Cls_All_Phase_01_On
            $ renpy.pause(AntSec_Cls003_RangeNormal, hard=True)

    $D_S6_CanAct = "Target Hit"
    return