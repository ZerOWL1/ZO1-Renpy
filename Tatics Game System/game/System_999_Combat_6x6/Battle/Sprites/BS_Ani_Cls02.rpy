init: 

#///////////////////////  Class 002 - Acher

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           ATTACKER
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls02_Idl:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_002/Class_002_001.png", horizontal=True, vertical=False)
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls02_Rdy:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_002/Class_002_016.png", horizontal=True, vertical=False)
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls02_Evd_Idl:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Evd_001.png", horizontal=True, vertical=False)
        0.2* BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Evd_002.png", horizontal=True, vertical=False)
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls02_Evd_Rtn:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Evd_002.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Evd_001.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_001.png", horizontal=True, vertical=False)
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls02_Atk_Range:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_002/Class_002_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_002.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_005.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_006.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_007.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_008.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_009.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_010.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_011.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_012.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_013.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_014.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_015.png", horizontal=True, vertical=False)
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls02_Atk_Range_Idle:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_002/Class_002_015.png", horizontal=True, vertical=False)

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls02_Atk_Range_Crit:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_002/Class_002_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Crit_001.png", horizontal=True, vertical=False)
        0.3 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Crit_002.png", horizontal=True, vertical=False)
        0.3 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Crit_003.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Crit_004.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Crit_005.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Crit_006.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Crit_007.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_Crit_008.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_011.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_012.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_013.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_014.png", horizontal=True, vertical=False)
        0.1 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_015.png", horizontal=True, vertical=False)
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image A_Cls02_Atk_Range_Return:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_002/Class_002_016.png", horizontal=True, vertical=False)
        0.3 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_002/Class_002_001.png", horizontal=True, vertical=False)
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
    image D_Cls02_Idl:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_002/Class_002_001.png"
    image D_Cls02_Rdy:
        "Images/Combat System/Class/Class_002/Class_002_016.png"
    image D_Cls02_Evd_Idl:
        "Images/Combat System/Class/Class_002/Class_002_Evd_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Evd_002.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls02_Evd_Rtn:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_002/Class_002_Evd_002.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Evd_001.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_001.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls02_Atk_Range:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_002/Class_002_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_002.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_005.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_006.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_007.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_008.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_009.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_010.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_011.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_012.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_013.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_014.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_015.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls02_Atk_Range_Idle:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_002/Class_002_015.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls02_Atk_Range_Crit:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_002/Class_002_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Crit_001.png"
        0.3 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Crit_002.png"
        0.3 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Crit_003.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Crit_004.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Crit_005.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Crit_006.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Crit_007.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_Crit_008.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_011.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_012.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_013.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_014.png"
        0.1 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_015.png"
        10.0
        repeat
        
#--------------------------------------------------------------------------------------------------------------------
    image D_Cls02_Atk_Range_Return:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_002/Class_002_016.png"
        0.3 * BS_ClockSpd
        "Images/Combat System/Class/Class_002/Class_002_001.png"
        10.0
        repeat
