screen Screen_UI_PI_Main:

    modal True

    if ((
    A_S1_Ctl_Type == "PI") or (
    A_S2_Ctl_Type == "PI") or (
    A_S3_Ctl_Type == "PI") or (
    A_S4_Ctl_Type == "PI") or (
    A_S5_Ctl_Type == "PI") or (
    A_S6_Ctl_Type == "PI")) or ((
    D_S1_Ctl_Type == "PI") or (
    D_S2_Ctl_Type == "PI") or (
    D_S3_Ctl_Type == "PI") or (
    D_S4_Ctl_Type == "PI") or (
    D_S5_Ctl_Type == "PI") or (
    D_S6_Ctl_Type == "PI")) or ((
    A_S1_Ctl_Type == "PI") and (
    A_S2_Ctl_Type == "PI") and (
    A_S3_Ctl_Type == "PI") and (
    A_S4_Ctl_Type == "PI") and (
    A_S5_Ctl_Type == "PI") and (
    A_S6_Ctl_Type == "PI") and (
    D_S1_Ctl_Type == "PI") and (
    D_S2_Ctl_Type == "PI") and (
    D_S3_Ctl_Type == "PI") and (
    D_S4_Ctl_Type == "PI") and (
    D_S5_Ctl_Type == "PI") and (
    D_S6_Ctl_Type == "PI")):

#-------------------------------------------------------
        if (
        BS_Who_Turn == "A_S1") or (
        BS_Who_Turn == "A_S2") or (
        BS_Who_Turn == "A_S3") or (
        BS_Who_Turn == "A_S4") or (
        BS_Who_Turn == "A_S5") or (
        BS_Who_Turn == "A_S6"):
            imagebutton auto "Images/Combat System/UI/Change_Ttc/ChangeTatic_Icon_%s.png" focus_mask True action ChgTtcClicked at A_Eft_ChgTtcButton
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action ChgPOSClicked at A_Eft_ChgPOSButton

            if BS_Who_Turn == "A_S1" and A_S1_Ctl_Type == "PI":
                if A_S1_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action A_S1_AtkClicked at A_Eft_ActionButton
                elif A_S1_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action A_S1_SkillClicked at A_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action A_S1_EndTurnClicked at A_Eft_EndTurnButton
            elif BS_Who_Turn == "A_S2" and A_S2_Ctl_Type == "PI":
                if A_S2_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action A_S2_AtkClicked at A_Eft_ActionButton
                elif A_S2_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action A_S2_SkillClicked at A_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action A_S2_EndTurnClicked at A_Eft_EndTurnButton
            elif BS_Who_Turn == "A_S3" and A_S3_Ctl_Type == "PI":
                if A_S3_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action A_S3_AtkClicked at A_Eft_ActionButton
                elif A_S3_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action A_S3_SkillClicked at A_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action A_S3_EndTurnClicked at A_Eft_EndTurnButton
            elif BS_Who_Turn == "A_S4" and A_S4_Ctl_Type == "PI":
                if A_S4_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action A_S4_AtkClicked at A_Eft_ActionButton
                elif A_S4_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action A_S4_SkillClicked at A_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action A_S4_EndTurnClicked at A_Eft_EndTurnButton
            elif BS_Who_Turn == "A_S5" and A_S5_Ctl_Type == "PI":
                if A_S5_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action A_S5_AtkClicked at A_Eft_ActionButton
                elif A_S5_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action A_S5_SkillClicked at A_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action A_S5_EndTurnClicked at A_Eft_EndTurnButton
            elif BS_Who_Turn == "A_S6" and A_S6_Ctl_Type == "PI":
                if A_S6_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action A_S6_AtkClicked at A_Eft_ActionButton
                elif A_S6_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action A_S6_SkillClicked at A_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action A_S6_EndTurnClicked at A_Eft_EndTurnButton

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

        elif (
        BS_Who_Turn == "D_S1") or (
        BS_Who_Turn == "D_S2") or (
        BS_Who_Turn == "D_S3") or (
        BS_Who_Turn == "D_S4") or (
        BS_Who_Turn == "D_S5") or (
        BS_Who_Turn == "D_S6"):
            imagebutton auto "Images/Combat System/UI/Change_Ttc/ChangeTatic_Icon_%s.png" focus_mask True action ChgTtcClicked at D_Eft_ChgTtcButton
            imagebutton auto "Images/Combat System/UI/Change_POS/ChangePOS_Icon_%s.png" focus_mask True action ChgPOSClicked at D_Eft_ChgPOSButton

            if BS_Who_Turn == "D_S1" and D_S1_Ctl_Type == "PI":
                if D_S1_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action D_S1_AtkClicked at D_Eft_ActionButton
                elif D_S1_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action D_S1_SkillClicked at D_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action D_S1_EndTurnClicked at D_Eft_EndTurnButton
            elif BS_Who_Turn == "D_S2" and D_S2_Ctl_Type == "PI":
                if D_S2_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action D_S2_AtkClicked at D_Eft_ActionButton
                elif D_S2_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action D_S2_SkillClicked at D_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action D_S2_EndTurnClicked at D_Eft_EndTurnButton
            elif BS_Who_Turn == "D_S3" and D_S3_Ctl_Type == "PI":
                if D_S3_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action D_S3_AtkClicked at D_Eft_ActionButton
                elif D_S3_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action D_S3_SkillClicked at D_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action D_S3_EndTurnClicked at D_Eft_EndTurnButton
            elif BS_Who_Turn == "D_S4" and D_S4_Ctl_Type == "PI":
                if D_S4_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action D_S4_AtkClicked at D_Eft_ActionButton
                elif D_S4_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action D_S4_SkillClicked at D_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action D_S4_EndTurnClicked at D_Eft_EndTurnButton
            elif BS_Who_Turn == "D_S5" and D_S5_Ctl_Type == "PI":
                if D_S5_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action D_S5_AtkClicked at D_Eft_ActionButton
                elif D_S5_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action D_S5_SkillClicked at D_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action D_S5_EndTurnClicked at D_Eft_EndTurnButton
            elif BS_Who_Turn == "D_S6" and D_S6_Ctl_Type == "PI":
                if D_S6_Tgt_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Attack_Icon_%s.png" focus_mask True action D_S6_AtkClicked at D_Eft_ActionButton
                elif D_S6_Tgt_Skill_Total > 0:
                    imagebutton auto "Images/Combat System/UI/Actions/Skill_Icon_%s.png" focus_mask True action D_S6_SkillClicked at D_Eft_ActionButton
                imagebutton auto "Images/Combat System/UI/Actions/End_Turn_Icon_%s.png" focus_mask True action D_S6_EndTurnClicked at D_Eft_EndTurnButton
