
#///////////////////////  ATTACKER SLOT 1
#=========================
label BS_Bhv_A_S1_Atk:
#=========================
#-----------------------------------
    call BS_A_S1_Chk_Can_Crit
    call BS_A_S1_Chk_ActWhat_Atk
#-----------------------------------
    call BS_A_S1_Chk_Can_Duel
    call BS_A_S1_Chk_Duel
#-----------------------------------
    call BS_A_S1_Chk_Rtn_Atk
    call BS_A_S1_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 2
#=========================
label BS_Bhv_A_S2_Atk:
#=========================
#-----------------------------------
    call BS_A_S2_Chk_Can_Crit
    call BS_A_S2_Chk_ActWhat_Atk
#-----------------------------------
    call BS_A_S2_Chk_Can_Duel
    call BS_A_S2_Chk_Duel
#-----------------------------------
    call BS_A_S2_Chk_Rtn_Atk
    call BS_A_S2_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 3
#=========================
label BS_Bhv_A_S3_Atk:
#=========================
#-----------------------------------
    call BS_A_S3_Chk_Can_Crit
    call BS_A_S3_Chk_ActWhat_Atk
#-----------------------------------
    call BS_A_S3_Chk_Can_Duel
    call BS_A_S3_Chk_Duel
#-----------------------------------
    call BS_A_S3_Chk_Rtn_Atk
    call BS_A_S3_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 4
#=========================
label BS_Bhv_A_S4_Atk:
#=========================
#-----------------------------------
    call BS_A_S4_Chk_Can_Crit
    call BS_A_S4_Chk_ActWhat_Atk
#-----------------------------------
    call BS_A_S4_Chk_Can_Duel
    call BS_A_S4_Chk_Duel
#-----------------------------------
    call BS_A_S4_Chk_Rtn_Atk
    call BS_A_S4_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 5
#=========================
label BS_Bhv_A_S5_Atk:
#=========================
#-----------------------------------
    call BS_A_S5_Chk_Can_Crit
    call BS_A_S5_Chk_ActWhat_Atk
#-----------------------------------
    call BS_A_S5_Chk_Can_Duel
    call BS_A_S5_Chk_Duel
#-----------------------------------
    call BS_A_S5_Chk_Rtn_Atk
    call BS_A_S5_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  ATTACKER SLOT 6
#=========================
label BS_Bhv_A_S6_Atk:
#=========================
#-----------------------------------
    call BS_A_S6_Chk_Can_Crit
    call BS_A_S6_Chk_ActWhat_Atk
#-----------------------------------
    call BS_A_S6_Chk_Can_Duel
    call BS_A_S6_Chk_Duel
#-----------------------------------
    call BS_A_S6_Chk_Rtn_Atk
    call BS_A_S6_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#=========================
label BS_Bhv_D_S1_Atk:
#=========================
#-----------------------------------
    call BS_D_S1_Chk_Can_Crit
    call BS_D_S1_Chk_ActWhat_Atk
#-----------------------------------
    call BS_D_S1_Chk_Can_Duel
    call BS_D_S1_Chk_Duel
#-----------------------------------
    call BS_D_S1_Chk_Rtn_Atk
    call BS_D_S1_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 2
#=========================
label BS_Bhv_D_S2_Atk:
#=========================
#-----------------------------------
    call BS_D_S2_Chk_Can_Crit
    call BS_D_S2_Chk_ActWhat_Atk
#-----------------------------------
    call BS_D_S2_Chk_Can_Duel
    call BS_D_S2_Chk_Duel
#-----------------------------------
    call BS_D_S2_Chk_Rtn_Atk
    call BS_D_S2_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 3
#=========================
label BS_Bhv_D_S3_Atk:
#=========================
#-----------------------------------
    call BS_D_S3_Chk_Can_Crit
    call BS_D_S3_Chk_ActWhat_Atk
#-----------------------------------
    call BS_D_S3_Chk_Can_Duel
    call BS_D_S3_Chk_Duel
#-----------------------------------
    call BS_D_S3_Chk_Rtn_Atk
    call BS_D_S3_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 4
#=========================
label BS_Bhv_D_S4_Atk:
#=========================
#-----------------------------------
    call BS_D_S4_Chk_Can_Crit
    call BS_D_S4_Chk_ActWhat_Atk
#-----------------------------------
    call BS_D_S4_Chk_Can_Duel
    call BS_D_S4_Chk_Duel
#-----------------------------------
    call BS_D_S4_Chk_Rtn_Atk
    call BS_D_S4_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 5
#=========================
label BS_Bhv_D_S5_Atk:
#=========================
#-----------------------------------
    call BS_D_S5_Chk_Can_Crit
    call BS_D_S5_Chk_ActWhat_Atk
#-----------------------------------
    call BS_D_S5_Chk_Can_Duel
    call BS_D_S5_Chk_Duel
#-----------------------------------
    call BS_D_S5_Chk_Rtn_Atk
    call BS_D_S5_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)

#///////////////////////  DEFFENDER SLOT 6
#=========================
label BS_Bhv_D_S6_Atk:
#=========================
#-----------------------------------
    call BS_D_S6_Chk_Can_Crit
    call BS_D_S6_Chk_ActWhat_Atk
#-----------------------------------
    call BS_D_S6_Chk_Can_Duel
    call BS_D_S6_Chk_Duel
#-----------------------------------
    call BS_D_S6_Chk_Rtn_Atk
    call BS_D_S6_Chk_EndTurn_Atk
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
        e "Error: Attack behavior, Who control = None"
        $ renpy.pause (hard=True)
