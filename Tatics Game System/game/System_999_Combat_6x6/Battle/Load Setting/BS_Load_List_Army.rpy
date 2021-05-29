
#====================================
label BS_Load_List_Army:
#====================================

    python:
        class List_Army_Slots:
            def __init__(self,
#-----------------------------------------
            RegNo, Ocu, Name, Level, Exp, Class):
#-----------------------------------------
                self.RegNo = RegNo
                self.Ocu = Ocu
                self.Name = Name
                self.Level = Level
                self.Exp = Exp
                self.Class = Class

        BM_A_ListArmy_Slots_001 = List_Army_Slots (0,1,'Slots_01',1,0,0)
        BM_A_ListArmy_Slots_002 = List_Army_Slots (0,1,'Slots_02',1,0,0)
        BM_A_ListArmy_Slots_003 = List_Army_Slots (0,1,'Slots_03',1,0,0)
        BM_A_ListArmy_Slots_004 = List_Army_Slots (0,1,'Slots_04',1,0,0)
        BM_A_ListArmy_Slots_005 = List_Army_Slots (0,1,'Slots_05',1,0,0)
        BM_A_ListArmy_Slots_006 = List_Army_Slots (0,1,'Slots_06',1,0,0)
        BM_A_ListArmy_Slots_007 = List_Army_Slots (0,1,'Slots_07',1,0,0)
        BM_A_ListArmy_Slots_008 = List_Army_Slots (0,1,'Slots_08',1,0,0)
        BM_A_ListArmy_Slots_009 = List_Army_Slots (0,1,'Slots_09',1,0,0)
        BM_A_ListArmy_Slots_010 = List_Army_Slots (0,1,'Slots_10',1,0,0)
        BM_A_ListArmy_Slots_011 = List_Army_Slots (0,1,'Slots_11',1,0,0)
        BM_A_ListArmy_Slots_012 = List_Army_Slots (0,1,'Slots_12',1,0,0)


        BM_D_ListArmy_Slots_001 = List_Army_Slots (0,1,'Slots_01',1,0,0)
        BM_D_ListArmy_Slots_002 = List_Army_Slots (0,1,'Slots_02',1,0,0)
        BM_D_ListArmy_Slots_003 = List_Army_Slots (0,1,'Slots_03',1,0,0)
        BM_D_ListArmy_Slots_004 = List_Army_Slots (0,1,'Slots_04',1,0,0)
        BM_D_ListArmy_Slots_005 = List_Army_Slots (0,1,'Slots_05',1,0,0)
        BM_D_ListArmy_Slots_006 = List_Army_Slots (0,1,'Slots_06',1,0,0)
        BM_D_ListArmy_Slots_007 = List_Army_Slots (0,1,'Slots_07',1,0,0)
        BM_D_ListArmy_Slots_008 = List_Army_Slots (0,1,'Slots_08',1,0,0)
        BM_D_ListArmy_Slots_009 = List_Army_Slots (0,1,'Slots_09',1,0,0)
        BM_D_ListArmy_Slots_010 = List_Army_Slots (0,1,'Slots_10',1,0,0)
        BM_D_ListArmy_Slots_011 = List_Army_Slots (0,1,'Slots_11',1,0,0)
        BM_D_ListArmy_Slots_012 = List_Army_Slots (0,1,'Slots_12',1,0,0)

    $ renpy.pause(BS_SysSpd, hard = True)
    return