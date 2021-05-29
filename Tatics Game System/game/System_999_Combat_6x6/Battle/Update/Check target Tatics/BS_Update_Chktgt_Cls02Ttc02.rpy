﻿
#==========================================
label BS_Update_A_S1_ChkTgt_Cls02_Ttc02:
#==========================================
    if D_S1_HP > 0:
        $ A_S1_Tgt_01 = 1
    if D_S2_HP > 0:
        $ A_S1_Tgt_02 = 0
    if D_S3_HP > 0:
        $ A_S1_Tgt_03 = 0
    if D_S4_HP > 0:
        $ A_S1_Tgt_04 = 0
    if D_S5_HP > 0:
        $ A_S1_Tgt_05 = 0
    if D_S6_HP > 0:
        $ A_S1_Tgt_06 = 0
    return

#==========================================
label BS_Update_A_S2_ChkTgt_Cls02_Ttc02:
#==========================================
    if D_S1_HP > 0:
        $ A_S2_Tgt_01 = 0
    if D_S2_HP > 0:
        $ A_S2_Tgt_02 = 1
    if D_S3_HP > 0:
        $ A_S2_Tgt_03 = 0
    if D_S4_HP > 0:
        $ A_S2_Tgt_04 = 0
    if D_S5_HP > 0:
        $ A_S2_Tgt_05 = 0
    if D_S6_HP > 0:
        $ A_S2_Tgt_06 = 0
    return

#==========================================
label BS_Update_A_S3_ChkTgt_Cls02_Ttc02:
#==========================================
    if D_S1_HP > 0:
        $ A_S3_Tgt_01 = 0
    if D_S2_HP > 0:
        $ A_S3_Tgt_02 = 0
    if D_S3_HP > 0:
        $ A_S3_Tgt_03 = 1
    if D_S4_HP > 0:
        $ A_S3_Tgt_04 = 0
    if D_S5_HP > 0:
        $ A_S3_Tgt_05 = 0
    if D_S6_HP > 0:
        $ A_S3_Tgt_06 = 0
    return

#==========================================
label BS_Update_A_S4_ChkTgt_Cls02_Ttc02:
#==========================================
    if D_S1_HP > 0:
        $ A_S4_Tgt_01 = 0
    if D_S2_HP > 0:
        $ A_S4_Tgt_02 = 0
    if D_S3_HP > 0:
        $ A_S4_Tgt_03 = 0
    if D_S4_HP > 0:
        $ A_S4_Tgt_04 = 0
    if D_S5_HP > 0:
        $ A_S4_Tgt_05 = 0
    if D_S6_HP > 0:
        $ A_S4_Tgt_06 = 0
    return

#==========================================
label BS_Update_A_S5_ChkTgt_Cls02_Ttc02:
#==========================================
    if D_S1_HP > 0:
        $ A_S5_Tgt_01 = 0
    if D_S2_HP > 0:
        $ A_S5_Tgt_02 = 0
    if D_S3_HP > 0:
        $ A_S5_Tgt_03 = 0
    if D_S4_HP > 0:
        $ A_S5_Tgt_04 = 0
    if D_S5_HP > 0:
        $ A_S5_Tgt_05 = 0
    if D_S6_HP > 0:
        $ A_S5_Tgt_06 = 0
    return

#==========================================
label BS_Update_A_S6_ChkTgt_Cls02_Ttc02:
#==========================================
    if D_S1_HP > 0:
        $ A_S6_Tgt_01 = 0
    if D_S2_HP > 0:
        $ A_S6_Tgt_02 = 0
    if D_S3_HP > 0:
        $ A_S6_Tgt_03 = 0
    if D_S4_HP > 0:
        $ A_S6_Tgt_04 = 0
    if D_S5_HP > 0:
        $ A_S6_Tgt_05 = 0
    if D_S6_HP > 0:
        $ A_S6_Tgt_06 = 0
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#==========================================
label BS_Update_D_S1_ChkTgt_Cls02_Ttc02:
#==========================================
    if A_S1_HP > 0:
        $ D_S1_Tgt_01 = 1
    if A_S2_HP > 0:
        $ D_S1_Tgt_02 = 0
    if A_S3_HP > 0:
        $ D_S1_Tgt_03 = 0
    if A_S4_HP > 0:
        $ D_S1_Tgt_04 = 0
    if A_S5_HP > 0:
        $ D_S1_Tgt_05 = 0
    if A_S6_HP > 0:
        $ D_S1_Tgt_06 = 0
    return

#==========================================
label BS_Update_D_S2_ChkTgt_Cls02_Ttc02:
#==========================================
    if A_S1_HP > 0:
        $ D_S2_Tgt_01 = 0
    if A_S2_HP > 0:
        $ D_S2_Tgt_02 = 1
    if A_S3_HP > 0:
        $ D_S2_Tgt_03 = 0
    if A_S4_HP > 0:
        $ D_S2_Tgt_04 = 0
    if A_S5_HP > 0:
        $ D_S2_Tgt_05 = 0
    if A_S6_HP > 0:
        $ D_S2_Tgt_06 = 0
    return

#==========================================
label BS_Update_D_S3_ChkTgt_Cls02_Ttc02:
#==========================================
    if A_S1_HP > 0:
        $ D_S3_Tgt_01 = 0
    if A_S2_HP > 0:
        $ D_S3_Tgt_02 = 0
    if A_S3_HP > 0:
        $ D_S3_Tgt_03 = 1
    if A_S4_HP > 0:
        $ D_S3_Tgt_04 = 0
    if A_S5_HP > 0:
        $ D_S3_Tgt_05 = 0
    if A_S6_HP > 0:
        $ D_S3_Tgt_06 = 0
    return

#==========================================
label BS_Update_D_S4_ChkTgt_Cls02_Ttc02:
#==========================================
    if A_S1_HP > 0:
        $ D_S4_Tgt_01 = 0
    if A_S2_HP > 0:
        $ D_S4_Tgt_02 = 0
    if A_S3_HP > 0:
        $ D_S4_Tgt_03 = 0
    if A_S4_HP > 0:
        $ D_S4_Tgt_04 = 0
    if A_S5_HP > 0:
        $ D_S4_Tgt_05 = 0
    if A_S6_HP > 0:
        $ D_S4_Tgt_06 = 0
    return

#==========================================
label BS_Update_D_S5_ChkTgt_Cls02_Ttc02:
#==========================================
    if A_S1_HP > 0:
        $ D_S5_Tgt_01 = 0
    if A_S2_HP > 0:
        $ D_S5_Tgt_02 = 0
    if A_S3_HP > 0:
        $ D_S5_Tgt_03 = 0
    if A_S4_HP > 0:
        $ D_S5_Tgt_04 = 0
    if A_S5_HP > 0:
        $ D_S5_Tgt_05 = 0
    if A_S6_HP > 0:
        $ D_S5_Tgt_06 = 0
    return

#==========================================
label BS_Update_D_S6_ChkTgt_Cls02_Ttc02:
#==========================================
    if A_S1_HP > 0:
        $ D_S6_Tgt_01 = 0
    if A_S2_HP > 0:
        $ D_S6_Tgt_02 = 0
    if A_S3_HP > 0:
        $ D_S6_Tgt_03 = 0
    if A_S4_HP > 0:
        $ D_S6_Tgt_04 = 0
    if A_S5_HP > 0:
        $ D_S6_Tgt_05 = 0
    if A_S6_HP > 0:
        $ D_S6_Tgt_06 = 0
    return
