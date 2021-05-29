
#///////////////////////  ATTACKER SLOT 1
#====================================
label AI_Bhv_A_S1_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (A_S1_Cls == 1 or A_S1_Cls == 3) and (
    A_S2_Cls == 1 or A_S2_Cls == 3) and (
    A_S3_Cls == 1 or A_S3_Cls == 3):
        pass
    else:
        if A_S1_Cls == 2 or A_S1_Cls == 4:
            if A_S4_Cls == 1 or A_S4_Cls == 3:
                call AI_Oth_A_S1_ChgFmt
                call BS_Chg_A_Pos01_04
            elif A_S5_Cls == 1 or A_S5_Cls == 3:
                call AI_Oth_A_S1_ChgFmt
                call BS_Chg_A_Pos01_05
            elif A_S6_Cls == 1 or A_S6_Cls == 3:
                call AI_Oth_A_S1_ChgFmt
                call BS_Chg_A_Pos01_06

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return

#///////////////////////  ATTACKER SLOT 2
#====================================
label AI_Bhv_A_S2_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (A_S1_Cls == 1 or A_S1_Cls == 3) and (
    A_S2_Cls == 1 or A_S2_Cls == 3) and (
    A_S3_Cls == 1 or A_S3_Cls == 3):
        pass
    else:
        if A_S2_Cls == 2 or A_S2_Cls == 4:
            if A_S5_Cls == 1 or A_S5_Cls == 3:
                call AI_Oth_A_S2_ChgFmt
                call BS_Chg_A_Pos02_05
            elif A_S4_Cls == 1 or A_S4_Cls == 3:
                call AI_Oth_A_S2_ChgFmt
                call BS_Chg_A_Pos02_04
            elif A_S6_Cls == 1 or A_S6_Cls == 3:
                call AI_Oth_A_S2_ChgFmt
                call BS_Chg_A_Pos02_06

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return

#///////////////////////  ATTACKER SLOT 3
#====================================
label AI_Bhv_A_S3_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (A_S1_Cls == 1 or A_S1_Cls == 3) and (
    A_S2_Cls == 1 or A_S2_Cls == 3) and (
    A_S3_Cls == 1 or A_S3_Cls == 3):
        pass
    else:
        if A_S3_Cls == 2 or A_S3_Cls == 4:
            if A_S6_Cls == 1 or A_S6_Cls == 3:
                call AI_Oth_A_S3_ChgFmt
                call BS_Chg_A_Pos03_06
            elif A_S5_Cls == 1 or A_S5_Cls == 3:
                call AI_Oth_A_S3_ChgFmt
                call BS_Chg_A_Pos03_05
            elif A_S4_Cls == 1 or A_S4_Cls == 3:
                call AI_Oth_A_S3_ChgFmt
                call BS_Chg_A_Pos03_04

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return

#///////////////////////  ATTACKER SLOT 4
#====================================
label AI_Bhv_A_S4_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (A_S1_Cls == 1 or A_S1_Cls == 3) and (
    A_S2_Cls == 1 or A_S2_Cls == 3) and (
    A_S3_Cls == 1 or A_S3_Cls == 3):
        pass
    else:
        if A_S4_Cls == 1 or A_S4_Cls == 3:
            if A_S1_Cls == 2 or A_S1_Cls == 4 or A_S1_Cls == 0:
                call AI_Oth_A_S4_ChgFmt
                call BS_Chg_A_Pos04_01
            elif A_S2_Cls == 2 or A_S2_Cls == 4 or A_S2_Cls == 0:
                call AI_Oth_A_S4_ChgFmt
                call BS_Chg_A_Pos04_02
            elif A_S3_Cls == 2 or A_S3_Cls == 4 or A_S3_Cls == 0:
                call AI_Oth_A_S4_ChgFmt
                call BS_Chg_A_Pos04_03
        elif A_S4_Cls == 2:
            if A_S5_Cls == 4:
                call AI_Oth_A_S4_ChgFmt
                call BS_Chg_A_Pos04_05

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return

#///////////////////////  ATTACKER SLOT 5
#====================================
label AI_Bhv_A_S5_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (A_S1_Cls == 1 or A_S1_Cls == 3) and (
    A_S2_Cls == 1 or A_S2_Cls == 3) and (
    A_S3_Cls == 1 or A_S3_Cls == 3):
        pass
    else:
        if A_S5_Cls == 1 or A_S5_Cls == 3:
            if A_S2_Cls == 2 or A_S2_Cls == 4 or A_S2_Cls == 0:
                call AI_Oth_A_S5_ChgFmt
                call BS_Chg_A_Pos05_02
            elif A_S1_Cls == 2 or A_S1_Cls == 4 or A_S1_Cls == 0:
                call AI_Oth_A_S5_ChgFmt
                call BS_Chg_A_Pos05_01
            elif A_S3_Cls == 2 or A_S3_Cls == 4 or A_S3_Cls == 0:
                call AI_Oth_A_S5_ChgFmt
                call BS_Chg_A_Pos05_03

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return


#///////////////////////  ATTACKER SLOT 6
#====================================
label AI_Bhv_A_S6_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (A_S1_Cls == 1 or A_S1_Cls == 3) and (
    A_S2_Cls == 1 or A_S2_Cls == 3) and (
    A_S3_Cls == 1 or A_S3_Cls == 3):
        pass
    else:
        if A_S6_Cls == 1 or A_S6_Cls == 3:
            if A_S3_Cls == 2 or A_S3_Cls == 4 or A_S3_Cls == 0:
                call AI_Oth_A_S6_ChgFmt
                call BS_Chg_A_Pos06_03
            elif A_S2_Cls == 2 or A_S2_Cls == 4 or A_S2_Cls == 0:
                call AI_Oth_A_S6_ChgFmt
                call BS_Chg_A_Pos06_02
            elif A_S1_Cls == 2 or A_S1_Cls == 4 or A_S1_Cls == 0:
                call AI_Oth_A_S6_ChgFmt
                call BS_Chg_A_Pos06_01
        elif A_S6_Cls == 2:
            if A_S5_Cls == 4:
                call AI_Oth_A_S6_ChgFmt
                call BS_Chg_A_Pos06_05

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return


    
    
    

    







#///////////////////////  DEFFENDER SLOT 1
#====================================
label AI_Bhv_D_S1_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (D_S1_Cls == 1 or D_S1_Cls == 3) and (
    D_S2_Cls == 1 or D_S2_Cls == 3) and (
    D_S3_Cls == 1 or D_S3_Cls == 3):
        pass
    else:
        if D_S1_Cls == 2 or D_S1_Cls == 4:
            if D_S4_Cls == 1 or D_S4_Cls == 3:
                call AI_Oth_D_S1_ChgFmt
                call BS_Chg_D_Pos01_04
            elif D_S5_Cls == 1 or D_S5_Cls == 3:
                call AI_Oth_D_S1_ChgFmt
                call BS_Chg_D_Pos01_05
            elif D_S6_Cls == 1 or D_S6_Cls == 3:
                call AI_Oth_D_S1_ChgFmt
                call BS_Chg_D_Pos01_06

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return

#///////////////////////  DEFFENDER SLOT 2
#====================================
label AI_Bhv_D_S2_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (D_S1_Cls == 1 or D_S1_Cls == 3) and (
    D_S2_Cls == 1 or D_S2_Cls == 3) and (
    D_S3_Cls == 1 or D_S3_Cls == 3):
        pass
    else:
        if D_S2_Cls == 2 or D_S2_Cls == 4:
            if D_S5_Cls == 1 or D_S5_Cls == 3:
                call AI_Oth_D_S2_ChgFmt
                call BS_Chg_D_Pos02_05
            elif D_S4_Cls == 1 or D_S4_Cls == 3:
                call AI_Oth_D_S2_ChgFmt
                call BS_Chg_D_Pos02_04
            elif D_S6_Cls == 1 or D_S6_Cls == 3:
                call AI_Oth_D_S2_ChgFmt
                call BS_Chg_D_Pos02_06

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return

#///////////////////////  DEFFENDER SLOT 3
#====================================
label AI_Bhv_D_S3_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (D_S1_Cls == 1 or D_S1_Cls == 3) and (
    D_S2_Cls == 1 or D_S2_Cls == 3) and (
    D_S3_Cls == 1 or D_S3_Cls == 3):
        pass
    else:
        if D_S3_Cls == 2 or D_S3_Cls == 4:
            if D_S6_Cls == 1 or D_S6_Cls == 3:
                call AI_Oth_D_S3_ChgFmt
                call BS_Chg_D_Pos03_06
            elif D_S5_Cls == 1 or D_S5_Cls == 3:
                call AI_Oth_D_S3_ChgFmt
                call BS_Chg_D_Pos03_05
            elif D_S4_Cls == 1 or D_S4_Cls == 3:
                call AI_Oth_D_S3_ChgFmt
                call BS_Chg_D_Pos03_04

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return

#///////////////////////  DEFFENDER SLOT 4
#====================================
label AI_Bhv_D_S4_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (D_S1_Cls == 1 or D_S1_Cls == 3) and (
    D_S2_Cls == 1 or D_S2_Cls == 3) and (
    D_S3_Cls == 1 or D_S3_Cls == 3):
        pass
    else:
        if D_S4_Cls == 1 or D_S4_Cls == 3:
            if D_S1_Cls == 2 or D_S1_Cls == 4 or D_S1_Cls == 0:
                call AI_Oth_D_S4_ChgFmt
                call BS_Chg_D_Pos04_01
            elif D_S2_Cls == 2 or D_S2_Cls == 4 or D_S2_Cls == 0:
                call AI_Oth_D_S4_ChgFmt
                call BS_Chg_D_Pos04_02
            elif D_S3_Cls == 2 or D_S3_Cls == 4 or D_S3_Cls == 0:
                call AI_Oth_D_S4_ChgFmt
                call BS_Chg_D_Pos04_03
        elif D_S4_Cls == 2:
            if D_S5_Cls == 4:
                call AI_Oth_D_S6_ChgFmt
                call BS_Chg_D_Pos04_05

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return

#///////////////////////  DEFFENDER SLOT 5
#====================================
label AI_Bhv_D_S5_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (D_S1_Cls == 1 or D_S1_Cls == 3) and (
    D_S2_Cls == 1 or D_S2_Cls == 3) and (
    D_S3_Cls == 1 or D_S3_Cls == 3):
        pass
    else:
        if D_S5_Cls == 1 or D_S5_Cls == 3:
            if D_S2_Cls == 2 or D_S2_Cls == 4 or D_S2_Cls == 0:
                call AI_Oth_D_S5_ChgFmt
                call BS_Chg_D_Pos05_02
            elif D_S1_Cls == 2 or D_S1_Cls == 4 or D_S1_Cls == 0:
                call AI_Oth_D_S5_ChgFmt
                call BS_Chg_D_Pos05_01
            elif D_S3_Cls == 2 or D_S3_Cls == 4 or D_S3_Cls == 0:
                call AI_Oth_D_S5_ChgFmt
                call BS_Chg_D_Pos05_03

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return


#///////////////////////  DEFFENDER SLOT 6
#====================================
label AI_Bhv_D_S6_Chg_Pos_Fmt:
#====================================

    $ BS_WhatKindOfChgPOS == "AI_ChgPOS"

    $ renpy.pause(SecWait_ChgPOS, hard = True)

    if (D_S1_Cls == 1 or D_S1_Cls == 3) and (
    D_S2_Cls == 1 or D_S2_Cls == 3) and (
    D_S3_Cls == 1 or D_S3_Cls == 3):
        pass
    else:
        if D_S6_Cls == 1 or D_S6_Cls == 3:
            if D_S3_Cls == 2 or D_S3_Cls == 4 or D_S3_Cls == 0:
                call AI_Oth_D_S6_ChgFmt
                call BS_Chg_D_Pos06_03
            elif D_S2_Cls == 2 or D_S2_Cls == 4 or D_S2_Cls == 0:
                call AI_Oth_D_S6_ChgFmt
                call BS_Chg_D_Pos06_02
            elif D_S1_Cls == 2 or D_S1_Cls == 4 or D_S1_Cls == 0:
                call AI_Oth_D_S6_ChgFmt
                call BS_Chg_D_Pos06_01
        elif D_S6_Cls == 2:
            if D_S5_Cls == 4:
                call AI_Oth_D_S6_ChgFmt
                call BS_Chg_D_Pos06_05

    $ renpy.pause(SecWait_ChgPOS, hard = True)
    return