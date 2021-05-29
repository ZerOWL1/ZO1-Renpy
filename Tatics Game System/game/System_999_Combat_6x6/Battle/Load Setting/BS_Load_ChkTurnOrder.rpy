label BS_Load_ChkTurnOrder:

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           CHECK WHO GO FIRST
#//////////////////////////////////////////////////////////////////////////////////////////////////////
    
    define Turn_No_1 = 0
    define Turn_No_2 = 0
    define Turn_No_3 = 0
    define Turn_No_4 = 0
    define Turn_No_5 = 0
    define Turn_No_6 = 0
    define Turn_No_7 = 0
    define Turn_No_8 = 0
    define Turn_No_9 = 0
    define Turn_No_10 = 0
    define Turn_No_11 = 0
    define Turn_No_12 = 0
    define Turn_No_13 = 0
    define Turn_DislayNo_1 = 0
    define Turn_DislayNo_2 = 0
    define Turn_DislayNo_3 = 0
    define Turn_DislayNo_4 = 0
    define Turn_DislayNo_5 = 0
    define Turn_DislayNo_6 = 0
    define Turn_DislayNo_7 = 0
    define Turn_DislayNo_8 = 0
    define Turn_DislayNo_9 = 0
    define Turn_DislayNo_10 = 0
    define Turn_DislayNo_11 = 0
    define Turn_DislayNo_12 = 0
    define Turn_DislayNo_13 = 0
    define Total_NoOcu = 0
    define Total_UnitCanAct = 0
    define CheckSpd = 0

    define A_S1_SpdChked = 0
    define A_S2_SpdChked = 0
    define A_S3_SpdChked = 0
    define A_S4_SpdChked = 0
    define A_S5_SpdChked = 0
    define A_S6_SpdChked = 0
    define D_S1_SpdChked = 0
    define D_S2_SpdChked = 0
    define D_S3_SpdChked = 0
    define D_S4_SpdChked = 0
    define D_S5_SpdChked = 0
    define D_S6_SpdChked = 0

    $ renpy.pause(BS_SysSpd, hard = True)
    return