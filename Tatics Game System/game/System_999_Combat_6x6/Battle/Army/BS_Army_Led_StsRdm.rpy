label BS_Army_Led_StsRdm:

#/////////////////////// LEADER ATTACKER SLOT 1
    if A_S1_Ctl_Type != "PI":
        if Led_A_S1_Type == "Solider":
            $ Led_A_S1_MHP += renpy.random.randint(1, 20)
            $ Led_A_S1_HP = Led_A_S1_MHP
            $ Led_A_S1_Str += renpy.random.randint(1, 10)
            $ Led_A_S1_Skl += renpy.random.randint(1, 5)
            $ Led_A_S1_Int += renpy.random.randint(1, 5)
            $ Led_A_S1_Spd += renpy.random.randint(1, 4)
            $ Led_A_S1_Def += renpy.random.randint(1, 7)
        elif Led_A_S1_Type == "Archer":
            $ Led_A_S1_MHP += renpy.random.randint(1, 10)
            $ Led_A_S1_HP = Led_A_S1_MHP
            $ Led_A_S1_Str += renpy.random.randint(1, 7)
            $ Led_A_S1_Skl += renpy.random.randint(1, 7)
            $ Led_A_S1_Int += renpy.random.randint(1, 7)
            $ Led_A_S1_Spd += renpy.random.randint(1, 8)
            $ Led_A_S1_Def += renpy.random.randint(1, 2)
        elif Led_A_S1_Type == "Horse_Rider":
            $ Led_A_S1_MHP += renpy.random.randint(1, 15)
            $ Led_A_S1_HP = Led_A_S1_MHP
            $ Led_A_S1_Str += renpy.random.randint(1, 9)
            $ Led_A_S1_Skl += renpy.random.randint(1, 8)
            $ Led_A_S1_Int += renpy.random.randint(1, 6)
            $ Led_A_S1_Spd += renpy.random.randint(1, 7)
            $ Led_A_S1_Def += renpy.random.randint(1, 5)
        elif Led_A_S1_Type == "Healer":
            $ Led_A_S1_MHP += renpy.random.randint(1, 10)
            $ Led_A_S1_HP = Led_A_S1_MHP
            $ Led_A_S1_Str += renpy.random.randint(1, 5)
            $ Led_A_S1_Skl += renpy.random.randint(1, 7)
            $ Led_A_S1_Int += renpy.random.randint(1, 10)
            $ Led_A_S1_Spd += renpy.random.randint(1, 6)
            $ Led_A_S1_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER ATTACKER SLOT 2
    if A_S2_Ctl_Type != "PI":
        if Led_A_S2_Type == "Solider":
            $ Led_A_S2_MHP += renpy.random.randint(1, 20)
            $ Led_A_S2_HP = Led_A_S2_MHP
            $ Led_A_S2_Str += renpy.random.randint(1, 10)
            $ Led_A_S2_Skl += renpy.random.randint(1, 5)
            $ Led_A_S2_Int += renpy.random.randint(1, 5)
            $ Led_A_S2_Spd += renpy.random.randint(1, 4)
            $ Led_A_S2_Def += renpy.random.randint(1, 7)
        elif Led_A_S2_Type == "Archer":
            $ Led_A_S2_MHP += renpy.random.randint(1, 10)
            $ Led_A_S2_HP = Led_A_S2_MHP
            $ Led_A_S2_Str += renpy.random.randint(1, 7)
            $ Led_A_S2_Skl += renpy.random.randint(1, 7)
            $ Led_A_S2_Int += renpy.random.randint(1, 7)
            $ Led_A_S2_Spd += renpy.random.randint(1, 8)
            $ Led_A_S2_Def += renpy.random.randint(1, 2)
        elif Led_A_S2_Type == "Horse_Rider":
            $ Led_A_S2_MHP += renpy.random.randint(1, 15)
            $ Led_A_S2_HP = Led_A_S2_MHP
            $ Led_A_S2_Str += renpy.random.randint(1, 9)
            $ Led_A_S2_Skl += renpy.random.randint(1, 8)
            $ Led_A_S2_Int += renpy.random.randint(1, 6)
            $ Led_A_S2_Spd += renpy.random.randint(1, 7)
            $ Led_A_S2_Def += renpy.random.randint(1, 5)
        elif Led_A_S2_Type == "Healer":
            $ Led_A_S2_MHP += renpy.random.randint(1, 10)
            $ Led_A_S2_HP = Led_A_S2_MHP
            $ Led_A_S2_Str += renpy.random.randint(1, 5)
            $ Led_A_S2_Skl += renpy.random.randint(1, 7)
            $ Led_A_S2_Int += renpy.random.randint(1, 10)
            $ Led_A_S2_Spd += renpy.random.randint(1, 6)
            $ Led_A_S2_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER ATTACKER SLOT 3
    if A_S3_Ctl_Type != "PI":
        if Led_A_S3_Type == "Solider":
            $ Led_A_S3_MHP += renpy.random.randint(1, 20)
            $ Led_A_S3_HP = Led_A_S3_MHP
            $ Led_A_S3_Str += renpy.random.randint(1, 10)
            $ Led_A_S3_Skl += renpy.random.randint(1, 5)
            $ Led_A_S3_Int += renpy.random.randint(1, 5)
            $ Led_A_S3_Spd += renpy.random.randint(1, 4)
            $ Led_A_S3_Def += renpy.random.randint(1, 7)
        elif Led_A_S3_Type == "Archer":
            $ Led_A_S3_MHP += renpy.random.randint(1, 10)
            $ Led_A_S3_HP = Led_A_S3_MHP
            $ Led_A_S3_Str += renpy.random.randint(1, 7)
            $ Led_A_S3_Skl += renpy.random.randint(1, 7)
            $ Led_A_S3_Int += renpy.random.randint(1, 7)
            $ Led_A_S3_Spd += renpy.random.randint(1, 8)
            $ Led_A_S3_Def += renpy.random.randint(1, 2)
        elif Led_A_S3_Type == "Horse_Rider":
            $ Led_A_S3_MHP += renpy.random.randint(1, 15)
            $ Led_A_S3_HP = Led_A_S3_MHP
            $ Led_A_S3_Str += renpy.random.randint(1, 9)
            $ Led_A_S3_Skl += renpy.random.randint(1, 8)
            $ Led_A_S3_Int += renpy.random.randint(1, 6)
            $ Led_A_S3_Spd += renpy.random.randint(1, 7)
            $ Led_A_S3_Def += renpy.random.randint(1, 5)
        elif Led_A_S3_Type == "Healer":
            $ Led_A_S3_MHP += renpy.random.randint(1, 10)
            $ Led_A_S3_HP = Led_A_S3_MHP
            $ Led_A_S3_Str += renpy.random.randint(1, 5)
            $ Led_A_S3_Skl += renpy.random.randint(1, 7)
            $ Led_A_S3_Int += renpy.random.randint(1, 10)
            $ Led_A_S3_Spd += renpy.random.randint(1, 6)
            $ Led_A_S3_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER ATTACKER SLOT 4
    if A_S4_Ctl_Type != "PI":
        if Led_A_S4_Type == "Solider":
            $ Led_A_S4_MHP += renpy.random.randint(1, 20)
            $ Led_A_S4_HP = Led_A_S4_MHP
            $ Led_A_S4_Str += renpy.random.randint(1, 10)
            $ Led_A_S4_Skl += renpy.random.randint(1, 5)
            $ Led_A_S4_Int += renpy.random.randint(1, 5)
            $ Led_A_S4_Spd += renpy.random.randint(1, 4)
            $ Led_A_S4_Def += renpy.random.randint(1, 7)
        elif Led_A_S4_Type == "Archer":
            $ Led_A_S4_MHP += renpy.random.randint(1, 10)
            $ Led_A_S4_HP = Led_A_S4_MHP
            $ Led_A_S4_Str += renpy.random.randint(1, 7)
            $ Led_A_S4_Skl += renpy.random.randint(1, 7)
            $ Led_A_S4_Int += renpy.random.randint(1, 7)
            $ Led_A_S4_Spd += renpy.random.randint(1, 8)
            $ Led_A_S4_Def += renpy.random.randint(1, 2)
        elif Led_A_S4_Type == "Horse_Rider":
            $ Led_A_S4_MHP += renpy.random.randint(1, 15)
            $ Led_A_S4_HP = Led_A_S4_MHP
            $ Led_A_S4_Str += renpy.random.randint(1, 9)
            $ Led_A_S4_Skl += renpy.random.randint(1, 8)
            $ Led_A_S4_Int += renpy.random.randint(1, 6)
            $ Led_A_S4_Spd += renpy.random.randint(1, 7)
            $ Led_A_S4_Def += renpy.random.randint(1, 5)
        elif Led_A_S4_Type == "Healer":
            $ Led_A_S4_MHP += renpy.random.randint(1, 10)
            $ Led_A_S4_HP = Led_A_S4_MHP
            $ Led_A_S4_Str += renpy.random.randint(1, 5)
            $ Led_A_S4_Skl += renpy.random.randint(1, 7)
            $ Led_A_S4_Int += renpy.random.randint(1, 10)
            $ Led_A_S4_Spd += renpy.random.randint(1, 6)
            $ Led_A_S4_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER ATTACKER SLOT 5
    if A_S5_Ctl_Type != "PI":
        if Led_A_S5_Type == "Solider":
            $ Led_A_S5_MHP += renpy.random.randint(1, 20)
            $ Led_A_S5_HP = Led_A_S5_MHP
            $ Led_A_S5_Str += renpy.random.randint(1, 10)
            $ Led_A_S5_Skl += renpy.random.randint(1, 5)
            $ Led_A_S5_Int += renpy.random.randint(1, 5)
            $ Led_A_S5_Spd += renpy.random.randint(1, 4)
            $ Led_A_S5_Def += renpy.random.randint(1, 7)
        elif Led_A_S5_Type == "Archer":
            $ Led_A_S5_MHP += renpy.random.randint(1, 10)
            $ Led_A_S5_HP = Led_A_S5_MHP
            $ Led_A_S5_Str += renpy.random.randint(1, 7)
            $ Led_A_S5_Skl += renpy.random.randint(1, 7)
            $ Led_A_S5_Int += renpy.random.randint(1, 7)
            $ Led_A_S5_Spd += renpy.random.randint(1, 8)
            $ Led_A_S5_Def += renpy.random.randint(1, 2)
        elif Led_A_S5_Type == "Horse_Rider":
            $ Led_A_S5_MHP += renpy.random.randint(1, 15)
            $ Led_A_S5_HP = Led_A_S5_MHP
            $ Led_A_S5_Str += renpy.random.randint(1, 9)
            $ Led_A_S5_Skl += renpy.random.randint(1, 8)
            $ Led_A_S5_Int += renpy.random.randint(1, 6)
            $ Led_A_S5_Spd += renpy.random.randint(1, 7)
            $ Led_A_S5_Def += renpy.random.randint(1, 5)
        elif Led_A_S5_Type == "Healer":
            $ Led_A_S5_MHP += renpy.random.randint(1, 10)
            $ Led_A_S5_HP = Led_A_S5_MHP
            $ Led_A_S5_Str += renpy.random.randint(1, 5)
            $ Led_A_S5_Skl += renpy.random.randint(1, 7)
            $ Led_A_S5_Int += renpy.random.randint(1, 10)
            $ Led_A_S5_Spd += renpy.random.randint(1, 6)
            $ Led_A_S5_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER ATTACKER SLOT 6
    if A_S6_Ctl_Type != "PI":
        if Led_A_S6_Type == "Solider":
            $ Led_A_S6_MHP += renpy.random.randint(1, 20)
            $ Led_A_S6_HP = Led_A_S6_MHP
            $ Led_A_S6_Str += renpy.random.randint(1, 10)
            $ Led_A_S6_Skl += renpy.random.randint(1, 5)
            $ Led_A_S6_Int += renpy.random.randint(1, 5)
            $ Led_A_S6_Spd += renpy.random.randint(1, 4)
            $ Led_A_S6_Def += renpy.random.randint(1, 7)
        elif Led_A_S6_Type == "Archer":
            $ Led_A_S6_MHP += renpy.random.randint(1, 10)
            $ Led_A_S6_HP = Led_A_S6_MHP
            $ Led_A_S6_Str += renpy.random.randint(1, 7)
            $ Led_A_S6_Skl += renpy.random.randint(1, 7)
            $ Led_A_S6_Int += renpy.random.randint(1, 7)
            $ Led_A_S6_Spd += renpy.random.randint(1, 8)
            $ Led_A_S6_Def += renpy.random.randint(1, 2)
        elif Led_A_S6_Type == "Horse_Rider":
            $ Led_A_S6_MHP += renpy.random.randint(1, 15)
            $ Led_A_S6_HP = Led_A_S6_MHP
            $ Led_A_S6_Str += renpy.random.randint(1, 9)
            $ Led_A_S6_Skl += renpy.random.randint(1, 8)
            $ Led_A_S6_Int += renpy.random.randint(1, 6)
            $ Led_A_S6_Spd += renpy.random.randint(1, 7)
            $ Led_A_S6_Def += renpy.random.randint(1, 5)
        elif Led_A_S6_Type == "Healer":
            $ Led_A_S6_MHP += renpy.random.randint(1, 10)
            $ Led_A_S6_HP = Led_A_S6_MHP
            $ Led_A_S6_Str += renpy.random.randint(1, 5)
            $ Led_A_S6_Skl += renpy.random.randint(1, 7)
            $ Led_A_S6_Int += renpy.random.randint(1, 10)
            $ Led_A_S6_Spd += renpy.random.randint(1, 6)
            $ Led_A_S6_Def += renpy.random.randint(1, 2)


        
        
        
        
                 



#/////////////////////// LEADER DEFFENDER SLOT 1
    if D_S1_Ctl_Type != "PI":
        if Led_D_S1_Type == "Solider":
            $ Led_D_S1_MHP += renpy.random.randint(1, 20)
            $ Led_D_S1_HP = Led_D_S1_MHP
            $ Led_D_S1_Str += renpy.random.randint(1, 10)
            $ Led_D_S1_Skl += renpy.random.randint(1, 5)
            $ Led_D_S1_Int += renpy.random.randint(1, 5)
            $ Led_D_S1_Spd += renpy.random.randint(1, 4)
            $ Led_D_S1_Def += renpy.random.randint(1, 7)
        elif Led_D_S1_Type == "Archer":
            $ Led_D_S1_MHP += renpy.random.randint(1, 10)
            $ Led_D_S1_HP = Led_D_S1_MHP
            $ Led_D_S1_Str += renpy.random.randint(1, 7)
            $ Led_D_S1_Skl += renpy.random.randint(1, 7)
            $ Led_D_S1_Int += renpy.random.randint(1, 7)
            $ Led_D_S1_Spd += renpy.random.randint(1, 8)
            $ Led_D_S1_Def += renpy.random.randint(1, 2)
        elif Led_D_S1_Type == "Horse_Rider":
            $ Led_D_S1_MHP += renpy.random.randint(1, 15)
            $ Led_D_S1_HP = Led_D_S1_MHP
            $ Led_D_S1_Str += renpy.random.randint(1, 9)
            $ Led_D_S1_Skl += renpy.random.randint(1, 8)
            $ Led_D_S1_Int += renpy.random.randint(1, 6)
            $ Led_D_S1_Spd += renpy.random.randint(1, 7)
            $ Led_D_S1_Def += renpy.random.randint(1, 5)
        elif Led_D_S1_Type == "Healer":
            $ Led_D_S1_MHP += renpy.random.randint(1, 10)
            $ Led_D_S1_HP = Led_D_S1_MHP
            $ Led_D_S1_Str += renpy.random.randint(1, 5)
            $ Led_D_S1_Skl += renpy.random.randint(1, 7)
            $ Led_D_S1_Int += renpy.random.randint(1, 10)
            $ Led_D_S1_Spd += renpy.random.randint(1, 6)
            $ Led_D_S1_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER DEFFENDER SLOT 2
    if D_S2_Ctl_Type != "PI":
        if Led_D_S2_Type == "Solider":
            $ Led_D_S2_MHP += renpy.random.randint(1, 20)
            $ Led_D_S2_HP = Led_D_S2_MHP
            $ Led_D_S2_Str += renpy.random.randint(1, 10)
            $ Led_D_S2_Skl += renpy.random.randint(1, 5)
            $ Led_D_S2_Int += renpy.random.randint(1, 5)
            $ Led_D_S2_Spd += renpy.random.randint(1, 4)
            $ Led_D_S2_Def += renpy.random.randint(1, 7)
        elif Led_D_S2_Type == "Archer":
            $ Led_D_S2_MHP += renpy.random.randint(1, 10)
            $ Led_D_S2_HP = Led_D_S2_MHP
            $ Led_D_S2_Str += renpy.random.randint(1, 7)
            $ Led_D_S2_Skl += renpy.random.randint(1, 7)
            $ Led_D_S2_Int += renpy.random.randint(1, 7)
            $ Led_D_S2_Spd += renpy.random.randint(1, 8)
            $ Led_D_S2_Def += renpy.random.randint(1, 2)
        elif Led_D_S2_Type == "Horse_Rider":
            $ Led_D_S2_MHP += renpy.random.randint(1, 15)
            $ Led_D_S2_HP = Led_D_S2_MHP
            $ Led_D_S2_Str += renpy.random.randint(1, 9)
            $ Led_D_S2_Skl += renpy.random.randint(1, 8)
            $ Led_D_S2_Int += renpy.random.randint(1, 6)
            $ Led_D_S2_Spd += renpy.random.randint(1, 7)
            $ Led_D_S2_Def += renpy.random.randint(1, 5)
        elif Led_D_S2_Type == "Healer":
            $ Led_D_S2_MHP += renpy.random.randint(1, 10)
            $ Led_D_S2_HP = Led_D_S2_MHP
            $ Led_D_S2_Str += renpy.random.randint(1, 5)
            $ Led_D_S2_Skl += renpy.random.randint(1, 7)
            $ Led_D_S2_Int += renpy.random.randint(1, 10)
            $ Led_D_S2_Spd += renpy.random.randint(1, 6)
            $ Led_D_S2_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER DEFFENDER SLOT 3
    if D_S3_Ctl_Type != "PI":
        if Led_D_S3_Type == "Solider":
            $ Led_D_S3_MHP += renpy.random.randint(1, 20)
            $ Led_D_S3_HP = Led_D_S3_MHP
            $ Led_D_S3_Str += renpy.random.randint(1, 10)
            $ Led_D_S3_Skl += renpy.random.randint(1, 5)
            $ Led_D_S3_Int += renpy.random.randint(1, 5)
            $ Led_D_S3_Spd += renpy.random.randint(1, 4)
            $ Led_D_S3_Def += renpy.random.randint(1, 7)
        elif Led_D_S3_Type == "Archer":
            $ Led_D_S3_MHP += renpy.random.randint(1, 10)
            $ Led_D_S3_HP = Led_D_S3_MHP
            $ Led_D_S3_Str += renpy.random.randint(1, 7)
            $ Led_D_S3_Skl += renpy.random.randint(1, 7)
            $ Led_D_S3_Int += renpy.random.randint(1, 7)
            $ Led_D_S3_Spd += renpy.random.randint(1, 8)
            $ Led_D_S3_Def += renpy.random.randint(1, 2)
        elif Led_D_S3_Type == "Horse_Rider":
            $ Led_D_S3_MHP += renpy.random.randint(1, 15)
            $ Led_D_S3_HP = Led_D_S3_MHP
            $ Led_D_S3_Str += renpy.random.randint(1, 9)
            $ Led_D_S3_Skl += renpy.random.randint(1, 8)
            $ Led_D_S3_Int += renpy.random.randint(1, 6)
            $ Led_D_S3_Spd += renpy.random.randint(1, 7)
            $ Led_D_S3_Def += renpy.random.randint(1, 5)
        elif Led_D_S3_Type == "Healer":
            $ Led_D_S3_MHP += renpy.random.randint(1, 10)
            $ Led_D_S3_HP = Led_D_S3_MHP
            $ Led_D_S3_Str += renpy.random.randint(1, 5)
            $ Led_D_S3_Skl += renpy.random.randint(1, 7)
            $ Led_D_S3_Int += renpy.random.randint(1, 10)
            $ Led_D_S3_Spd += renpy.random.randint(1, 6)
            $ Led_D_S3_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER DEFFENDER SLOT 4
    if D_S4_Ctl_Type != "PI":
        if Led_D_S4_Type == "Solider":
            $ Led_D_S4_MHP += renpy.random.randint(1, 20)
            $ Led_D_S4_HP = Led_D_S4_MHP
            $ Led_D_S4_Str += renpy.random.randint(1, 10)
            $ Led_D_S4_Skl += renpy.random.randint(1, 5)
            $ Led_D_S4_Int += renpy.random.randint(1, 5)
            $ Led_D_S4_Spd += renpy.random.randint(1, 4)
            $ Led_D_S4_Def += renpy.random.randint(1, 7)
        elif Led_D_S4_Type == "Archer":
            $ Led_D_S4_MHP += renpy.random.randint(1, 10)
            $ Led_D_S4_HP = Led_D_S4_MHP
            $ Led_D_S4_Str += renpy.random.randint(1, 7)
            $ Led_D_S4_Skl += renpy.random.randint(1, 7)
            $ Led_D_S4_Int += renpy.random.randint(1, 7)
            $ Led_D_S4_Spd += renpy.random.randint(1, 8)
            $ Led_D_S4_Def += renpy.random.randint(1, 2)
        elif Led_D_S4_Type == "Horse_Rider":
            $ Led_D_S4_MHP += renpy.random.randint(1, 15)
            $ Led_D_S4_HP = Led_D_S4_MHP
            $ Led_D_S4_Str += renpy.random.randint(1, 9)
            $ Led_D_S4_Skl += renpy.random.randint(1, 8)
            $ Led_D_S4_Int += renpy.random.randint(1, 6)
            $ Led_D_S4_Spd += renpy.random.randint(1, 7)
            $ Led_D_S4_Def += renpy.random.randint(1, 5)
        elif Led_D_S4_Type == "Healer":
            $ Led_D_S4_MHP += renpy.random.randint(1, 10)
            $ Led_D_S4_HP = Led_D_S4_MHP
            $ Led_D_S4_Str += renpy.random.randint(1, 5)
            $ Led_D_S4_Skl += renpy.random.randint(1, 7)
            $ Led_D_S4_Int += renpy.random.randint(1, 10)
            $ Led_D_S4_Spd += renpy.random.randint(1, 6)
            $ Led_D_S4_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER DEFFENDER SLOT 5
    if D_S5_Ctl_Type != "PI":
        if Led_D_S5_Type == "Solider":
            $ Led_D_S5_MHP += renpy.random.randint(1, 20)
            $ Led_D_S5_HP = Led_D_S5_MHP
            $ Led_D_S5_Str += renpy.random.randint(1, 10)
            $ Led_D_S5_Skl += renpy.random.randint(1, 5)
            $ Led_D_S5_Int += renpy.random.randint(1, 5)
            $ Led_D_S5_Spd += renpy.random.randint(1, 4)
            $ Led_D_S5_Def += renpy.random.randint(1, 7)
        elif Led_D_S5_Type == "Archer":
            $ Led_D_S5_MHP += renpy.random.randint(1, 10)
            $ Led_D_S5_HP = Led_D_S5_MHP
            $ Led_D_S5_Str += renpy.random.randint(1, 7)
            $ Led_D_S5_Skl += renpy.random.randint(1, 7)
            $ Led_D_S5_Int += renpy.random.randint(1, 7)
            $ Led_D_S5_Spd += renpy.random.randint(1, 8)
            $ Led_D_S5_Def += renpy.random.randint(1, 2)
        elif Led_D_S5_Type == "Horse_Rider":
            $ Led_D_S5_MHP += renpy.random.randint(1, 15)
            $ Led_D_S5_HP = Led_D_S5_MHP
            $ Led_D_S5_Str += renpy.random.randint(1, 9)
            $ Led_D_S5_Skl += renpy.random.randint(1, 8)
            $ Led_D_S5_Int += renpy.random.randint(1, 6)
            $ Led_D_S5_Spd += renpy.random.randint(1, 7)
            $ Led_D_S5_Def += renpy.random.randint(1, 5)
        elif Led_D_S5_Type == "Healer":
            $ Led_D_S5_MHP += renpy.random.randint(1, 10)
            $ Led_D_S5_HP = Led_D_S5_MHP
            $ Led_D_S5_Str += renpy.random.randint(1, 5)
            $ Led_D_S5_Skl += renpy.random.randint(1, 7)
            $ Led_D_S5_Int += renpy.random.randint(1, 10)
            $ Led_D_S5_Spd += renpy.random.randint(1, 6)
            $ Led_D_S5_Def += renpy.random.randint(1, 2)

#/////////////////////// LEADER DEFFENDER SLOT 6
    if D_S6_Ctl_Type != "PI":
        if Led_D_S6_Type == "Solider":
            $ Led_D_S6_MHP += renpy.random.randint(1, 20)
            $ Led_D_S6_HP = Led_D_S6_MHP
            $ Led_D_S6_Str += renpy.random.randint(1, 10)
            $ Led_D_S6_Skl += renpy.random.randint(1, 5)
            $ Led_D_S6_Int += renpy.random.randint(1, 5)
            $ Led_D_S6_Spd += renpy.random.randint(1, 4)
            $ Led_D_S6_Def += renpy.random.randint(1, 7)
        elif Led_D_S6_Type == "Archer":
            $ Led_D_S6_MHP += renpy.random.randint(1, 10)
            $ Led_D_S6_HP = Led_D_S6_MHP
            $ Led_D_S6_Str += renpy.random.randint(1, 7)
            $ Led_D_S6_Skl += renpy.random.randint(1, 7)
            $ Led_D_S6_Int += renpy.random.randint(1, 7)
            $ Led_D_S6_Spd += renpy.random.randint(1, 8)
            $ Led_D_S6_Def += renpy.random.randint(1, 2)
        elif Led_D_S6_Type == "Horse_Rider":
            $ Led_D_S6_MHP += renpy.random.randint(1, 15)
            $ Led_D_S6_HP = Led_D_S6_MHP
            $ Led_D_S6_Str += renpy.random.randint(1, 9)
            $ Led_D_S6_Skl += renpy.random.randint(1, 8)
            $ Led_D_S6_Int += renpy.random.randint(1, 6)
            $ Led_D_S6_Spd += renpy.random.randint(1, 7)
            $ Led_D_S6_Def += renpy.random.randint(1, 5)
        elif Led_D_S6_Type == "Healer":
            $ Led_D_S6_MHP += renpy.random.randint(1, 10)
            $ Led_D_S6_HP = Led_D_S6_MHP
            $ Led_D_S6_Str += renpy.random.randint(1, 5)
            $ Led_D_S6_Skl += renpy.random.randint(1, 7)
            $ Led_D_S6_Int += renpy.random.randint(1, 10)
            $ Led_D_S6_Spd += renpy.random.randint(1, 6)
            $ Led_D_S6_Def += renpy.random.randint(1, 2)

    return