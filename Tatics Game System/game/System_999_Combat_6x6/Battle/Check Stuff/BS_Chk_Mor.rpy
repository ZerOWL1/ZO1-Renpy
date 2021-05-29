
#///////////////////////  ATTACKER SLOT 1
#=====================================================
label BS_A_S1_Chk_Mor:
#=====================================================
#-----------------------------------
    $ A_S1_MorChg = A_S1_Mor + A_S1_MorIcr - A_S1_MorDcr + (
    (A_S1_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (A_S1_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if A_S1_MorChg >= 200:
        $ A_S1_MorChg = 200
    elif A_S1_MorChg > 100:
        $ A_S1_MMor = A_S1_MorChg - 100
#-----------------------------------
    call BS_Update_A_S1_AtkChange
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 2
#=====================================================
label BS_A_S2_Chk_Mor:
#=====================================================
#-----------------------------------
    $ A_S2_MorChg = A_S2_Mor + A_S2_MorIcr - A_S2_MorDcr + (
    (A_S2_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (A_S2_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if A_S2_MorChg >= 200:
        $ A_S2_MorChg = 200
    elif A_S2_MorChg > 100:
        $ A_S2_MMor = A_S2_MorChg - 100
#-----------------------------------
    call BS_Update_A_S2_AtkChange
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 3
#=====================================================
label BS_A_S3_Chk_Mor:
#=====================================================
#-----------------------------------
    $ A_S3_MorChg = A_S3_Mor + A_S3_MorIcr - A_S3_MorDcr + (
    (A_S3_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (A_S3_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if A_S3_MorChg >= 200:
        $ A_S3_MorChg = 200
    elif A_S3_MorChg > 100:
        $ A_S3_MMor = A_S3_MorChg - 100
#-----------------------------------
    call BS_Update_A_S3_AtkChange
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 4
#=====================================================
label BS_A_S4_Chk_Mor:
#=====================================================
#-----------------------------------
    $ A_S4_MorChg = A_S4_Mor + A_S4_MorIcr - A_S4_MorDcr + (
    (A_S4_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (A_S4_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if A_S4_MorChg >= 200:
        $ A_S4_MorChg = 200
    elif A_S4_MorChg > 100:
        $ A_S4_MMor = A_S4_MorChg - 100
#-----------------------------------
    call BS_Update_A_S4_AtkChange
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 5
#=====================================================
label BS_A_S5_Chk_Mor:
#=====================================================
#-----------------------------------
    $ A_S5_MorChg = A_S5_Mor + A_S5_MorIcr - A_S5_MorDcr + (
    (A_S5_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (A_S5_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if A_S5_MorChg >= 200:
        $ A_S5_MorChg = 200
    elif A_S5_MorChg > 100:
        $ A_S5_MMor = A_S5_MorChg - 100
#-----------------------------------
    call BS_Update_A_S5_AtkChange
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 6
#=====================================================
label BS_A_S6_Chk_Mor:
#=====================================================
#-----------------------------------
    $ A_S6_MorChg = A_S6_Mor + A_S6_MorIcr - A_S6_MorDcr + (
    (A_S6_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (A_S6_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if A_S6_MorChg >= 200:
        $ A_S6_MorChg = 200
    elif A_S6_MorChg > 100:
        $ A_S6_MMor = A_S6_MorChg - 100
#-----------------------------------
    call BS_Update_A_S6_AtkChange
#-----------------------------------
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#=====================================================
label BS_D_S1_Chk_Mor:
#=====================================================
#-----------------------------------
    $ D_S1_MorChg = D_S1_Mor + D_S1_MorIcr - D_S1_MorDcr + (
    (D_S1_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (D_S1_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if D_S1_MorChg >= 200:
        $ D_S1_MorChg = 200
    elif D_S1_MorChg > 100:
        $ D_S1_MMor = D_S1_MorChg - 100
#-----------------------------------
    call BS_Update_D_S1_AtkChange
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 2
#=====================================================
label BS_D_S2_Chk_Mor:
#=====================================================
#-----------------------------------
    $ D_S2_MorChg = D_S2_Mor + D_S2_MorIcr - D_S2_MorDcr + (
    (D_S2_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (D_S2_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if D_S2_MorChg >= 200:
        $ D_S2_MorChg = 200
    elif D_S2_MorChg > 100:
        $ D_S2_MMor = D_S2_MorChg - 100
#-----------------------------------
    call BS_Update_D_S2_AtkChange
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 3
#=====================================================
label BS_D_S3_Chk_Mor:
#=====================================================
#-----------------------------------
    $ D_S3_MorChg = D_S3_Mor + D_S3_MorIcr - D_S3_MorDcr + (
    (D_S3_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (D_S3_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if D_S3_MorChg >= 200:
        $ D_S3_MorChg = 200
    elif D_S3_MorChg > 100:
        $ D_S3_MMor = D_S3_MorChg - 100
#-----------------------------------
    call BS_Update_D_S3_AtkChange
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 4
#=====================================================
label BS_D_S4_Chk_Mor:
#=====================================================
#-----------------------------------
    $ D_S4_MorChg = D_S4_Mor + D_S4_MorIcr - D_S4_MorDcr + (
    (D_S4_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (D_S4_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if D_S4_MorChg >= 200:
        $ D_S4_MorChg = 200
    elif D_S4_MorChg > 100:
        $ D_S4_MMor = D_S4_MorChg - 100
#-----------------------------------
    call BS_Update_D_S4_AtkChange
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 5
#=====================================================
label BS_D_S5_Chk_Mor:
#=====================================================
#-----------------------------------
    $ D_S5_MorChg = D_S5_Mor + D_S5_MorIcr - D_S5_MorDcr + (
    (D_S5_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (D_S5_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if D_S5_MorChg >= 200:
        $ D_S5_MorChg = 200
    elif D_S5_MorChg > 100:
        $ D_S5_MMor = D_S5_MorChg - 100
#-----------------------------------
    call BS_Update_D_S5_AtkChange
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 6
#=====================================================
label BS_D_S6_Chk_Mor:
#=====================================================
#-----------------------------------
    $ D_S6_MorChg = D_S6_Mor + D_S6_MorIcr - D_S6_MorDcr + (
    (D_S6_Kill * BS_KillRate)/ BS_MorChgRate) - (
    (D_S6_Killed * BS_KilledRate)/ BS_MorChgRate)
#-----------------------------------
    if D_S6_MorChg >= 200:
        $ D_S6_MorChg = 200
    elif D_S6_MorChg > 100:
        $ D_S6_MMor = D_S6_MorChg - 100
#-----------------------------------
    call BS_Update_D_S6_AtkChange
#-----------------------------------
    return
