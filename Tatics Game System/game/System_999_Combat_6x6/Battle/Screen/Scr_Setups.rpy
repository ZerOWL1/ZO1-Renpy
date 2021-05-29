init python:
    def HP_frame(hp, MHP, **properties):
        ui.bar(MHP, hp,
                xmaximum=120, ymaximum=Scr_002_HP_Vertical,
                left_bar=Frame("Images/Combat System/Bars/rrslider_full.png", 0, 0),
                right_bar=Frame("Images/Combat System/Bars/rrslider_empty.png", 0, 0),
                thumb=None,
                thumb_shadow=None, **properties)

    def ATB_frame(Atb,MAtb,**properties):
        ui.bar(MAtb,Atb,
                xmaximum=120, ymaximum=Scr_002_ATB_Vertical,
                left_bar=Frame("Images/Combat System/Bars/ATB_full.png", 0, 0),
                right_bar=None,
                thumb=None,
                thumb_shadow=None, **properties)

    def Morale_frame(Mor,MMor,**properties):
        ui.bar(MMor,Mor,
                xmaximum=120, ymaximum=Scr_002_Mor_Vertical,
                left_bar=Frame("Images/Combat System/Bars/Morale_normal.png", 0, 0),
                right_bar=Frame("Images/Combat System/Bars/Morale_empty.png", 0, 0),
                thumb=None,
                thumb_shadow=None, **properties)

    def MaxMorale_frame(MaxMor,MMaxMor,**properties):
        ui.bar(MMaxMor,MaxMor,
                xmaximum=120, ymaximum=Scr_002_Mor_Vertical,
                left_bar=Frame("Images/Combat System/Bars/Morale_full.png", 0, 0),
                right_bar=Frame("Images/Combat System/Bars/Morale_normal.png", 0, 0),
                thumb=None,
                thumb_shadow=None, **properties)

    def Exp_frame(Exp,MExp,**properties):
        ui.bar(MExp,Exp,
                xmaximum=120, ymaximum=Scr_002_Exp_Vertical,
                left_bar=Frame("Images/Combat System/Bars/Exp_full.png", 0, 0),
                right_bar=Frame("Images/Combat System/Bars/Exp_empty.png", 0, 0),
                thumb=None,
                thumb_shadow=None, **properties)      