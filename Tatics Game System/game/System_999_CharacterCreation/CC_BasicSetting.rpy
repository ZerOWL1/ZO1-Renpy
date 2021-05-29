label CC_BasicSetting:

    define Player01_ArmyOcu = 0
    define Player01_ArmyName = 0
    define Player01_ArmyLevel = 0
    define Player01_ArmyCls = 0
    define Player01_ArmyTtc = 0
    define Player01_ArmyMHP = 0
    define Player01_ArmyHP = 0
    define Player01_ArmyAtk = 0
    define Player01_ArmyDef = 0
    define Player01_ArmySpd = 0
    define Player01_ArmyCrtChc = 0
    define Player01_ArmyEvdChc = 0

    define Player01_Attributes = 0
    define Player01_Home = 0
    define Player01_Name = 0
    define Player01_Level = 0
    define Player01_Type = 0
    define Player01_MHP = 0
    define Player01_HP = Player01_MHP
    define Player01_Str = 0
    define Player01_Skl = 0
    define Player01_Int = 0
    define Player01_Spd = 0
    define Player01_Def = 0

    define CC_Progress = 0
    define CC_ClsPicked = 0
    define CC_RaisedAttributes = 0

    $ CC_Picked_Cls001 = Hide ("Scr_CC_PickClass"), Show ("Scr_CC_ClsPicked"), SetVariable ("BS_Progress", 1), SetVariable (
    "Player01_Type", "Solider"), SetVariable ("CC_ClsPicked", "Solider"), SetVariable ("CC_Progress", 2), SetVariable (
    "Player01_Level", 1), SetVariable (
    "Player01_MHP", 16), SetVariable (
    "Player01_Str", 6), SetVariable (
    "Player01_Skl", 4), SetVariable (
    "Player01_Int", 3), SetVariable (
    "Player01_Spd", 3), SetVariable (
    "Player01_Def", 2), Jump ("CC_Start")

    $ CC_Picked_Cls002 = Hide ("Scr_CC_PickClass"), Show ("Scr_CC_ClsPicked"), SetVariable (
    "Player01_Type", "Archer"), SetVariable ("CC_ClsPicked", "Archer"), SetVariable ("CC_Progress", 2), SetVariable (
    "Player01_Level", 1), SetVariable (
    "Player01_MHP", 10), SetVariable (
    "Player01_Str", 5), SetVariable (
    "Player01_Skl", 6), SetVariable (
    "Player01_Int", 6), SetVariable (
    "Player01_Spd", 6), SetVariable (
    "Player01_Def", 1), Jump ("CC_Start")

    $ CC_Picked_Cls003 = Hide ("Scr_CC_PickClass"), Show ("Scr_CC_ClsPicked"), SetVariable (
    "Player01_Type", "Horse_Rider"), SetVariable ("CC_ClsPicked", "Horse_Rider"), SetVariable ("CC_Progress", 2), SetVariable (
    "Player01_Level", 1), SetVariable (
    "Player01_MHP", 12), SetVariable (
    "Player01_Str", 8), SetVariable (
    "Player01_Skl", 4), SetVariable (
    "Player01_Int", 4), SetVariable (
    "Player01_Spd", 5), SetVariable (
    "Player01_Def", 3), Jump ("CC_Start")

    $ CC_ChooseYes = Hide ("Scr_CC_ClsPicked"), Hide ("Scr_CC_PickClass_Confirm"), SetVariable ("CC_Progress", 3), Jump ("CC_Start")
    $ CC_ChooseNo = Hide ("Scr_CC_ClsPicked"), Hide ("Scr_CC_PickClass_Confirm"), SetVariable ("CC_Progress", 1), Jump ("CC_Start")
    $ CC_RaiseHP = SetVariable ("CC_RaisedAttributes", "HP"), Jump ("CC_AttributesUsed")
    $ CC_RaiseSTR = SetVariable ("CC_RaisedAttributes", "STR"), Jump ("CC_AttributesUsed")
    $ CC_RaiseSKL = SetVariable ("CC_RaisedAttributes", "SKL"), Jump ("CC_AttributesUsed")
    $ CC_RaiseINT = SetVariable ("CC_RaisedAttributes", "INT"), Jump ("CC_AttributesUsed")
    $ CC_RaiseSPD = SetVariable ("CC_RaisedAttributes", "SPD"), Jump ("CC_AttributesUsed")
    $ CC_RaiseDEF = SetVariable ("CC_RaisedAttributes", "DEF"), Jump ("CC_AttributesUsed")
    $ CC_UseAttributesDONE = Hide ("Scr_Player_UseAttributes"), SetVariable ("CC_RaisedAttributes", "NONE"), SetVariable ("CC_Progress", 6), Jump ("CC_Start")

    return