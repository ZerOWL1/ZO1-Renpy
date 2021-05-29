label BS_Load_Unt_Cls_BasSts:

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           Class 001 - Spear 
#//////////////////////////////////////////////////////////////////////////////////////////////////////

    define Cls001_BAS_HP = 100
    define Cls001_BAS_MHP = Cls001_BAS_HP
    define Cls001_BAS_Atk = 12
    define Cls001_BAS_Def = 4
    define Cls001_BAS_Spd = 3.0
    define Cls001_BAS_CrtChc = 5
    define Cls001_BAS_CrtRate = 1
    define Cls001_BAS_EvdChc = 5
    define Cls001_BAS_EvdRate = 1
    define Cls001_BAS_AtkType = 0
    define Cls001_BAS_DefType = 0

    define Cls001_PLV_HP = 5
    define Cls001_PLV_MHP = Cls001_PLV_HP
    define Cls001_PLV_Atk = 3
    define Cls001_PLV_Def = 1
    define Cls001_PLV_Spd = 0.1
    define Cls001_PLV_CrtChc = 0.5
    define Cls001_PLV_EvdChc = 0.5

    define Cls001_Ttc01_DmgRate = 100
    define Cls001_Ttc02_DmgRate = 50

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           Class 002 - Archer
#//////////////////////////////////////////////////////////////////////////////////////////////////////

    define Cls002_BAS_HP = 60
    define Cls002_BAS_MHP = Cls002_BAS_HP
    define Cls002_BAS_Atk = 18
    define Cls002_BAS_Def = 1
    define Cls002_BAS_Spd = 3.5
    define Cls002_BAS_CrtChc = 8
    define Cls002_BAS_CrtRate = 1
    define Cls002_BAS_EvdChc = 10
    define Cls002_BAS_EvdRate = 1
    define Cls002_BAS_AtkType = 0
    define Cls002_BAS_DefType = 0

    define Cls002_PLV_HP = 3
    define Cls002_PLV_MHP = Cls002_PLV_HP
    define Cls002_PLV_Atk = 4
    define Cls002_PLV_Def = 0
    define Cls002_PLV_Spd = 0.2
    define Cls002_PLV_CrtChc = 0.8
    define Cls002_PLV_EvdChc = 1.0

    define Cls002_Ttc01_DmgRate = 100
    define Cls002_Ttc02_DmgRate = 20

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           Class 003 - Horse man
#//////////////////////////////////////////////////////////////////////////////////////////////////////

    define Cls003_BAS_HP = 30
    define Cls003_BAS_MHP = Cls003_BAS_HP
    define Cls003_BAS_Atk = 25
    define Cls003_BAS_Def = 10
    define Cls003_BAS_Spd = 4.0
    define Cls003_BAS_CrtChc = 6
    define Cls003_BAS_CrtRate = 1
    define Cls003_BAS_EvdChc = 2
    define Cls003_BAS_EvdRate = 1
    define Cls003_BAS_AtkType = 0
    define Cls003_BAS_DefType = 0

    define Cls003_PLV_HP = 2
    define Cls003_PLV_MHP = Cls003_PLV_HP
    define Cls003_PLV_Atk = 5
    define Cls003_PLV_Def = 2
    define Cls003_PLV_Spd = 0.3
    define Cls003_PLV_CrtChc = 0.6
    define Cls003_PLV_EvdChc = 0.2

    define Cls003_Ttc01_DmgRate = 100
    define Cls003_Ttc02_DmgRate = 80

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           Class 004 - Healer
#//////////////////////////////////////////////////////////////////////////////////////////////////////

    define Cls004_BAS_HP = 20
    define Cls004_BAS_MHP = Cls004_BAS_HP
    define Cls004_BAS_Atk = 5
    define Cls004_BAS_Def = 1
    define Cls004_BAS_Spd = 3.2
    define Cls004_BAS_CrtChc = 3
    define Cls004_BAS_CrtRate = 1
    define Cls004_BAS_EvdChc = 7
    define Cls004_BAS_EvdRate = 1
    define Cls004_BAS_AtkType = "Heal"
    define Cls004_BAS_DefType = 0

    define Cls004_PLV_HP = 1
    define Cls004_PLV_MHP = Cls004_PLV_HP
    define Cls004_PLV_Atk = 2
    define Cls004_PLV_Def = 0
    define Cls004_PLV_Spd = 0.2
    define Cls004_PLV_CrtChc = 0.2
    define Cls004_PLV_EvdChc = 0.4

    define Cls004_Ttc01_HealRate = 100
    define Cls004_Ttc02_HealRate = 200

    $ renpy.pause(BS_SysSpd, hard = True)
    return