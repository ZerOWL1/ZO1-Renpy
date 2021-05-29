label BS_Stg001_Evt_002:

    e "Đây là Events 2"
    e "Toàn bộ Sơn tặc sẽ bị giảm 50 Morales"

    $ D_S1_MorIcr -= 50
    $ D_S2_MorIcr -= 50
    $ D_S3_MorIcr -= 50
    $ D_S4_MorIcr -= 50
    $ D_S5_MorIcr -= 50
    $ D_S6_MorIcr -= 50

    call BS_Chk_Mor

    return
