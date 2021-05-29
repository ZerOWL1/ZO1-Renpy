screen Scr_CC_PickClass:

    modal True

    imagebutton auto "Images/Character Creation/Class/Class_001/Class_001_001_%s.png" focus_mask True action CC_Picked_Cls001 at CC_Eft_PickCls001
    imagebutton auto "Images/Character Creation/Class/Class_002/Class_002_001_%s.png" focus_mask True action CC_Picked_Cls002 at CC_Eft_PickCls002
    imagebutton auto "Images/Character Creation/Class/Class_003/Class_003_001_%s.png" focus_mask True action CC_Picked_Cls003 at CC_Eft_PickCls003

screen Scr_CC_ClsPicked:

    if CC_ClsPicked == "Solider":
        image "Images/Character Creation/Class/Class_001/Class_001_001_hover.png" anchor (0.5,0.5) align (0.5,0.3) zoom 3.0
    elif CC_ClsPicked == "Archer":
        image "Images/Character Creation/Class/Class_002/Class_002_001_hover.png" anchor (0.5,0.5) align (0.5,0.3) zoom 3.0
    elif CC_ClsPicked == "Horse_Rider":
        image "Images/Character Creation/Class/Class_003/Class_003_001_hover.png" anchor (0.5,0.5) align (0.5,0.3) zoom 3.0

screen Scr_CC_PickClass_Confirm:

    modal True
    use Scr_Player_Attributes

    textbutton "Yes" action CC_ChooseYes anchor (0.5,0.5) align (0.45,0.5)
    textbutton "No" action CC_ChooseNo anchor (0.5,0.5) align (0.55,0.5)

screen Scr_Player_Attributes:
    frame:
        xalign 0.7
        yalign 0.1
        vbox:
            text "{size=24}Name: [Player01_Name]{/size}"
            text "{size=24}Home: [Player01_Home]{/size}"
            text "{size=24}Type: [Player01_Type]{/size}"
            text "{size=24}Lv: [Player01_Level]{/size}"
            text "{size=24}HP: [Player01_MHP]{/size}"
            text "{size=24}Str: [Player01_Str]{/size}"
            text "{size=24}Skl: [Player01_Skl]{/size}"
            text "{size=24}Int: [Player01_Int]{/size}"
            text "{size=24}Spd: [Player01_Spd]{/size}"
            text "{size=24}Def: [Player01_Def]{/size}"

screen Scr_Player_UseAttributes:

    modal True
    use Scr_Player_Attributes
    use Scr_CC_ClsPicked

    text "{size=24}Attributes: [Player01_Attributes]{/size}" anchor (0.5,0.5) align (0.5,0.5)

    if Player01_Attributes > 0:
        textbutton "+ HP" action CC_RaiseHP anchor (0.5,0.5) align (0.35,0.6)
        textbutton "+ Str" action CC_RaiseSTR anchor (0.5,0.5) align (0.40,0.6)
        textbutton "+ Skl" action CC_RaiseSKL anchor (0.5,0.5) align (0.45,0.6)
        textbutton "+ Int" action CC_RaiseINT anchor (0.5,0.5) align (0.50,0.6)
        textbutton "+ Spd" action CC_RaiseSPD anchor (0.5,0.5) align (0.55,0.6)
        textbutton "+ Def" action CC_RaiseDEF anchor (0.5,0.5) align (0.60,0.6)
    else:
        textbutton "Done" action CC_UseAttributesDONE anchor (0.5,0.5) align (0.5,0.6)
