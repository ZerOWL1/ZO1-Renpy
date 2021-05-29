init: 

#///////////////////////  Class 004 - Healer

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           ATTACKER
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls04_Idl:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_001.png", horizontal=True, vertical=False)

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls04_Rdy:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_002.png", horizontal=True, vertical=False)

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls04_Evd_Idl:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Evd_001.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Evd_002.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls04_Evd_Rtn:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Evd_002.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Evd_001.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_001.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls04_Skill:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_001.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_002.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_003.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_004.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_005.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_006.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_007.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_008.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_009.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_010.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_011.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_012.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_013.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_014.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_015.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_016.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_017.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_018.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_019.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_020.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_021.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_022.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_023.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_024.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_025.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_026.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_027.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_028.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_029.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_030.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_031.png", horizontal=True, vertical=False)
        0.05 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_032.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls04_Heal_Idle:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_032.png", horizontal=True, vertical=False)
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image A_Cls04_Heal_Return:
#--------------------------------------------------------------------------------------------------------------------
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_032.png", horizontal=True, vertical=False)
        0.5 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_033.png", horizontal=True, vertical=False)
        0.2 * BS_ClockSpd
        im.Flip("Images/Combat System/Class/Class_004/Class_004_Heal_001.png", horizontal=True, vertical=False)
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
    image D_Cls04_Idl:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_004/Class_004_Heal_001.png"

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls04_Rdy:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_004/Class_004_Heal_002.png"

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls04_Evd_Idl:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_004/Class_004_Evd_001.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Evd_002.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls04_Evd_Rtn:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_004/Class_004_Evd_002.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Evd_001.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_001.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls04_Skill:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_004/Class_004_Heal_001.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_002.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_003.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_004.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_005.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_006.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_007.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_008.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_009.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_010.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_011.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_012.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_013.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_014.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_015.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_016.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_017.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_018.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_019.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_020.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_021.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_022.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_023.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_024.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_025.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_026.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_027.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_028.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_029.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_030.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_031.png"
        0.05 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_032.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls04_Heal_Idle:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_004/Class_004_Heal_032.png"
        10.0
        repeat

#--------------------------------------------------------------------------------------------------------------------
    image D_Cls04_Heal_Return:
#--------------------------------------------------------------------------------------------------------------------
        "Images/Combat System/Class/Class_004/Class_004_Heal_032.png"
        0.5 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_033.png"
        0.2 * BS_ClockSpd
        "Images/Combat System/Class/Class_004/Class_004_Heal_001.png"
        10.0
        repeat

