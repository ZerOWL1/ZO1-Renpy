label BS_Load_Evt_Check:

    if BS_Turns == 3 and BS_Stage001_Event001 == "ON":
        call BS_Stg001_Evt_001
        $ BS_Stage001_Event001 = "OFF"

    elif BS_Turns == 4 and BS_Stage001_Event002 == "ON":
        call BS_Stg001_Evt_002
        $ BS_Stage001_Event002 = "OFF"

    elif BS_Turns == 5 and BS_Stage001_Event003 == "ON":
        call BS_Stg001_Evt_003
        $ BS_Stage001_Event003 = "OFF"

    return
