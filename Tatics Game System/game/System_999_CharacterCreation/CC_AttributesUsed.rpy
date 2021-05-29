label CC_AttributesUsed:
    if Player01_Attributes == 0:
        $ CC_Progress = 5
    else:
        $ Player01_Attributes -= 1

        if CC_RaisedAttributes == "HP":
            $ Player01_MHP += 1
        elif CC_RaisedAttributes == "STR":
            $ Player01_Str += 1
        elif CC_RaisedAttributes == "SKL":
            $ Player01_Skl += 1
        elif CC_RaisedAttributes == "INT":
            $ Player01_Int += 1
        elif CC_RaisedAttributes == "SPD":
            $ Player01_Spd += 1
        elif CC_RaisedAttributes == "DEF":
            $ Player01_Def += 1

        jump CC_Start
