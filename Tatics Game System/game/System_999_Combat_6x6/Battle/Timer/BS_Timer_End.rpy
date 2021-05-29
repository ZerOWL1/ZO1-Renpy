label BS_BS_Timer_End:

    if BS_Timer >= BS_Chk_Timer:
        $ BS_Timer = 0
        $ BS_Turns +=1

    if ((A_S1_Fgt >= 100) or (
    A_S2_Fgt >= 100) or (
    A_S3_Fgt >= 100) or (
    A_S4_Fgt >= 100) or (
    A_S5_Fgt >= 100) or (
    A_S6_Fgt >= 100) or (
    D_S1_Fgt >= 100) or (
    D_S2_Fgt >=100) or (
    D_S3_Fgt >= 100) or (
    D_S4_Fgt >= 100) or (
    D_S5_Fgt >= 100) or (
    D_S6_Fgt >= 100)) or ((
    A_S1_Fgt >= 100) and (
    A_S2_Fgt >= 100) and (
    A_S3_Fgt >= 100) and (
    A_S4_Fgt >= 100) and (
    A_S5_Fgt >= 100) and (
    A_S6_Fgt >= 100) and (
    D_S1_Fgt >= 100) and (
    D_S2_Fgt >=100) and (
    D_S3_Fgt >= 100) and (
    D_S4_Fgt >= 100) and (
    D_S5_Fgt >= 100) and (
    D_S6_Fgt >= 100)):
        call BS_Can_Act

    return

label BS_Can_Act:

    if A_S1_Fgt >= 100 and A_S1_HP > 0:
        $ A_S1_Fgt = 0
        $ A_S1_CanAct = 1

    if A_S2_Fgt >= 100 and A_S2_HP > 0:
        $ A_S2_Fgt = 0
        $ A_S2_CanAct = 1

    if A_S3_Fgt >= 100 and A_S3_HP > 0:
        $ A_S3_Fgt = 0
        $ A_S3_CanAct = 1

    if A_S4_Fgt >= 100 and A_S4_HP > 0:
        $ A_S4_Fgt = 0
        $ A_S4_CanAct = 1

    if A_S5_Fgt >= 100 and A_S5_HP > 0:
        $ A_S5_Fgt = 0          
        $ A_S5_CanAct = 1

    if A_S6_Fgt >= 100 and A_S6_HP > 0:
        $ A_S6_Fgt = 0
        $ A_S6_CanAct = 1
        
    if D_S1_Fgt >= 100 and D_S1_HP > 0:
        $ D_S1_Fgt = 0
        $ D_S1_CanAct = 1

    if D_S2_Fgt >= 100 and D_S2_HP > 0:
        $ D_S2_Fgt = 0
        $ D_S2_CanAct = 1

    if D_S3_Fgt >= 100 and D_S3_HP > 0:
        $ D_S3_Fgt = 0
        $ D_S3_CanAct = 1

    if D_S4_Fgt >= 100 and D_S4_HP > 0:
        $ D_S4_Fgt = 0
        $ D_S4_CanAct = 1

    if D_S5_Fgt >= 100 and D_S5_HP > 0:
        $ D_S5_Fgt = 0
        $ D_S5_CanAct = 1

    if D_S6_Fgt >= 100 and D_S6_HP > 0:
        $ D_S6_Fgt = 0
        $ D_S6_CanAct = 1

    return