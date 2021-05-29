label BS_Load_Unt_Effect:

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#/                                           Class effect setups
#//////////////////////////////////////////////////////////////////////////////////////////////////////

    define Class_ColumnStartPoint = 0.5
    define Class_RowStartPoint = 0.38
    define Class_Horizontal = 0.09
    define Class_Vertical = 0.12
    define Class_VsLine = 0.05

    define Class_001_ColumnOdd = 0
    define Class_001_RowOdd = 0
    define Class_002_ColumnOdd = 0.025
    define Class_002_RowOdd = 0.025
    define Class_003_ColumnOdd = 0
    define Class_003_RowOdd = 0.03
    define Class_004_ColumnOdd = 0.035
    define Class_004_RowOdd = 0.005

    define Class_001_Zoom = 2.6
    define Class_001_anchorX = 0.5
    define Class_001_anchorY = 0.5
    define Class_001_A_Column001 = Class_ColumnStartPoint + Class_001_ColumnOdd + Class_VsLine
    define Class_001_A_Column002 = Class_001_A_Column001 + Class_Horizontal
    define Class_001_D_Column001 = Class_ColumnStartPoint - Class_001_ColumnOdd - Class_VsLine
    define Class_001_D_Column002 = Class_001_D_Column001 - Class_Horizontal
    define Class_001_Row001 = Class_RowStartPoint + Class_001_RowOdd
    define Class_001_Row002 = Class_001_Row001 + Class_Vertical
    define Class_001_Row003 = Class_001_Row002 + Class_Vertical
    define Class_001_ClsDmged_Xmove = 0.005

    define Class_002_Zoom = 2.4
    define Class_002_anchorX = 0.5
    define Class_002_anchorY = 0.5
    define Class_002_A_Column001 = Class_ColumnStartPoint + Class_002_ColumnOdd + Class_VsLine
    define Class_002_A_Column002 = Class_002_A_Column001 + Class_Horizontal
    define Class_002_D_Column001 = Class_ColumnStartPoint - Class_002_ColumnOdd - Class_VsLine
    define Class_002_D_Column002 = Class_002_D_Column001 - Class_Horizontal
    define Class_002_Row001 = Class_RowStartPoint + Class_002_RowOdd
    define Class_002_Row002 = Class_002_Row001 + Class_Vertical
    define Class_002_Row003 = Class_002_Row002 + Class_Vertical
    define Class_002_ClsDmged_Xmove = 0.005

    define Class_003_Zoom = 2.4
    define Class_003_anchorX = 0.5
    define Class_003_anchorY = 0.5
    define Class_003_A_Column001 = Class_ColumnStartPoint + Class_003_ColumnOdd + Class_VsLine
    define Class_003_A_Column002 = Class_003_A_Column001 + Class_Horizontal
    define Class_003_D_Column001 = Class_ColumnStartPoint - Class_003_ColumnOdd - Class_VsLine
    define Class_003_D_Column002 = Class_003_D_Column001 - Class_Horizontal
    define Class_003_Row001 = Class_RowStartPoint - Class_003_RowOdd
    define Class_003_Row002 = Class_003_Row001 + Class_Vertical
    define Class_003_Row003 = Class_003_Row002 + Class_Vertical
    define Class_003_ClsDmged_Xmove = 0.005

    define Class_004_Zoom = 2.5
    define Class_004_anchorX = 0.5
    define Class_004_anchorY = 0.5
    define Class_004_A_Column001 = Class_ColumnStartPoint + Class_004_ColumnOdd + Class_VsLine
    define Class_004_A_Column002 = Class_004_A_Column001 + Class_Horizontal
    define Class_004_D_Column001 = Class_ColumnStartPoint - Class_004_ColumnOdd - Class_VsLine
    define Class_004_D_Column002 = Class_004_D_Column001 - Class_Horizontal
    define Class_004_Row001 = Class_RowStartPoint  + Class_004_RowOdd
    define Class_004_Row002 = Class_004_Row001 + Class_Vertical
    define Class_004_Row003 = Class_004_Row002 + Class_Vertical
    define Class_004_ClsDmged_Xmove = 0.005

    $ renpy.pause(BS_SysSpd, hard = True)
    return