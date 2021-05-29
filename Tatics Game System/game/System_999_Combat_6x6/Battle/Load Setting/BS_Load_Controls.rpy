label BS_Load_Controls:

    if BS_Ctl_PlayerSide == 3:
        if A_S1_Ctl_Type == 0:
            $ A_S1_Ctl_Type = "PI"
        if A_S2_Ctl_Type == 0:
            $ A_S2_Ctl_Type = "PI"
        if A_S3_Ctl_Type == 0:
            $ A_S3_Ctl_Type = "PI"
        if A_S4_Ctl_Type == 0:
            $ A_S4_Ctl_Type = "PI"
        if A_S5_Ctl_Type == 0:
            $ A_S5_Ctl_Type = "PI"
        if A_S6_Ctl_Type == 0:
            $ A_S6_Ctl_Type = "PI"

        if D_S1_Ctl_Type == 0:
            $ D_S1_Ctl_Type = "PI"
        if D_S2_Ctl_Type == 0:
            $ D_S2_Ctl_Type = "PI"
        if D_S3_Ctl_Type == 0:
            $ D_S3_Ctl_Type = "PI"
        if D_S4_Ctl_Type == 0:
            $ D_S4_Ctl_Type = "PI"
        if D_S5_Ctl_Type == 0:
            $ D_S5_Ctl_Type = "PI"
        if D_S6_Ctl_Type == 0:
            $ D_S6_Ctl_Type = "PI"

    elif BS_Ctl_PlayerSide == 2:
        if D_S1_Ctl_Type == 0:
            $ D_S1_Ctl_Type = "PI"
        if D_S2_Ctl_Type == 0:
            $ D_S2_Ctl_Type = "PI"
        if D_S3_Ctl_Type == 0:
            $ D_S3_Ctl_Type = "PI"
        if D_S4_Ctl_Type == 0:
            $ D_S4_Ctl_Type = "PI"
        if D_S5_Ctl_Type == 0:
            $ D_S5_Ctl_Type = "PI"
        if D_S6_Ctl_Type == 0:
            $ D_S6_Ctl_Type = "PI"

    elif BS_Ctl_PlayerSide == 1:
        if A_S1_Ctl_Type == 0:
            $ A_S1_Ctl_Type = "PI"
        if A_S2_Ctl_Type == 0:
            $ A_S2_Ctl_Type = "PI"
        if A_S3_Ctl_Type == 0:
            $ A_S3_Ctl_Type = "PI"
        if A_S4_Ctl_Type == 0:
            $ A_S4_Ctl_Type = "PI"
        if A_S5_Ctl_Type == 0:
            $ A_S5_Ctl_Type = "PI"
        if A_S6_Ctl_Type == 0:
            $ A_S6_Ctl_Type = "PI"

    $ renpy.pause(BS_SysSpd, hard = True)
    return