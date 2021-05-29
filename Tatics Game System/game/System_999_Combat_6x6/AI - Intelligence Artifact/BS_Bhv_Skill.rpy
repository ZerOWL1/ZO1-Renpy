
#///////////////////////  ATTACKER SLOT 1
#=================================
label BS_Bhv_A_S1_Skill:
#=================================
#-----------------------------------
    call BS_A_S1_Chk_SklType
    call BS_A_S1_Chk_ActWhat_Skill
#-----------------------------------
    if A_S1_Ttc == 1 or A_S1_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_A_S1_Chk_Rtn_Skill
    call BS_A_S1_Chk_EndTurn_Skill
#-----------------------------------
    call BS_A_Rst_DmgRcv
    call BS_A_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 2
#=================================
label BS_Bhv_A_S2_Skill:
#=================================
#-----------------------------------
    call BS_A_S2_Chk_SklType
    call BS_A_S2_Chk_ActWhat_Skill
#-----------------------------------
    if A_S2_Ttc == 1 or A_S2_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_A_S2_Chk_Rtn_Skill
    call BS_A_S2_Chk_EndTurn_Skill
#-----------------------------------
    call BS_A_Rst_DmgRcv
    call BS_A_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 3
#=================================
label BS_Bhv_A_S3_Skill:
#=================================
#-----------------------------------
    call BS_A_S3_Chk_SklType
    call BS_A_S3_Chk_ActWhat_Skill
#-----------------------------------
    if A_S3_Ttc == 1 or A_S3_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_A_S3_Chk_Rtn_Skill
    call BS_A_S3_Chk_EndTurn_Skill
#-----------------------------------
    call BS_A_Rst_DmgRcv
    call BS_A_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 4
#=================================
label BS_Bhv_A_S4_Skill:
#=================================
#-----------------------------------
    call BS_A_S4_Chk_SklType
    call BS_A_S4_Chk_ActWhat_Skill
#-----------------------------------
    if A_S4_Ttc == 1 or A_S4_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_A_S4_Chk_Rtn_Skill
    call BS_A_S4_Chk_EndTurn_Skill
#-----------------------------------
    call BS_A_Rst_DmgRcv
    call BS_A_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 5
#=================================
label BS_Bhv_A_S5_Skill:
#=================================
#-----------------------------------
    call BS_A_S5_Chk_SklType
    call BS_A_S5_Chk_ActWhat_Skill
#-----------------------------------
    if A_S5_Ttc == 1 or A_S5_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_A_S5_Chk_Rtn_Skill
    call BS_A_S5_Chk_EndTurn_Skill
#-----------------------------------
    call BS_A_Rst_DmgRcv
    call BS_A_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 6
#=================================
label BS_Bhv_A_S6_Skill:
#=================================
#-----------------------------------
    call BS_A_S6_Chk_SklType
    call BS_A_S6_Chk_ActWhat_Skill
#-----------------------------------
    if A_S6_Ttc == 1 or A_S6_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_A_S6_Chk_Rtn_Skill
    call BS_A_S6_Chk_EndTurn_Skill
#-----------------------------------
    call BS_A_Rst_DmgRcv
    call BS_A_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#=================================
label BS_Bhv_D_S1_Skill:
#=================================
#-----------------------------------
    call BS_D_S1_Chk_SklType
    call BS_D_S1_Chk_ActWhat_Skill
#-----------------------------------
    if D_S1_Ttc == 1 or D_S1_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_D_S1_Chk_Rtn_Skill
    call BS_D_S1_Chk_EndTurn_Skill
#-----------------------------------
    call BS_D_Rst_DmgRcv
    call BS_D_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 2
#=================================
label BS_Bhv_D_S2_Skill:
#=================================
#-----------------------------------
    call BS_D_S2_Chk_SklType
    call BS_D_S2_Chk_ActWhat_Skill
#-----------------------------------
    if D_S2_Ttc == 1 or D_S2_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_D_S2_Chk_Rtn_Skill
    call BS_D_S2_Chk_EndTurn_Skill
#-----------------------------------
    call BS_D_Rst_DmgRcv
    call BS_D_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 3
#=================================
label BS_Bhv_D_S3_Skill:
#=================================
#-----------------------------------
    call BS_D_S3_Chk_SklType
    call BS_D_S3_Chk_ActWhat_Skill
#-----------------------------------
    if D_S3_Ttc == 1 or D_S3_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_D_S3_Chk_Rtn_Skill
    call BS_D_S3_Chk_EndTurn_Skill
#-----------------------------------
    call BS_D_Rst_DmgRcv
    call BS_D_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 4
#=================================
label BS_Bhv_D_S4_Skill:
#=================================
#-----------------------------------
    call BS_D_S4_Chk_SklType
    call BS_D_S4_Chk_ActWhat_Skill
#-----------------------------------
    if D_S4_Ttc == 1 or D_S4_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_D_S4_Chk_Rtn_Skill
    call BS_D_S4_Chk_EndTurn_Skill
#-----------------------------------
    call BS_D_Rst_DmgRcv
    call BS_D_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 5
#=================================
label BS_Bhv_D_S5_Skill:
#=================================
#-----------------------------------
    call BS_D_S5_Chk_SklType
    call BS_D_S5_Chk_ActWhat_Skill
#-----------------------------------
    if D_S5_Ttc == 1 or D_S5_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_D_S5_Chk_Rtn_Skill
    call BS_D_S5_Chk_EndTurn_Skill
#-----------------------------------
    call BS_D_Rst_DmgRcv
    call BS_D_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 6
#=================================
label BS_Bhv_D_S6_Skill:
#=================================
#-----------------------------------
    call BS_D_S6_Chk_SklType
    call BS_D_S6_Chk_ActWhat_Skill
#-----------------------------------
    if D_S6_Ttc == 1 or D_S6_Ttc == 2:
        call Update_Scr_Cls_All_Phase_03_On
        call Update_Scr_HealRcv_Txt_On
#-----------------------------------
    call BS_D_S6_Chk_Rtn_Skill
    call BS_D_S6_Chk_EndTurn_Skill
#-----------------------------------
    call BS_D_Rst_DmgRcv
    call BS_D_Rst_DmgRcvType
#-----------------------------------
    call Update_Scr_Cls_All_Phase_00_On
#-----------------------------------
    if BS_WhoControl == "PI":
        call BS_Rst_Control
        jump BS_Chk_WhoAct
    elif BS_WhoControl == "AI":
        call BS_Rst_Control
        return
    else:
        e "Error: Skill behavior, Who control = None"
        $ renpy.pause (hard=True)
