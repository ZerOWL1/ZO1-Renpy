label BS_Load_ActionButton:

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           ACTION SETUPS
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////// Attack Clicked

    $ A_S1_AtkClicked = SetVariable ("BS_WhoAct", "A_S1"), Jump ("AB_AtkClicked")
    $ A_S2_AtkClicked = SetVariable ("BS_WhoAct", "A_S2"), Jump ("AB_AtkClicked")
    $ A_S3_AtkClicked = SetVariable ("BS_WhoAct", "A_S3"), Jump ("AB_AtkClicked")
    $ A_S4_AtkClicked = SetVariable ("BS_WhoAct", "A_S4"), Jump ("AB_AtkClicked")
    $ A_S5_AtkClicked = SetVariable ("BS_WhoAct", "A_S5"), Jump ("AB_AtkClicked")
    $ A_S6_AtkClicked = SetVariable ("BS_WhoAct", "A_S6"), Jump ("AB_AtkClicked")

    $ D_S1_AtkClicked = SetVariable ("BS_WhoAct", "D_S1"), Jump ("AB_AtkClicked")
    $ D_S2_AtkClicked = SetVariable ("BS_WhoAct", "D_S2"), Jump ("AB_AtkClicked")
    $ D_S3_AtkClicked = SetVariable ("BS_WhoAct", "D_S3"), Jump ("AB_AtkClicked")
    $ D_S4_AtkClicked = SetVariable ("BS_WhoAct", "D_S4"), Jump ("AB_AtkClicked")
    $ D_S5_AtkClicked = SetVariable ("BS_WhoAct", "D_S5"), Jump ("AB_AtkClicked")
    $ D_S6_AtkClicked = SetVariable ("BS_WhoAct", "D_S6"), Jump ("AB_AtkClicked")

#/////////////////////////////////////////////// Skill Clicked

    $ A_S1_SkillClicked = SetVariable ("BS_WhoAct", "A_S1"), Jump ("AB_SkillClicked")
    $ A_S2_SkillClicked = SetVariable ("BS_WhoAct", "A_S2"), Jump ("AB_SkillClicked")
    $ A_S3_SkillClicked = SetVariable ("BS_WhoAct", "A_S3"), Jump ("AB_SkillClicked")
    $ A_S4_SkillClicked = SetVariable ("BS_WhoAct", "A_S4"), Jump ("AB_SkillClicked")
    $ A_S5_SkillClicked = SetVariable ("BS_WhoAct", "A_S5"), Jump ("AB_SkillClicked")
    $ A_S6_SkillClicked = SetVariable ("BS_WhoAct", "A_S6"), Jump ("AB_SkillClicked")

    $ D_S1_SkillClicked = SetVariable ("BS_WhoAct", "D_S1"), Jump ("AB_SkillClicked")
    $ D_S2_SkillClicked = SetVariable ("BS_WhoAct", "D_S2"), Jump ("AB_SkillClicked")
    $ D_S3_SkillClicked = SetVariable ("BS_WhoAct", "D_S3"), Jump ("AB_SkillClicked")
    $ D_S4_SkillClicked = SetVariable ("BS_WhoAct", "D_S4"), Jump ("AB_SkillClicked")
    $ D_S5_SkillClicked = SetVariable ("BS_WhoAct", "D_S5"), Jump ("AB_SkillClicked")
    $ D_S6_SkillClicked = SetVariable ("BS_WhoAct", "D_S6"), Jump ("AB_SkillClicked")

#/////////////////////////////////////////////// End turn Clicked

    $ A_S1_EndTurnClicked = SetVariable ("A_S1_CanAct", 0), SetVariable ("BS_WhoAct", "A_S1"), Jump ("AB_EndTurnClicked")
    $ A_S2_EndTurnClicked = SetVariable ("A_S2_CanAct", 0), SetVariable ("BS_WhoAct", "A_S2"), Jump ("AB_EndTurnClicked")
    $ A_S3_EndTurnClicked = SetVariable ("A_S3_CanAct", 0), SetVariable ("BS_WhoAct", "A_S3"), Jump ("AB_EndTurnClicked")
    $ A_S4_EndTurnClicked = SetVariable ("A_S4_CanAct", 0), SetVariable ("BS_WhoAct", "A_S4"), Jump ("AB_EndTurnClicked")
    $ A_S5_EndTurnClicked = SetVariable ("A_S5_CanAct", 0), SetVariable ("BS_WhoAct", "A_S5"), Jump ("AB_EndTurnClicked")
    $ A_S6_EndTurnClicked = SetVariable ("A_S6_CanAct", 0), SetVariable ("BS_WhoAct", "A_S6"), Jump ("AB_EndTurnClicked")

    $ D_S1_EndTurnClicked = SetVariable ("D_S1_CanAct", 0), SetVariable ("BS_WhoAct", "D_S1"), Jump ("AB_EndTurnClicked")
    $ D_S2_EndTurnClicked = SetVariable ("D_S2_CanAct", 0), SetVariable ("BS_WhoAct", "D_S2"), Jump ("AB_EndTurnClicked")
    $ D_S3_EndTurnClicked = SetVariable ("D_S3_CanAct", 0), SetVariable ("BS_WhoAct", "D_S3"), Jump ("AB_EndTurnClicked")
    $ D_S4_EndTurnClicked = SetVariable ("D_S4_CanAct", 0), SetVariable ("BS_WhoAct", "D_S4"), Jump ("AB_EndTurnClicked")
    $ D_S5_EndTurnClicked = SetVariable ("D_S5_CanAct", 0), SetVariable ("BS_WhoAct", "D_S5"), Jump ("AB_EndTurnClicked")
    $ D_S6_EndTurnClicked = SetVariable ("D_S6_CanAct", 0), SetVariable ("BS_WhoAct", "D_S6"), Jump ("AB_EndTurnClicked")

#/////////////////////////////////////////////// Change Posittions Clicked

    $ ChgPOSClicked = Show ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc")

#/////////////////////////////////////////////// Change Tatics Clicked

    $ ChgTtcClicked = Show ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS")


#/////////////////////////////////////////////// Change Tatics Sub screen

    $ A_S1_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S1_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ A_S1_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S1_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ A_S1_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S1_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ A_S1_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S1_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ A_S1_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S1_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ A_S2_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S2_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ A_S2_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S2_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ A_S2_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S2_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ A_S2_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S2_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ A_S2_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S2_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ A_S3_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S3_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ A_S3_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S3_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ A_S3_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S3_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ A_S3_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S3_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ A_S3_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S3_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ A_S4_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S4_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ A_S4_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S4_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ A_S4_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S4_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ A_S4_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S4_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ A_S4_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S4_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ A_S5_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S5_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ A_S5_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S5_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ A_S5_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S5_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ A_S5_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S5_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ A_S5_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S5_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ A_S6_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S6_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ A_S6_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S6_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ A_S6_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S6_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ A_S6_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S6_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ A_S6_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("A_S6_Ttc", 5), Jump ("BS_Chk_WhoTurn")
#---------------------------------------------------------
    $ D_S1_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S1_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ D_S1_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S1_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ D_S1_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S1_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ D_S1_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S1_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ D_S1_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S1_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ D_S2_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S2_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ D_S2_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S2_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ D_S2_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S2_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ D_S2_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S2_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ D_S2_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S2_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ D_S3_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S3_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ D_S3_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S3_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ D_S3_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S3_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ D_S3_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S3_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ D_S3_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S3_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ D_S4_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S4_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ D_S4_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S4_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ D_S4_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S4_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ D_S4_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S4_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ D_S4_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S4_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ D_S5_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S5_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ D_S5_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S5_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ D_S5_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S5_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ D_S5_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S5_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ D_S5_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S5_Ttc", 5), Jump ("BS_Chk_WhoTurn")

    $ D_S6_ChgTtc01Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S6_Ttc", 1), Jump ("BS_Chk_WhoTurn")
    $ D_S6_ChgTtc02Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S6_Ttc", 2), Jump ("BS_Chk_WhoTurn")
    $ D_S6_ChgTtc03Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S6_Ttc", 3), Jump ("BS_Chk_WhoTurn")
    $ D_S6_ChgTtc04Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S6_Ttc", 4), Jump ("BS_Chk_WhoTurn")
    $ D_S6_ChgTtc05Clicked = Hide ("Screen_UI_PI_ChgTtc"), Hide ("Screen_UI_PI_ChgPOS"), SetVariable ("D_S6_Ttc", 5), Jump ("BS_Chk_WhoTurn")


#/////////////////////////////////////////////// Change Posittions Sub screen

    $ A_S1_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos01_02")
    $ A_S1_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos01_03")
    $ A_S1_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos01_04")
    $ A_S1_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos01_05")
    $ A_S1_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos01_06")

    $ A_S2_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos02_01")
    $ A_S2_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos02_03")
    $ A_S2_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos02_04")
    $ A_S2_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos02_05")
    $ A_S2_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos02_06")

    $ A_S3_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos03_01")
    $ A_S3_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos03_02")
    $ A_S3_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos03_04")
    $ A_S3_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos03_05")
    $ A_S3_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos03_06")

    $ A_S4_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos04_01")
    $ A_S4_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos04_02")
    $ A_S4_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos04_03")
    $ A_S4_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos04_05")
    $ A_S4_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos04_06")

    $ A_S5_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos05_01")
    $ A_S5_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos05_02")
    $ A_S5_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos05_03")
    $ A_S5_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos05_04")
    $ A_S5_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos05_06")

    $ A_S6_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos06_01")
    $ A_S6_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos06_02")
    $ A_S6_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos06_03")
    $ A_S6_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos06_04")
    $ A_S6_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_A_Pos06_05")
#---------------------------------------------------------
    $ D_S1_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos01_02")
    $ D_S1_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos01_03")
    $ D_S1_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos01_04")
    $ D_S1_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos01_05")
    $ D_S1_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos01_06")

    $ D_S2_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos02_01")
    $ D_S2_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos02_03")
    $ D_S2_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos02_04")
    $ D_S2_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos02_05")
    $ D_S2_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos02_06")

    $ D_S3_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos03_01")
    $ D_S3_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos03_02")
    $ D_S3_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos03_04")
    $ D_S3_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos03_05")
    $ D_S3_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos03_06")

    $ D_S4_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos04_01")
    $ D_S4_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos04_02")
    $ D_S4_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos04_03")
    $ D_S4_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos04_05")
    $ D_S4_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos04_06")

    $ D_S5_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos05_01")
    $ D_S5_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos05_02")
    $ D_S5_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos05_03")
    $ D_S5_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos05_04")
    $ D_S5_ChgPOS06Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos05_06")

    $ D_S6_ChgPOS01Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos06_01")
    $ D_S6_ChgPOS02Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos06_02")
    $ D_S6_ChgPOS03Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos06_03")
    $ D_S6_ChgPOS04Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos06_04")
    $ D_S6_ChgPOS05Clicked = Hide ("Screen_UI_PI_ChgPOS"), Hide ("Screen_UI_PI_ChgTtc"), SetVariable ("BS_WhatKindOfChgPOS", 'PI_ChgPOS'),  Jump ("BS_Chg_D_Pos06_05")

    $ renpy.pause(BS_SysSpd, hard = True)
    return