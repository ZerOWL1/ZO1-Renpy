label BS_Load_Scr_POS:

#///////////////////////////////////////////// Screen Slots Stats

    define Scr_001_BoxSizeX = 0.085    # Khoảng cách Chiều ngang của các box
    define Scr_001_BoxSizeY = 0.5      # Khoảng cách Chiều dọc của các box
    define Scr_001_SpaceX = 0.06          # Khoảng cách ngang Giứa các Box
    define Scr_001_anchorX = 0.5
    define Scr_001_anchorY = 0.5

    define Scr_001_R_Column002 = 1.0
    define Scr_001_R_Column001 = Scr_001_R_Column002 - Scr_001_BoxSizeX - Scr_001_SpaceX
    define Scr_001_L_Column002 = 0.0
    define Scr_001_L_Column001 = Scr_001_L_Column002 + Scr_001_BoxSizeX + Scr_001_SpaceX
    define Scr_001_Row001 = 0.0
    define Scr_001_Row002 = Scr_001_Row001 + Scr_001_BoxSizeY
    define Scr_001_Row003 = Scr_001_Row002 + Scr_001_BoxSizeY

#///////////////////////////////////////////// Screen HP - ATB - Mor - Exp

    define Scr_002_StartPointX = 0.5
    define Scr_002_StartPointY = 50
    define Scr_002_anchorX = 0.5
    define Scr_002_anchorY = 0

    define Scr_002_SpaceX = 0.08        # Khoảng cách ngang box giữa 2 bên 
    define Scr_002_SpaceY = 50          # Khoảng cách dọc giữa các box
    define Scr_002_Horizontal = 0.08    # Khoảng cách ngang giữa các box
    define Scr_002_ATB_Vertical = 5 # Chiều cao của Thanh ATB
    define Scr_002_Mor_Vertical = 5     # Chiều cao của Thanh Morale
    define Scr_002_HP_Vertical = 24     # Chiều cao của Thanh HP
    define Scr_002_Exp_Vertical = 10     # Chiều cao của Thanh Exp
    define Scr_002_HPTxt_Vertical = 2   # Khoảng cách của Số Hp
    define Scr_002_ExpTxt_Vertical = 20   # Khoảng cách của Số Exp
    define Scr_002_LvTxt_Vertical = 16 # Khoảng cách của Số Lv
    define Scr_002_Icon_Vertical = 14       # Khoảng cách dọc của Icon với box
    define Scr_002_Icon_Header = 0.02    # Khoảng cách ngang của Icon với điểm xuất phát của box
    define Scr_002_Icon_Horizontal = 0.015 # Khoảng cách giữa các Icon với nhau
    define Scr_002_Icon_Zoom = 0.3 

    define Scr_002_A_Column001 = Scr_002_StartPointX + Scr_002_SpaceX
    define Scr_002_A_Column002 = Scr_002_A_Column001 + Scr_002_Horizontal
    define Scr_002_D_Column001 = Scr_002_StartPointX - Scr_002_SpaceX
    define Scr_002_D_Column002 = Scr_002_D_Column001 - Scr_002_Horizontal

    define Scr_002_A_Icon001_Column001 = Scr_002_A_Column001 - Scr_002_Icon_Header
    define Scr_002_A_Icon002_Column001 = Scr_002_A_Icon001_Column001 + Scr_002_Icon_Horizontal
    define Scr_002_A_Icon003_Column001 = Scr_002_A_Icon002_Column001 + Scr_002_Icon_Horizontal
    define Scr_002_A_Icon001_Column002 = Scr_002_A_Column002 - Scr_002_Icon_Header
    define Scr_002_A_Icon002_Column002 = Scr_002_A_Icon001_Column002 + Scr_002_Icon_Horizontal
    define Scr_002_A_Icon003_Column002 = Scr_002_A_Icon002_Column002 + Scr_002_Icon_Horizontal
    define Scr_002_D_Icon001_Column001 = Scr_002_D_Column001 - Scr_002_Icon_Header
    define Scr_002_D_Icon002_Column001 = Scr_002_D_Icon001_Column001 + Scr_002_Icon_Horizontal
    define Scr_002_D_Icon003_Column001 = Scr_002_D_Icon002_Column001 + Scr_002_Icon_Horizontal
    define Scr_002_D_Icon001_Column002 = Scr_002_D_Column002 - Scr_002_Icon_Header
    define Scr_002_D_Icon002_Column002 = Scr_002_D_Icon001_Column002 + Scr_002_Icon_Horizontal
    define Scr_002_D_Icon003_Column002 = Scr_002_D_Icon002_Column002 + Scr_002_Icon_Horizontal

    define Scr_002_ATB_Row001 = Scr_002_StartPointY
    define Scr_002_Mor_Row001 = Scr_002_ATB_Row001 + Scr_002_ATB_Vertical
    define Scr_002_HP_Row001 = Scr_002_Mor_Row001 + Scr_002_Mor_Vertical
    define Scr_002_Exp_Row001 = Scr_002_HP_Row001 + Scr_002_HP_Vertical
    define Scr_002_Icon_Row001 = Scr_002_HP_Row001 + Scr_002_HP_Vertical + Scr_002_Icon_Vertical

    define Scr_002_ATB_Row002 = Scr_002_HP_Row001 + Scr_002_HP_Vertical + Scr_002_SpaceY
    define Scr_002_Mor_Row002 = Scr_002_ATB_Row002 + Scr_002_ATB_Vertical
    define Scr_002_HP_Row002 = Scr_002_Mor_Row002 + Scr_002_Mor_Vertical
    define Scr_002_Exp_Row002 = Scr_002_HP_Row002 + Scr_002_HP_Vertical
    define Scr_002_Icon_Row002 = Scr_002_HP_Row002 + Scr_002_HP_Vertical + Scr_002_Icon_Vertical

    define Scr_002_ATB_Row003 = Scr_002_HP_Row002 + Scr_002_HP_Vertical + Scr_002_SpaceY
    define Scr_002_Mor_Row003 = Scr_002_ATB_Row003 + Scr_002_ATB_Vertical
    define Scr_002_HP_Row003 = Scr_002_Mor_Row003 + Scr_002_Mor_Vertical
    define Scr_002_Exp_Row003 = Scr_002_HP_Row003 + Scr_002_HP_Vertical
    define Scr_002_Icon_Row003 = Scr_002_HP_Row003 + Scr_002_HP_Vertical + Scr_002_Icon_Vertical

#///////////////////////////////////////////// Screen Leader Stats

    define Scr_003_Horizontal = 0.18 # Size of Slot box
    define Scr_003_Vertical = 0.45
    define Scr_003_SpaceX = Scr_001_BoxSizeX
    define Scr_003_anchorX = 0.5
    define Scr_003_anchorY = 0.5

    define Scr_003_R_Column002 = Scr_001_R_Column002 - Scr_001_BoxSizeX
    define Scr_003_R_Column001 = Scr_001_R_Column001 - Scr_001_BoxSizeX
    define Scr_003_L_Column002 = Scr_001_L_Column002 + Scr_001_BoxSizeX
    define Scr_003_L_Column001 = Scr_001_L_Column001 + Scr_001_BoxSizeX
    define Scr_003_Row001 = Scr_001_Row001
    define Scr_003_Row002 = Scr_001_Row002
    define Scr_003_Row003 = Scr_001_Row003

#///////////////////////////////////////////// Screen Change tatics

    define Scr_004_StartPointX = 0.5
    define Scr_004_StartPointY = 0.95
    define Scr_004_anchorX = 0.5
    define Scr_004_anchorY = 0.5
    define Scr_004_SpaceX = 0.07        # Khoảng cách ngang giữa 2 bên
    define Scr_004_SpaceY = 0.1        # Khoảng cách ngang giữa Main và Sub Screen
    define Scr_004_Horizontal = 0.11     # Khoảng cách ngang giữa cac
    define Scr_004_Vertical = 0.12
    define Scr_004_IconsSpace = 0.04
    define Scr_004_AtkIconsZoom = 0.3
    define Scr_004_AtkIconsSize = 0.03
    define Scr_004_ChgTtcIconsZoom = 0.18
    define Scr_004_ChgTtcIconsSize = 0.03
    define Scr_004_ChgTtcIconsSpaces = 0.03
    define Scr_004_ChgTtcIcons_All_Zoom = 0.15
    define Scr_004_ChgTtcIcons_All_Size = 0.03
    define Scr_004_ChgTtcIcons_All_Spaces = 0.03
    define Scr_004_ChgPOSIconsZoom = 0.18
    define Scr_004_ChgPOSIconsSize = 0.03
    define Scr_004_ChgPOSIconsSpaces = 0.03
    define Scr_004_ChgPOS_01_06_IconsZoom = 0.1
    define Scr_004_ChgPOS_01_06_IconsSize = 0.03
    define Scr_004_ChgPOS_01_06_IconsSpaces = 0.03
    define Scr_004_EndTurnIconsZoom = 0.18
    define Scr_004_EndTurnIconsSize = 0.03
    define Scr_004_EndTurnIconsSpaces = 0.03
    
    define Scr_004_Horizontal = 0.08    # Khoảng cách ngang giữa các box

    define Scr_004_R_AtkIcons = Scr_004_StartPointX + Scr_004_SpaceX
    define Scr_004_L_AtkIcons = Scr_004_StartPointX - Scr_004_SpaceX
    define Scr_004_R_ChgTtcicon = Scr_004_R_AtkIcons + Scr_004_AtkIconsSize + Scr_004_IconsSpace
    define Scr_004_L_ChgTtcicon = Scr_004_L_AtkIcons - Scr_004_AtkIconsSize - Scr_004_IconsSpace
    define Scr_004_R_ChgPOSicon = Scr_004_R_ChgTtcicon + Scr_004_IconsSpace
    define Scr_004_L_ChgPOSicon = Scr_004_L_ChgTtcicon - Scr_004_IconsSpace
    define Scr_004_R_ChgPOSicon_Column01 = Scr_004_R_ChgPOSicon
    define Scr_004_R_ChgPOSicon_Column02 = Scr_004_R_ChgPOSicon_Column01 + Scr_004_IconsSpace
    define Scr_004_L_ChgPOSicon_Column01 = Scr_004_L_ChgPOSicon
    define Scr_004_L_ChgPOSicon_Column02 = Scr_004_L_ChgPOSicon_Column01 - Scr_004_IconsSpace
    define Scr_004_R_EndTurnicon = Scr_004_R_ChgPOSicon + Scr_004_IconsSpace
    define Scr_004_L_EndTurnicon = Scr_004_L_ChgPOSicon - Scr_004_IconsSpace
#---------------------------------------------------------
    define Scr_004_R_ChgTtc01icon = Scr_004_R_ChgTtcicon - (Scr_004_ChgTtcIconsSpaces * 2)
    define Scr_004_R_ChgTtc02icon = Scr_004_R_ChgTtcicon - Scr_004_ChgTtcIconsSpaces
    define Scr_004_R_ChgTtc03icon = Scr_004_R_ChgTtcicon
    define Scr_004_R_ChgTtc04icon = Scr_004_R_ChgTtcicon + Scr_004_ChgTtcIconsSpaces
    define Scr_004_R_ChgTtc05icon = Scr_004_R_ChgTtcicon + (Scr_004_ChgTtcIconsSpaces * 2)
    define Scr_004_L_ChgTtc01icon = Scr_004_L_ChgTtcicon + (Scr_004_ChgTtcIconsSpaces * 2)
    define Scr_004_L_ChgTtc02icon = Scr_004_L_ChgTtcicon + Scr_004_ChgTtcIconsSpaces
    define Scr_004_L_ChgTtc03icon = Scr_004_L_ChgTtcicon
    define Scr_004_L_ChgTtc04icon = Scr_004_L_ChgTtcicon - Scr_004_ChgTtcIconsSpaces
    define Scr_004_L_ChgTtc05icon = Scr_004_L_ChgTtcicon - (Scr_004_ChgTtcIconsSpaces * 2)
#---------------------------------------------------------
    define Scr_004_Row001 = Scr_004_StartPointY - Scr_004_SpaceX - Scr_004_IconsSpace
    define Scr_004_Row002 = Scr_004_Row001 - Scr_004_SpaceY
    define Scr_004_SubRow003 = Scr_004_Row002 - Scr_004_IconsSpace
    define Scr_004_SubRow002 = Scr_004_SubRow003 - Scr_004_IconsSpace
    define Scr_004_SubRow001 = Scr_004_SubRow002 - Scr_004_IconsSpace

    $ renpy.pause(BS_SysSpd, hard = True)
    return