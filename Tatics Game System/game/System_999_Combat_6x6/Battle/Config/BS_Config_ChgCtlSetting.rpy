label BS_Config_ChgCtlSetting:

    menu:
        "Which side do you wish to control ?"

        "Attacker":
            $ BS_Ctl_PlayerSide = 1
            $ A_S1_Ctl_Type = "PI"
            $ A_S2_Ctl_Type = "PI"
            $ A_S3_Ctl_Type = "PI"
            $ A_S4_Ctl_Type = "PI"
            $ A_S5_Ctl_Type = "PI"
            $ A_S6_Ctl_Type = "PI"

        "Deffender":
            $ BS_Ctl_PlayerSide = 2
            $ D_S1_Ctl_Type = "PI"
            $ D_S2_Ctl_Type = "PI"
            $ D_S3_Ctl_Type = "PI"
            $ D_S4_Ctl_Type = "PI"
            $ D_S5_Ctl_Type = "PI"
            $ D_S6_Ctl_Type = "PI"

        "Both":
            $ BS_Ctl_PlayerSide = 3
            $ A_S1_Ctl_Type = "PI"
            $ A_S2_Ctl_Type = "PI"
            $ A_S3_Ctl_Type = "PI"
            $ A_S4_Ctl_Type = "PI"
            $ A_S5_Ctl_Type = "PI"
            $ A_S6_Ctl_Type = "PI"

            $ D_S1_Ctl_Type = "PI"
            $ D_S2_Ctl_Type = "PI"
            $ D_S3_Ctl_Type = "PI"
            $ D_S4_Ctl_Type = "PI"
            $ D_S5_Ctl_Type = "PI"
            $ D_S6_Ctl_Type = "PI"

        "Skip":
            pass

    $ renpy.pause(BS_SysSpd, hard = True)
    return