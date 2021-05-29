
#///////////////////////  ATTACKER SLOT 1
label BS_A_S1_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if A_S1_CrtChc >= Critical_hit:
        $ A_S1_CanCrt = 1
        $ A_S1_CrtRate = BS_CritRate
        $ BS_A_CrtDam = 1
        $ A_S1_CanAct = "Critial Hit"
    else:
        $ A_S1_CrtRate = 1
        $ A_S1_CanAct = "Normal Hit"

    return

#///////////////////////  ATTACKER SLOT 2
label BS_A_S2_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if A_S2_CrtChc >= Critical_hit:
        $ A_S2_CanCrt = 1
        $ A_S2_CrtRate = BS_CritRate
        $ BS_A_CrtDam = 1
        $ A_S2_CanAct = "Critial Hit"
    else:
        $ A_S2_CrtRate = 1
        $ A_S2_CanAct = "Normal Hit"

    return

#///////////////////////  ATTACKER SLOT 3
label BS_A_S3_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if A_S3_CrtChc >= Critical_hit:
        $ A_S3_CanCrt = 1
        $ A_S3_CrtRate = BS_CritRate
        $ BS_A_CrtDam = 1
        $ A_S3_CanAct = "Critial Hit"
    else:
        $ A_S3_CrtRate = 1
        $ A_S3_CanAct = "Normal Hit"

    return

#///////////////////////  ATTACKER SLOT 4
label BS_A_S4_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if A_S4_CrtChc >= Critical_hit:
        $ A_S4_CanCrt = 1
        $ A_S4_CrtRate = BS_CritRate
        $ BS_A_CrtDam = 1
        $ A_S4_CanAct = "Critial Hit"
    else:
        $ A_S4_CrtRate = 1
        $ A_S4_CanAct = "Normal Hit"

    return

#///////////////////////  ATTACKER SLOT 5
label BS_A_S5_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if A_S5_CrtChc >= Critical_hit:
        $ A_S5_CanCrt = 1
        $ A_S5_CrtRate = BS_CritRate
        $ BS_A_CrtDam = 1
        $ A_S5_CanAct = "Critial Hit"
    else:
        $ A_S5_CrtRate = 1
        $ A_S5_CanAct = "Normal Hit"

    return

#///////////////////////  ATTACKER SLOT 6
label BS_A_S6_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if A_S6_CrtChc >= Critical_hit:
        $ A_S6_CanCrt = 1
        $ A_S6_CrtRate = BS_CritRate
        $ BS_A_CrtDam = 1
        $ A_S6_CanAct = "Critial Hit"
    else:
        $ A_S6_CrtRate = 1
        $ A_S6_CanAct = "Normal Hit"

    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
label BS_D_S1_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if D_S1_CrtChc >= Critical_hit:
        $ D_S1_CanCrt = 1
        $ D_S1_CrtRate = BS_CritRate
        $ BS_D_CrtDam = 1
        $ D_S1_CanAct = "Critial Hit"
    else:
        $ D_S1_CrtRate = 1
        $ D_S1_CanAct = "Normal Hit"

    return

#///////////////////////  DEFFENDER SLOT 2
label BS_D_S2_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if D_S2_CrtChc >= Critical_hit:
        $ D_S2_CanCrt = 1
        $ D_S2_CrtRate = BS_CritRate
        $ BS_D_CrtDam = 1
        $ D_S2_CanAct = "Critial Hit"
    else:
        $ D_S2_CrtRate = 1
        $ D_S2_CanAct = "Normal Hit"

    return

#///////////////////////  DEFFENDER SLOT 3
label BS_D_S3_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if D_S3_CrtChc >= Critical_hit:
        $ D_S3_CanCrt = 1
        $ D_S3_CrtRate = BS_CritRate
        $ BS_D_CrtDam = 1
        $ D_S3_CanAct = "Critial Hit"
    else:
        $ D_S3_CrtRate = 1
        $ D_S3_CanAct = "Normal Hit"

    return

#///////////////////////  DEFFENDER SLOT 4
label BS_D_S4_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if D_S4_CrtChc >= Critical_hit:
        $ D_S4_CanCrt = 1
        $ D_S4_CrtRate = BS_CritRate
        $ BS_D_CrtDam = 1
        $ D_S4_CanAct = "Critial Hit"
    else:
        $ D_S4_CrtRate = 1
        $ D_S4_CanAct = "Normal Hit"

    return

#///////////////////////  DEFFENDER SLOT 5
label BS_D_S5_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if D_S5_CrtChc >= Critical_hit:
        $ D_S5_CanCrt = 1
        $ D_S5_CrtRate = BS_CritRate
        $ BS_D_CrtDam = 1
        $ D_S5_CanAct = "Critial Hit"
    else:
        $ D_S5_CrtRate = 1
        $ D_S5_CanAct = "Normal Hit"

    return

#///////////////////////  DEFFENDER SLOT 6
label BS_D_S6_Chk_Can_Crit:

    call Call_Scr_Txt_Cls_Crit

    $ Critical_hit = renpy.random.randint(1, 100)
    if D_S6_CrtChc >= Critical_hit:
        $ D_S6_CanCrt = 1
        $ D_S6_CrtRate = BS_CritRate
        $ BS_D_CrtDam = 1
        $ D_S6_CanAct = "Critial Hit"
    else:
        $ D_S6_CrtRate = 1
        $ D_S6_CanAct = "Normal Hit"

    return