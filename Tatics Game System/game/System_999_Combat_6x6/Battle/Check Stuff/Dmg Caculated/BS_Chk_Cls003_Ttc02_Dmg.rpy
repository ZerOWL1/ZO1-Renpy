
#///////////////////////  ATTACKER SLOT 1
#==========================================
label BS_A_S1_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_A_S1_Chk_Mor
    $ A_S1_DmgType = "Range"

    call BS_Update_A_S1_AtkChange

    if A_S1_Tgt_01 == 1:
        call BS_Update_D_S1_DefChange
        $ A_S1_Dmg_01 = ((A_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S1_CrtRate) - D_S1_DefChg
        if A_S1_Dmg_01 <= 0:
            $ A_S1_Dmg_01 = 1
        $ A_S1_Dmg_Total += A_S1_Dmg_01
        call BS_D_S1_Chk_Can_Evd
        call BS_A_S1_Chk_Kil
        call BS_A_S1_Chk_Mor
        $ D_S1_Dmg_Rcv += (A_S1_Dmg_01) * D_S1_EvdRate
        if D_S1_Dmg_Rcv >= D_S1_HP and D_S1_CanEvd == 0:
            $ D_S1_Dmg_Rcv =  D_S1_HP
        call BS_D_S1_Chk_Kld
        call BS_D_S1_Chk_Mor
        call BS_D_S1_Chg_HP
        call BS_D_S1_Chk_Evd

    if A_S1_Tgt_02 == 1:
        call BS_Update_D_S2_DefChange
        $ A_S1_Dmg_02 = ((A_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S1_CrtRate) - D_S2_DefChg
        if A_S1_Dmg_02 <= 0:
            $ A_S1_Dmg_02 = 1
        $ A_S1_Dmg_Total += A_S1_Dmg_02
        call BS_D_S2_Chk_Can_Evd
        call BS_A_S1_Chk_Kil
        call BS_A_S1_Chk_Mor
        $ D_S2_Dmg_Rcv += (A_S1_Dmg_02) * D_S2_EvdRate
        if D_S2_Dmg_Rcv >= D_S2_HP and D_S2_CanEvd == 0:
            $ D_S2_Dmg_Rcv =  D_S2_HP
        call BS_D_S2_Chk_Kld
        call BS_D_S2_Chk_Mor
        call BS_D_S2_Chg_HP
        call BS_D_S2_Chk_Evd

    if A_S1_Tgt_03 == 1:
        call BS_Update_D_S3_DefChange
        $ A_S1_Dmg_03 = ((A_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S1_CrtRate) - D_S3_DefChg
        if A_S1_Dmg_03 <= 0:
            $ A_S1_Dmg_03 = 1
        $ A_S1_Dmg_Total += A_S1_Dmg_03
        call BS_D_S3_Chk_Can_Evd
        call BS_A_S1_Chk_Kil
        call BS_A_S1_Chk_Mor
        $ D_S3_Dmg_Rcv += (A_S1_Dmg_03) * D_S3_EvdRate
        if D_S3_Dmg_Rcv >= D_S3_HP and D_S3_CanEvd == 0:
            $ D_S3_Dmg_Rcv =  D_S3_HP
        call BS_D_S3_Chk_Kld
        call BS_D_S3_Chk_Mor
        call BS_D_S3_Chg_HP
        call BS_D_S3_Chk_Evd

    if A_S1_Tgt_04 == 1:
        call BS_Update_D_S4_DefChange
        $ A_S1_Dmg_04 = ((A_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S1_CrtRate) - D_S4_DefChg
        if A_S1_Dmg_04 <= 0:
            $ A_S1_Dmg_04 = 1
        $ A_S1_Dmg_Total += A_S1_Dmg_04
        call BS_D_S4_Chk_Can_Evd
        call BS_A_S1_Chk_Kil
        call BS_A_S1_Chk_Mor
        $ D_S4_Dmg_Rcv += (A_S1_Dmg_04) * D_S4_EvdRate
        if D_S4_Dmg_Rcv >= D_S4_HP and D_S4_CanEvd == 0:
            $ D_S4_Dmg_Rcv =  D_S4_HP
        call BS_D_S4_Chk_Kld
        call BS_D_S4_Chk_Mor
        call BS_D_S4_Chg_HP
        call BS_D_S4_Chk_Evd

    if A_S1_Tgt_05 == 1:
        call BS_Update_D_S5_DefChange
        $ A_S1_Dmg_05 = ((A_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S1_CrtRate) - D_S5_DefChg
        if A_S1_Dmg_05 <= 0:
            $ A_S1_Dmg_05 = 1
        $ A_S1_Dmg_Total += A_S1_Dmg_05
        call BS_D_S5_Chk_Can_Evd
        call BS_A_S1_Chk_Kil
        call BS_A_S1_Chk_Mor
        $ D_S5_Dmg_Rcv += (A_S1_Dmg_05) * D_S5_EvdRate
        if D_S5_Dmg_Rcv >= D_S5_HP and D_S5_CanEvd == 0:
            $ D_S5_Dmg_Rcv =  D_S5_HP
        call BS_D_S5_Chk_Kld
        call BS_D_S5_Chk_Mor
        call BS_D_S5_Chg_HP
        call BS_D_S5_Chk_Evd

    if A_S1_Tgt_06 == 1:
        call BS_Update_D_S6_DefChange
        $ A_S1_Dmg_06 = ((A_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S1_CrtRate) - D_S6_DefChg
        if A_S1_Dmg_06 <= 0:
            $ A_S1_Dmg_06 = 1
        $ A_S1_Dmg_Total += A_S1_Dmg_06
        call BS_D_S6_Chk_Can_Evd
        call BS_A_S1_Chk_Kil
        call BS_A_S1_Chk_Mor
        $ D_S6_Dmg_Rcv += (A_S1_Dmg_06) * D_S6_EvdRate
        if D_S6_Dmg_Rcv >= D_S6_HP and D_S6_CanEvd == 0:
            $ D_S6_Dmg_Rcv =  D_S6_HP
        call BS_D_S6_Chk_Kld
        call BS_D_S6_Chk_Mor
        call BS_D_S6_Chg_HP
        call BS_D_S6_Chk_Evd

    return

#///////////////////////  ATTACKER SLOT 2
#==========================================
label BS_A_S2_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_A_S2_Chk_Mor
    $ A_S2_DmgType = "Range"

    call BS_Update_A_S2_AtkChange

    if A_S2_Tgt_01 == 1:
        call BS_Update_D_S1_DefChange
        $ A_S2_Dmg_01 = ((A_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S2_CrtRate) - D_S1_DefChg
        if A_S2_Dmg_01 <= 0:
            $ A_S2_Dmg_01 = 1
        $ A_S2_Dmg_Total += A_S2_Dmg_01
        call BS_D_S1_Chk_Can_Evd
        call BS_A_S2_Chk_Kil
        call BS_A_S2_Chk_Mor
        $ D_S1_Dmg_Rcv += (A_S2_Dmg_01) * D_S1_EvdRate
        if D_S1_Dmg_Rcv >= D_S1_HP and D_S1_CanEvd == 0:
            $ D_S1_Dmg_Rcv =  D_S1_HP
        call BS_D_S1_Chk_Kld
        call BS_D_S1_Chk_Mor
        call BS_D_S1_Chg_HP
        call BS_D_S1_Chk_Evd

    if A_S2_Tgt_02 == 1:
        call BS_Update_D_S2_DefChange
        $ A_S2_Dmg_02 = ((A_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S2_CrtRate) - D_S2_DefChg
        if A_S2_Dmg_02 <= 0:
            $ A_S2_Dmg_02 = 1
        $ A_S2_Dmg_Total += A_S2_Dmg_02
        call BS_D_S2_Chk_Can_Evd
        call BS_A_S2_Chk_Kil
        call BS_A_S2_Chk_Mor
        $ D_S2_Dmg_Rcv += (A_S2_Dmg_02) * D_S2_EvdRate
        if D_S2_Dmg_Rcv >= D_S2_HP and D_S2_CanEvd == 0:
            $ D_S2_Dmg_Rcv =  D_S2_HP
        call BS_D_S2_Chk_Kld
        call BS_D_S2_Chk_Mor
        call BS_D_S2_Chg_HP
        call BS_D_S2_Chk_Evd

    if A_S2_Tgt_03 == 1:
        call BS_Update_D_S3_DefChange
        $ A_S2_Dmg_03 = ((A_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S2_CrtRate) - D_S3_DefChg
        if A_S2_Dmg_03 <= 0:
            $ A_S2_Dmg_03 = 1
        $ A_S2_Dmg_Total += A_S2_Dmg_03
        call BS_D_S3_Chk_Can_Evd
        call BS_A_S2_Chk_Kil
        call BS_A_S2_Chk_Mor
        $ D_S3_Dmg_Rcv += (A_S2_Dmg_03) * D_S3_EvdRate
        if D_S3_Dmg_Rcv >= D_S3_HP and D_S3_CanEvd == 0:
            $ D_S3_Dmg_Rcv =  D_S3_HP
        call BS_D_S3_Chk_Kld
        call BS_D_S3_Chk_Mor
        call BS_D_S3_Chg_HP
        call BS_D_S3_Chk_Evd

    if A_S2_Tgt_04 == 1:
        call BS_Update_D_S4_DefChange
        $ A_S2_Dmg_04 = ((A_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S2_CrtRate) - D_S4_DefChg
        if A_S2_Dmg_04 <= 0:
            $ A_S2_Dmg_04 = 1
        $ A_S2_Dmg_Total += A_S2_Dmg_04
        call BS_D_S4_Chk_Can_Evd
        call BS_A_S2_Chk_Kil
        call BS_A_S2_Chk_Mor
        $ D_S4_Dmg_Rcv += (A_S2_Dmg_04) * D_S4_EvdRate
        if D_S4_Dmg_Rcv >= D_S4_HP and D_S4_CanEvd == 0:
            $ D_S4_Dmg_Rcv =  D_S4_HP
        call BS_D_S4_Chk_Kld
        call BS_D_S4_Chk_Mor
        call BS_D_S4_Chg_HP
        call BS_D_S4_Chk_Evd

    if A_S2_Tgt_05 == 1:
        call BS_Update_D_S5_DefChange
        $ A_S2_Dmg_05 = ((A_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S2_CrtRate) - D_S5_DefChg
        if A_S2_Dmg_05 <= 0:
            $ A_S2_Dmg_05 = 1
        $ A_S2_Dmg_Total += A_S2_Dmg_05
        call BS_D_S5_Chk_Can_Evd
        call BS_A_S2_Chk_Kil
        call BS_A_S2_Chk_Mor
        $ D_S5_Dmg_Rcv += (A_S2_Dmg_05) * D_S5_EvdRate
        if D_S5_Dmg_Rcv >= D_S5_HP and D_S5_CanEvd == 0:
            $ D_S5_Dmg_Rcv =  D_S5_HP
        call BS_D_S5_Chk_Kld
        call BS_D_S5_Chk_Mor
        call BS_D_S5_Chg_HP
        call BS_D_S5_Chk_Evd

    if A_S2_Tgt_06 == 1:
        call BS_Update_D_S6_DefChange
        $ A_S2_Dmg_06 = ((A_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S2_CrtRate) - D_S6_DefChg
        if A_S2_Dmg_06 <= 0:
            $ A_S2_Dmg_06 = 1
        $ A_S2_Dmg_Total += A_S2_Dmg_06
        call BS_D_S6_Chk_Can_Evd
        call BS_A_S2_Chk_Kil
        call BS_A_S2_Chk_Mor
        $ D_S6_Dmg_Rcv += (A_S2_Dmg_06) * D_S6_EvdRate
        if D_S6_Dmg_Rcv >= D_S6_HP and D_S6_CanEvd == 0:
            $ D_S6_Dmg_Rcv =  D_S6_HP
        call BS_D_S6_Chk_Kld
        call BS_D_S6_Chk_Mor
        call BS_D_S6_Chg_HP
        call BS_D_S6_Chk_Evd

    return

#///////////////////////  ATTACKER SLOT 3
#==========================================
label BS_A_S3_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_A_S3_Chk_Mor
    $ A_S3_DmgType = "Range"

    call BS_Update_A_S3_AtkChange

    if A_S3_Tgt_01 == 1:
        call BS_Update_D_S1_DefChange
        $ A_S3_Dmg_01 = ((A_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S3_CrtRate) - D_S1_DefChg
        if A_S3_Dmg_01 <= 0:
            $ A_S3_Dmg_01 = 1
        $ A_S3_Dmg_Total += A_S3_Dmg_01
        call BS_D_S1_Chk_Can_Evd
        call BS_A_S3_Chk_Kil
        call BS_A_S3_Chk_Mor
        $ D_S1_Dmg_Rcv += (A_S3_Dmg_01) * D_S1_EvdRate
        if D_S1_Dmg_Rcv >= D_S1_HP and D_S1_CanEvd == 0:
            $ D_S1_Dmg_Rcv =  D_S1_HP
        call BS_D_S1_Chk_Kld
        call BS_D_S1_Chk_Mor
        call BS_D_S1_Chg_HP
        call BS_D_S1_Chk_Evd

    if A_S3_Tgt_02 == 1:
        call BS_Update_D_S2_DefChange
        $ A_S3_Dmg_02 = ((A_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S3_CrtRate) - D_S2_DefChg
        if A_S3_Dmg_02 <= 0:
            $ A_S3_Dmg_02 = 1
        $ A_S3_Dmg_Total += A_S3_Dmg_02
        call BS_D_S2_Chk_Can_Evd
        call BS_A_S3_Chk_Kil
        call BS_A_S3_Chk_Mor
        $ D_S2_Dmg_Rcv += (A_S3_Dmg_02) * D_S2_EvdRate
        if D_S2_Dmg_Rcv >= D_S2_HP and D_S2_CanEvd == 0:
            $ D_S2_Dmg_Rcv =  D_S2_HP
        call BS_D_S2_Chk_Kld
        call BS_D_S2_Chk_Mor
        call BS_D_S2_Chg_HP
        call BS_D_S2_Chk_Evd

    if A_S3_Tgt_03 == 1:
        call BS_Update_D_S3_DefChange
        $ A_S3_Dmg_03 = ((A_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S3_CrtRate) - D_S3_DefChg
        if A_S3_Dmg_03 <= 0:
            $ A_S3_Dmg_03 = 1
        $ A_S3_Dmg_Total += A_S3_Dmg_03
        call BS_D_S3_Chk_Can_Evd
        call BS_A_S3_Chk_Kil
        call BS_A_S3_Chk_Mor
        $ D_S3_Dmg_Rcv += (A_S3_Dmg_03) * D_S3_EvdRate
        if D_S3_Dmg_Rcv >= D_S3_HP and D_S3_CanEvd == 0:
            $ D_S3_Dmg_Rcv =  D_S3_HP
        call BS_D_S3_Chk_Kld
        call BS_D_S3_Chk_Mor
        call BS_D_S3_Chg_HP
        call BS_D_S3_Chk_Evd

    if A_S3_Tgt_04 == 1:
        call BS_Update_D_S4_DefChange
        $ A_S3_Dmg_04 = ((A_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S3_CrtRate) - D_S4_DefChg
        if A_S3_Dmg_04 <= 0:
            $ A_S3_Dmg_04 = 1
        $ A_S3_Dmg_Total += A_S3_Dmg_04
        call BS_D_S4_Chk_Can_Evd
        call BS_A_S3_Chk_Kil
        call BS_A_S3_Chk_Mor
        $ D_S4_Dmg_Rcv += (A_S3_Dmg_04) * D_S4_EvdRate
        if D_S4_Dmg_Rcv >= D_S4_HP and D_S4_CanEvd == 0:
            $ D_S4_Dmg_Rcv =  D_S4_HP
        call BS_D_S4_Chk_Kld
        call BS_D_S4_Chk_Mor
        call BS_D_S4_Chg_HP
        call BS_D_S4_Chk_Evd

    if A_S3_Tgt_05 == 1:
        call BS_Update_D_S5_DefChange
        $ A_S3_Dmg_05 = ((A_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S3_CrtRate) - D_S5_DefChg
        if A_S3_Dmg_05 <= 0:
            $ A_S3_Dmg_05 = 1
        $ A_S3_Dmg_Total += A_S3_Dmg_05
        call BS_D_S5_Chk_Can_Evd
        call BS_A_S3_Chk_Kil
        call BS_A_S3_Chk_Mor
        $ D_S5_Dmg_Rcv += (A_S3_Dmg_05) * D_S5_EvdRate
        if D_S5_Dmg_Rcv >= D_S5_HP and D_S5_CanEvd == 0:
            $ D_S5_Dmg_Rcv =  D_S5_HP
        call BS_D_S5_Chk_Kld
        call BS_D_S5_Chk_Mor
        call BS_D_S5_Chg_HP
        call BS_D_S5_Chk_Evd

    if A_S3_Tgt_06 == 1:
        call BS_Update_D_S6_DefChange
        $ A_S3_Dmg_06 = ((A_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S3_CrtRate) - D_S6_DefChg
        if A_S3_Dmg_06 <= 0:
            $ A_S3_Dmg_06 = 1
        $ A_S3_Dmg_Total += A_S3_Dmg_06
        call BS_D_S6_Chk_Can_Evd
        call BS_A_S3_Chk_Kil
        call BS_A_S3_Chk_Mor
        $ D_S6_Dmg_Rcv += (A_S3_Dmg_06) * D_S6_EvdRate
        if D_S6_Dmg_Rcv >= D_S6_HP and D_S6_CanEvd == 0:
            $ D_S6_Dmg_Rcv =  D_S6_HP
        call BS_D_S6_Chk_Kld
        call BS_D_S6_Chk_Mor
        call BS_D_S6_Chg_HP
        call BS_D_S6_Chk_Evd

    return

#///////////////////////  ATTACKER SLOT 4
#==========================================
label BS_A_S4_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_A_S4_Chk_Mor
    $ A_S4_DmgType = "Range"

    call BS_Update_A_S4_AtkChange

    if A_S4_Tgt_01 == 1:
        call BS_Update_D_S1_DefChange
        $ A_S4_Dmg_01 = ((A_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S4_CrtRate) - D_S1_DefChg
        if A_S4_Dmg_01 <= 0:
            $ A_S4_Dmg_01 = 1
        $ A_S4_Dmg_Total += A_S4_Dmg_01
        call BS_D_S1_Chk_Can_Evd
        call BS_A_S4_Chk_Kil
        call BS_A_S4_Chk_Mor
        $ D_S1_Dmg_Rcv += (A_S4_Dmg_01) * D_S1_EvdRate
        if D_S1_Dmg_Rcv >= D_S1_HP and D_S1_CanEvd == 0:
            $ D_S1_Dmg_Rcv =  D_S1_HP
        call BS_D_S1_Chk_Kld
        call BS_D_S1_Chk_Mor
        call BS_D_S1_Chg_HP
        call BS_D_S1_Chk_Evd

    if A_S4_Tgt_02 == 1:
        call BS_Update_D_S2_DefChange
        $ A_S4_Dmg_02 = ((A_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S4_CrtRate) - D_S2_DefChg
        if A_S4_Dmg_02 <= 0:
            $ A_S4_Dmg_02 = 1
        $ A_S4_Dmg_Total += A_S4_Dmg_02
        call BS_D_S2_Chk_Can_Evd
        call BS_A_S4_Chk_Kil
        call BS_A_S4_Chk_Mor
        $ D_S2_Dmg_Rcv += (A_S4_Dmg_02) * D_S2_EvdRate
        if D_S2_Dmg_Rcv >= D_S2_HP and D_S2_CanEvd == 0:
            $ D_S2_Dmg_Rcv =  D_S2_HP
        call BS_D_S2_Chk_Kld
        call BS_D_S2_Chk_Mor
        call BS_D_S2_Chg_HP
        call BS_D_S2_Chk_Evd

    if A_S4_Tgt_03 == 1:
        call BS_Update_D_S3_DefChange
        $ A_S4_Dmg_03 = ((A_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S4_CrtRate) - D_S3_DefChg
        if A_S4_Dmg_03 <= 0:
            $ A_S4_Dmg_03 = 1
        $ A_S4_Dmg_Total += A_S4_Dmg_03
        call BS_D_S3_Chk_Can_Evd
        call BS_A_S4_Chk_Kil
        call BS_A_S4_Chk_Mor
        $ D_S3_Dmg_Rcv += (A_S4_Dmg_03) * D_S3_EvdRate
        if D_S3_Dmg_Rcv >= D_S3_HP and D_S3_CanEvd == 0:
            $ D_S3_Dmg_Rcv =  D_S3_HP
        call BS_D_S3_Chk_Kld
        call BS_D_S3_Chk_Mor
        call BS_D_S3_Chg_HP
        call BS_D_S3_Chk_Evd

    if A_S4_Tgt_04 == 1:
        call BS_Update_D_S4_DefChange
        $ A_S4_Dmg_04 = ((A_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S4_CrtRate) - D_S4_DefChg
        if A_S4_Dmg_04 <= 0:
            $ A_S4_Dmg_04 = 1
        $ A_S4_Dmg_Total += A_S4_Dmg_04
        call BS_D_S4_Chk_Can_Evd
        call BS_A_S4_Chk_Kil
        call BS_A_S4_Chk_Mor
        $ D_S4_Dmg_Rcv += (A_S4_Dmg_04) * D_S4_EvdRate
        if D_S4_Dmg_Rcv >= D_S4_HP and D_S4_CanEvd == 0:
            $ D_S4_Dmg_Rcv =  D_S4_HP
        call BS_D_S4_Chk_Kld
        call BS_D_S4_Chk_Mor
        call BS_D_S4_Chg_HP
        call BS_D_S4_Chk_Evd

    if A_S4_Tgt_05 == 1:
        call BS_Update_D_S5_DefChange
        $ A_S4_Dmg_05 = ((A_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S4_CrtRate) - D_S5_DefChg
        if A_S4_Dmg_05 <= 0:
            $ A_S4_Dmg_05 = 1
        $ A_S4_Dmg_Total += A_S4_Dmg_05
        call BS_D_S5_Chk_Can_Evd
        call BS_A_S4_Chk_Kil
        call BS_A_S4_Chk_Mor
        $ D_S5_Dmg_Rcv += (A_S4_Dmg_05) * D_S5_EvdRate
        if D_S5_Dmg_Rcv >= D_S5_HP and D_S5_CanEvd == 0:
            $ D_S5_Dmg_Rcv =  D_S5_HP
        call BS_D_S5_Chk_Kld
        call BS_D_S5_Chk_Mor
        call BS_D_S5_Chg_HP
        call BS_D_S5_Chk_Evd

    if A_S4_Tgt_06 == 1:
        call BS_Update_D_S6_DefChange
        $ A_S4_Dmg_06 = ((A_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S4_CrtRate) - D_S6_DefChg
        if A_S4_Dmg_06 <= 0:
            $ A_S4_Dmg_06 = 1
        $ A_S4_Dmg_Total += A_S4_Dmg_06
        call BS_D_S6_Chk_Can_Evd
        call BS_A_S4_Chk_Kil
        call BS_A_S4_Chk_Mor
        $ D_S6_Dmg_Rcv += (A_S4_Dmg_06) * D_S6_EvdRate
        if D_S6_Dmg_Rcv >= D_S6_HP and D_S6_CanEvd == 0:
            $ D_S6_Dmg_Rcv =  D_S6_HP
        call BS_D_S6_Chk_Kld
        call BS_D_S6_Chk_Mor
        call BS_D_S6_Chg_HP
        call BS_D_S6_Chk_Evd

    return

#///////////////////////  ATTACKER SLOT 5
#==========================================
label BS_A_S5_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_A_S5_Chk_Mor
    $ A_S5_DmgType = "Range"

    call BS_Update_A_S5_AtkChange

    if A_S5_Tgt_01 == 1:
        call BS_Update_D_S1_DefChange
        $ A_S5_Dmg_01 = ((A_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S5_CrtRate) - D_S1_DefChg
        if A_S5_Dmg_01 <= 0:
            $ A_S5_Dmg_01 = 1
        $ A_S5_Dmg_Total += A_S5_Dmg_01
        call BS_D_S1_Chk_Can_Evd
        call BS_A_S5_Chk_Kil
        call BS_A_S5_Chk_Mor
        $ D_S1_Dmg_Rcv += (A_S5_Dmg_01) * D_S1_EvdRate
        if D_S1_Dmg_Rcv >= D_S1_HP and D_S1_CanEvd == 0:
            $ D_S1_Dmg_Rcv =  D_S1_HP
        call BS_D_S1_Chk_Kld
        call BS_D_S1_Chk_Mor
        call BS_D_S1_Chg_HP
        call BS_D_S1_Chk_Evd

    if A_S5_Tgt_02 == 1:
        call BS_Update_D_S2_DefChange
        $ A_S5_Dmg_02 = ((A_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S5_CrtRate) - D_S2_DefChg
        if A_S5_Dmg_02 <= 0:
            $ A_S5_Dmg_02 = 1
        $ A_S5_Dmg_Total += A_S5_Dmg_02
        call BS_D_S2_Chk_Can_Evd
        call BS_A_S5_Chk_Kil
        call BS_A_S5_Chk_Mor
        $ D_S2_Dmg_Rcv += (A_S5_Dmg_02) * D_S2_EvdRate
        if D_S2_Dmg_Rcv >= D_S2_HP and D_S2_CanEvd == 0:
            $ D_S2_Dmg_Rcv =  D_S2_HP
        call BS_D_S2_Chk_Kld
        call BS_D_S2_Chk_Mor
        call BS_D_S2_Chg_HP
        call BS_D_S2_Chk_Evd

    if A_S5_Tgt_03 == 1:
        call BS_Update_D_S3_DefChange
        $ A_S5_Dmg_03 = ((A_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S5_CrtRate) - D_S3_DefChg
        if A_S5_Dmg_03 <= 0:
            $ A_S5_Dmg_03 = 1
        $ A_S5_Dmg_Total += A_S5_Dmg_03
        call BS_D_S3_Chk_Can_Evd
        call BS_A_S5_Chk_Kil
        call BS_A_S5_Chk_Mor
        $ D_S3_Dmg_Rcv += (A_S5_Dmg_03) * D_S3_EvdRate
        if D_S3_Dmg_Rcv >= D_S3_HP and D_S3_CanEvd == 0:
            $ D_S3_Dmg_Rcv =  D_S3_HP
        call BS_D_S3_Chk_Kld
        call BS_D_S3_Chk_Mor
        call BS_D_S3_Chg_HP
        call BS_D_S3_Chk_Evd

    if A_S5_Tgt_04 == 1:
        call BS_Update_D_S4_DefChange
        $ A_S5_Dmg_04 = ((A_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S5_CrtRate) - D_S4_DefChg
        if A_S5_Dmg_04 <= 0:
            $ A_S5_Dmg_04 = 1
        $ A_S5_Dmg_Total += A_S5_Dmg_04
        call BS_D_S4_Chk_Can_Evd
        call BS_A_S5_Chk_Kil
        call BS_A_S5_Chk_Mor
        $ D_S4_Dmg_Rcv += (A_S5_Dmg_04) * D_S4_EvdRate
        if D_S4_Dmg_Rcv >= D_S4_HP and D_S4_CanEvd == 0:
            $ D_S4_Dmg_Rcv =  D_S4_HP
        call BS_D_S4_Chk_Kld
        call BS_D_S4_Chk_Mor
        call BS_D_S4_Chg_HP
        call BS_D_S4_Chk_Evd

    if A_S5_Tgt_05 == 1:
        call BS_Update_D_S5_DefChange
        $ A_S5_Dmg_05 = ((A_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S5_CrtRate) - D_S5_DefChg
        if A_S5_Dmg_05 <= 0:
            $ A_S5_Dmg_05 = 1
        $ A_S5_Dmg_Total += A_S5_Dmg_05
        call BS_D_S5_Chk_Can_Evd
        call BS_A_S5_Chk_Kil
        call BS_A_S5_Chk_Mor
        $ D_S5_Dmg_Rcv += (A_S5_Dmg_05) * D_S5_EvdRate
        if D_S5_Dmg_Rcv >= D_S5_HP and D_S5_CanEvd == 0:
            $ D_S5_Dmg_Rcv =  D_S5_HP
        call BS_D_S5_Chk_Kld
        call BS_D_S5_Chk_Mor
        call BS_D_S5_Chg_HP
        call BS_D_S5_Chk_Evd

    if A_S5_Tgt_06 == 1:
        call BS_Update_D_S6_DefChange
        $ A_S5_Dmg_06 = ((A_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S5_CrtRate) - D_S6_DefChg
        if A_S5_Dmg_06 <= 0:
            $ A_S5_Dmg_06 = 1
        $ A_S5_Dmg_Total += A_S5_Dmg_06
        call BS_D_S6_Chk_Can_Evd
        call BS_A_S5_Chk_Kil
        call BS_A_S5_Chk_Mor
        $ D_S6_Dmg_Rcv += (A_S5_Dmg_06) * D_S6_EvdRate
        if D_S6_Dmg_Rcv >= D_S6_HP and D_S6_CanEvd == 0:
            $ D_S6_Dmg_Rcv =  D_S6_HP
        call BS_D_S6_Chk_Kld
        call BS_D_S6_Chk_Mor
        call BS_D_S6_Chg_HP
        call BS_D_S6_Chk_Evd

    return

#///////////////////////  ATTACKER SLOT 6
#==========================================
label BS_A_S6_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_A_S6_Chk_Mor
    $ A_S6_DmgType = "Range"

    call BS_Update_A_S6_AtkChange

    if A_S6_Tgt_01 == 1:
        call BS_Update_D_S1_DefChange
        $ A_S6_Dmg_01 = ((A_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S6_CrtRate) - D_S1_DefChg
        if A_S6_Dmg_01 <= 0:
            $ A_S6_Dmg_01 = 1
        $ A_S6_Dmg_Total += A_S6_Dmg_01
        call BS_D_S1_Chk_Can_Evd
        call BS_A_S6_Chk_Kil
        call BS_A_S6_Chk_Mor
        $ D_S1_Dmg_Rcv += (A_S6_Dmg_01) * D_S1_EvdRate
        if D_S1_Dmg_Rcv >= D_S1_HP and D_S1_CanEvd == 0:
            $ D_S1_Dmg_Rcv =  D_S1_HP
        call BS_D_S1_Chk_Kld
        call BS_D_S1_Chk_Mor
        call BS_D_S1_Chg_HP
        call BS_D_S1_Chk_Evd

    if A_S6_Tgt_02 == 1:
        call BS_Update_D_S2_DefChange
        $ A_S6_Dmg_02 = ((A_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S6_CrtRate) - D_S2_DefChg
        if A_S6_Dmg_02 <= 0:
            $ A_S6_Dmg_02 = 1
        $ A_S6_Dmg_Total += A_S6_Dmg_02
        call BS_D_S2_Chk_Can_Evd
        call BS_A_S6_Chk_Kil
        call BS_A_S6_Chk_Mor
        $ D_S2_Dmg_Rcv += (A_S6_Dmg_02) * D_S2_EvdRate
        if D_S2_Dmg_Rcv >= D_S2_HP and D_S2_CanEvd == 0:
            $ D_S2_Dmg_Rcv =  D_S2_HP
        call BS_D_S2_Chk_Kld
        call BS_D_S2_Chk_Mor
        call BS_D_S2_Chg_HP
        call BS_D_S2_Chk_Evd

    if A_S6_Tgt_03 == 1:
        call BS_Update_D_S3_DefChange
        $ A_S6_Dmg_03 = ((A_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S6_CrtRate) - D_S3_DefChg
        if A_S6_Dmg_03 <= 0:
            $ A_S6_Dmg_03 = 1
        $ A_S6_Dmg_Total += A_S6_Dmg_03
        call BS_D_S3_Chk_Can_Evd
        call BS_A_S6_Chk_Kil
        call BS_A_S6_Chk_Mor
        $ D_S3_Dmg_Rcv += (A_S6_Dmg_03) * D_S3_EvdRate
        if D_S3_Dmg_Rcv >= D_S3_HP and D_S3_CanEvd == 0:
            $ D_S3_Dmg_Rcv =  D_S3_HP
        call BS_D_S3_Chk_Kld
        call BS_D_S3_Chk_Mor
        call BS_D_S3_Chg_HP
        call BS_D_S3_Chk_Evd

    if A_S6_Tgt_04 == 1:
        call BS_Update_D_S4_DefChange
        $ A_S6_Dmg_04 = ((A_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S6_CrtRate) - D_S4_DefChg
        if A_S6_Dmg_04 <= 0:
            $ A_S6_Dmg_04 = 1
        $ A_S6_Dmg_Total += A_S6_Dmg_04
        call BS_D_S4_Chk_Can_Evd
        call BS_A_S6_Chk_Kil
        call BS_A_S6_Chk_Mor
        $ D_S4_Dmg_Rcv += (A_S6_Dmg_04) * D_S4_EvdRate
        if D_S4_Dmg_Rcv >= D_S4_HP and D_S4_CanEvd == 0:
            $ D_S4_Dmg_Rcv =  D_S4_HP
        call BS_D_S4_Chk_Kld
        call BS_D_S4_Chk_Mor
        call BS_D_S4_Chg_HP
        call BS_D_S4_Chk_Evd

    if A_S6_Tgt_05 == 1:
        call BS_Update_D_S5_DefChange
        $ A_S6_Dmg_05 = ((A_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S6_CrtRate) - D_S5_DefChg
        if A_S6_Dmg_05 <= 0:
            $ A_S6_Dmg_05 = 1
        $ A_S6_Dmg_Total += A_S6_Dmg_05
        call BS_D_S5_Chk_Can_Evd
        call BS_A_S6_Chk_Kil
        call BS_A_S6_Chk_Mor
        $ D_S5_Dmg_Rcv += (A_S6_Dmg_05) * D_S5_EvdRate
        if D_S5_Dmg_Rcv >= D_S5_HP and D_S5_CanEvd == 0:
            $ D_S5_Dmg_Rcv =  D_S5_HP
        call BS_D_S5_Chk_Kld
        call BS_D_S5_Chk_Mor
        call BS_D_S5_Chg_HP
        call BS_D_S5_Chk_Evd

    if A_S6_Tgt_06 == 1:
        call BS_Update_D_S6_DefChange
        $ A_S6_Dmg_06 = ((A_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * A_S6_CrtRate) - D_S6_DefChg
        if A_S6_Dmg_06 <= 0:
            $ A_S6_Dmg_06 = 1
        $ A_S6_Dmg_Total += A_S6_Dmg_06
        call BS_D_S6_Chk_Can_Evd
        call BS_A_S6_Chk_Kil
        call BS_A_S6_Chk_Mor
        $ D_S6_Dmg_Rcv += (A_S6_Dmg_06) * D_S6_EvdRate
        if D_S6_Dmg_Rcv >= D_S6_HP and D_S6_CanEvd == 0:
            $ D_S6_Dmg_Rcv =  D_S6_HP
        call BS_D_S6_Chk_Kld
        call BS_D_S6_Chk_Mor
        call BS_D_S6_Chg_HP
        call BS_D_S6_Chk_Evd

    return

#================================================================
#================================================================
#================================================================    
#================================================================  
#================================================================
#================================================================
#================================================================    
#================================================================  

#///////////////////////  DEFFENDER SLOT 1
#==========================================
label BS_D_S1_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_D_S1_Chk_Mor
    $ D_S1_DmgType = "Range"

    call BS_Update_D_S1_AtkChange

    if D_S1_Tgt_01 == 1:
        call BS_Update_A_S1_DefChange
        $ D_S1_Dmg_01 = ((D_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S1_CrtRate) - A_S1_DefChg
        if D_S1_Dmg_01 <= 0:
            $ D_S1_Dmg_01 = 1
        $ D_S1_Dmg_Total += D_S1_Dmg_01
        call BS_A_S1_Chk_Can_Evd
        call BS_D_S1_Chk_Kil
        call BS_D_S1_Chk_Mor
        $ A_S1_Dmg_Rcv += (D_S1_Dmg_01) * A_S1_EvdRate
        if A_S1_Dmg_Rcv >= A_S1_HP and A_S1_CanEvd == 0:
            $ A_S1_Dmg_Rcv =  A_S1_HP
        call BS_A_S1_Chk_Kld
        call BS_A_S1_Chk_Mor
        call BS_A_S1_Chg_HP
        call BS_A_S1_Chk_Evd

    if D_S1_Tgt_02 == 1:
        call BS_Update_A_S2_DefChange
        $ D_S1_Dmg_02 = ((D_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S1_CrtRate) - A_S2_DefChg
        if D_S1_Dmg_02 <= 0:
            $ D_S1_Dmg_02 = 1
        $ D_S1_Dmg_Total += D_S1_Dmg_02
        call BS_A_S2_Chk_Can_Evd
        call BS_D_S1_Chk_Kil
        call BS_D_S1_Chk_Mor
        $ A_S2_Dmg_Rcv += (D_S1_Dmg_02) * A_S2_EvdRate
        if A_S2_Dmg_Rcv >= A_S2_HP and A_S2_CanEvd == 0:
            $ A_S2_Dmg_Rcv =  A_S2_HP
        call BS_A_S2_Chk_Kld
        call BS_A_S2_Chk_Mor
        call BS_A_S2_Chg_HP
        call BS_A_S2_Chk_Evd

    if D_S1_Tgt_03 == 1:
        call BS_Update_A_S3_DefChange
        $ D_S1_Dmg_03 = ((D_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S1_CrtRate) - A_S3_DefChg
        if D_S1_Dmg_03 <= 0:
            $ D_S1_Dmg_03 = 1
        $ D_S1_Dmg_Total += D_S1_Dmg_03
        call BS_A_S3_Chk_Can_Evd
        call BS_D_S1_Chk_Kil
        call BS_D_S1_Chk_Mor
        $ A_S3_Dmg_Rcv += (D_S1_Dmg_03) * A_S3_EvdRate
        if A_S3_Dmg_Rcv >= A_S3_HP and A_S3_CanEvd == 0:
            $ A_S3_Dmg_Rcv =  A_S3_HP
        call BS_A_S3_Chk_Kld
        call BS_A_S3_Chk_Mor
        call BS_A_S3_Chg_HP
        call BS_A_S3_Chk_Evd

    if D_S1_Tgt_04 == 1:
        call BS_Update_A_S4_DefChange
        $ D_S1_Dmg_04 = ((D_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S1_CrtRate) - A_S4_DefChg
        if D_S1_Dmg_04 <= 0:
            $ D_S1_Dmg_04 = 1
        $ D_S1_Dmg_Total += D_S1_Dmg_04
        call BS_A_S4_Chk_Can_Evd
        call BS_D_S1_Chk_Kil
        call BS_D_S1_Chk_Mor
        $ A_S4_Dmg_Rcv += (D_S1_Dmg_04) * A_S4_EvdRate
        if A_S4_Dmg_Rcv >= A_S4_HP and A_S4_CanEvd == 0:
            $ A_S4_Dmg_Rcv =  A_S4_HP
        call BS_A_S4_Chk_Kld
        call BS_A_S4_Chk_Mor
        call BS_A_S4_Chg_HP
        call BS_A_S4_Chk_Evd

    if D_S1_Tgt_05 == 1:
        call BS_Update_A_S5_DefChange
        $ D_S1_Dmg_05 = ((D_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S1_CrtRate) - A_S5_DefChg
        if D_S1_Dmg_05 <= 0:
            $ D_S1_Dmg_05 = 1
        $ D_S1_Dmg_Total += D_S1_Dmg_05
        call BS_A_S5_Chk_Can_Evd
        call BS_D_S1_Chk_Kil
        call BS_D_S1_Chk_Mor
        $ A_S5_Dmg_Rcv += (D_S1_Dmg_05) * A_S5_EvdRate
        if A_S5_Dmg_Rcv >= A_S5_HP and A_S5_CanEvd == 0:
            $ A_S5_Dmg_Rcv =  A_S5_HP
        call BS_A_S5_Chk_Kld
        call BS_A_S5_Chk_Mor
        call BS_A_S5_Chg_HP
        call BS_A_S5_Chk_Evd

    if D_S1_Tgt_06 == 1:
        call BS_Update_A_S6_DefChange
        $ D_S1_Dmg_06 = ((D_S1_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S1_CrtRate) - A_S6_DefChg
        if D_S1_Dmg_06 <= 0:
            $ D_S1_Dmg_06 = 1
        $ D_S1_Dmg_Total += D_S1_Dmg_06
        call BS_A_S6_Chk_Can_Evd
        call BS_D_S1_Chk_Kil
        call BS_D_S1_Chk_Mor
        $ A_S6_Dmg_Rcv += (D_S1_Dmg_06) * A_S6_EvdRate
        if A_S6_Dmg_Rcv >= A_S6_HP and A_S6_CanEvd == 0:
            $ A_S6_Dmg_Rcv =  A_S6_HP
        call BS_A_S6_Chk_Kld
        call BS_A_S6_Chk_Mor
        call BS_A_S6_Chg_HP
        call BS_A_S6_Chk_Evd

    return

#///////////////////////  DEFFENDER SLOT 2
#==========================================
label BS_D_S2_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_D_S2_Chk_Mor
    $ D_S2_DmgType = "Range"

    call BS_Update_D_S2_AtkChange

    if D_S2_Tgt_01 == 1:
        call BS_Update_A_S1_DefChange
        $ D_S2_Dmg_01 = ((D_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S2_CrtRate) - A_S1_DefChg
        if D_S2_Dmg_01 <= 0:
            $ D_S2_Dmg_01 = 1
        $ D_S2_Dmg_Total += D_S2_Dmg_01
        call BS_A_S1_Chk_Can_Evd
        call BS_D_S2_Chk_Kil
        call BS_D_S2_Chk_Mor
        $ A_S1_Dmg_Rcv += (D_S2_Dmg_01) * A_S1_EvdRate
        if A_S1_Dmg_Rcv >= A_S1_HP and A_S1_CanEvd == 0:
            $ A_S1_Dmg_Rcv =  A_S1_HP
        call BS_A_S1_Chk_Kld
        call BS_A_S1_Chk_Mor
        call BS_A_S1_Chg_HP
        call BS_A_S1_Chk_Evd

    if D_S2_Tgt_02 == 1:
        call BS_Update_A_S2_DefChange
        $ D_S2_Dmg_02 = ((D_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S2_CrtRate) - A_S2_DefChg
        if D_S2_Dmg_02 <= 0:
            $ D_S2_Dmg_02 = 1
        $ D_S2_Dmg_Total += D_S2_Dmg_02
        call BS_A_S2_Chk_Can_Evd
        call BS_D_S2_Chk_Kil
        call BS_D_S2_Chk_Mor
        $ A_S2_Dmg_Rcv += (D_S2_Dmg_02) * A_S2_EvdRate
        if A_S2_Dmg_Rcv >= A_S2_HP and A_S2_CanEvd == 0:
            $ A_S2_Dmg_Rcv =  A_S2_HP
        call BS_A_S2_Chk_Kld
        call BS_A_S2_Chk_Mor
        call BS_A_S2_Chg_HP
        call BS_A_S2_Chk_Evd

    if D_S2_Tgt_03 == 1:
        call BS_Update_A_S3_DefChange
        $ D_S2_Dmg_03 = ((D_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S2_CrtRate) - A_S3_DefChg
        if D_S2_Dmg_03 <= 0:
            $ D_S2_Dmg_03 = 1
        $ D_S2_Dmg_Total += D_S2_Dmg_03
        call BS_A_S3_Chk_Can_Evd
        call BS_D_S2_Chk_Kil
        call BS_D_S2_Chk_Mor
        $ A_S3_Dmg_Rcv += (D_S2_Dmg_03) * A_S3_EvdRate
        if A_S3_Dmg_Rcv >= A_S3_HP and A_S3_CanEvd == 0:
            $ A_S3_Dmg_Rcv =  A_S3_HP
        call BS_A_S3_Chk_Kld
        call BS_A_S3_Chk_Mor
        call BS_A_S3_Chg_HP
        call BS_A_S3_Chk_Evd

    if D_S2_Tgt_04 == 1:
        call BS_Update_A_S4_DefChange
        $ D_S2_Dmg_04 = ((D_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S2_CrtRate) - A_S4_DefChg
        if D_S2_Dmg_04 <= 0:
            $ D_S2_Dmg_04 = 1
        $ D_S2_Dmg_Total += D_S2_Dmg_04
        call BS_A_S4_Chk_Can_Evd
        call BS_D_S2_Chk_Kil
        call BS_D_S2_Chk_Mor
        $ A_S4_Dmg_Rcv += (D_S2_Dmg_04) * A_S4_EvdRate
        if A_S4_Dmg_Rcv >= A_S4_HP and A_S4_CanEvd == 0:
            $ A_S4_Dmg_Rcv =  A_S4_HP
        call BS_A_S4_Chk_Kld
        call BS_A_S4_Chk_Mor
        call BS_A_S4_Chg_HP
        call BS_A_S4_Chk_Evd

    if D_S2_Tgt_05 == 1:
        call BS_Update_A_S5_DefChange
        $ D_S2_Dmg_05 = ((D_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S2_CrtRate) - A_S5_DefChg
        if D_S2_Dmg_05 <= 0:
            $ D_S2_Dmg_05 = 1
        $ D_S2_Dmg_Total += D_S2_Dmg_05
        call BS_A_S5_Chk_Can_Evd
        call BS_D_S2_Chk_Kil
        call BS_D_S2_Chk_Mor
        $ A_S5_Dmg_Rcv += (D_S2_Dmg_05) * A_S5_EvdRate
        if A_S5_Dmg_Rcv >= A_S5_HP and A_S5_CanEvd == 0:
            $ A_S5_Dmg_Rcv =  A_S5_HP
        call BS_A_S5_Chk_Kld
        call BS_A_S5_Chk_Mor
        call BS_A_S5_Chg_HP
        call BS_A_S5_Chk_Evd

    if D_S2_Tgt_06 == 1:
        call BS_Update_A_S6_DefChange
        $ D_S2_Dmg_06 = ((D_S2_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S2_CrtRate) - A_S6_DefChg
        if D_S2_Dmg_06 <= 0:
            $ D_S2_Dmg_06 = 1
        $ D_S2_Dmg_Total += D_S2_Dmg_06
        call BS_A_S6_Chk_Can_Evd
        call BS_D_S2_Chk_Kil
        call BS_D_S2_Chk_Mor
        $ A_S6_Dmg_Rcv += (D_S2_Dmg_06) * A_S6_EvdRate
        if A_S6_Dmg_Rcv >= A_S6_HP and A_S6_CanEvd == 0:
            $ A_S6_Dmg_Rcv =  A_S6_HP
        call BS_A_S6_Chk_Kld
        call BS_A_S6_Chk_Mor
        call BS_A_S6_Chg_HP
        call BS_A_S6_Chk_Evd

    return

#///////////////////////  DEFFENDER SLOT 3
#==========================================
label BS_D_S3_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_D_S3_Chk_Mor
    $ D_S3_DmgType = "Range"

    call BS_Update_D_S3_AtkChange

    if D_S3_Tgt_01 == 1:
        call BS_Update_A_S1_DefChange
        $ D_S3_Dmg_01 = ((D_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S3_CrtRate) - A_S1_DefChg
        if D_S3_Dmg_01 <= 0:
            $ D_S3_Dmg_01 = 1
        $ D_S3_Dmg_Total += D_S3_Dmg_01
        call BS_A_S1_Chk_Can_Evd
        call BS_D_S3_Chk_Kil
        call BS_D_S3_Chk_Mor
        $ A_S1_Dmg_Rcv += (D_S3_Dmg_01) * A_S1_EvdRate
        if A_S1_Dmg_Rcv >= A_S1_HP and A_S1_CanEvd == 0:
            $ A_S1_Dmg_Rcv =  A_S1_HP
        call BS_A_S1_Chk_Kld
        call BS_A_S1_Chk_Mor
        call BS_A_S1_Chg_HP
        call BS_A_S1_Chk_Evd

    if D_S3_Tgt_02 == 1:
        call BS_Update_A_S2_DefChange
        $ D_S3_Dmg_02 = ((D_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S3_CrtRate) - A_S2_DefChg
        if D_S3_Dmg_02 <= 0:
            $ D_S3_Dmg_02 = 1
        $ D_S3_Dmg_Total += D_S3_Dmg_02
        call BS_A_S2_Chk_Can_Evd
        call BS_D_S3_Chk_Kil
        call BS_D_S3_Chk_Mor
        $ A_S2_Dmg_Rcv += (D_S3_Dmg_02) * A_S2_EvdRate
        if A_S2_Dmg_Rcv >= A_S2_HP and A_S2_CanEvd == 0:
            $ A_S2_Dmg_Rcv =  A_S2_HP
        call BS_A_S2_Chk_Kld
        call BS_A_S2_Chk_Mor
        call BS_A_S2_Chg_HP
        call BS_A_S2_Chk_Evd

    if D_S3_Tgt_03 == 1:
        call BS_Update_A_S3_DefChange
        $ D_S3_Dmg_03 = ((D_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S3_CrtRate) - A_S3_DefChg
        if D_S3_Dmg_03 <= 0:
            $ D_S3_Dmg_03 = 1
        $ D_S3_Dmg_Total += D_S3_Dmg_03
        call BS_A_S3_Chk_Can_Evd
        call BS_D_S3_Chk_Kil
        call BS_D_S3_Chk_Mor
        $ A_S3_Dmg_Rcv += (D_S3_Dmg_03) * A_S3_EvdRate
        if A_S3_Dmg_Rcv >= A_S3_HP and A_S3_CanEvd == 0:
            $ A_S3_Dmg_Rcv =  A_S3_HP
        call BS_A_S3_Chk_Kld
        call BS_A_S3_Chk_Mor
        call BS_A_S3_Chg_HP
        call BS_A_S3_Chk_Evd

    if D_S3_Tgt_04 == 1:
        call BS_Update_A_S4_DefChange
        $ D_S3_Dmg_04 = ((D_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S3_CrtRate) - A_S4_DefChg
        if D_S3_Dmg_04 <= 0:
            $ D_S3_Dmg_04 = 1
        $ D_S3_Dmg_Total += D_S3_Dmg_04
        call BS_A_S4_Chk_Can_Evd
        call BS_D_S3_Chk_Kil
        call BS_D_S3_Chk_Mor
        $ A_S4_Dmg_Rcv += (D_S3_Dmg_04) * A_S4_EvdRate
        if A_S4_Dmg_Rcv >= A_S4_HP and A_S4_CanEvd == 0:
            $ A_S4_Dmg_Rcv =  A_S4_HP
        call BS_A_S4_Chk_Kld
        call BS_A_S4_Chk_Mor
        call BS_A_S4_Chg_HP
        call BS_A_S4_Chk_Evd

    if D_S3_Tgt_05 == 1:
        call BS_Update_A_S5_DefChange
        $ D_S3_Dmg_05 = ((D_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S3_CrtRate) - A_S5_DefChg
        if D_S3_Dmg_05 <= 0:
            $ D_S3_Dmg_05 = 1
        $ D_S3_Dmg_Total += D_S3_Dmg_05
        call BS_A_S5_Chk_Can_Evd
        call BS_D_S3_Chk_Kil
        call BS_D_S3_Chk_Mor
        $ A_S5_Dmg_Rcv += (D_S3_Dmg_05) * A_S5_EvdRate
        if A_S5_Dmg_Rcv >= A_S5_HP and A_S5_CanEvd == 0:
            $ A_S5_Dmg_Rcv =  A_S5_HP
        call BS_A_S5_Chk_Kld
        call BS_A_S5_Chk_Mor
        call BS_A_S5_Chg_HP
        call BS_A_S5_Chk_Evd

    if D_S3_Tgt_06 == 1:
        call BS_Update_A_S6_DefChange
        $ D_S3_Dmg_06 = ((D_S3_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S3_CrtRate) - A_S6_DefChg
        if D_S3_Dmg_06 <= 0:
            $ D_S3_Dmg_06 = 1
        $ D_S3_Dmg_Total += D_S3_Dmg_06
        call BS_A_S6_Chk_Can_Evd
        call BS_D_S3_Chk_Kil
        call BS_D_S3_Chk_Mor
        $ A_S6_Dmg_Rcv += (D_S3_Dmg_06) * A_S6_EvdRate
        if A_S6_Dmg_Rcv >= A_S6_HP and A_S6_CanEvd == 0:
            $ A_S6_Dmg_Rcv =  A_S6_HP
        call BS_A_S6_Chk_Kld
        call BS_A_S6_Chk_Mor
        call BS_A_S6_Chg_HP
        call BS_A_S6_Chk_Evd

    return

#///////////////////////  DEFFENDER SLOT 4
#==========================================
label BS_D_S4_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_D_S4_Chk_Mor
    $ D_S4_DmgType = "Range"

    call BS_Update_D_S4_AtkChange

    if D_S4_Tgt_01 == 1:
        call BS_Update_A_S1_DefChange
        $ D_S4_Dmg_01 = ((D_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S4_CrtRate) - A_S1_DefChg
        if D_S4_Dmg_01 <= 0:
            $ D_S4_Dmg_01 = 1
        $ D_S4_Dmg_Total += D_S4_Dmg_01
        call BS_A_S1_Chk_Can_Evd
        call BS_D_S4_Chk_Kil
        call BS_D_S4_Chk_Mor
        $ A_S1_Dmg_Rcv += (D_S4_Dmg_01) * A_S1_EvdRate
        if A_S1_Dmg_Rcv >= A_S1_HP and A_S1_CanEvd == 0:
            $ A_S1_Dmg_Rcv =  A_S1_HP
        call BS_A_S1_Chk_Kld
        call BS_A_S1_Chk_Mor
        call BS_A_S1_Chg_HP
        call BS_A_S1_Chk_Evd

    if D_S4_Tgt_02 == 1:
        call BS_Update_A_S2_DefChange
        $ D_S4_Dmg_02 = ((D_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S4_CrtRate) - A_S2_DefChg
        if D_S4_Dmg_02 <= 0:
            $ D_S4_Dmg_02 = 1
        $ D_S4_Dmg_Total += D_S4_Dmg_02
        call BS_A_S2_Chk_Can_Evd
        call BS_D_S4_Chk_Kil
        call BS_D_S4_Chk_Mor
        $ A_S2_Dmg_Rcv += (D_S4_Dmg_02) * A_S2_EvdRate
        if A_S2_Dmg_Rcv >= A_S2_HP and A_S2_CanEvd == 0:
            $ A_S2_Dmg_Rcv =  A_S2_HP
        call BS_A_S2_Chk_Kld
        call BS_A_S2_Chk_Mor
        call BS_A_S2_Chg_HP
        call BS_A_S2_Chk_Evd

    if D_S4_Tgt_03 == 1:
        call BS_Update_A_S3_DefChange
        $ D_S4_Dmg_03 = ((D_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S4_CrtRate) - A_S3_DefChg
        if D_S4_Dmg_03 <= 0:
            $ D_S4_Dmg_03 = 1
        $ D_S4_Dmg_Total += D_S4_Dmg_03
        call BS_A_S3_Chk_Can_Evd
        call BS_D_S4_Chk_Kil
        call BS_D_S4_Chk_Mor
        $ A_S3_Dmg_Rcv += (D_S4_Dmg_03) * A_S3_EvdRate
        if A_S3_Dmg_Rcv >= A_S3_HP and A_S3_CanEvd == 0:
            $ A_S3_Dmg_Rcv =  A_S3_HP
        call BS_A_S3_Chk_Kld
        call BS_A_S3_Chk_Mor
        call BS_A_S3_Chg_HP
        call BS_A_S3_Chk_Evd

    if D_S4_Tgt_04 == 1:
        call BS_Update_A_S4_DefChange
        $ D_S4_Dmg_04 = ((D_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S4_CrtRate) - A_S4_DefChg
        if D_S4_Dmg_04 <= 0:
            $ D_S4_Dmg_04 = 1
        $ D_S4_Dmg_Total += D_S4_Dmg_04
        call BS_A_S4_Chk_Can_Evd
        call BS_D_S4_Chk_Kil
        call BS_D_S4_Chk_Mor
        $ A_S4_Dmg_Rcv += (D_S4_Dmg_04) * A_S4_EvdRate
        if A_S4_Dmg_Rcv >= A_S4_HP and A_S4_CanEvd == 0:
            $ A_S4_Dmg_Rcv =  A_S4_HP
        call BS_A_S4_Chk_Kld
        call BS_A_S4_Chk_Mor
        call BS_A_S4_Chg_HP
        call BS_A_S4_Chk_Evd

    if D_S4_Tgt_05 == 1:
        call BS_Update_A_S5_DefChange
        $ D_S4_Dmg_05 = ((D_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S4_CrtRate) - A_S5_DefChg
        if D_S4_Dmg_05 <= 0:
            $ D_S4_Dmg_05 = 1
        $ D_S4_Dmg_Total += D_S4_Dmg_05
        call BS_A_S5_Chk_Can_Evd
        call BS_D_S4_Chk_Kil
        call BS_D_S4_Chk_Mor
        $ A_S5_Dmg_Rcv += (D_S4_Dmg_05) * A_S5_EvdRate
        if A_S5_Dmg_Rcv >= A_S5_HP and A_S5_CanEvd == 0:
            $ A_S5_Dmg_Rcv =  A_S5_HP
        call BS_A_S5_Chk_Kld
        call BS_A_S5_Chk_Mor
        call BS_A_S5_Chg_HP
        call BS_A_S5_Chk_Evd

    if D_S4_Tgt_06 == 1:
        call BS_Update_A_S6_DefChange
        $ D_S4_Dmg_06 = ((D_S4_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S4_CrtRate) - A_S6_DefChg
        if D_S4_Dmg_06 <= 0:
            $ D_S4_Dmg_06 = 1
        $ D_S4_Dmg_Total += D_S4_Dmg_06
        call BS_A_S6_Chk_Can_Evd
        call BS_D_S4_Chk_Kil
        call BS_D_S4_Chk_Mor
        $ A_S6_Dmg_Rcv += (D_S4_Dmg_06) * A_S6_EvdRate
        if A_S6_Dmg_Rcv >= A_S6_HP and A_S6_CanEvd == 0:
            $ A_S6_Dmg_Rcv =  A_S6_HP
        call BS_A_S6_Chk_Kld
        call BS_A_S6_Chk_Mor
        call BS_A_S6_Chg_HP
        call BS_A_S6_Chk_Evd

    return

#///////////////////////  DEFFENDER SLOT 5
#==========================================
label BS_D_S5_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_D_S5_Chk_Mor
    $ D_S5_DmgType = "Range"

    call BS_Update_D_S5_AtkChange

    if D_S5_Tgt_01 == 1:
        call BS_Update_A_S1_DefChange
        $ D_S5_Dmg_01 = ((D_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S5_CrtRate) - A_S1_DefChg
        if D_S5_Dmg_01 <= 0:
            $ D_S5_Dmg_01 = 1
        $ D_S5_Dmg_Total += D_S5_Dmg_01
        call BS_A_S1_Chk_Can_Evd
        call BS_D_S5_Chk_Kil
        call BS_D_S5_Chk_Mor
        $ A_S1_Dmg_Rcv += (D_S5_Dmg_01) * A_S1_EvdRate
        if A_S1_Dmg_Rcv >= A_S1_HP and A_S1_CanEvd == 0:
            $ A_S1_Dmg_Rcv =  A_S1_HP
        call BS_A_S1_Chk_Kld
        call BS_A_S1_Chk_Mor
        call BS_A_S1_Chg_HP
        call BS_A_S1_Chk_Evd

    if D_S5_Tgt_02 == 1:
        call BS_Update_A_S2_DefChange
        $ D_S5_Dmg_02 = ((D_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S5_CrtRate) - A_S2_DefChg
        if D_S5_Dmg_02 <= 0:
            $ D_S5_Dmg_02 = 1
        $ D_S5_Dmg_Total += D_S5_Dmg_02
        call BS_A_S2_Chk_Can_Evd
        call BS_D_S5_Chk_Kil
        call BS_D_S5_Chk_Mor
        $ A_S2_Dmg_Rcv += (D_S5_Dmg_02) * A_S2_EvdRate
        if A_S2_Dmg_Rcv >= A_S2_HP and A_S2_CanEvd == 0:
            $ A_S2_Dmg_Rcv =  A_S2_HP
        call BS_A_S2_Chk_Kld
        call BS_A_S2_Chk_Mor
        call BS_A_S2_Chg_HP
        call BS_A_S2_Chk_Evd

    if D_S5_Tgt_03 == 1:
        call BS_Update_A_S3_DefChange
        $ D_S5_Dmg_03 = ((D_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S5_CrtRate) - A_S3_DefChg
        if D_S5_Dmg_03 <= 0:
            $ D_S5_Dmg_03 = 1
        $ D_S5_Dmg_Total += D_S5_Dmg_03
        call BS_A_S3_Chk_Can_Evd
        call BS_D_S5_Chk_Kil
        call BS_D_S5_Chk_Mor
        $ A_S3_Dmg_Rcv += (D_S5_Dmg_03) * A_S3_EvdRate
        if A_S3_Dmg_Rcv >= A_S3_HP and A_S3_CanEvd == 0:
            $ A_S3_Dmg_Rcv =  A_S3_HP
        call BS_A_S3_Chk_Kld
        call BS_A_S3_Chk_Mor
        call BS_A_S3_Chg_HP
        call BS_A_S3_Chk_Evd

    if D_S5_Tgt_04 == 1:
        call BS_Update_A_S4_DefChange
        $ D_S5_Dmg_04 = ((D_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S5_CrtRate) - A_S4_DefChg
        if D_S5_Dmg_04 <= 0:
            $ D_S5_Dmg_04 = 1
        $ D_S5_Dmg_Total += D_S5_Dmg_04
        call BS_A_S4_Chk_Can_Evd
        call BS_D_S5_Chk_Kil
        call BS_D_S5_Chk_Mor
        $ A_S4_Dmg_Rcv += (D_S5_Dmg_04) * A_S4_EvdRate
        if A_S4_Dmg_Rcv >= A_S4_HP and A_S4_CanEvd == 0:
            $ A_S4_Dmg_Rcv =  A_S4_HP
        call BS_A_S4_Chk_Kld
        call BS_A_S4_Chk_Mor
        call BS_A_S4_Chg_HP
        call BS_A_S4_Chk_Evd

    if D_S5_Tgt_05 == 1:
        call BS_Update_A_S5_DefChange
        $ D_S5_Dmg_05 = ((D_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S5_CrtRate) - A_S5_DefChg
        if D_S5_Dmg_05 <= 0:
            $ D_S5_Dmg_05 = 1
        $ D_S5_Dmg_Total += D_S5_Dmg_05
        call BS_A_S5_Chk_Can_Evd
        call BS_D_S5_Chk_Kil
        call BS_D_S5_Chk_Mor
        $ A_S5_Dmg_Rcv += (D_S5_Dmg_05) * A_S5_EvdRate
        if A_S5_Dmg_Rcv >= A_S5_HP and A_S5_CanEvd == 0:
            $ A_S5_Dmg_Rcv =  A_S5_HP
        call BS_A_S5_Chk_Kld
        call BS_A_S5_Chk_Mor
        call BS_A_S5_Chg_HP
        call BS_A_S5_Chk_Evd

    if D_S5_Tgt_06 == 1:
        call BS_Update_A_S6_DefChange
        $ D_S5_Dmg_06 = ((D_S5_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S5_CrtRate) - A_S6_DefChg
        if D_S5_Dmg_06 <= 0:
            $ D_S5_Dmg_06 = 1
        $ D_S5_Dmg_Total += D_S5_Dmg_06
        call BS_A_S6_Chk_Can_Evd
        call BS_D_S5_Chk_Kil
        call BS_D_S5_Chk_Mor
        $ A_S6_Dmg_Rcv += (D_S5_Dmg_06) * A_S6_EvdRate
        if A_S6_Dmg_Rcv >= A_S6_HP and A_S6_CanEvd == 0:
            $ A_S6_Dmg_Rcv =  A_S6_HP
        call BS_A_S6_Chk_Kld
        call BS_A_S6_Chk_Mor
        call BS_A_S6_Chg_HP
        call BS_A_S6_Chk_Evd

    return

#///////////////////////  DEFFENDER SLOT 6
#==========================================
label BS_D_S6_Chk_Cls003_Ttc02_Dmg:
#==========================================
    call BS_D_S6_Chk_Mor
    $ D_S6_DmgType = "Range"

    call BS_Update_D_S6_AtkChange

    if D_S6_Tgt_01 == 1:
        call BS_Update_A_S1_DefChange
        $ D_S6_Dmg_01 = ((D_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S6_CrtRate) - A_S1_DefChg
        if D_S6_Dmg_01 <= 0:
            $ D_S6_Dmg_01 = 1
        $ D_S6_Dmg_Total += D_S6_Dmg_01
        call BS_A_S1_Chk_Can_Evd
        call BS_D_S6_Chk_Kil
        call BS_D_S6_Chk_Mor
        $ A_S1_Dmg_Rcv += (D_S6_Dmg_01) * A_S1_EvdRate
        if A_S1_Dmg_Rcv >= A_S1_HP and A_S1_CanEvd == 0:
            $ A_S1_Dmg_Rcv =  A_S1_HP
        call BS_A_S1_Chk_Kld
        call BS_A_S1_Chk_Mor
        call BS_A_S1_Chg_HP
        call BS_A_S1_Chk_Evd

    if D_S6_Tgt_02 == 1:
        call BS_Update_A_S2_DefChange
        $ D_S6_Dmg_02 = ((D_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S6_CrtRate) - A_S2_DefChg
        if D_S6_Dmg_02 <= 0:
            $ D_S6_Dmg_02 = 1
        $ D_S6_Dmg_Total += D_S6_Dmg_02
        call BS_A_S2_Chk_Can_Evd
        call BS_D_S6_Chk_Kil
        call BS_D_S6_Chk_Mor
        $ A_S2_Dmg_Rcv += (D_S6_Dmg_02) * A_S2_EvdRate
        if A_S2_Dmg_Rcv >= A_S2_HP and A_S2_CanEvd == 0:
            $ A_S2_Dmg_Rcv =  A_S2_HP
        call BS_A_S2_Chk_Kld
        call BS_A_S2_Chk_Mor
        call BS_A_S2_Chg_HP
        call BS_A_S2_Chk_Evd

    if D_S6_Tgt_03 == 1:
        call BS_Update_A_S3_DefChange
        $ D_S6_Dmg_03 = ((D_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S6_CrtRate) - A_S3_DefChg
        if D_S6_Dmg_03 <= 0:
            $ D_S6_Dmg_03 = 1
        $ D_S6_Dmg_Total += D_S6_Dmg_03
        call BS_A_S3_Chk_Can_Evd
        call BS_D_S6_Chk_Kil
        call BS_D_S6_Chk_Mor
        $ A_S3_Dmg_Rcv += (D_S6_Dmg_03) * A_S3_EvdRate
        if A_S3_Dmg_Rcv >= A_S3_HP and A_S3_CanEvd == 0:
            $ A_S3_Dmg_Rcv =  A_S3_HP
        call BS_A_S3_Chk_Kld
        call BS_A_S3_Chk_Mor
        call BS_A_S3_Chg_HP
        call BS_A_S3_Chk_Evd

    if D_S6_Tgt_04 == 1:
        call BS_Update_A_S4_DefChange
        $ D_S6_Dmg_04 = ((D_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S6_CrtRate) - A_S4_DefChg
        if D_S6_Dmg_04 <= 0:
            $ D_S6_Dmg_04 = 1
        $ D_S6_Dmg_Total += D_S6_Dmg_04
        call BS_A_S4_Chk_Can_Evd
        call BS_D_S6_Chk_Kil
        call BS_D_S6_Chk_Mor
        $ A_S4_Dmg_Rcv += (D_S6_Dmg_04) * A_S4_EvdRate
        if A_S4_Dmg_Rcv >= A_S4_HP and A_S4_CanEvd == 0:
            $ A_S4_Dmg_Rcv =  A_S4_HP
        call BS_A_S4_Chk_Kld
        call BS_A_S4_Chk_Mor
        call BS_A_S4_Chg_HP
        call BS_A_S4_Chk_Evd

    if D_S6_Tgt_05 == 1:
        call BS_Update_A_S5_DefChange
        $ D_S6_Dmg_05 = ((D_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S6_CrtRate) - A_S5_DefChg
        if D_S6_Dmg_05 <= 0:
            $ D_S6_Dmg_05 = 1
        $ D_S6_Dmg_Total += D_S6_Dmg_05
        call BS_A_S5_Chk_Can_Evd
        call BS_D_S6_Chk_Kil
        call BS_D_S6_Chk_Mor
        $ A_S5_Dmg_Rcv += (D_S6_Dmg_05) * A_S5_EvdRate
        if A_S5_Dmg_Rcv >= A_S5_HP and A_S5_CanEvd == 0:
            $ A_S5_Dmg_Rcv =  A_S5_HP
        call BS_A_S5_Chk_Kld
        call BS_A_S5_Chk_Mor
        call BS_A_S5_Chg_HP
        call BS_A_S5_Chk_Evd

    if D_S6_Tgt_06 == 1:
        call BS_Update_A_S6_DefChange
        $ D_S6_Dmg_06 = ((D_S6_AtkChg * Cls003_Ttc02_DmgRate/100) * D_S6_CrtRate) - A_S6_DefChg
        if D_S6_Dmg_06 <= 0:
            $ D_S6_Dmg_06 = 1
        $ D_S6_Dmg_Total += D_S6_Dmg_06
        call BS_A_S6_Chk_Can_Evd
        call BS_D_S6_Chk_Kil
        call BS_D_S6_Chk_Mor
        $ A_S6_Dmg_Rcv += (D_S6_Dmg_06) * A_S6_EvdRate
        if A_S6_Dmg_Rcv >= A_S6_HP and A_S6_CanEvd == 0:
            $ A_S6_Dmg_Rcv =  A_S6_HP
        call BS_A_S6_Chk_Kld
        call BS_A_S6_Chk_Mor
        call BS_A_S6_Chg_HP
        call BS_A_S6_Chk_Evd

    return