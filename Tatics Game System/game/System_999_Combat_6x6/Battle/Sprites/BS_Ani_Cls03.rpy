init: 

#///////////////////////  Class 003 - horse cavalry

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           ATTACKER
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Idl:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_001.png", horizontal=True, vertical=False)
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Rdy:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_001.png", horizontal=True, vertical=False)
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Evd_Idl:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Evd_001.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Evd_002.png", horizontal=True, vertical=False)
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Evd_Rtn:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Evd_002.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Evd_001.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_001.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Atk_Melee:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_002.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_003.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_004.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_005.png", horizontal=True, vertical=False)
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Atk_Melee_Idle:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_005.png", horizontal=True, vertical=False)

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Atk_Melee_Crit:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_001.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_002.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_005.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_006.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_007.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_003.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_004.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_005.png", horizontal=True, vertical=False)
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Atk_Melee_Return: 
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_006.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_007.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_008.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_009.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_010.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_011.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_012.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_013.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_014.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_015.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_016.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_017.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_018.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_001.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Atk_Range:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_001.png", horizontal=True, vertical=False)
        0.4 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_004.png", horizontal=True, vertical=False)
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Atk_Range_Idle:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_004.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Atk_Range_Crit:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_001.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_004.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_005.png", horizontal=True, vertical=False)
        0.3 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_006.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_001.png", horizontal=True, vertical=False)
        0.3 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_004.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls03_Atk_Range_Return:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_004.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_Ranged_005.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_003/Class_003_001.png", horizontal=True, vertical=False)
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
    image D_Cls03_Idl:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_001.png"

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Rdy:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_Crit_001.png"

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Evd_Idl:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_Evd_001.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Evd_002.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Evd_Rtn:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_Evd_002.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Evd_001.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_001.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Atk_Melee:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_002.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_003.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_004.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_005.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Atk_Melee_Idle:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_005.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Atk_Melee_Crit:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_001.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_002.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_005.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_006.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_007.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_003.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_004.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_005.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Atk_Melee_Return:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_006.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_007.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_008.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_009.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_010.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_011.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_012.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_013.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_014.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_015.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_016.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_017.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_018.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_001.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Atk_Range:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_001.png"
        0.4 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_004.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Atk_Range_Idle:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_Ranged_004.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Atk_Range_Crit:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_004.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_005.png"
        0.3 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Crit_Ranged_006.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_001.png"
        0.3 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_004.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls03_Atk_Range_Return:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_003/Class_003_Ranged_004.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_Ranged_005.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_003/Class_003_001.png"
        10.0
        repeat