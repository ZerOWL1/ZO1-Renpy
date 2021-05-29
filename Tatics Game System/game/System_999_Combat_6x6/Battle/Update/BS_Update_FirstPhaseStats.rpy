label BS_Update_FirstPhaseStats:

    call BS_Update_A_S1_AtkChange
    call BS_Update_A_S2_AtkChange
    call BS_Update_A_S3_AtkChange
    call BS_Update_A_S4_AtkChange
    call BS_Update_A_S5_AtkChange
    call BS_Update_A_S6_AtkChange
    call BS_Update_D_S1_AtkChange
    call BS_Update_D_S2_AtkChange
    call BS_Update_D_S3_AtkChange
    call BS_Update_D_S4_AtkChange
    call BS_Update_D_S5_AtkChange
    call BS_Update_D_S6_AtkChange

    call BS_Update_A_S1_DefChange
    call BS_Update_A_S2_DefChange
    call BS_Update_A_S3_DefChange
    call BS_Update_A_S4_DefChange
    call BS_Update_A_S5_DefChange
    call BS_Update_A_S6_DefChange
    call BS_Update_D_S1_DefChange
    call BS_Update_D_S2_DefChange
    call BS_Update_D_S3_DefChange
    call BS_Update_D_S4_DefChange
    call BS_Update_D_S5_DefChange
    call BS_Update_D_S6_DefChange

    call BS_Update_A_S1_MaxExp
    call BS_Update_A_S2_MaxExp
    call BS_Update_A_S3_MaxExp
    call BS_Update_A_S4_MaxExp
    call BS_Update_A_S5_MaxExp
    call BS_Update_A_S6_MaxExp
    call BS_Update_D_S1_MaxExp
    call BS_Update_D_S2_MaxExp
    call BS_Update_D_S3_MaxExp
    call BS_Update_D_S4_MaxExp
    call BS_Update_D_S5_MaxExp
    call BS_Update_D_S6_MaxExp

    $ renpy.pause(BS_SysSpd, hard = True)
    return