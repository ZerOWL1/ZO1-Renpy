
label AB_EndTurnClicked:

    hide screen Screen_UI_PI_Main
    hide screen Screen_UI_PI_ChgTtc
    hide screen Screen_UI_PI_ChgPOS
    $ BS_WhoControl = "PI"

    if BS_WhoAct == "A_S1":
        call BS_A_S1_Rst_Tgt
    elif BS_WhoAct == "A_S2":
        call BS_A_S2_Rst_Tgt
    elif BS_WhoAct == "A_S3":
        call BS_A_S3_Rst_Tgt
    elif BS_WhoAct == "A_S4":
        call BS_A_S4_Rst_Tgt
    elif BS_WhoAct == "A_S5":
        call BS_A_S5_Rst_Tgt
    elif BS_WhoAct == "A_S6":
        call BS_A_S6_Rst_Tgt

    elif BS_WhoAct == "D_S1":
        call BS_D_S1_Rst_Tgt
    elif BS_WhoAct == "D_S2":
        call BS_D_S2_Rst_Tgt
    elif BS_WhoAct == "D_S3":
        call BS_D_S3_Rst_Tgt
    elif BS_WhoAct == "D_S4":
        call BS_D_S4_Rst_Tgt
    elif BS_WhoAct == "D_S5":
        call BS_D_S5_Rst_Tgt
    elif BS_WhoAct == "D_S6":
        call BS_D_S6_Rst_Tgt

    else:
        e "Error: AB_EndTurnClicked, Who reset target = None"
        $ renpy.pause (hard=True)

    call BS_Rst_Control
    jump BS_Chk_WhoTurn