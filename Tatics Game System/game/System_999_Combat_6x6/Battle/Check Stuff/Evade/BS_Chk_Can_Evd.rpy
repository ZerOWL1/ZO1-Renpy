
#///////////////////////  ATTACKER SLOT 1
label BS_A_S1_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if A_S1_EvdChc >= BS_EvdRate:
        $ A_S1_CanEvd = 1
        $ A_S1_DmgRcvType = "Missed"
        $ A_S1_EvdRate = 0
    else:
        $ A_S1_DmgRcvType = "Damaged"
        $ A_S1_EvdRate = 1 
    return

#///////////////////////  ATTACKER SLOT 2
label BS_A_S2_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if A_S2_EvdChc >= BS_EvdRate:
        $ A_S2_CanEvd = 1
        $ A_S2_DmgRcvType = "Missed"
        $ A_S2_EvdRate = 0
    else:
        $ A_S2_DmgRcvType = "Damaged"
        $ A_S2_EvdRate = 1 
    return

#///////////////////////  ATTACKER SLOT 3
label BS_A_S3_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if A_S3_EvdChc >= BS_EvdRate:
        $ A_S3_CanEvd = 1
        $ A_S3_DmgRcvType = "Missed"
        $ A_S3_EvdRate = 0
    else:
        $ A_S3_DmgRcvType = "Damaged"
        $ A_S3_EvdRate = 1
    return

#///////////////////////  ATTACKER SLOT 4
label BS_A_S4_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if A_S4_EvdChc >= BS_EvdRate:
        $ A_S4_CanEvd = 1
        $ A_S4_DmgRcvType = "Missed"
        $ A_S4_EvdRate = 0
    else:
        $ A_S4_DmgRcvType = "Damaged"
        $ A_S4_EvdRate = 1
    return

#///////////////////////  ATTACKER SLOT 5
label BS_A_S5_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if A_S5_EvdChc >= BS_EvdRate:
        $ A_S5_CanEvd = 1
        $ A_S5_DmgRcvType = "Missed"
        $ A_S5_EvdRate = 0
    else:
        $ A_S5_DmgRcvType = "Damaged"
        $ A_S5_EvdRate = 1
    return

#///////////////////////  ATTACKER SLOT 6
label BS_A_S6_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if A_S6_EvdChc >= BS_EvdRate:
        $ A_S6_CanEvd = 1
        $ A_S6_DmgRcvType = "Missed"
        $ A_S6_EvdRate = 0
    else:
        $ A_S6_DmgRcvType = "Damaged"
        $ A_S6_EvdRate = 1
    return
        
        
        
        
        
        
        

#///////////////////////  DEFFENDER SLOT 1
label BS_D_S1_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if D_S1_EvdChc >= BS_EvdRate:
        $ D_S1_CanEvd = 1
        $ D_S1_DmgRcvType = "Missed"
        $ D_S1_EvdRate = 0
    else:
        $ D_S1_DmgRcvType = "Damaged"
        $ D_S1_EvdRate = 1 
    return

#///////////////////////  DEFFENDER SLOT 2
label BS_D_S2_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if D_S2_EvdChc >= BS_EvdRate:
        $ D_S2_CanEvd = 1
        $ D_S2_DmgRcvType = "Missed"
        $ D_S2_EvdRate = 0
    else:
        $ D_S2_DmgRcvType = "Damaged"
        $ D_S2_EvdRate = 1 
    return

#///////////////////////  DEFFENDER SLOT 3
label BS_D_S3_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if D_S3_EvdChc >= BS_EvdRate:
        $ D_S3_CanEvd = 1
        $ D_S3_DmgRcvType = "Missed"
        $ D_S3_EvdRate = 0
    else:
        $ D_S3_DmgRcvType = "Damaged"
        $ D_S3_EvdRate = 1
    return

#///////////////////////  DEFFENDER SLOT 4
label BS_D_S4_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if D_S4_EvdChc >= BS_EvdRate:
        $ D_S4_CanEvd = 1
        $ D_S4_DmgRcvType = "Missed"
        $ D_S4_EvdRate = 0
    else:
        $ D_S4_DmgRcvType = "Damaged"
        $ D_S4_EvdRate = 1
    return

#///////////////////////  DEFFENDER SLOT 5
label BS_D_S5_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if D_S5_EvdChc >= BS_EvdRate:
        $ D_S5_CanEvd = 1
        $ D_S5_DmgRcvType = "Missed"
        $ D_S5_EvdRate = 0
    else:
        $ D_S5_DmgRcvType = "Damaged"
        $ D_S5_EvdRate = 1
    return

#///////////////////////  DEFFENDER SLOT 6
label BS_D_S6_Chk_Can_Evd:
    $ BS_EvdRate = renpy.random.randint(1, 100)
    if D_S6_EvdChc >= BS_EvdRate:
        $ D_S6_CanEvd = 1
        $ D_S6_DmgRcvType = "Missed"
        $ D_S6_EvdRate = 0
    else:
        $ D_S6_DmgRcvType = "Damaged"
        $ D_S6_EvdRate = 1
    return