label BS_Load_ActionButton_BM:

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           ACTION SETUPS
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////// Pick Slot

    $ BS_ChooseYes = Hide ("Scr_PI_PickPos"), Hide ("Scr_PI_PosPicked"), SetVariable ("BS_Progress", 2), SetVariable ("CC_Progress", 0), Jump ("BM_Start")
    $ BS_ChooseNo = Jump ("BS_Player_ResetChoice")

    $ BS_Pick_A_S1_Slot = SetVariable ("BS_PickedSlot", "A_S1"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_A_S2_Slot = SetVariable ("BS_PickedSlot", "A_S2"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_A_S3_Slot = SetVariable ("BS_PickedSlot", "A_S3"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_A_S4_Slot = SetVariable ("BS_PickedSlot", "A_S4"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_A_S5_Slot = SetVariable ("BS_PickedSlot", "A_S5"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_A_S6_Slot = SetVariable ("BS_PickedSlot", "A_S6"), Jump ("AB_BM_PickSlots")

    $ BS_Pick_D_S1_Slot = SetVariable ("BS_PickedSlot", "D_S1"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_D_S2_Slot = SetVariable ("BS_PickedSlot", "D_S2"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_D_S3_Slot = SetVariable ("BS_PickedSlot", "D_S3"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_D_S4_Slot = SetVariable ("BS_PickedSlot", "D_S4"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_D_S5_Slot = SetVariable ("BS_PickedSlot", "D_S5"), Jump ("AB_BM_PickSlots")
    $ BS_Pick_D_S6_Slot = SetVariable ("BS_PickedSlot", "D_S6"), Jump ("AB_BM_PickSlots")

#/////////////////////////////////////////////// Change POS Clicked

    $ BS_ChooseDone = Hide ("Scr_PI_PosPicked"), Hide ("Scr_PI_ChgPos"), Hide ("Scr_PI_ChgPos_All"), SetVariable ("BS_Progress", 99), Jump ("BM_Start")
    $ BS_BM_ChgPOSCancel = SetVariable ("BS_Progress", 2), Hide ("Scr_PI_ChgPos_All"), Jump ("BM_Start")

    $ BM_A_S1_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S1"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_A_S2_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S2"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_A_S3_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S3"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_A_S4_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S4"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_A_S5_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S5"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_A_S6_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S6"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")

    $ BM_D_S1_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S1"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_D_S2_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S2"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_D_S3_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S3"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_D_S4_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S4"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_D_S5_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S5"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")
    $ BM_D_S6_ChgPOSClicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S6"), Hide ("Scr_PI_ChgPos"), Show ("Scr_PI_ChgPos_All")

    $ BM_A_S1_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos01_02")
    $ BM_A_S1_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos01_03")
    $ BM_A_S1_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos01_04")
    $ BM_A_S1_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos01_05")
    $ BM_A_S1_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos01_06")

    $ BM_A_S2_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos02_01")
    $ BM_A_S2_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos02_03")
    $ BM_A_S2_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos02_04")
    $ BM_A_S2_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos02_05")
    $ BM_A_S2_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos02_06")

    $ BM_A_S3_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos03_01")
    $ BM_A_S3_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos03_02")
    $ BM_A_S3_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos03_04")
    $ BM_A_S3_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos03_05")
    $ BM_A_S3_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos03_06")

    $ BM_A_S4_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos04_01")
    $ BM_A_S4_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos04_02")
    $ BM_A_S4_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos04_03")
    $ BM_A_S4_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos04_05")
    $ BM_A_S4_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos04_06")

    $ BM_A_S5_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos05_01")
    $ BM_A_S5_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos05_02")
    $ BM_A_S5_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos05_03")
    $ BM_A_S5_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos05_04")
    $ BM_A_S5_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos05_06")

    $ BM_A_S6_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos06_01")
    $ BM_A_S6_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos06_02")
    $ BM_A_S6_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos06_03")
    $ BM_A_S6_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos06_04")
    $ BM_A_S6_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "A_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_A_Pos06_05")

    $ BM_D_S1_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos01_02")
    $ BM_D_S1_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos01_03")
    $ BM_D_S1_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos01_04")
    $ BM_D_S1_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos01_05")
    $ BM_D_S1_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S1"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos01_06")

    $ BM_D_S2_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos02_01")
    $ BM_D_S2_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos02_03")
    $ BM_D_S2_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos02_04")
    $ BM_D_S2_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos02_05")
    $ BM_D_S2_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S2"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos02_06")

    $ BM_D_S3_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos03_01")
    $ BM_D_S3_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos03_02")
    $ BM_D_S3_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos03_04")
    $ BM_D_S3_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos03_05")
    $ BM_D_S3_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S3"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos03_06")

    $ BM_D_S4_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos04_01")
    $ BM_D_S4_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos04_02")
    $ BM_D_S4_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos04_03")
    $ BM_D_S4_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos04_05")
    $ BM_D_S4_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S4"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos04_06")

    $ BM_D_S5_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos05_01")
    $ BM_D_S5_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos05_02")
    $ BM_D_S5_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos05_03")
    $ BM_D_S5_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos05_04")
    $ BM_D_S5_ChgPOS06Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S5"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos05_06")

    $ BM_D_S6_ChgPOS01Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos06_01")
    $ BM_D_S6_ChgPOS02Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos06_02")
    $ BM_D_S6_ChgPOS03Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos06_03")
    $ BM_D_S6_ChgPOS04Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos06_04")
    $ BM_D_S6_ChgPOS05Clicked = SetVariable ("BM_WhoPickedToChgPOS", "D_S6"), SetVariable (
    "BS_WhatKindOfChgPOS", "BM_PI_ChgPOS"), Hide (
    "Scr_PI_ChgPos_All"), Show ("Scr_PI_ChgPos"), Jump ("BS_Chg_D_Pos06_05")

    $ renpy.pause(BS_SysSpd, hard = True)
    return