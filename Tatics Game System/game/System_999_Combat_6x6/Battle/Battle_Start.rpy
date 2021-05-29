#=====================================================
label Battle_Start:
#=====================================================

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    call Update_Scr_Loading_On
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#----------------------------------------------
    call BS_Load_Basic_Setting
    call BS_Load_Controls
    call BS_Load_ActionButton
    call BS_Load_ActionButton_BM
    call BS_Load_ActionButton_BM_List
    call BS_Load_ChkTurnOrder
    call BS_Load_Img_Settings
    call BS_Load_Scr_POS
    call BS_Load_Txt_Effect
    call BS_Load_Unt_Settings
    call BS_Load_Unt_Name
    call BS_Load_Unt_Effect
    call BS_Load_Unt_AniSpd
    call BS_Load_Unt_Cls_BasSts
    call BS_Load_Unt_Cls_Skills
    call BS_Load_Led_Setting
    call BS_Load_Evt_List
    call BS_Load_Evt_Trigger
    call BS_Load_List_Army
    call BS_Load_List_Led
#----------------------------------------------
    call BS_Config_ChgSetting
    call BS_Config_ChgCtlSetting
#----------------------------------------------
    call BS_BM_Start
#----------------------------------------------
    call BS_Army_Cls_BAS
    call BS_Army_Led_BAS
    call BS_Update_FirstPhaseStats
#----------------------------------------------

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    call Update_Scr_Loading_Off
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#----------------------------------------------
    $ BS_BGRdm = renpy.random.randint(1, 6)
    call Update_Scr_BackGround_On
    call Update_Scr_Cls_All_Phase_00_On
    call Update_Scr_BattleInfo_On
    #call Update_Scr_Test_BattleInfo
#----------------------------------------------
    $ renpy.pause(SecWait_Engage, hard = True)
    $ BS_BattleEnd = False
#----------------------------------------------

    call BS_Engage

    return

#=====================================================
label BS_Engage:
#=====================================================
#----------------------------------------------
    call BS_Chk_Over
#----------------------------------------------
    if BS_BattleEnd != True:
        #call BS_Load_Evt_Check
        call BS_Chk_PosChg
        call AI
#----------------------------------------------
        while BS_Timer < BS_Chk_Timer:
            call BS_ATB
            call BS_BS_Timer
            $ renpy.pause(BS_SysSpd, hard = True)
#----------------------------------------------
        call BS_BS_Timer_End
        call BS_A_Chk_SklSlt_Staus
        call BS_D_Chk_SklSlt_Staus
#----------------------------------------------
        jump BS_Engage
#----------------------------------------------
    else:
        return
