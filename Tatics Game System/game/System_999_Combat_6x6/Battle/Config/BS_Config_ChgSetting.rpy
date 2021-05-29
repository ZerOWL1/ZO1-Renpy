label BS_Config_ChgSetting:

    menu:
        "Change System Speed"
        "x1.0 (Very slow)":
            $ BS_SysSpd = 1.0
            $ BS_ClockSpd = 1.5
        "x0.5 (Slow)":
            $ BS_SysSpd = 0.5
            $ BS_ClockSpd = 1.25
        "x0.1 (Normal)":
            $ BS_SysSpd = 0.1
            $ BS_ClockSpd = 1.0
        "x0.05 (Fast)":
            $ BS_SysSpd = 0.05
            $ BS_ClockSpd = 0.5
        "x0.01 (Fastest)":
            $ BS_SysSpd = 0.01
            $ BS_ClockSpd = 0.1
        "Skip":
            pass

    $ Txt_AntSec_ON = Txt_AntSec_ON  * BS_ClockSpd
    $ Txt_AntSec_OFF = Txt_AntSec_OFF * BS_ClockSpd
    $ Txt_AntSec_Dmg = Txt_AntSec_Dmg * BS_ClockSpd
    $ Txt_AntSec_Ttl = Txt_AntSec_Ttl * BS_ClockSpd

    $ AntSec_Wait_To_Die = AntSec_Wait_To_Die * BS_ClockSpd
    $ SecWait_NextUnit = SecWait_NextUnit * BS_ClockSpd
    $ SecWait_LoadBG = SecWait_LoadBG * BS_ClockSpd
    $ SecWait_Engage = SecWait_Engage * BS_ClockSpd
    $ SecWait_EndDuel = SecWait_EndDuel * BS_ClockSpd
    $ SecWait_ChgPOS = SecWait_ChgPOS * BS_ClockSpd
    $ SecWait_Act = SecWait_Act * BS_ClockSpd

    $ AntSec_Cls001_MeleeNormal = AntSec_Cls001_MeleeNormal * BS_ClockSpd
    $ AntSec_Cls001_MeleeCrit = AntSec_Cls001_MeleeCrit * BS_ClockSpd
    $ AntSec_Cls001_RangeNormal = AntSec_Cls001_RangeNormal * BS_ClockSpd
    $ AntSec_Cls001_RangeCrit = AntSec_Cls001_RangeCrit * BS_ClockSpd
    $ AntSec_Cls001_MeleeReturn = AntSec_Cls001_MeleeReturn * BS_ClockSpd
    $ AntSec_Cls001_RangeReturn = AntSec_Cls001_RangeReturn * BS_ClockSpd

    $ AntSec_Cls002_MeleeNormal = AntSec_Cls002_MeleeNormal * BS_ClockSpd
    $ AntSec_Cls002_MeleeCrit = AntSec_Cls002_MeleeCrit * BS_ClockSpd
    $ AntSec_Cls002_RangeNormal = AntSec_Cls002_RangeNormal * BS_ClockSpd
    $ AntSec_Cls002_RangeCrit = AntSec_Cls002_RangeCrit * BS_ClockSpd
    $ AntSec_Cls002_MeleeReturn = AntSec_Cls002_MeleeReturn * BS_ClockSpd
    $ AntSec_Cls002_RangeReturn = AntSec_Cls002_RangeReturn * BS_ClockSpd

    $ AntSec_Cls003_MeleeNormal = AntSec_Cls003_MeleeNormal * BS_ClockSpd
    $ AntSec_Cls003_MeleeCrit = AntSec_Cls003_MeleeCrit * BS_ClockSpd
    $ AntSec_Cls003_RangeNormal = AntSec_Cls003_RangeNormal * BS_ClockSpd
    $ AntSec_Cls003_RangeCrit = AntSec_Cls003_RangeCrit * BS_ClockSpd
    $ AntSec_Cls003_MeleeReturn = AntSec_Cls003_MeleeReturn * BS_ClockSpd
    $ AntSec_Cls003_RangeReturn = AntSec_Cls003_RangeReturn * BS_ClockSpd

    $ AntSec_Cls004_SkillNormal = AntSec_Cls004_SkillNormal * BS_ClockSpd
    $ AntSec_Cls004_SkillReturn = AntSec_Cls004_SkillReturn * BS_ClockSpd

    $ renpy.pause(BS_SysSpd, hard = True)
    return