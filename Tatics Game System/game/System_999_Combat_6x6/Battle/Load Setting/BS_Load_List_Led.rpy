
#====================================
label BS_Load_List_Led:
#====================================

    python:
        class List_Led_Slots:
            def __init__(self,
#-----------------------------------------
            Ocu, RegNo, Name, Level, Exp, Class):
#-----------------------------------------
                self.RegNo = RegNo
                self.Ocu = Ocu
                self.Name = Name
                self.Level = Level
                self.Exp = Exp
                self.Class = Class

        BM_A_ListLed_Slots_001 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_002 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_003 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_004 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_005 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_006 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_007 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_008 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_009 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_010 = List_Led_Slots (0,0,'...',0,0,0)
        BM_A_ListLed_Slots_012 = List_Led_Slots (0,0,'...',0,0,0)


        BM_D_ListLed_Slots_001 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_002 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_003 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_004 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_005 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_006 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_007 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_008 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_009 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_010 = List_Led_Slots (0,0,'...',0,0,0)
        BM_D_ListLed_Slots_012 = List_Led_Slots (0,0,'...',0,0,0)

    $ renpy.pause(BS_SysSpd, hard = True)
    return