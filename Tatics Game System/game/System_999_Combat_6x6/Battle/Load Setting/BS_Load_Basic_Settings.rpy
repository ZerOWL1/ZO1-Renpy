label BS_Load_Basic_Setting:
#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           BASIC BATTLE SETUPS
#//////////////////////////////////////////////////////////////////////////////////////////////////////

    define BS_Ctl_PlayerSide = 0
    define BS_WhoControl = 0
    define BS_WhoAct = 0
    define BS_WhatKindOfChgPOS = 0
    define BM_WhoPickedToChgPOS = 0
    define BM_WhoToChgPOS = 0
    define BM_ListArmy_Whoswap = 0
    define BM_Army_Whoswap = 0

    define BS_BGRdm = 0
    define BS_ATBSpd = 1
    define BS_SysSpd = 0.01
    define BS_ClockSpd = 1.0
    define BS_AniPhase = 0
    define BS_Progress = 2
    define BS_PickedSlot = 0
    define BS_BattleEnd = 0
    define BS_PlayerInteracted = False

    define BS_TtcRdm = 0
    define BS_NonEvdRate = 1
    define BS_EvdRate = 0
    define BS_Duelrate = 0
    define BS_CritHit = 0
    define BS_NonCritRate = 1
    define BS_CritRate = 2
    define BS_KillRate = 2
    define BS_KilledRate = 1
    define BS_MorChgRate = 100
    
    define BS_Timer = 0
    define BS_Turns = 0
    define BS_TurnsMax = 20
    define BS_Chk_Timer = 100

    define BS_MaxMor = 100
    define BS_MaxFgt = 100
    define BS_All_MorIcr = 0
    define BS_All_MorDcr = 0
    define BS_DuelWin_MorIcr = 20
    define BS_DuelLos_MorDcr = 20

    define BS_Who_Turn = 0
    define BS_Which_Side = 0
    define BS_A_CrtDam = 0
    define BS_D_CrtDam = 0

    define DS_Which_Side = 0
    define DS_StrikeFirst_Side = 0
    define DS_Attacker = 0
    define DS_Deffender = 0

    define SecWait_NextUnit = 1.0
    define SecWait_LoadBG = 1.0
    define SecWait_Engage = 1.0
    define SecWait_EndDuel = 1.0
    define SecWait_ChgPOS = 1.0
    define SecWait_Act = 1.0

    $ renpy.pause(BS_SysSpd, hard = True)
    return