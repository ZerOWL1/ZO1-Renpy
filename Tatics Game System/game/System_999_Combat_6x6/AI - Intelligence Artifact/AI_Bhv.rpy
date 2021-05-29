#///////////////////////  ATTACKER SLOT 1
#=========================
label AI_Bhv_A_S1:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_A_S1_Chg_Pos_Fmt
#-------------------------------------------------------
    if A_S1_Cls == 1 or A_S1_Cls == 2 or A_S1_Cls == 3:
        call AI_Bhv_A_S1_ChkAtk
    elif A_S1_Cls == 4:
        call AI_Bhv_A_S1_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  ATTACKER SLOT 2
#=========================
label AI_Bhv_A_S2:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_A_S2_Chg_Pos_Fmt
#-------------------------------------------------------
    if A_S2_Cls == 1 or A_S2_Cls == 2 or A_S2_Cls == 3:
        call AI_Bhv_A_S2_ChkAtk
    elif A_S2_Cls == 4:
        call AI_Bhv_A_S2_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  ATTACKER SLOT 3
#=========================
label AI_Bhv_A_S3:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_A_S3_Chg_Pos_Fmt
#-------------------------------------------------------
    if A_S3_Cls == 1 or A_S3_Cls == 2 or A_S3_Cls == 3:
        call AI_Bhv_A_S3_ChkAtk
    elif A_S3_Cls == 4:
        call AI_Bhv_A_S3_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  ATTACKER SLOT 4
#=========================
label AI_Bhv_A_S4:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_A_S4_Chg_Pos_Fmt
#-------------------------------------------------------
    if A_S4_Cls == 1 or A_S4_Cls == 2 or A_S4_Cls == 3:
        call AI_Bhv_A_S4_ChkAtk
    elif A_S4_Cls == 4:
        call AI_Bhv_A_S4_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  ATTACKER SLOT 5
#=========================
label AI_Bhv_A_S5:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_A_S5_Chg_Pos_Fmt
#-------------------------------------------------------
    if A_S5_Cls == 1 or A_S5_Cls == 2 or A_S5_Cls == 3:
        call AI_Bhv_A_S5_ChkAtk
    elif A_S5_Cls == 4:
        call AI_Bhv_A_S5_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  ATTACKER SLOT 6
#=========================
label AI_Bhv_A_S6:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_A_S6_Chg_Pos_Fmt
#-------------------------------------------------------
    if A_S6_Cls == 1 or A_S6_Cls == 2 or A_S6_Cls == 3:
        call AI_Bhv_A_S6_ChkAtk
    elif A_S6_Cls == 4:
        call AI_Bhv_A_S6_ChkSkill

    call BS_Rst_Control
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#=========================
label AI_Bhv_D_S1:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_D_S1_Chg_Pos_Fmt
#-------------------------------------------------------
    if D_S1_Cls == 1 or D_S1_Cls == 2 or D_S1_Cls == 3:
        call AI_Bhv_D_S1_ChkAtk
    elif D_S1_Cls == 4:
        call AI_Bhv_D_S1_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  DEFFENDER SLOT 2
#=========================
label AI_Bhv_D_S2:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_D_S2_Chg_Pos_Fmt
#-------------------------------------------------------
    if D_S2_Cls == 1 or D_S2_Cls == 2 or D_S2_Cls == 3:
        call AI_Bhv_D_S2_ChkAtk
    elif D_S2_Cls == 4:
        call AI_Bhv_D_S2_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  DEFFENDER SLOT 3
#=========================
label AI_Bhv_D_S3:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_D_S3_Chg_Pos_Fmt
#-------------------------------------------------------
    if D_S3_Cls == 1 or D_S3_Cls == 2 or D_S3_Cls == 3:
        call AI_Bhv_D_S3_ChkAtk
    elif D_S3_Cls == 4:
        call AI_Bhv_D_S3_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  DEFFENDER SLOT 4
#=========================
label AI_Bhv_D_S4:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_D_S4_Chg_Pos_Fmt
#-------------------------------------------------------
    if D_S4_Cls == 1 or D_S4_Cls == 2 or D_S4_Cls == 3:
        call AI_Bhv_D_S4_ChkAtk
    elif D_S4_Cls == 4:
        call AI_Bhv_D_S4_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  DEFFENDER SLOT 5
#=========================
label AI_Bhv_D_S5:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_D_S5_Chg_Pos_Fmt
#-------------------------------------------------------
    if D_S5_Cls == 1 or D_S5_Cls == 2 or D_S5_Cls == 3:
        call AI_Bhv_D_S5_ChkAtk
    elif D_S5_Cls == 4:
        call AI_Bhv_D_S5_ChkSkill

    call BS_Rst_Control
    return

#///////////////////////  DEFFENDER SLOT 6
#=========================
label AI_Bhv_D_S6:
#=========================
#-------------------------------------------------------
    $ BS_WhoControl = "AI"
    call AI_Bhv_D_S6_Chg_Pos_Fmt
#-------------------------------------------------------
    if D_S6_Cls == 1 or D_S6_Cls == 2 or D_S6_Cls == 3:
        call AI_Bhv_D_S6_ChkAtk
    elif D_S6_Cls == 4:
        call AI_Bhv_D_S6_ChkSkill

    call BS_Rst_Control
    return
