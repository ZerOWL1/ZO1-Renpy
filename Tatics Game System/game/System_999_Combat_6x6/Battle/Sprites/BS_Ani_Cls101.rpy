init: 

#///////////////////////  Class 101 - Bandit

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           ATTACKER
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls101_Idl:
        im.Flip("Images/Combat System/Class/Class_101/Class_101_001.png", horizontal=True, vertical=False)
    image A_Cls101_Rdy:
        im.Flip("Images/Combat System/Class/Class_101/Class_101_Crit_001.png", horizontal=True, vertical=False)
    image A_Cls101_Evd_Idl:
        im.Flip("Images/Combat System/Class/Class_101/Class_101_002.png", horizontal=True, vertical=False)
    image A_Cls101_Evd_Rtn:
        im.Flip("Images/Combat System/Class/Class_101/Class_101_Crit_001.png", horizontal=True, vertical=False)
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls101_Atk_Melee:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_101/Class_101_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_005.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_006.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_007.png", horizontal=True, vertical=False)
        10.0
        repeat
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls101_Atk_Melee_Idle:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_101/Class_101_007.png", horizontal=True, vertical=False)
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls101_Atk_Melee_Crit:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_101/Class_101_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_Crit_001.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_Crit_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_Crit_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_Crit_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_001.png", horizontal=True, vertical=False)
        10.0
        repeat
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls101_Atk_Melee_Return:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_101/Class_101_007.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_008.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_009.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_010.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_011.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_012.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_013.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_101/Class_101_014.png", horizontal=True, vertical=False)
        10.0
        repeat

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           DEFFENDER
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls101_Idl:
        "Images/Combat System/Class/Class_101/Class_101_001.png"
    image D_Cls101_Rdy:
        "Images/Combat System/Class/Class_101/Class_101_Crit_001.png"
    image D_Cls101_Evd_Idl:
        "Images/Combat System/Class/Class_101/Class_101_002.png"
    image D_Cls101_Evd_Rtn:
        "Images/Combat System/Class/Class_101/Class_101_Crit_001.png"
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls101_Atk_Melee:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_101/Class_101_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_005.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_006.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_007.png"
        10.0
        repeat
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls101_Atk_Melee_Idle:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_101/Class_101_007.png"
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls101_Atk_Melee_Crit:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_101/Class_101_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_Crit_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_Crit_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_Crit_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_Crit_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_001.png"
        10.0
        repeat
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls101_Atk_Melee_Return:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_101/Class_101_007.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_008.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_009.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_010.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_011.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_012.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_013.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_101/Class_101_014.png"
        10.0
        repeat
