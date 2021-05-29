
#///////////////////////  ATTACKER SLOT 1
label BS_A_S1_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ A_S1_CanAct = "Return"
#-----------------------------------
    if A_S1_Tgt_01 == 1:
        call BS_D_S1_Chk_Evd
    if A_S1_Tgt_02 == 1:
        call BS_D_S2_Chk_Evd
    if A_S1_Tgt_03 == 1:
        call BS_D_S3_Chk_Evd
    if A_S1_Tgt_04 == 1:
        call BS_D_S4_Chk_Evd
    if A_S1_Tgt_05 == 1:
        call BS_D_S5_Chk_Evd
    if A_S1_Tgt_06 == 1:
        call BS_D_S6_Chk_Evd
#-----------------------------------
    if A_S1_Cls == 1:
        if A_S1_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif A_S1_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif A_S1_Cls == 2:
        if A_S1_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif A_S1_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif A_S1_Cls == 3:
        if A_S1_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif A_S1_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 2
label BS_A_S2_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ A_S2_CanAct = "Return"
#-----------------------------------
    if A_S2_Tgt_01 == 1:
        call BS_D_S1_Chk_Evd
    if A_S2_Tgt_02 == 1:
        call BS_D_S2_Chk_Evd
    if A_S2_Tgt_03 == 1:
        call BS_D_S3_Chk_Evd
    if A_S2_Tgt_04 == 1:
        call BS_D_S4_Chk_Evd
    if A_S2_Tgt_05 == 1:
        call BS_D_S5_Chk_Evd
    if A_S2_Tgt_06 == 1:
        call BS_D_S6_Chk_Evd
#-----------------------------------
    if A_S2_Cls == 1:
        if A_S2_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif A_S2_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif A_S2_Cls == 2:
        if A_S2_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif A_S2_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif A_S2_Cls == 3:
        if A_S2_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif A_S2_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 3
label BS_A_S3_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ A_S3_CanAct = "Return"
#-----------------------------------
    if A_S2_Tgt_01 == 1:
        call BS_D_S1_Chk_Evd
    if A_S2_Tgt_02 == 1:
        call BS_D_S2_Chk_Evd
    if A_S2_Tgt_03 == 1:
        call BS_D_S3_Chk_Evd
    if A_S2_Tgt_04 == 1:
        call BS_D_S4_Chk_Evd
    if A_S2_Tgt_05 == 1:
        call BS_D_S5_Chk_Evd
    if A_S2_Tgt_06 == 1:
        call BS_D_S6_Chk_Evd
#-----------------------------------
    if A_S3_Cls == 1:
        if A_S3_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif A_S3_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif A_S3_Cls == 2:
        if A_S3_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif A_S3_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif A_S3_Cls == 3:
        if A_S3_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif A_S3_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 4
label BS_A_S4_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ A_S4_CanAct = "Return"
#-----------------------------------
    if A_S4_Tgt_01 == 1:
        call BS_D_S1_Chk_Evd
    if A_S4_Tgt_02 == 1:
        call BS_D_S2_Chk_Evd
    if A_S4_Tgt_03 == 1:
        call BS_D_S3_Chk_Evd
    if A_S4_Tgt_04 == 1:
        call BS_D_S4_Chk_Evd
    if A_S4_Tgt_05 == 1:
        call BS_D_S5_Chk_Evd
    if A_S4_Tgt_06 == 1:
        call BS_D_S6_Chk_Evd
#-----------------------------------
    if A_S4_Cls == 1:
        if A_S4_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif A_S4_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif A_S4_Cls == 2:
        if A_S4_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif A_S4_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif A_S4_Cls == 3:
        if A_S4_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif A_S4_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 5
label BS_A_S5_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ A_S5_CanAct = "Return"
#-----------------------------------
    if A_S5_Tgt_01 == 1:
        call BS_D_S1_Chk_Evd
    if A_S5_Tgt_02 == 1:
        call BS_D_S2_Chk_Evd
    if A_S5_Tgt_03 == 1:
        call BS_D_S3_Chk_Evd
    if A_S5_Tgt_04 == 1:
        call BS_D_S4_Chk_Evd
    if A_S5_Tgt_05 == 1:
        call BS_D_S5_Chk_Evd
    if A_S5_Tgt_06 == 1:
        call BS_D_S6_Chk_Evd
#-----------------------------------
    if A_S5_Cls == 1:
        if A_S5_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif A_S5_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif A_S5_Cls == 2:
        if A_S5_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif A_S5_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif A_S5_Cls == 3:
        if A_S5_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif A_S5_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 6
label BS_A_S6_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ A_S6_CanAct = "Return"
#-----------------------------------
    if A_S6_Tgt_01 == 1:
        call BS_D_S1_Chk_Evd
    if A_S6_Tgt_02 == 1:
        call BS_D_S2_Chk_Evd
    if A_S6_Tgt_03 == 1:
        call BS_D_S3_Chk_Evd
    if A_S6_Tgt_04 == 1:
        call BS_D_S4_Chk_Evd
    if A_S6_Tgt_05 == 1:
        call BS_D_S5_Chk_Evd
    if A_S6_Tgt_06 == 1:
        call BS_D_S6_Chk_Evd
#-----------------------------------
    if A_S6_Cls == 1:
        if A_S6_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif A_S6_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif A_S6_Cls == 2:
        if A_S6_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif A_S6_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif A_S6_Cls == 3:
        if A_S6_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif A_S6_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
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
label BS_D_S1_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ D_S1_CanAct = "Return"
#-----------------------------------
    if D_S1_Tgt_01 == 1:
        call BS_A_S1_Chk_Evd
    if D_S1_Tgt_02 == 1:
        call BS_A_S2_Chk_Evd
    if D_S1_Tgt_03 == 1:
        call BS_A_S3_Chk_Evd
    if D_S1_Tgt_04 == 1:
        call BS_A_S4_Chk_Evd
    if D_S1_Tgt_05 == 1:
        call BS_A_S5_Chk_Evd
    if D_S1_Tgt_06 == 1:
        call BS_A_S6_Chk_Evd
#-----------------------------------
    if D_S1_Cls == 1:
        if D_S1_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif D_S1_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif D_S1_Cls == 2:
        if D_S1_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif D_S1_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif D_S1_Cls == 3:
        if D_S1_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif D_S1_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 2
label BS_D_S2_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ D_S2_CanAct = "Return"
#-----------------------------------
    if D_S2_Tgt_01 == 1:
        call BS_A_S1_Chk_Evd
    if D_S2_Tgt_02 == 1:
        call BS_A_S2_Chk_Evd
    if D_S2_Tgt_03 == 1:
        call BS_A_S3_Chk_Evd
    if D_S2_Tgt_04 == 1:
        call BS_A_S4_Chk_Evd
    if D_S2_Tgt_05 == 1:
        call BS_A_S5_Chk_Evd
    if D_S2_Tgt_06 == 1:
        call BS_A_S6_Chk_Evd
#-----------------------------------
    if D_S2_Cls == 1:
        if D_S2_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif D_S2_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif D_S2_Cls == 2:
        if D_S2_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif D_S2_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif D_S2_Cls == 3:
        if D_S2_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif D_S2_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 3
label BS_D_S3_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ D_S3_CanAct = "Return"
#-----------------------------------
    if D_S2_Tgt_01 == 1:
        call BS_A_S1_Chk_Evd
    if D_S2_Tgt_02 == 1:
        call BS_A_S2_Chk_Evd
    if D_S2_Tgt_03 == 1:
        call BS_A_S3_Chk_Evd
    if D_S2_Tgt_04 == 1:
        call BS_A_S4_Chk_Evd
    if D_S2_Tgt_05 == 1:
        call BS_A_S5_Chk_Evd
    if D_S2_Tgt_06 == 1:
        call BS_A_S6_Chk_Evd
#-----------------------------------
    if D_S3_Cls == 1:
        if D_S3_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif D_S3_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif D_S3_Cls == 2:
        if D_S3_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif D_S3_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif D_S3_Cls == 3:
        if D_S3_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif D_S3_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 4
label BS_D_S4_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ D_S4_CanAct = "Return"
#-----------------------------------
    if D_S4_Tgt_01 == 1:
        call BS_A_S1_Chk_Evd
    if D_S4_Tgt_02 == 1:
        call BS_A_S2_Chk_Evd
    if D_S4_Tgt_03 == 1:
        call BS_A_S3_Chk_Evd
    if D_S4_Tgt_04 == 1:
        call BS_A_S4_Chk_Evd
    if D_S4_Tgt_05 == 1:
        call BS_A_S5_Chk_Evd
    if D_S4_Tgt_06 == 1:
        call BS_A_S6_Chk_Evd
#-----------------------------------
    if D_S4_Cls == 1:
        if D_S4_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif D_S4_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif D_S4_Cls == 2:
        if D_S4_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif D_S4_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif D_S4_Cls == 3:
        if D_S4_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif D_S4_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 5
label BS_D_S5_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ D_S5_CanAct = "Return"
#-----------------------------------
    if D_S5_Tgt_01 == 1:
        call BS_A_S1_Chk_Evd
    if D_S5_Tgt_02 == 1:
        call BS_A_S2_Chk_Evd
    if D_S5_Tgt_03 == 1:
        call BS_A_S3_Chk_Evd
    if D_S5_Tgt_04 == 1:
        call BS_A_S4_Chk_Evd
    if D_S5_Tgt_05 == 1:
        call BS_A_S5_Chk_Evd
    if D_S5_Tgt_06 == 1:
        call BS_A_S6_Chk_Evd
#-----------------------------------
    if D_S5_Cls == 1:
        if D_S5_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif D_S5_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif D_S5_Cls == 2:
        if D_S5_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif D_S5_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif D_S5_Cls == 3:
        if D_S5_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif D_S5_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 6
label BS_D_S6_Chk_Rtn_Atk:
#-----------------------------------
    call Update_Scr_Cls_All_Phase_04_On
    $ D_S6_CanAct = "Return"
#-----------------------------------
    if D_S6_Tgt_01 == 1:
        call BS_A_S1_Chk_Evd
    if D_S6_Tgt_02 == 1:
        call BS_A_S2_Chk_Evd
    if D_S6_Tgt_03 == 1:
        call BS_A_S3_Chk_Evd
    if D_S6_Tgt_04 == 1:
        call BS_A_S4_Chk_Evd
    if D_S6_Tgt_05 == 1:
        call BS_A_S5_Chk_Evd
    if D_S6_Tgt_06 == 1:
        call BS_A_S6_Chk_Evd
#-----------------------------------
    if D_S6_Cls == 1:
        if D_S6_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls001_MeleeReturn, hard=True)
        elif D_S6_DmgType == "Range":
            $ renpy.pause(AntSec_Cls001_RangeReturn, hard=True)
    elif D_S6_Cls == 2:
        if D_S6_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls002_MeleeReturn, hard=True)
        elif D_S6_DmgType == "Range":
            $ renpy.pause(AntSec_Cls002_RangeReturn, hard=True)
    elif D_S6_Cls == 3:
        if D_S6_DmgType == "Melee":
            $ renpy.pause(AntSec_Cls003_MeleeReturn, hard=True)
        elif D_S6_DmgType == "Range":
            $ renpy.pause(AntSec_Cls003_RangeReturn, hard=True)
#-----------------------------------
    return
