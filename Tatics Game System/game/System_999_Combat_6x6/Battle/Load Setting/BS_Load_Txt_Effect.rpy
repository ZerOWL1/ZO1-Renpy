label BS_Load_Txt_Effect:

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           Txt effect setups
#//////////////////////////////////////////////////////////////////////////////////////////////////////

    define Txt_ColumnStartPoint = 0.5
    define Txt_RowStartPoint = 0.38
    define Txt_Horizontal = 0.09
    define Txt_Vertical = 0.14
    define Txt_VsLine = 0.08

    define Txt_anchorX = 0.5
    define Txt_anchorY = 0.5
    define Txt_A_Column001 = Txt_ColumnStartPoint + Txt_VsLine
    define Txt_A_Column002 = Txt_A_Column001 + Txt_Horizontal
    define Txt_D_Column001 = Txt_ColumnStartPoint - Txt_VsLine
    define Txt_D_Column002 = Txt_D_Column001 - Txt_Horizontal
    define Txt_Row001 = Txt_RowStartPoint
    define Txt_Row002 = Txt_Row001 + Txt_Vertical
    define Txt_Row003 = Txt_Row002 + Txt_Vertical

    define Txt_MoveUp_01 = 0.05
    define Txt_MoveUp_02 = 0.07
    define Txt_Zoom = 0.0
    define Txt_Zoom_CritDmg = 2.0
    define Icon_Zoom_Tgt = 0.4
    define Icon_Zoom_Atk = 0.0
    define Icon_Zoom_Heal = 0.25
    define Icon_Zoom_Atker = 0.3

    define Txt_AntSec_ON = 0.8  
    define Txt_AntSec_OFF = 0.2 
    define Txt_AntSec_Dmg = 0.5 
    define Txt_AntSec_Ttl = Txt_AntSec_ON + Txt_AntSec_OFF

    $ renpy.pause(BS_SysSpd, hard = True)
    return