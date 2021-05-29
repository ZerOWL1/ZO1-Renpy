
#==========================================
label Update_Scr_Dueltxt_On:
#==========================================
#-----------------------------------
    hide screen Scr_Txt_Duel
    show screen Scr_Txt_Duel
    $ renpy.pause(Txt_AntSec_Ttl, hard=True)
#-----------------------------------
    return

#==========================================
label Update_Scr_BackGround_On:
#==========================================
#-----------------------------------
    if BS_BGRdm == 1:
        hide BS_BF_001 with Dissolve (SecWait_LoadBG)
        show BS_BF_001 with Dissolve (SecWait_LoadBG)
    elif BS_BGRdm == 2:
        hide BS_BF_002 with Dissolve (SecWait_LoadBG)
        show BS_BF_002 with Dissolve (SecWait_LoadBG)
    elif BS_BGRdm == 3:
        hide BS_BF_003 with Dissolve (SecWait_LoadBG)
        show BS_BF_003 with Dissolve (SecWait_LoadBG)
    elif BS_BGRdm == 4:
        hide BS_BF_004 with Dissolve (SecWait_LoadBG)
        show BS_BF_004 with Dissolve (SecWait_LoadBG)
    elif BS_BGRdm == 5:
        hide BS_BF_005 with Dissolve (SecWait_LoadBG)
        show BS_BF_005 with Dissolve (SecWait_LoadBG)
    elif BS_BGRdm == 6:
        hide BS_BF_006 with Dissolve (SecWait_LoadBG)
        show BS_BF_006 with Dissolve (SecWait_LoadBG)
#-----------------------------------
    return

#==========================================
label Update_Scr_Loading_On:
#==========================================
#-----------------------------------
    hide screen Scr_Loading
    show screen Scr_Loading 
    with Dissolve(0.5)
    $ renpy.pause(1.0, hard = True)
#-----------------------------------
    return

#==========================================
label Update_Scr_Loading_Off:
#==========================================
#-----------------------------------
    $ renpy.pause(1.0, hard = True)
    hide screen Scr_Loading 
    with Dissolve(0.5)
#-----------------------------------
    return

#==========================================
label Update_Scr_BattleInfo_On:
#==========================================
#-----------------------------------
    hide screen Scr_BattleInfo
    show screen Scr_BattleInfo
#-----------------------------------
    return

#==========================================
label Update_Scr_Test_BattleInfo:
#==========================================
#-----------------------------------
    hide screen Scr_Test_BattleInfo
    show screen Scr_Test_BattleInfo
#-----------------------------------
    return

#==========================================
label Update_Scr_Cls_All_Phase_00_On:
#==========================================
#-----------------------------------
    hide screen Scr_Cls_All_Phase_01
    hide screen Scr_Cls_All_Phase_02
    hide screen Scr_Cls_All_Phase_03
    hide screen Scr_Cls_All_Phase_04
    $ BS_AniPhase = 0 
    show screen Scr_Cls_All_Phase_00
#-----------------------------------
    return

#==========================================
label Update_Scr_Cls_All_Phase_01_On:
#==========================================
#-----------------------------------
    hide screen Scr_Cls_All_Phase_00
    $ BS_AniPhase = 1
    show screen Scr_Cls_All_Phase_01
#-----------------------------------
    return

#==========================================
label Update_Scr_Cls_All_Phase_02_On:
#==========================================
#-----------------------------------
    hide screen Scr_Cls_All_Phase_01
    $ BS_AniPhase = 2
    show screen Scr_Cls_All_Phase_02
#-----------------------------------
    return

#==========================================
label Update_Scr_Cls_All_Phase_03_On:
#==========================================
#-----------------------------------
    hide screen Scr_Cls_All_Phase_02
    $ BS_AniPhase = 3
    show screen Scr_Cls_All_Phase_03
#-----------------------------------
    return

#==========================================
label Update_Scr_Cls_All_Phase_04_On:
#==========================================
#-----------------------------------
    hide screen Scr_Cls_All_Phase_03
    $ BS_AniPhase = 4
    show screen Scr_Cls_All_Phase_04
#-----------------------------------
    return

#==========================================
label Update_Scr_Atker_On:
#==========================================
#-----------------------------------
    hide screen Scr_Atker
    show screen Scr_Atker
#-----------------------------------
    return

#==========================================
label Update_Scr_Atker_Off:
#==========================================
#-----------------------------------
    hide screen Scr_Atker
#-----------------------------------
    return

#==========================================
label Update_Scr_SkillEffect_Icon:
#==========================================
#-----------------------------------
    hide screen Scr_SkillEffect_Icon
    show screen Scr_SkillEffect_Icon
#-----------------------------------
    return

#==========================================
label Call_Scr_Mor:
#==========================================
#-----------------------------------
    hide screen Scr_Mor
    show screen Scr_Mor
#-----------------------------------
    return

#==========================================
label Call_Scr_Txt_Cls_Crit:
#==========================================
#-----------------------------------
    hide screen Scr_Txt_Cls_Crit
    show screen Scr_Txt_Cls_Crit
#-----------------------------------
    return

#==========================================
label Call_Scr_DuelResult:
#==========================================
#-----------------------------------
    show screen Scr_DuelResult
    $ renpy.pause(Txt_AntSec_Ttl, hard=True)
    hide screen Scr_DuelResult
#-----------------------------------
    return

#==========================================
label Call_Scr_DuelResult_Mor:
#==========================================
#-----------------------------------
    show screen Scr_DuelResult_Mor
    $ renpy.pause(Txt_AntSec_Ttl, hard=True)
    hide screen Scr_DuelResult_Mor
#-----------------------------------
    return

#==========================================
label Update_Scr_HealRcv_Txt_On:
#==========================================
#-----------------------------------
    show screen Scr_HealRcv_Txt
    $ renpy.pause(Txt_AntSec_Ttl, hard=True)
    hide screen Scr_HealRcv_Txt
#-----------------------------------
    return

#==========================================
label Call_Scr_DmgRcv_Eft_On_Off:
#==========================================
#-----------------------------------
    show screen Scr_Eft
    show screen Scr_DmgRcv
    $ renpy.pause(Txt_AntSec_Ttl, hard=True)
    hide screen Scr_DmgRcv
    hide screen Scr_Eft
#-----------------------------------
    return

#==========================================
label Call_Scr_Tgt_Ttc_On_Off:
#==========================================
#-----------------------------------
    show screen Scr_Tgt
    show screen Scr_Ttc
    $ renpy.pause(Txt_AntSec_Ttl, hard=True)
    hide screen Scr_Ttc
    hide screen Scr_Tgt
#-----------------------------------
    return

#==========================================
label Call_Scr_TgtHeal_Ttc_On_Off:
#==========================================
#-----------------------------------
    show screen Scr_TgtHeal
    show screen Scr_Ttc
    $ renpy.pause(Txt_AntSec_Ttl, hard=True)
    hide screen Scr_Ttc
    hide screen Scr_TgtHeal
#-----------------------------------
    return
