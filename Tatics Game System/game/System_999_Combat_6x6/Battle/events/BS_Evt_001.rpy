label BS_Stg001_Evt_001:

    e "Đây là Events 1"
    e "Toàn bộ Quân của Vu uông sẽ được tăng 30 Morales"

    $ A_S1_MorIcr += 30
    $ A_S2_MorIcr += 30
    $ A_S3_MorIcr += 30
    $ A_S4_MorIcr += 30
    $ A_S5_MorIcr += 30
    $ A_S6_MorIcr += 30

    call BS_Chk_Mor

    return
