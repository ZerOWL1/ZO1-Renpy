
#///////////////////////  ATTACKER SLOT 1
label BS_A_S1_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if A_S1_DuelChc >= BS_Duelrate and (
    A_S1_HP > 0 and D_S1_HP > 0) and (
    Led_A_S1_HP > 0 and Led_D_S1_HP > 0) and (
    D_S1_CanEvd == 0) and (
    A_S1_DuelEvd == "OFF"):
        $ A_S1_CanDuel = 1
    else:
        $ A_S1_CanDuel = 0
        
    return

#///////////////////////  ATTACKER SLOT 2
label BS_A_S2_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if A_S2_DuelChc >= BS_Duelrate and (
    A_S2_HP > 0 and D_S2_HP > 0) and (
    Led_A_S2_HP > 0 and Led_D_S2_HP > 0) and (
    D_S2_CanEvd == 0) and (
    A_S2_DuelEvd == "OFF"):
        $ A_S2_CanDuel = 1
    else:
        $ A_S2_CanDuel = 0
        
    return

#///////////////////////  ATTACKER SLOT 3
label BS_A_S3_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if A_S3_DuelChc >= BS_Duelrate and (
    A_S3_HP > 0 and D_S3_HP > 0) and (
    Led_A_S3_HP > 0 and Led_D_S3_HP > 0) and (
    D_S3_CanEvd == 0) and (
    A_S3_DuelEvd == "OFF"):
        $ A_S3_CanDuel = 1
    else:
        $ A_S3_CanDuel = 0
        
    return

#///////////////////////  ATTACKER SLOT 4
label BS_A_S4_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if A_S4_DuelChc >= BS_Duelrate and (
    A_S4_HP > 0 and D_S4_HP > 0) and (
    Led_A_S4_HP > 0 and Led_D_S4_HP > 0) and (
    D_S4_CanEvd == 0) and (
    A_S4_DuelEvd == "OFF"):
        $ A_S4_CanDuel = 1
    else:
        $ A_S4_CanDuel = 0
        
    return

#///////////////////////  ATTACKER SLOT 5
label BS_A_S5_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if A_S5_DuelChc >= BS_Duelrate and (
    A_S5_HP > 0 and D_S5_HP > 0) and (
    Led_A_S5_HP > 0 and Led_D_S5_HP > 0) and (
    D_S5_CanEvd == 0) and (
    A_S5_DuelEvd == "OFF"):
        $ A_S5_CanDuel = 1
    else:
        $ A_S5_CanDuel = 0
        
    return

#///////////////////////  ATTACKER SLOT 6
label BS_A_S6_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if A_S6_DuelChc >= BS_Duelrate and (
    A_S6_HP > 0 and D_S6_HP > 0) and (
    Led_A_S6_HP > 0 and Led_D_S6_HP > 0) and (
    D_S6_CanEvd == 0) and (
    A_S6_DuelEvd == "OFF"):
        $ A_S6_CanDuel = 1
    else:
        $ A_S6_CanDuel = 0
        
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
label BS_D_S1_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if D_S1_DuelChc >= BS_Duelrate and (
    D_S1_HP > 0 and A_S1_HP > 0) and (
    Led_D_S1_HP > 0 and Led_A_S1_HP > 0) and (
    A_S1_CanEvd == 0) and (
    D_S1_DuelEvd == "OFF"):
        $ D_S1_CanDuel = 1
    else:
        $ D_S1_CanDuel = 0
        
    return

#///////////////////////  DEFFENDER SLOT 2
label BS_D_S2_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if D_S2_DuelChc >= BS_Duelrate and (
    D_S2_HP > 0 and A_S2_HP > 0) and (
    Led_D_S2_HP > 0 and Led_A_S2_HP > 0) and (
    A_S2_CanEvd == 0) and (
    D_S2_DuelEvd == "OFF"):
        $ D_S2_CanDuel = 1
    else:
        $ D_S2_CanDuel = 0
        
    return

#///////////////////////  DEFFENDER SLOT 3
label BS_D_S3_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if D_S3_DuelChc >= BS_Duelrate and (
    D_S3_HP > 0 and A_S3_HP > 0) and (
    Led_D_S3_HP > 0 and Led_A_S3_HP > 0) and (
    A_S3_CanEvd == 0) and (
    D_S3_DuelEvd == "OFF"):
        $ D_S3_CanDuel = 1
    else:
        $ D_S3_CanDuel = 0
        
    return

#///////////////////////  DEFFENDER SLOT 4
label BS_D_S4_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if D_S4_DuelChc >= BS_Duelrate and (
    D_S4_HP > 0 and A_S4_HP > 0) and (
    Led_D_S4_HP > 0 and Led_A_S4_HP > 0) and (
    A_S4_CanEvd == 0) and (
    D_S4_DuelEvd == "OFF"):
        $ D_S4_CanDuel = 1
    else:
        $ D_S4_CanDuel = 0
        
    return

#///////////////////////  DEFFENDER SLOT 5
label BS_D_S5_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if D_S5_DuelChc >= BS_Duelrate and (
    D_S5_HP > 0 and A_S5_HP > 0) and (
    Led_D_S5_HP > 0 and Led_A_S5_HP > 0) and (
    A_S5_CanEvd == 0) and (
    D_S5_DuelEvd == "OFF"):
        $ D_S5_CanDuel = 1
    else:
        $ D_S5_CanDuel = 0
        
    return

#///////////////////////  DEFFENDER SLOT 6
label BS_D_S6_Chk_Can_Duel:

    $ BS_Duelrate = renpy.random.randint(1, 100)
    
    if D_S6_DuelChc >= BS_Duelrate and (
    D_S6_HP > 0 and A_S6_HP > 0) and (
    Led_D_S6_HP > 0 and Led_A_S6_HP > 0) and (
    A_S6_CanEvd == 0) and (
    D_S6_DuelEvd == "OFF"):
        $ D_S6_CanDuel = 1
    else:
        $ D_S6_CanDuel = 0
        
    return
