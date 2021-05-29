
#///////////////////////  ATTACKER SLOT 1
#=========================
label BS_A_S1_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if A_S1_Tgt_01 == 1:
        call BS_Chk_D_S1_UntEvt
        call BS_Chk_D_S1_LedEvt
        $ D_S1_Dmg_Rcv = 0
        $ D_S1_DmgRcvType = 0
        $ D_S1_CanEvd = 0
        $ D_S1_EvdRate = 1
    if A_S1_Tgt_02 == 1:
        call BS_Chk_D_S2_UntEvt
        call BS_Chk_D_S2_LedEvt
        $ D_S2_Dmg_Rcv = 0
        $ D_S2_DmgRcvType = 0
        $ D_S2_CanEvd = 0
        $ D_S2_EvdRate = 1
    if A_S1_Tgt_03 == 1:
        call BS_Chk_D_S3_UntEvt
        call BS_Chk_D_S3_LedEvt
        $ D_S3_Dmg_Rcv = 0
        $ D_S3_DmgRcvType = 0
        $ D_S3_CanEvd = 0
        $ D_S3_EvdRate = 1
    if A_S1_Tgt_04 == 1:
        call BS_Chk_D_S4_UntEvt
        call BS_Chk_D_S4_LedEvt
        $ D_S4_Dmg_Rcv = 0
        $ D_S4_DmgRcvType = 0
        $ D_S4_CanEvd = 0
        $ D_S4_EvdRate = 1
    if A_S1_Tgt_05 == 1:
        call BS_Chk_D_S5_UntEvt
        call BS_Chk_D_S5_LedEvt
        $ D_S5_Dmg_Rcv = 0
        $ D_S5_DmgRcvType = 0
        $ D_S5_CanEvd = 0
        $ D_S5_EvdRate = 1
    if A_S1_Tgt_06 == 1:
        call BS_Chk_D_S6_UntEvt
        call BS_Chk_D_S6_LedEvt
        $ D_S6_Dmg_Rcv = 0
        $ D_S6_DmgRcvType = 0
        $ D_S6_CanEvd = 0
        $ D_S6_EvdRate = 1
#-----------------------------------
    call BS_A_S1_Rst_Dmg
    call BS_A_S1_Rst_Crit
    call BS_A_S1_Rst_Tgt
    $ A_S1_CanAct = 0
    $ A_S1_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 1
#=========================
label BS_A_S2_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if A_S2_Tgt_01 == 1:
        call BS_Chk_D_S1_UntEvt
        call BS_Chk_D_S1_LedEvt
        $ D_S1_Dmg_Rcv = 0
        $ D_S1_DmgRcvType = 0
        $ D_S1_CanEvd = 0
        $ D_S1_EvdRate = 1
    if A_S2_Tgt_02 == 1:
        call BS_Chk_D_S2_UntEvt
        call BS_Chk_D_S2_LedEvt
        $ D_S2_Dmg_Rcv = 0
        $ D_S2_DmgRcvType = 0
        $ D_S2_CanEvd = 0
        $ D_S2_EvdRate = 1
    if A_S2_Tgt_03 == 1:
        call BS_Chk_D_S3_UntEvt
        call BS_Chk_D_S3_LedEvt
        $ D_S3_Dmg_Rcv = 0
        $ D_S3_DmgRcvType = 0
        $ D_S3_CanEvd = 0
        $ D_S3_EvdRate = 1
    if A_S2_Tgt_04 == 1:
        call BS_Chk_D_S4_UntEvt
        call BS_Chk_D_S4_LedEvt
        $ D_S4_Dmg_Rcv = 0
        $ D_S4_DmgRcvType = 0
        $ D_S4_CanEvd = 0
        $ D_S4_EvdRate = 1
    if A_S2_Tgt_05 == 1:
        call BS_Chk_D_S5_UntEvt
        call BS_Chk_D_S5_LedEvt
        $ D_S5_Dmg_Rcv = 0
        $ D_S5_DmgRcvType = 0
        $ D_S5_CanEvd = 0
        $ D_S5_EvdRate = 1
    if A_S2_Tgt_06 == 1:
        call BS_Chk_D_S6_UntEvt
        call BS_Chk_D_S6_LedEvt
        $ D_S6_Dmg_Rcv = 0
        $ D_S6_DmgRcvType = 0
        $ D_S6_CanEvd = 0
        $ D_S6_EvdRate = 1
#-----------------------------------
    call BS_A_S2_Rst_Dmg
    call BS_A_S2_Rst_Crit
    call BS_A_S2_Rst_Tgt
    $ A_S2_CanAct = 0
    $ A_S2_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 1
#=========================
label BS_A_S3_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if A_S3_Tgt_01 == 1:
        call BS_Chk_D_S1_UntEvt
        call BS_Chk_D_S1_LedEvt
        $ D_S1_Dmg_Rcv = 0
        $ D_S1_DmgRcvType = 0
        $ D_S1_CanEvd = 0
        $ D_S1_EvdRate = 1
    if A_S3_Tgt_02 == 1:
        call BS_Chk_D_S2_UntEvt
        call BS_Chk_D_S2_LedEvt
        $ D_S2_Dmg_Rcv = 0
        $ D_S2_DmgRcvType = 0
        $ D_S2_CanEvd = 0
        $ D_S2_EvdRate = 1
    if A_S3_Tgt_03 == 1:
        call BS_Chk_D_S3_UntEvt
        call BS_Chk_D_S3_LedEvt
        $ D_S3_Dmg_Rcv = 0
        $ D_S3_DmgRcvType = 0
        $ D_S3_CanEvd = 0
        $ D_S3_EvdRate = 1
    if A_S3_Tgt_04 == 1:
        call BS_Chk_D_S4_UntEvt
        call BS_Chk_D_S4_LedEvt
        $ D_S4_Dmg_Rcv = 0
        $ D_S4_DmgRcvType = 0
        $ D_S4_CanEvd = 0
        $ D_S4_EvdRate = 1
    if A_S3_Tgt_05 == 1:
        call BS_Chk_D_S5_UntEvt
        call BS_Chk_D_S5_LedEvt
        $ D_S5_Dmg_Rcv = 0
        $ D_S5_DmgRcvType = 0
        $ D_S5_CanEvd = 0
        $ D_S5_EvdRate = 1
    if A_S3_Tgt_06 == 1:
        call BS_Chk_D_S6_UntEvt
        call BS_Chk_D_S6_LedEvt
        $ D_S6_Dmg_Rcv = 0
        $ D_S6_DmgRcvType = 0
        $ D_S6_CanEvd = 0
        $ D_S6_EvdRate = 1
#-----------------------------------
    call BS_A_S3_Rst_Dmg
    call BS_A_S3_Rst_Crit
    call BS_A_S3_Rst_Tgt
    $ A_S3_CanAct = 0
    $ A_S3_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 1
#=========================
label BS_A_S4_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if A_S4_Tgt_01 == 1:
        call BS_Chk_D_S1_UntEvt
        call BS_Chk_D_S1_LedEvt
        $ D_S1_Dmg_Rcv = 0
        $ D_S1_DmgRcvType = 0
        $ D_S1_CanEvd = 0
        $ D_S1_EvdRate = 1
    if A_S4_Tgt_02 == 1:
        call BS_Chk_D_S2_UntEvt
        call BS_Chk_D_S2_LedEvt
        $ D_S2_Dmg_Rcv = 0
        $ D_S2_DmgRcvType = 0
        $ D_S2_CanEvd = 0
        $ D_S2_EvdRate = 1
    if A_S4_Tgt_03 == 1:
        call BS_Chk_D_S3_UntEvt
        call BS_Chk_D_S3_LedEvt
        $ D_S3_Dmg_Rcv = 0
        $ D_S3_DmgRcvType = 0
        $ D_S3_CanEvd = 0
        $ D_S3_EvdRate = 1
    if A_S4_Tgt_04 == 1:
        call BS_Chk_D_S4_UntEvt
        call BS_Chk_D_S4_LedEvt
        $ D_S4_Dmg_Rcv = 0
        $ D_S4_DmgRcvType = 0
        $ D_S4_CanEvd = 0
        $ D_S4_EvdRate = 1
    if A_S4_Tgt_05 == 1:
        call BS_Chk_D_S5_UntEvt
        call BS_Chk_D_S5_LedEvt
        $ D_S5_Dmg_Rcv = 0
        $ D_S5_DmgRcvType = 0
        $ D_S5_CanEvd = 0
        $ D_S5_EvdRate = 1
    if A_S4_Tgt_06 == 1:
        call BS_Chk_D_S6_UntEvt
        call BS_Chk_D_S6_LedEvt
        $ D_S6_Dmg_Rcv = 0
        $ D_S6_DmgRcvType = 0
        $ D_S6_CanEvd = 0
        $ D_S6_EvdRate = 1
#-----------------------------------
    call BS_A_S4_Rst_Dmg
    call BS_A_S4_Rst_Crit
    call BS_A_S4_Rst_Tgt
    $ A_S4_CanAct = 0
    $ A_S4_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 1
#=========================
label BS_A_S5_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if A_S5_Tgt_01 == 1:
        call BS_Chk_D_S1_UntEvt
        call BS_Chk_D_S1_LedEvt
        $ D_S1_Dmg_Rcv = 0
        $ D_S1_DmgRcvType = 0
        $ D_S1_CanEvd = 0
        $ D_S1_EvdRate = 1
    if A_S5_Tgt_02 == 1:
        call BS_Chk_D_S2_UntEvt
        call BS_Chk_D_S2_LedEvt
        $ D_S2_Dmg_Rcv = 0
        $ D_S2_DmgRcvType = 0
        $ D_S2_CanEvd = 0
        $ D_S2_EvdRate = 1
    if A_S5_Tgt_03 == 1:
        call BS_Chk_D_S3_UntEvt
        call BS_Chk_D_S3_LedEvt
        $ D_S3_Dmg_Rcv = 0
        $ D_S3_DmgRcvType = 0
        $ D_S3_CanEvd = 0
        $ D_S3_EvdRate = 1
    if A_S5_Tgt_04 == 1:
        call BS_Chk_D_S4_UntEvt
        call BS_Chk_D_S4_LedEvt
        $ D_S4_Dmg_Rcv = 0
        $ D_S4_DmgRcvType = 0
        $ D_S4_CanEvd = 0
        $ D_S4_EvdRate = 1
    if A_S5_Tgt_05 == 1:
        call BS_Chk_D_S5_UntEvt
        call BS_Chk_D_S5_LedEvt
        $ D_S5_Dmg_Rcv = 0
        $ D_S5_DmgRcvType = 0
        $ D_S5_CanEvd = 0
        $ D_S5_EvdRate = 1
    if A_S5_Tgt_06 == 1:
        call BS_Chk_D_S6_UntEvt
        call BS_Chk_D_S6_LedEvt
        $ D_S6_Dmg_Rcv = 0
        $ D_S6_DmgRcvType = 0
        $ D_S6_CanEvd = 0
        $ D_S6_EvdRate = 1
#-----------------------------------
    call BS_A_S5_Rst_Dmg
    call BS_A_S5_Rst_Crit
    call BS_A_S5_Rst_Tgt
    $ A_S5_CanAct = 0
    $ A_S5_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  ATTACKER SLOT 1
#=========================
label BS_A_S6_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if A_S6_Tgt_01 == 1:
        call BS_Chk_D_S1_UntEvt
        call BS_Chk_D_S1_LedEvt
        $ D_S1_Dmg_Rcv = 0
        $ D_S1_DmgRcvType = 0
        $ D_S1_CanEvd = 0
        $ D_S1_EvdRate = 1
    if A_S6_Tgt_02 == 1:
        call BS_Chk_D_S2_UntEvt
        call BS_Chk_D_S2_LedEvt
        $ D_S2_Dmg_Rcv = 0
        $ D_S2_DmgRcvType = 0
        $ D_S2_CanEvd = 0
        $ D_S2_EvdRate = 1
    if A_S6_Tgt_03 == 1:
        call BS_Chk_D_S3_UntEvt
        call BS_Chk_D_S3_LedEvt
        $ D_S3_Dmg_Rcv = 0
        $ D_S3_DmgRcvType = 0
        $ D_S3_CanEvd = 0
        $ D_S3_EvdRate = 1
    if A_S6_Tgt_04 == 1:
        call BS_Chk_D_S4_UntEvt
        call BS_Chk_D_S4_LedEvt
        $ D_S4_Dmg_Rcv = 0
        $ D_S4_DmgRcvType = 0
        $ D_S4_CanEvd = 0
        $ D_S4_EvdRate = 1
    if A_S6_Tgt_05 == 1:
        call BS_Chk_D_S5_UntEvt
        call BS_Chk_D_S5_LedEvt
        $ D_S5_Dmg_Rcv = 0
        $ D_S5_DmgRcvType = 0
        $ D_S5_CanEvd = 0
        $ D_S5_EvdRate = 1
    if A_S6_Tgt_06 == 1:
        call BS_Chk_D_S6_UntEvt
        call BS_Chk_D_S6_LedEvt
        $ D_S6_Dmg_Rcv = 0
        $ D_S6_DmgRcvType = 0
        $ D_S6_CanEvd = 0
        $ D_S6_EvdRate = 1
#-----------------------------------
    call BS_A_S6_Rst_Dmg
    call BS_A_S6_Rst_Crit
    call BS_A_S6_Rst_Tgt
    $ A_S6_CanAct = 0
    $ A_S6_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================
#=======================================================================

#///////////////////////  DEFFENDER SLOT 1
#=========================
label BS_D_S1_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if D_S1_Tgt_01 == 1:
        call BS_Chk_A_S1_UntEvt
        call BS_Chk_A_S1_LedEvt
        $ A_S1_Dmg_Rcv = 0
        $ A_S1_DmgRcvType = 0
        $ A_S1_CanEvd = 0
        $ A_S1_EvdRate = 1
    if D_S1_Tgt_02 == 1:
        call BS_Chk_A_S2_UntEvt
        call BS_Chk_A_S2_LedEvt
        $ A_S2_Dmg_Rcv = 0
        $ A_S2_DmgRcvType = 0
        $ A_S2_CanEvd = 0
        $ A_S2_EvdRate = 1
    if D_S1_Tgt_03 == 1:
        call BS_Chk_A_S3_UntEvt
        call BS_Chk_A_S3_LedEvt
        $ A_S3_Dmg_Rcv = 0
        $ A_S3_DmgRcvType = 0
        $ A_S3_CanEvd = 0
        $ A_S3_EvdRate = 1
    if D_S1_Tgt_04 == 1:
        call BS_Chk_A_S4_UntEvt
        call BS_Chk_A_S4_LedEvt
        $ A_S4_Dmg_Rcv = 0
        $ A_S4_DmgRcvType = 0
        $ A_S4_CanEvd = 0
        $ A_S4_EvdRate = 1
    if D_S1_Tgt_05 == 1:
        call BS_Chk_A_S5_UntEvt
        call BS_Chk_A_S5_LedEvt
        $ A_S5_Dmg_Rcv = 0
        $ A_S5_DmgRcvType = 0
        $ A_S5_CanEvd = 0
        $ A_S5_EvdRate = 1
    if D_S1_Tgt_06 == 1:
        call BS_Chk_A_S6_UntEvt
        call BS_Chk_A_S6_LedEvt
        $ A_S6_Dmg_Rcv = 0
        $ A_S6_DmgRcvType = 0
        $ A_S6_CanEvd = 0
        $ A_S6_EvdRate = 1
#-----------------------------------
    call BS_D_S1_Rst_Dmg
    call BS_D_S1_Rst_Crit
    call BS_D_S1_Rst_Tgt
    $ D_S1_CanAct = 0
    $ D_S1_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 1
#=========================
label BS_D_S2_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if D_S2_Tgt_01 == 1:
        call BS_Chk_A_S1_UntEvt
        call BS_Chk_A_S1_LedEvt
        $ A_S1_Dmg_Rcv = 0
        $ A_S1_DmgRcvType = 0
        $ A_S1_CanEvd = 0
        $ A_S1_EvdRate = 1
    if D_S2_Tgt_02 == 1:
        call BS_Chk_A_S2_UntEvt
        call BS_Chk_A_S2_LedEvt
        $ A_S2_Dmg_Rcv = 0
        $ A_S2_DmgRcvType = 0
        $ A_S2_CanEvd = 0
        $ A_S2_EvdRate = 1
    if D_S2_Tgt_03 == 1:
        call BS_Chk_A_S3_UntEvt
        call BS_Chk_A_S3_LedEvt
        $ A_S3_Dmg_Rcv = 0
        $ A_S3_DmgRcvType = 0
        $ A_S3_CanEvd = 0
        $ A_S3_EvdRate = 1
    if D_S2_Tgt_04 == 1:
        call BS_Chk_A_S4_UntEvt
        call BS_Chk_A_S4_LedEvt
        $ A_S4_Dmg_Rcv = 0
        $ A_S4_DmgRcvType = 0
        $ A_S4_CanEvd = 0
        $ A_S4_EvdRate = 1
    if D_S2_Tgt_05 == 1:
        call BS_Chk_A_S5_UntEvt
        call BS_Chk_A_S5_LedEvt
        $ A_S5_Dmg_Rcv = 0
        $ A_S5_DmgRcvType = 0
        $ A_S5_CanEvd = 0
        $ A_S5_EvdRate = 1
    if D_S2_Tgt_06 == 1:
        call BS_Chk_A_S6_UntEvt
        call BS_Chk_A_S6_LedEvt
        $ A_S6_Dmg_Rcv = 0
        $ A_S6_DmgRcvType = 0
        $ A_S6_CanEvd = 0
        $ A_S6_EvdRate = 1
#-----------------------------------
    call BS_D_S2_Rst_Dmg
    call BS_D_S2_Rst_Crit
    call BS_D_S2_Rst_Tgt
    $ D_S2_CanAct = 0
    $ D_S2_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 1
#=========================
label BS_D_S3_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if D_S3_Tgt_01 == 1:
        call BS_Chk_A_S1_UntEvt
        call BS_Chk_A_S1_LedEvt
        $ A_S1_Dmg_Rcv = 0
        $ A_S1_DmgRcvType = 0
        $ A_S1_CanEvd = 0
        $ A_S1_EvdRate = 1
    if D_S3_Tgt_02 == 1:
        call BS_Chk_A_S2_UntEvt
        call BS_Chk_A_S2_LedEvt
        $ A_S2_Dmg_Rcv = 0
        $ A_S2_DmgRcvType = 0
        $ A_S2_CanEvd = 0
        $ A_S2_EvdRate = 1
    if D_S3_Tgt_03 == 1:
        call BS_Chk_A_S3_UntEvt
        call BS_Chk_A_S3_LedEvt
        $ A_S3_Dmg_Rcv = 0
        $ A_S3_DmgRcvType = 0
        $ A_S3_CanEvd = 0
        $ A_S3_EvdRate = 1
    if D_S3_Tgt_04 == 1:
        call BS_Chk_A_S4_UntEvt
        call BS_Chk_A_S4_LedEvt
        $ A_S4_Dmg_Rcv = 0
        $ A_S4_DmgRcvType = 0
        $ A_S4_CanEvd = 0
        $ A_S4_EvdRate = 1
    if D_S3_Tgt_05 == 1:
        call BS_Chk_A_S5_UntEvt
        call BS_Chk_A_S5_LedEvt
        $ A_S5_Dmg_Rcv = 0
        $ A_S5_DmgRcvType = 0
        $ A_S5_CanEvd = 0
        $ A_S5_EvdRate = 1
    if D_S3_Tgt_06 == 1:
        call BS_Chk_A_S6_UntEvt
        call BS_Chk_A_S6_LedEvt
        $ A_S6_Dmg_Rcv = 0
        $ A_S6_DmgRcvType = 0
        $ A_S6_CanEvd = 0
        $ A_S6_EvdRate = 1
#-----------------------------------
    call BS_D_S3_Rst_Dmg
    call BS_D_S3_Rst_Crit
    call BS_D_S3_Rst_Tgt
    $ D_S3_CanAct = 0
    $ D_S3_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 1
#=========================
label BS_D_S4_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if D_S4_Tgt_01 == 1:
        call BS_Chk_A_S1_UntEvt
        call BS_Chk_A_S1_LedEvt
        $ A_S1_Dmg_Rcv = 0
        $ A_S1_DmgRcvType = 0
        $ A_S1_CanEvd = 0
        $ A_S1_EvdRate = 1
    if D_S4_Tgt_02 == 1:
        call BS_Chk_A_S2_UntEvt
        call BS_Chk_A_S2_LedEvt
        $ A_S2_Dmg_Rcv = 0
        $ A_S2_DmgRcvType = 0
        $ A_S2_CanEvd = 0
        $ A_S2_EvdRate = 1
    if D_S4_Tgt_03 == 1:
        call BS_Chk_A_S3_UntEvt
        call BS_Chk_A_S3_LedEvt
        $ A_S3_Dmg_Rcv = 0
        $ A_S3_DmgRcvType = 0
        $ A_S3_CanEvd = 0
        $ A_S3_EvdRate = 1
    if D_S4_Tgt_04 == 1:
        call BS_Chk_A_S4_UntEvt
        call BS_Chk_A_S4_LedEvt
        $ A_S4_Dmg_Rcv = 0
        $ A_S4_DmgRcvType = 0
        $ A_S4_CanEvd = 0
        $ A_S4_EvdRate = 1
    if D_S4_Tgt_05 == 1:
        call BS_Chk_A_S5_UntEvt
        call BS_Chk_A_S5_LedEvt
        $ A_S5_Dmg_Rcv = 0
        $ A_S5_DmgRcvType = 0
        $ A_S5_CanEvd = 0
        $ A_S5_EvdRate = 1
    if D_S4_Tgt_06 == 1:
        call BS_Chk_A_S6_UntEvt
        call BS_Chk_A_S6_LedEvt
        $ A_S6_Dmg_Rcv = 0
        $ A_S6_DmgRcvType = 0
        $ A_S6_CanEvd = 0
        $ A_S6_EvdRate = 1
#-----------------------------------
    call BS_D_S4_Rst_Dmg
    call BS_D_S4_Rst_Crit
    call BS_D_S4_Rst_Tgt
    $ D_S4_CanAct = 0
    $ D_S4_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 1
#=========================
label BS_D_S5_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if D_S5_Tgt_01 == 1:
        call BS_Chk_A_S1_UntEvt
        call BS_Chk_A_S1_LedEvt
        $ A_S1_Dmg_Rcv = 0
        $ A_S1_DmgRcvType = 0
        $ A_S1_CanEvd = 0
        $ A_S1_EvdRate = 1
    if D_S5_Tgt_02 == 1:
        call BS_Chk_A_S2_UntEvt
        call BS_Chk_A_S2_LedEvt
        $ A_S2_Dmg_Rcv = 0
        $ A_S2_DmgRcvType = 0
        $ A_S2_CanEvd = 0
        $ A_S2_EvdRate = 1
    if D_S5_Tgt_03 == 1:
        call BS_Chk_A_S3_UntEvt
        call BS_Chk_A_S3_LedEvt
        $ A_S3_Dmg_Rcv = 0
        $ A_S3_DmgRcvType = 0
        $ A_S3_CanEvd = 0
        $ A_S3_EvdRate = 1
    if D_S5_Tgt_04 == 1:
        call BS_Chk_A_S4_UntEvt
        call BS_Chk_A_S4_LedEvt
        $ A_S4_Dmg_Rcv = 0
        $ A_S4_DmgRcvType = 0
        $ A_S4_CanEvd = 0
        $ A_S4_EvdRate = 1
    if D_S5_Tgt_05 == 1:
        call BS_Chk_A_S5_UntEvt
        call BS_Chk_A_S5_LedEvt
        $ A_S5_Dmg_Rcv = 0
        $ A_S5_DmgRcvType = 0
        $ A_S5_CanEvd = 0
        $ A_S5_EvdRate = 1
    if D_S5_Tgt_06 == 1:
        call BS_Chk_A_S6_UntEvt
        call BS_Chk_A_S6_LedEvt
        $ A_S6_Dmg_Rcv = 0
        $ A_S6_DmgRcvType = 0
        $ A_S6_CanEvd = 0
        $ A_S6_EvdRate = 1
#-----------------------------------
    call BS_D_S5_Rst_Dmg
    call BS_D_S5_Rst_Crit
    call BS_D_S5_Rst_Tgt
    $ D_S5_CanAct = 0
    $ D_S5_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return

#///////////////////////  DEFFENDER SLOT 1
#=========================
label BS_D_S6_Chk_EndTurn_Atk:
#=========================
#-----------------------------------
    if D_S6_Tgt_01 == 1:
        call BS_Chk_A_S1_UntEvt
        call BS_Chk_A_S1_LedEvt
        $ A_S1_Dmg_Rcv = 0
        $ A_S1_DmgRcvType = 0
        $ A_S1_CanEvd = 0
        $ A_S1_EvdRate = 1
    if D_S6_Tgt_02 == 1:
        call BS_Chk_A_S2_UntEvt
        call BS_Chk_A_S2_LedEvt
        $ A_S2_Dmg_Rcv = 0
        $ A_S2_DmgRcvType = 0
        $ A_S2_CanEvd = 0
        $ A_S2_EvdRate = 1
    if D_S6_Tgt_03 == 1:
        call BS_Chk_A_S3_UntEvt
        call BS_Chk_A_S3_LedEvt
        $ A_S3_Dmg_Rcv = 0
        $ A_S3_DmgRcvType = 0
        $ A_S3_CanEvd = 0
        $ A_S3_EvdRate = 1
    if D_S6_Tgt_04 == 1:
        call BS_Chk_A_S4_UntEvt
        call BS_Chk_A_S4_LedEvt
        $ A_S4_Dmg_Rcv = 0
        $ A_S4_DmgRcvType = 0
        $ A_S4_CanEvd = 0
        $ A_S4_EvdRate = 1
    if D_S6_Tgt_05 == 1:
        call BS_Chk_A_S5_UntEvt
        call BS_Chk_A_S5_LedEvt
        $ A_S5_Dmg_Rcv = 0
        $ A_S5_DmgRcvType = 0
        $ A_S5_CanEvd = 0
        $ A_S5_EvdRate = 1
    if D_S6_Tgt_06 == 1:
        call BS_Chk_A_S6_UntEvt
        call BS_Chk_A_S6_LedEvt
        $ A_S6_Dmg_Rcv = 0
        $ A_S6_DmgRcvType = 0
        $ A_S6_CanEvd = 0
        $ A_S6_EvdRate = 1
#-----------------------------------
    call BS_D_S6_Rst_Dmg
    call BS_D_S6_Rst_Crit
    call BS_D_S6_Rst_Tgt
    $ D_S6_CanAct = 0
    $ D_S6_ChgTtc_Count = 0
    hide screen Scr_Atker
#-----------------------------------
    return
