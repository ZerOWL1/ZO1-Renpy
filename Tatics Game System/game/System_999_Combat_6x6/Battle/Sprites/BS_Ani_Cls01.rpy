init: 

#///////////////////////  Class 001 - Spear

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           ATTACKER
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Idl:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_001.png", horizontal=True, vertical=False)
#--------------------------------------------------------------------------------------------------------------------

    image A_Cls01_Rdy:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_012.png", horizontal=True, vertical=False)
#--------------------------------------------------------------------------------------------------------------------

    image A_Cls01_Evd_Idl:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Evd_001.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Evd_002.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Evd_Rtn:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Evd_002.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Evd_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_001.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Atk_Melee:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_005.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Atk_Melee_Idle:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_005.png", horizontal=True, vertical=False)

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Atk_Melee_Crit:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Crit_001.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Crit_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Crit_003.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_005.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Atk_Melee_Return:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_006.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_007.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_008.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_009.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_010.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_011.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_012.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_001.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Atk_Range:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_001.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_005.png", horizontal=True, vertical=False)
        10.0
        repeat
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Atk_Range_Idle:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_005.png", horizontal=True, vertical=False)

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Atk_Range_Crit:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Crit_Ranged_001.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Crit_Ranged_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_001.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_005.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls01_Atk_Range_Return:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_005.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_Ranged_001.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_001/Class_001_001.png", horizontal=True, vertical=False)
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
    image D_Cls01_Idl:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_001.png"
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Rdy:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_012.png"
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Evd_Idl:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_Evd_001.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Evd_002.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Evd_Rtn:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_Evd_002.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Evd_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_001.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Atk_Melee:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_005.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Atk_Melee_Idle:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_005.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Atk_Melee_Crit:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Crit_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Crit_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Crit_003.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_005.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Atk_Melee_Return:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_006.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_007.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_008.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_009.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_010.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_011.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_012.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_001.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Atk_Range:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_005.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Atk_Range_Idle:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_Ranged_005.png"
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Atk_Range_Crit:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Crit_Ranged_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Crit_Ranged_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_005.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls01_Atk_Range_Return:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_001/Class_001_Ranged_005.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_Ranged_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_001/Class_001_001.png"
        10.0
        repeat
