
label AB_SkillClicked:

    hide screen Screen_UI_PI_Main
    hide screen Screen_UI_PI_ChgTtc
    hide screen Screen_UI_PI_ChgPOS
    $ BS_WhoControl = "PI"

    if BS_WhoAct == "A_S1":
        jump BS_Bhv_A_S1_Skill
    elif BS_WhoAct == "A_S2":
        jump BS_Bhv_A_S2_Skill
    elif BS_WhoAct == "A_S3":
        jump BS_Bhv_A_S3_Skill
    elif BS_WhoAct == "A_S4":
        jump BS_Bhv_A_S4_Skill
    elif BS_WhoAct == "A_S5":
        jump BS_Bhv_A_S5_Skill
    elif BS_WhoAct == "A_S6":
        jump BS_Bhv_A_S6_Skill

    elif BS_WhoAct == "D_S1":
        jump BS_Bhv_D_S1_Skill
    elif BS_WhoAct == "D_S2":
        jump BS_Bhv_D_S2_Skill
    elif BS_WhoAct == "D_S3":
        jump BS_Bhv_D_S3_Skill
    elif BS_WhoAct == "D_S4":
        jump BS_Bhv_D_S4_Skill
    elif BS_WhoAct == "D_S5":
        jump BS_Bhv_D_S5_Skill
    elif BS_WhoAct == "D_S6":
        jump BS_Bhv_D_S6_Skill

    else:
        e "Error: AB_SkillClicked, Who control = None"
        $ renpy.pause (hard=True)