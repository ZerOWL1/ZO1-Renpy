label Start_CharCreation:
    
    menu:
        "Do you wish to join this journey ?"
        "Yes":
            call CC_BasicSetting
            call CC_Start
        "No":
            pass
    return

label CC_Start:

    $ renpy.pause(BS_SysSpd, hard = True)

    if CC_Progress == 0:
        $ Player01_Name = renpy.input("What is your name ?")
        $ Player01_Name = Player01_Name.strip()
        if not Player01_Name:
             $ Player01_Name = "Unknown"

        e "So, your name is {b}[Player01_Name]{/b} right ?"
        e "Is a good name, you're sure blessed"

        $ Player01_Home = renpy.input("Where are you from ?")
        $ Player01_Home = Player01_Home.strip()
        if not Player01_Home:
             $ Player01_Home = "Unknown"

        e "So, you're {b}[Player01_Name]{/b} from {b}[Player01_Home]{/b} ?"
        e "That place must be brilliant to give a birth for such a courage soul"

        $ CC_Progress = 1
        jump CC_Start

    elif CC_Progress == 1:
        show screen Scr_CC_PickClass
        e "What is your class ?"
        $ renpy.pause (hard = True)

    elif CC_Progress == 2:
        if Player01_Type == "Solider":
            show screen Scr_CC_PickClass_Confirm
            e "So... you're solider, who excel at spear and shield, is that right ?"
            $ renpy.pause (hard = True)
        elif Player01_Type == "Archer":
            show screen Scr_CC_PickClass_Confirm
            e "So... you're Archer, who excel at Shooting from afar, is that right ?"
            $ renpy.pause (hard = True)
        elif Player01_Type == "Horse_Rider":
            show screen Scr_CC_PickClass_Confirm
            e "So... you're Horse Rider, who excel at Mounting and strike with surprise, is that right ?"
            $ renpy.pause (hard = True)

    elif CC_Progress == 3:
        e "A leader without Army is nothing so does the Army. It like the snake without head and the tiger with no claws and teeths"
        e "You must pick some good men, Which one do you prefer ?"
        menu:
            "A Group of Spear Men":
                $ Player01_ArmyName = "Novice Soliders"
                $ Player01_ArmyCls = 1
            "A Group of Archer":
                $ Player01_ArmyName = "Novice Archers"
                $ Player01_ArmyCls = 2
            "A Group of Horse Men":
                $ Player01_ArmyName = "Novice Horse Men"
                $ Player01_ArmyCls = 3
        $ Player01_ArmyOcu = 1
        $ Player01_ArmyLevel = 1
        $ Player01_ArmyTtc = 1
        e "Very good, i think that should be enough"
        $ CC_Progress = 4
        jump CC_Start

    elif CC_Progress == 4:
        e "{b}[Player01_Name]{/b}, {b}[Player01_Type]{/b} of {b}[Player01_Home]{/b}, Leading an Army of {b}[Player01_ArmyName]{/b} is set to venture on journey"
        e "What lies ahead is your to decide"
        e "For such a difficulty, i wish to grant you a little Gift, use it well Courage Soul."
        $ Player01_Attributes = 4
        $ CC_Progress = 5
        jump CC_Start

    elif CC_Progress == 5:
        show screen Scr_Player_UseAttributes
        $ renpy.pause (hard = True)

    $ Player01_HP = Player01_MHP
    e "All have been set, good luck on your journey"
    $ CC_Progress = "Done"
    return