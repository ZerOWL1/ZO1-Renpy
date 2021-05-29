
#///////////////////////  ATTACKER SLOT 1
label AI_Bhv_A_S1_ChkSkill:
#-------------------------------------------------------
    while A_S1_CanAct == 1:
        call BS_A_S1_Chk_TgtSkill
        if A_S1_ChgTtc_Count >= 3:
            $ A_S1_CanAct = 0
            $ A_S1_ChgTtc_Count = 0
        elif A_S1_Tgt_Skill_Total == 0:
            call AI_Bhv_A_S1_Chg_SkillTtc
        elif A_S1_Tgt_Skill_Total >= 1:
            call BS_Bhv_A_S1_Skill
        call BS_A_S1_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 2
label AI_Bhv_A_S2_ChkSkill:
#-------------------------------------------------------
    while A_S2_CanAct == 1:
        call BS_A_S2_Chk_TgtSkill
        if A_S2_ChgTtc_Count >= 3:
            $ A_S2_CanAct = 0
            $ A_S2_ChgTtc_Count = 0
        elif A_S2_Tgt_Skill_Total == 0:
            call AI_Bhv_A_S2_Chg_SkillTtc
        elif A_S2_Tgt_Skill_Total >= 1:
            call BS_Bhv_A_S2_Skill
        call BS_A_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 3
label AI_Bhv_A_S3_ChkSkill:
#-------------------------------------------------------
    while A_S3_CanAct == 1:
        call BS_A_S3_Chk_TgtSkill
        if A_S3_ChgTtc_Count >= 3:
            $ A_S3_CanAct = 0
            $ A_S3_ChgTtc_Count = 0
        elif A_S3_Tgt_Skill_Total == 0:
            call AI_Bhv_A_S3_Chg_SkillTtc
        elif A_S3_Tgt_Skill_Total >= 1:
            call BS_Bhv_A_S3_Skill
        call BS_A_S3_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 4
label AI_Bhv_A_S4_ChkSkill:
#-------------------------------------------------------
    while A_S4_CanAct == 1:
        call BS_A_S4_Chk_TgtSkill
        if A_S4_ChgTtc_Count >= 3:
            $ A_S4_CanAct = 0
            $ A_S4_ChgTtc_Count = 0
        elif A_S4_Tgt_Skill_Total == 0:
            call AI_Bhv_A_S4_Chg_SkillTtc
        elif A_S4_Tgt_Skill_Total >= 1:
            call BS_Bhv_A_S4_Skill
        call BS_A_S4_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 5
label AI_Bhv_A_S5_ChkSkill:
#-------------------------------------------------------
    while A_S5_CanAct == 1:
        call BS_A_S5_Chk_TgtSkill
        if A_S5_ChgTtc_Count >= 3:
            $ A_S5_CanAct = 0
            $ A_S5_ChgTtc_Count = 0
        elif A_S5_Tgt_Skill_Total == 0:
            call AI_Bhv_A_S5_Chg_SkillTtc
        elif A_S5_Tgt_Skill_Total >= 1:
            call BS_Bhv_A_S5_Skill
        call BS_A_S5_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 6
label AI_Bhv_A_S6_ChkSkill:
#-------------------------------------------------------
    while A_S6_CanAct == 1:
        call BS_A_S6_Chk_TgtSkill
        if A_S6_ChgTtc_Count >= 3:
            $ A_S6_CanAct = 0
            $ A_S6_ChgTtc_Count = 0
        elif A_S6_Tgt_Skill_Total == 0:
            call AI_Bhv_A_S6_Chg_SkillTtc
        elif A_S6_Tgt_Skill_Total >= 1:
            call BS_Bhv_A_S6_Skill
        call BS_A_S6_Rst_Tgt
#-------------------------------------------------------
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
label AI_Bhv_D_S1_ChkSkill:
#-------------------------------------------------------
    while D_S1_CanAct == 1:
        call BS_D_S1_Chk_TgtSkill
        if D_S1_ChgTtc_Count >= 3:
            $ D_S1_CanAct = 0
            $ D_S1_ChgTtc_Count = 0
        elif D_S1_Tgt_Skill_Total == 0:
            call AI_Bhv_D_S1_Chg_SkillTtc
        elif D_S1_Tgt_Skill_Total >= 1:
            call BS_Bhv_D_S1_Skill
        call BS_D_S1_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 2
label AI_Bhv_D_S2_ChkSkill:
#-------------------------------------------------------
    while D_S2_CanAct == 1:
        call BS_D_S2_Chk_TgtSkill
        if D_S2_ChgTtc_Count >= 3:
            $ D_S2_CanAct = 0
            $ D_S2_ChgTtc_Count = 0
        elif D_S2_Tgt_Skill_Total == 0:
            call AI_Bhv_D_S2_Chg_SkillTtc
        elif D_S2_Tgt_Skill_Total >= 1:
            call BS_Bhv_D_S2_Skill
        call BS_D_S2_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 3
label AI_Bhv_D_S3_ChkSkill:
#-------------------------------------------------------
    while D_S3_CanAct == 1:
        call BS_D_S3_Chk_TgtSkill
        if D_S3_ChgTtc_Count >= 3:
            $ D_S3_CanAct = 0
            $ D_S3_ChgTtc_Count = 0
        elif D_S3_Tgt_Skill_Total == 0:
            call AI_Bhv_D_S3_Chg_SkillTtc
        elif D_S3_Tgt_Skill_Total >= 1:
            call BS_Bhv_D_S3_Skill
        call BS_D_S3_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 4
label AI_Bhv_D_S4_ChkSkill:
#-------------------------------------------------------
    while D_S4_CanAct == 1:
        call BS_D_S4_Chk_TgtSkill
        if D_S4_ChgTtc_Count >= 3:
            $ D_S4_CanAct = 0
            $ D_S4_ChgTtc_Count = 0
        elif D_S4_Tgt_Skill_Total == 0:
            call AI_Bhv_D_S4_Chg_SkillTtc
        elif D_S4_Tgt_Skill_Total >= 1:
            call BS_Bhv_D_S4_Skill
        call BS_D_S4_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 5
label AI_Bhv_D_S5_ChkSkill:
#-------------------------------------------------------
    while D_S5_CanAct == 1:
        call BS_D_S5_Chk_TgtSkill
        if D_S5_ChgTtc_Count >= 3:
            $ D_S5_CanAct = 0
            $ D_S5_ChgTtc_Count = 0
        elif D_S5_Tgt_Skill_Total == 0:
            call AI_Bhv_D_S5_Chg_SkillTtc
        elif D_S5_Tgt_Skill_Total >= 1:
            call BS_Bhv_D_S5_Skill
        call BS_D_S5_Rst_Tgt
#-------------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 6
label AI_Bhv_D_S6_ChkSkill:
#-------------------------------------------------------
    while D_S6_CanAct == 1:
        call BS_D_S6_Chk_TgtSkill
        if D_S6_ChgTtc_Count >= 3:
            $ D_S6_CanAct = 0
            $ D_S6_ChgTtc_Count = 0
        elif D_S6_Tgt_Skill_Total == 0:
            call AI_Bhv_D_S6_Chg_SkillTtc
        elif D_S6_Tgt_Skill_Total >= 1:
            call BS_Bhv_D_S6_Skill
        call BS_D_S6_Rst_Tgt
#-------------------------------------------------------
    return
