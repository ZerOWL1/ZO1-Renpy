
#///////////////////////  ATTACKER SLOT 1
#===========================================================
label BS_A_S1_Chk_SklType:
#------------------------------------------------
    $ A_S1_DmgType = "Skill"
#------------------------------------------------
    if A_S1_Ttc == 3 or A_S1_Ttc == 4 or A_S1_Ttc == 5:
        if A_S1_Ttc == 3:
            $ A_S1_Skil = BS_Cls004_Buf01_Name
            $ A_S1_Skil_No = BS_Cls004_Buf01_No
            $ A_S1_Skil_Type = BS_Cls004_Buf01_Type
            call BS_A_S1_Chk_AddSkl_Allies
            call BS_A_S1_Buf01_Tgt
        elif A_S1_Ttc == 4:
            $ A_S1_Skil = BS_Cls004_Buf02_Name
            $ A_S1_Skil_No = BS_Cls004_Buf02_No
            $ A_S1_Skil_Type = BS_Cls004_Buf02_Type
            call BS_A_S1_Chk_AddSkl_Allies
            call BS_A_S1_Buf02_Tgt
        elif A_S1_Ttc == 5:
            $ A_S1_Skil = BS_Cls004_Buf03_Name
            $ A_S1_Skil_No = BS_Cls004_Buf03_No
            $ A_S1_Skil_Type = BS_Cls004_Buf03_Type
            call BS_A_S1_Chk_AddSkl_Allies
            call BS_A_S1_Buf03_Tgt
#------------------------------------------------
    else:
        if A_S1_Ttc == 1:
            call BS_A_S1_Chk_HealOrg_Ttc01
        elif A_S1_Ttc == 2:
            call BS_A_S1_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 2
#===========================================================
label BS_A_S2_Chk_SklType:
#------------------------------------------------
    $ A_S2_DmgType = "Skill"
#------------------------------------------------
    if A_S2_Ttc == 3 or A_S2_Ttc == 4 or A_S2_Ttc == 5:
        if A_S2_Ttc == 3:
            $ A_S2_Skil = BS_Cls004_Buf01_Name
            $ A_S2_Skil_No = BS_Cls004_Buf01_No
            $ A_S2_Skil_Type = BS_Cls004_Buf01_Type
            call BS_A_S2_Chk_AddSkl_Allies
            call BS_A_S2_Buf01_Tgt
        elif A_S2_Ttc == 4:
            $ A_S2_Skil = BS_Cls004_Buf02_Name
            $ A_S2_Skil_No = BS_Cls004_Buf02_No
            $ A_S2_Skil_Type = BS_Cls004_Buf02_Type
            call BS_A_S2_Chk_AddSkl_Allies
            call BS_A_S2_Buf02_Tgt
        elif A_S2_Ttc == 5:
            $ A_S2_Skil = BS_Cls004_Buf03_Name
            $ A_S2_Skil_No = BS_Cls004_Buf03_No
            $ A_S2_Skil_Type = BS_Cls004_Buf03_Type
            call BS_A_S2_Chk_AddSkl_Allies
            call BS_A_S2_Buf03_Tgt
#------------------------------------------------
    else:
        if A_S2_Ttc == 1:
            call BS_A_S2_Chk_HealOrg_Ttc01
        elif A_S2_Ttc == 2:
            call BS_A_S2_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 3
#===========================================================
label BS_A_S3_Chk_SklType:
#------------------------------------------------
    $ A_S3_DmgType = "Skill"
#------------------------------------------------
    if A_S3_Ttc == 3 or A_S3_Ttc == 4 or A_S3_Ttc == 5:
        if A_S3_Ttc == 3:
            $ A_S3_Skil = BS_Cls004_Buf01_Name
            $ A_S3_Skil_No = BS_Cls004_Buf01_No
            $ A_S3_Skil_Type = BS_Cls004_Buf01_Type
            call BS_A_S3_Chk_AddSkl_Allies
            call BS_A_S3_Buf01_Tgt
        elif A_S3_Ttc == 4:
            $ A_S3_Skil = BS_Cls004_Buf02_Name
            $ A_S3_Skil_No = BS_Cls004_Buf02_No
            $ A_S3_Skil_Type = BS_Cls004_Buf02_Type
            call BS_A_S3_Chk_AddSkl_Allies
            call BS_A_S3_Buf02_Tgt
        elif A_S3_Ttc == 5:
            $ A_S3_Skil = BS_Cls004_Buf03_Name
            $ A_S3_Skil_No = BS_Cls004_Buf03_No
            $ A_S3_Skil_Type = BS_Cls004_Buf03_Type
            call BS_A_S3_Chk_AddSkl_Allies
            call BS_A_S3_Buf03_Tgt
#------------------------------------------------
    else:
        if A_S3_Ttc == 1:
            call BS_A_S3_Chk_HealOrg_Ttc01
        elif A_S3_Ttc == 2:
            call BS_A_S3_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 4
#===========================================================
label BS_A_S4_Chk_SklType:
#------------------------------------------------
    $ A_S4_DmgType = "Skill"
#------------------------------------------------
    if A_S4_Ttc == 3 or A_S4_Ttc == 4 or A_S4_Ttc == 5:
        if A_S4_Ttc == 3:
            $ A_S4_Skil = BS_Cls004_Buf01_Name
            $ A_S4_Skil_No = BS_Cls004_Buf01_No
            $ A_S4_Skil_Type = BS_Cls004_Buf01_Type
            call BS_A_S4_Chk_AddSkl_Allies
            call BS_A_S4_Buf01_Tgt
        elif A_S4_Ttc == 4:
            $ A_S4_Skil = BS_Cls004_Buf02_Name
            $ A_S4_Skil_No = BS_Cls004_Buf02_No
            $ A_S4_Skil_Type = BS_Cls004_Buf02_Type
            call BS_A_S4_Chk_AddSkl_Allies
            call BS_A_S4_Buf02_Tgt
        elif A_S4_Ttc == 5:
            $ A_S4_Skil = BS_Cls004_Buf03_Name
            $ A_S4_Skil_No = BS_Cls004_Buf03_No
            $ A_S4_Skil_Type = BS_Cls004_Buf03_Type
            call BS_A_S4_Chk_AddSkl_Allies
            call BS_A_S4_Buf03_Tgt
#------------------------------------------------
    else:
        if A_S4_Ttc == 1:
            call BS_A_S4_Chk_HealOrg_Ttc01
        elif A_S4_Ttc == 2:
            call BS_A_S4_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 5
#===========================================================
label BS_A_S5_Chk_SklType:
#------------------------------------------------
    $ A_S5_DmgType = "Skill"
#------------------------------------------------
    if A_S5_Ttc == 3 or A_S5_Ttc == 4 or A_S5_Ttc == 5:
        if A_S5_Ttc == 3:
            $ A_S5_Skil = BS_Cls004_Buf01_Name
            $ A_S5_Skil_No = BS_Cls004_Buf01_No
            $ A_S5_Skil_Type = BS_Cls004_Buf01_Type
            call BS_A_S5_Chk_AddSkl_Allies
            call BS_A_S5_Buf01_Tgt
        elif A_S5_Ttc == 4:
            $ A_S5_Skil = BS_Cls004_Buf02_Name
            $ A_S5_Skil_No = BS_Cls004_Buf02_No
            $ A_S5_Skil_Type = BS_Cls004_Buf02_Type
            call BS_A_S5_Chk_AddSkl_Allies
            call BS_A_S5_Buf02_Tgt
        elif A_S5_Ttc == 5:
            $ A_S5_Skil = BS_Cls004_Buf03_Name
            $ A_S5_Skil_No = BS_Cls004_Buf03_No
            $ A_S5_Skil_Type = BS_Cls004_Buf03_Type
            call BS_A_S5_Chk_AddSkl_Allies
            call BS_A_S5_Buf03_Tgt
#------------------------------------------------
    else:
        if A_S5_Ttc == 1:
            call BS_A_S5_Chk_HealOrg_Ttc01
        elif A_S5_Ttc == 2:
            call BS_A_S5_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  ATTACKER SLOT 6
#===========================================================
label BS_A_S6_Chk_SklType:
#------------------------------------------------
    $ A_S6_DmgType = "Skill"
#------------------------------------------------
    if A_S6_Ttc == 3 or A_S6_Ttc == 4 or A_S6_Ttc == 5:
        if A_S6_Ttc == 3:
            $ A_S6_Skil = BS_Cls004_Buf01_Name
            $ A_S6_Skil_No = BS_Cls004_Buf01_No
            $ A_S6_Skil_Type = BS_Cls004_Buf01_Type
            call BS_A_S6_Chk_AddSkl_Allies
            call BS_A_S6_Buf01_Tgt
        elif A_S6_Ttc == 4:
            $ A_S6_Skil = BS_Cls004_Buf02_Name
            $ A_S6_Skil_No = BS_Cls004_Buf02_No
            $ A_S6_Skil_Type = BS_Cls004_Buf02_Type
            call BS_A_S6_Chk_AddSkl_Allies
            call BS_A_S6_Buf02_Tgt
        elif A_S6_Ttc == 5:
            $ A_S6_Skil = BS_Cls004_Buf03_Name
            $ A_S6_Skil_No = BS_Cls004_Buf03_No
            $ A_S6_Skil_Type = BS_Cls004_Buf03_Type
            call BS_A_S6_Chk_AddSkl_Allies
            call BS_A_S6_Buf03_Tgt
#------------------------------------------------
    else:
        if A_S6_Ttc == 1:
            call BS_A_S6_Chk_HealOrg_Ttc01
        elif A_S6_Ttc == 2:
            call BS_A_S6_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#===========================================================
label BS_D_S1_Chk_SklType:
#------------------------------------------------
    $ D_S1_DmgType = "Skill"
#------------------------------------------------
    if D_S1_Ttc == 3 or D_S1_Ttc == 4 or D_S1_Ttc == 5:
        if D_S1_Ttc == 3:
            $ D_S1_Skil = BS_Cls004_Buf01_Name
            $ D_S1_Skil_No = BS_Cls004_Buf01_No
            $ D_S1_Skil_Type = BS_Cls004_Buf01_Type
            call BS_D_S1_Chk_AddSkl_Allies
            call BS_D_S1_Buf01_Tgt
        elif D_S1_Ttc == 4:
            $ D_S1_Skil = BS_Cls004_Buf02_Name
            $ D_S1_Skil_No = BS_Cls004_Buf02_No
            $ D_S1_Skil_Type = BS_Cls004_Buf02_Type
            call BS_D_S1_Chk_AddSkl_Allies
            call BS_D_S1_Buf02_Tgt
        elif D_S1_Ttc == 5:
            $ D_S1_Skil = BS_Cls004_Buf03_Name
            $ D_S1_Skil_No = BS_Cls004_Buf03_No
            $ D_S1_Skil_Type = BS_Cls004_Buf03_Type
            call BS_D_S1_Chk_AddSkl_Allies
            call BS_D_S1_Buf03_Tgt
#------------------------------------------------
    else:
        if D_S1_Ttc == 1:
            call BS_D_S1_Chk_HealOrg_Ttc01
        elif D_S1_Ttc == 2:
            call BS_D_S1_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 2
#===========================================================
label BS_D_S2_Chk_SklType:
#------------------------------------------------
    $ D_S2_DmgType = "Skill"
#------------------------------------------------
    if D_S2_Ttc == 3 or D_S2_Ttc == 4 or D_S2_Ttc == 5:
        if D_S2_Ttc == 3:
            $ D_S2_Skil = BS_Cls004_Buf01_Name
            $ D_S2_Skil_No = BS_Cls004_Buf01_No
            $ D_S2_Skil_Type = BS_Cls004_Buf01_Type
            call BS_D_S2_Chk_AddSkl_Allies
            call BS_D_S2_Buf01_Tgt
        elif D_S2_Ttc == 4:
            $ D_S2_Skil = BS_Cls004_Buf02_Name
            $ D_S2_Skil_No = BS_Cls004_Buf02_No
            $ D_S2_Skil_Type = BS_Cls004_Buf02_Type
            call BS_D_S2_Chk_AddSkl_Allies
            call BS_D_S2_Buf02_Tgt
        elif D_S2_Ttc == 5:
            $ D_S2_Skil = BS_Cls004_Buf03_Name
            $ D_S2_Skil_No = BS_Cls004_Buf03_No
            $ D_S2_Skil_Type = BS_Cls004_Buf03_Type
            call BS_D_S2_Chk_AddSkl_Allies
            call BS_D_S2_Buf03_Tgt
#------------------------------------------------
    else:
        if D_S2_Ttc == 1:
            call BS_D_S2_Chk_HealOrg_Ttc01
        elif D_S2_Ttc == 2:
            call BS_D_S2_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 3
#===========================================================
label BS_D_S3_Chk_SklType:
#------------------------------------------------
    $ D_S3_DmgType = "Skill"
#------------------------------------------------
    if D_S3_Ttc == 3 or D_S3_Ttc == 4 or D_S3_Ttc == 5:
        if D_S3_Ttc == 3:
            $ D_S3_Skil = BS_Cls004_Buf01_Name
            $ D_S3_Skil_No = BS_Cls004_Buf01_No
            $ D_S3_Skil_Type = BS_Cls004_Buf01_Type
            call BS_D_S3_Chk_AddSkl_Allies
            call BS_D_S3_Buf01_Tgt
        elif D_S3_Ttc == 4:
            $ D_S3_Skil = BS_Cls004_Buf02_Name
            $ D_S3_Skil_No = BS_Cls004_Buf02_No
            $ D_S3_Skil_Type = BS_Cls004_Buf02_Type
            call BS_D_S3_Chk_AddSkl_Allies
            call BS_D_S3_Buf02_Tgt
        elif D_S3_Ttc == 5:
            $ D_S3_Skil = BS_Cls004_Buf03_Name
            $ D_S3_Skil_No = BS_Cls004_Buf03_No
            $ D_S3_Skil_Type = BS_Cls004_Buf03_Type
            call BS_D_S3_Chk_AddSkl_Allies
            call BS_D_S3_Buf03_Tgt
#------------------------------------------------
    else:
        if D_S3_Ttc == 1:
            call BS_D_S3_Chk_HealOrg_Ttc01
        elif D_S3_Ttc == 2:
            call BS_D_S3_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 4
#===========================================================
label BS_D_S4_Chk_SklType:
#------------------------------------------------
    $ D_S4_DmgType = "Skill"
#------------------------------------------------
    if D_S4_Ttc == 3 or D_S4_Ttc == 4 or D_S4_Ttc == 5:
        if D_S4_Ttc == 3:
            $ D_S4_Skil = BS_Cls004_Buf01_Name
            $ D_S4_Skil_No = BS_Cls004_Buf01_No
            $ D_S4_Skil_Type = BS_Cls004_Buf01_Type
            call BS_D_S4_Chk_AddSkl_Allies
            call BS_D_S4_Buf01_Tgt
        elif D_S4_Ttc == 4:
            $ D_S4_Skil = BS_Cls004_Buf02_Name
            $ D_S4_Skil_No = BS_Cls004_Buf02_No
            $ D_S4_Skil_Type = BS_Cls004_Buf02_Type
            call BS_D_S4_Chk_AddSkl_Allies
            call BS_D_S4_Buf02_Tgt
        elif D_S4_Ttc == 5:
            $ D_S4_Skil = BS_Cls004_Buf03_Name
            $ D_S4_Skil_No = BS_Cls004_Buf03_No
            $ D_S4_Skil_Type = BS_Cls004_Buf03_Type
            call BS_D_S4_Chk_AddSkl_Allies
            call BS_D_S4_Buf03_Tgt
#------------------------------------------------
    else:
        if D_S4_Ttc == 1:
            call BS_D_S4_Chk_HealOrg_Ttc01
        elif D_S4_Ttc == 2:
            call BS_D_S4_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 5
#===========================================================
label BS_D_S5_Chk_SklType:
#------------------------------------------------
    $ D_S5_DmgType = "Skill"
#------------------------------------------------
    if D_S5_Ttc == 3 or D_S5_Ttc == 4 or D_S5_Ttc == 5:
        if D_S5_Ttc == 3:
            $ D_S5_Skil = BS_Cls004_Buf01_Name
            $ D_S5_Skil_No = BS_Cls004_Buf01_No
            $ D_S5_Skil_Type = BS_Cls004_Buf01_Type
            call BS_D_S5_Chk_AddSkl_Allies
            call BS_D_S5_Buf01_Tgt
        elif D_S5_Ttc == 4:
            $ D_S5_Skil = BS_Cls004_Buf02_Name
            $ D_S5_Skil_No = BS_Cls004_Buf02_No
            $ D_S5_Skil_Type = BS_Cls004_Buf02_Type
            call BS_D_S5_Chk_AddSkl_Allies
            call BS_D_S5_Buf02_Tgt
        elif D_S5_Ttc == 5:
            $ D_S5_Skil = BS_Cls004_Buf03_Name
            $ D_S5_Skil_No = BS_Cls004_Buf03_No
            $ D_S5_Skil_Type = BS_Cls004_Buf03_Type
            call BS_D_S5_Chk_AddSkl_Allies
            call BS_D_S5_Buf03_Tgt
#------------------------------------------------
    else:
        if D_S5_Ttc == 1:
            call BS_D_S5_Chk_HealOrg_Ttc01
        elif D_S5_Ttc == 2:
            call BS_D_S5_Chk_HealOrg_Ttc02
#------------------------------------------------
    return

#///////////////////////  DEFFENDER SLOT 6
#===========================================================
label BS_D_S6_Chk_SklType:
#------------------------------------------------
    $ D_S6_DmgType = "Skill"
#------------------------------------------------
    if D_S6_Ttc == 3 or D_S6_Ttc == 4 or D_S6_Ttc == 5:
        if D_S6_Ttc == 3:
            $ D_S6_Skil = BS_Cls004_Buf01_Name
            $ D_S6_Skil_No = BS_Cls004_Buf01_No
            $ D_S6_Skil_Type = BS_Cls004_Buf01_Type
            call BS_D_S6_Chk_AddSkl_Allies
            call BS_D_S6_Buf01_Tgt
        elif D_S6_Ttc == 4:
            $ D_S6_Skil = BS_Cls004_Buf02_Name
            $ D_S6_Skil_No = BS_Cls004_Buf02_No
            $ D_S6_Skil_Type = BS_Cls004_Buf02_Type
            call BS_D_S6_Chk_AddSkl_Allies
            call BS_D_S6_Buf02_Tgt
        elif D_S6_Ttc == 5:
            $ D_S6_Skil = BS_Cls004_Buf03_Name
            $ D_S6_Skil_No = BS_Cls004_Buf03_No
            $ D_S6_Skil_Type = BS_Cls004_Buf03_Type
            call BS_D_S6_Chk_AddSkl_Allies
            call BS_D_S6_Buf03_Tgt
#------------------------------------------------
    else:
        if D_S6_Ttc == 1:
            call BS_D_S6_Chk_HealOrg_Ttc01
        elif D_S6_Ttc == 2:
            call BS_D_S6_Chk_HealOrg_Ttc02
#------------------------------------------------
    return
