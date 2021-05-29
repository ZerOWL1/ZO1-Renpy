
#///////////////////////  ATTACKER SLOT 1
#==========================================
label BS_A_S1_Chk_Duel:
#==========================================
    if A_S1_CanDuel == 1:
        if A_S1_Cls == 1 or A_S1_Cls == 3:
            if A_S1_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S1"
                $ DS_Deffender = "Led_D_S1"
                $ DS_Which_Side = "Attacker"
                $ DS_StrikeFirst_Side = "Attacker"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_A_S1_UntEvt
                call BS_Chk_A_S1_LedEvt
                call BS_Chk_D_S1_UntEvt
                call BS_Chk_D_S1_LedEvt
#-----------------------------------
    $ A_S1_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 2
#==========================================
label BS_A_S2_Chk_Duel:
#==========================================
    if A_S2_CanDuel == 1:
        if A_S2_Cls == 1 or A_S2_Cls == 3:
            if A_S2_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S2"
                $ DS_Deffender = "Led_D_S2"
                $ DS_Which_Side = "Attacker"
                $ DS_StrikeFirst_Side = "Attacker"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_A_S2_UntEvt
                call BS_Chk_A_S2_LedEvt
                call BS_Chk_D_S2_UntEvt
                call BS_Chk_D_S2_LedEvt
#-----------------------------------
    $ A_S2_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 3
#==========================================
label BS_A_S3_Chk_Duel:
#==========================================
    if A_S3_CanDuel == 1:
        if A_S3_Cls == 1 or A_S3_Cls == 3:
            if A_S3_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S3"
                $ DS_Deffender = "Led_D_S3"
                $ DS_Which_Side = "Attacker"
                $ DS_StrikeFirst_Side = "Attacker"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_A_S3_UntEvt
                call BS_Chk_A_S3_LedEvt
                call BS_Chk_D_S3_UntEvt
                call BS_Chk_D_S3_LedEvt
#-----------------------------------
    $ A_S3_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 4
#==========================================
label BS_A_S4_Chk_Duel:
#==========================================
    if A_S4_CanDuel == 1:
        if A_S4_Cls == 1 or A_S4_Cls == 3:
            if A_S4_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S4"
                $ DS_Deffender = "Led_D_S4"
                $ DS_Which_Side = "Attacker"
                $ DS_StrikeFirst_Side = "Attacker"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_A_S4_UntEvt
                call BS_Chk_A_S4_LedEvt
                call BS_Chk_D_S4_UntEvt
                call BS_Chk_D_S4_LedEvt
#-----------------------------------
    $ A_S4_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 5
#==========================================
label BS_A_S5_Chk_Duel:
#==========================================
    if A_S5_CanDuel == 1:
        if A_S5_Cls == 1 or A_S5_Cls == 3:
            if A_S5_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S5"
                $ DS_Deffender = "Led_D_S5"
                $ DS_Which_Side = "Attacker"
                $ DS_StrikeFirst_Side = "Attacker"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_A_S5_UntEvt
                call BS_Chk_A_S5_LedEvt
                call BS_Chk_D_S5_UntEvt
                call BS_Chk_D_S5_LedEvt
#-----------------------------------
    $ A_S5_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 6
#==========================================
label BS_A_S6_Chk_Duel:
#==========================================
    if A_S6_CanDuel == 1:
        if A_S6_Cls == 1 or A_S6_Cls == 3:
            if A_S6_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S6"
                $ DS_Deffender = "Led_D_S6"
                $ DS_Which_Side = "Attacker"
                $ DS_StrikeFirst_Side = "Attacker"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_A_S6_UntEvt
                call BS_Chk_A_S6_LedEvt
                call BS_Chk_D_S6_UntEvt
                call BS_Chk_D_S6_LedEvt
#-----------------------------------
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
#==========================================
label BS_D_S1_Chk_Duel:
#==========================================
    if D_S1_CanDuel == 1:
        if D_S1_Cls == 1 or D_S1_Cls == 3:
            if D_S1_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S1"
                $ DS_Deffender = "Led_D_S1"
                $ DS_Which_Side = "Deffender"
                $ DS_StrikeFirst_Side = "Deffender"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_D_S1_UntEvt
                call BS_Chk_D_S1_LedEvt
                call BS_Chk_A_S1_UntEvt
                call BS_Chk_A_S1_LedEvt
#-----------------------------------
    $ D_S1_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 2
#==========================================
label BS_D_S2_Chk_Duel:
#==========================================
    if D_S2_CanDuel == 1:
        if D_S2_Cls == 1 or D_S2_Cls == 3:
            if D_S2_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S2"
                $ DS_Deffender = "Led_D_S2"
                $ DS_Which_Side = "Deffender"
                $ DS_StrikeFirst_Side = "Deffender"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_D_S2_UntEvt
                call BS_Chk_D_S2_LedEvt
                call BS_Chk_A_S2_UntEvt
                call BS_Chk_A_S2_LedEvt
#-----------------------------------
    $ D_S2_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 3
#==========================================
label BS_D_S3_Chk_Duel:
#==========================================
    if D_S3_CanDuel == 1:
        if D_S3_Cls == 1 or D_S3_Cls == 3:
            if D_S3_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S3"
                $ DS_Deffender = "Led_D_S3"
                $ DS_Which_Side = "Deffender"
                $ DS_StrikeFirst_Side = "Deffender"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_D_S3_UntEvt
                call BS_Chk_D_S3_LedEvt
                call BS_Chk_A_S3_UntEvt
                call BS_Chk_A_S3_LedEvt
#-----------------------------------
    $ D_S3_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 4
#==========================================
label BS_D_S4_Chk_Duel:
#==========================================
    if D_S4_CanDuel == 1:
        if D_S4_Cls == 1 or D_S4_Cls == 3:
            if D_S4_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S4"
                $ DS_Deffender = "Led_D_S4"
                $ DS_Which_Side = "Deffender"
                $ DS_StrikeFirst_Side = "Deffender"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_D_S4_UntEvt
                call BS_Chk_D_S4_LedEvt
                call BS_Chk_A_S4_UntEvt
                call BS_Chk_A_S4_LedEvt
#-----------------------------------
    $ D_S4_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 5
#==========================================
label BS_D_S5_Chk_Duel:
#==========================================
    if D_S5_CanDuel == 1:
        if D_S5_Cls == 1 or D_S5_Cls == 3:
            if D_S5_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S5"
                $ DS_Deffender = "Led_D_S5"
                $ DS_Which_Side = "Deffender"
                $ DS_StrikeFirst_Side = "Deffender"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_D_S5_UntEvt
                call BS_Chk_D_S5_LedEvt
                call BS_Chk_A_S5_UntEvt
                call BS_Chk_A_S5_LedEvt
#-----------------------------------
    $ D_S5_CanDuel = 0
    return

#///////////////////////  ATTACKER SLOT 6
#==========================================
label BS_D_S6_Chk_Duel:
#==========================================
    if D_S6_CanDuel == 1:
        if D_S6_Cls == 1 or D_S6_Cls == 3:
            if D_S6_DmgType == "Melee":
#-----------------------------------
                $ DS_Attacker = "Led_A_S6"
                $ DS_Deffender = "Led_D_S6"
                $ DS_Which_Side = "Deffender"
                $ DS_StrikeFirst_Side = "Deffender"
#-----------------------------------
                call Update_Scr_Dueltxt_On
#-----------------------------------
                call Duel_Start
                call BS_Chk_DuelResult
                call BS_Chk_D_S6_UntEvt
                call BS_Chk_D_S6_LedEvt
                call BS_Chk_A_S6_UntEvt
                call BS_Chk_A_S6_LedEvt
#-----------------------------------
    $ D_S6_CanDuel = 0
    return
