label BS_Load_ActionButton_BM_List:

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           ACTION SETUPS
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////// Pick Slot

    $ BM_Army_A_S1_Picked = SetVariable ("BM_Army_Whoswap", "A_S1"), Jump ("AB_BM_A_List_Swap")
    $ BM_Army_A_S2_Picked = SetVariable ("BM_Army_Whoswap", "A_S2"), Jump ("AB_BM_A_List_Swap")
    $ BM_Army_A_S3_Picked = SetVariable ("BM_Army_Whoswap", "A_S3"), Jump ("AB_BM_A_List_Swap")
    $ BM_Army_A_S4_Picked = SetVariable ("BM_Army_Whoswap", "A_S4"), Jump ("AB_BM_A_List_Swap")
    $ BM_Army_A_S5_Picked = SetVariable ("BM_Army_Whoswap", "A_S5"), Jump ("AB_BM_A_List_Swap")
    $ BM_Army_A_S6_Picked = SetVariable ("BM_Army_Whoswap", "A_S6"), Jump ("AB_BM_A_List_Swap")

    $ BM_Army_D_S1_Picked = SetVariable ("BM_Army_Whoswap", "D_S1"), Jump ("AB_BM_D_List_Swap")
    $ BM_Army_D_S2_Picked = SetVariable ("BM_Army_Whoswap", "D_S2"), Jump ("AB_BM_D_List_Swap")
    $ BM_Army_D_S3_Picked = SetVariable ("BM_Army_Whoswap", "D_S3"), Jump ("AB_BM_D_List_Swap")
    $ BM_Army_D_S4_Picked = SetVariable ("BM_Army_Whoswap", "D_S4"), Jump ("AB_BM_D_List_Swap")
    $ BM_Army_D_S5_Picked = SetVariable ("BM_Army_Whoswap", "D_S5"), Jump ("AB_BM_D_List_Swap")
    $ BM_Army_D_S6_Picked = SetVariable ("BM_Army_Whoswap", "D_S6"), Jump ("AB_BM_D_List_Swap")

    $ BM_ListArmy_A_Slot001_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot001"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot002_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot002"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot003_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot003"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot004_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot004"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot005_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot005"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot006_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot006"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot007_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot007"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot008_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot008"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot009_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot009"), Jump ("AB_BM_A_List_Swap")
    $ BM_ListArmy_A_Slot010_Picked = SetVariable ("BM_ListArmy_Whoswap", "A_Slot010"), Jump ("AB_BM_A_List_Swap")

    $ BM_ListArmy_D_Slot001_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot001"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot002_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot002"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot003_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot003"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot004_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot004"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot005_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot005"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot006_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot006"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot007_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot007"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot008_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot008"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot009_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot009"), Jump ("AB_BM_D_List_Swap")
    $ BM_ListArmy_D_Slot010_Picked = SetVariable ("BM_ListArmy_Whoswap", "D_Slot010"), Jump ("AB_BM_D_List_Swap")

    $ renpy.pause(BS_SysSpd, hard = True)
    return