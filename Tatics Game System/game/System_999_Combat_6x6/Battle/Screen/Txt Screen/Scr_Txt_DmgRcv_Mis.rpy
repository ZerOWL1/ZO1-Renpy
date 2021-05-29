screen Scr_DmgRcv:

#///////////////////////  ATTACKER SLOT 1

    if A_S1_Dmg_Rcv <= 0 and A_S1_CanEvd >= 1:
        text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at A_S1_Eft_Txt_Mis
    elif A_S1_Dmg_Rcv >= 1 and BS_D_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[A_S1_Dmg_Rcv]{/color}{/size}{/b}" at A_S1_Eft_Txt_CritDmg
    elif A_S1_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[A_S1_Dmg_Rcv]{/color}{/size}{/b}" at A_S1_Eft_Txt_Dmg

#///////////////////////  ATTACKER SLOT 2

    if A_S2_Dmg_Rcv <= 0 and A_S2_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at A_S2_Eft_Txt_Mis
    elif A_S2_Dmg_Rcv >= 1 and BS_D_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[A_S2_Dmg_Rcv]{/color}{/size}{/b}" at A_S2_Eft_Txt_CritDmg
    elif A_S2_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[A_S2_Dmg_Rcv]{/color}{/size}{/b}" at A_S2_Eft_Txt_Dmg

#///////////////////////  ATTACKER SLOT 3

    if A_S3_Dmg_Rcv <= 0 and A_S3_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at A_S3_Eft_Txt_Mis
    elif A_S3_Dmg_Rcv >= 1 and BS_D_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[A_S3_Dmg_Rcv]{/color}{/size}{/b}" at A_S3_Eft_Txt_CritDmg
    elif A_S3_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[A_S3_Dmg_Rcv]{/color}{/size}{/b}" at A_S3_Eft_Txt_Dmg

#///////////////////////  ATTACKER SLOT 4

    if A_S4_Dmg_Rcv <= 0 and A_S4_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at A_S4_Eft_Txt_Mis
    elif A_S4_Dmg_Rcv >= 1 and BS_D_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[A_S4_Dmg_Rcv]{/color}{/size}{/b}" at A_S4_Eft_Txt_CritDmg
    elif A_S4_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[A_S4_Dmg_Rcv]{/color}{/size}{/b}" at A_S4_Eft_Txt_Dmg

#///////////////////////  ATTACKER SLOT 5

    if A_S5_Dmg_Rcv <= 0 and A_S5_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at A_S5_Eft_Txt_Mis
    elif A_S5_Dmg_Rcv >= 1 and BS_D_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[A_S5_Dmg_Rcv]{/color}{/size}{/b}" at A_S5_Eft_Txt_CritDmg
    elif A_S5_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[A_S5_Dmg_Rcv]{/color}{/size}{/b}" at A_S5_Eft_Txt_Dmg

#///////////////////////  ATTACKER SLOT 6

    if A_S6_Dmg_Rcv <= 0 and A_S6_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at A_S6_Eft_Txt_Mis
    elif A_S6_Dmg_Rcv >= 1 and BS_D_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[A_S6_Dmg_Rcv]{/color}{/size}{/b}" at A_S6_Eft_Txt_CritDmg
    elif A_S6_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[A_S6_Dmg_Rcv]{/color}{/size}{/b}" at A_S6_Eft_Txt_Dmg

        
        
        

        


#///////////////////////  DEFFENDER SLOT 1

    if D_S1_Dmg_Rcv <= 0 and D_S1_CanEvd >= 1:
        text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at D_S1_Eft_Txt_Mis
    elif D_S1_Dmg_Rcv >= 1 and BS_A_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[D_S1_Dmg_Rcv]{/color}{/size}{/b}" at D_S1_Eft_Txt_CritDmg
    elif D_S1_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[D_S1_Dmg_Rcv]{/color}{/size}{/b}" at D_S1_Eft_Txt_Dmg

#///////////////////////  DEFFENDER SLOT 2

    if D_S2_Dmg_Rcv <= 0 and D_S2_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at D_S2_Eft_Txt_Mis
    elif D_S2_Dmg_Rcv >= 1 and BS_A_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[D_S2_Dmg_Rcv]{/color}{/size}{/b}" at D_S2_Eft_Txt_CritDmg
    elif D_S2_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[D_S2_Dmg_Rcv]{/color}{/size}{/b}" at D_S2_Eft_Txt_Dmg

#///////////////////////  DEFFENDER SLOT 3

    if D_S3_Dmg_Rcv <= 0 and D_S3_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at D_S3_Eft_Txt_Mis
    elif D_S3_Dmg_Rcv >= 1 and BS_A_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[D_S3_Dmg_Rcv]{/color}{/size}{/b}" at D_S3_Eft_Txt_CritDmg
    elif D_S3_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[D_S3_Dmg_Rcv]{/color}{/size}{/b}" at D_S3_Eft_Txt_Dmg

#///////////////////////  DEFFENDER SLOT 4

    if D_S4_Dmg_Rcv <= 0 and D_S4_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at D_S4_Eft_Txt_Mis
    elif D_S4_Dmg_Rcv >= 1 and BS_A_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[D_S4_Dmg_Rcv]{/color}{/size}{/b}" at D_S4_Eft_Txt_CritDmg
    elif D_S4_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[D_S4_Dmg_Rcv]{/color}{/size}{/b}" at D_S4_Eft_Txt_Dmg

#///////////////////////  DEFFENDER SLOT 5

    if D_S5_Dmg_Rcv <= 0 and D_S5_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at D_S5_Eft_Txt_Mis
    elif D_S5_Dmg_Rcv >= 1 and BS_A_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[D_S5_Dmg_Rcv]{/color}{/size}{/b}" at D_S5_Eft_Txt_CritDmg
    elif D_S5_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[D_S5_Dmg_Rcv]{/color}{/size}{/b}" at D_S5_Eft_Txt_Dmg

#///////////////////////  DEFFENDER SLOT 6

    if D_S6_Dmg_Rcv <= 0 and D_S6_CanEvd >= 1:
            text "{b}{size=40}{color=#FFFFFF}Miss{/color}{/size}{/b}" at D_S6_Eft_Txt_Mis
    elif D_S6_Dmg_Rcv >= 1 and BS_A_CrtDam == 1:
        text "{b}{size=50}{color=#FF0000}[D_S6_Dmg_Rcv]{/color}{/size}{/b}" at D_S6_Eft_Txt_CritDmg
    elif D_S6_Dmg_Rcv >= 1:
        text "{b}{size=35}{color=#0000ff}[D_S6_Dmg_Rcv]{/color}{/size}{/b}" at D_S6_Eft_Txt_Dmg