## started coding 12.08.2019
## finished coding 12.08.2019

Zırhlar = {"Çelik":70,
           "Platin":80,}
Büyüler = {"Karabasan":30, # Hasar Verir
           "Güneş":50} # Can verir

karakterler = {
    "Arda":{
            "İsim":"Arda",
            "Güç":300,
            "Sağlık":100,
            "Zırh":Zırhlar["Çelik"],
            "Büyü":"Karabasan"},
    "Samet":{
            "İsim":"Samet",
            "Güç":30,
            "Sağlık":100,
            "Zırh":Zırhlar["Platin"],
            "Büyü":"Güneş"}
}


def saldır(Saldıran,Saldırılan):
    saldıranisim = Saldıran["İsim"]
    saldırılanisim = Saldırılan["İsim"]
    güc = Saldıran["Güç"]
    zırh = Saldırılan["Zırh"]
    can = Saldırılan["Sağlık"]
    savunma = zırh + can
    if savunma > güc:
        print(saldıranisim, "adlı oyuncu", saldırılanisim, "adlı oyuncuya saldırdı.")
        damage = savunma - güc
        print("Kalan Can:", damage)
    elif güc > savunma:
        damage = savunma - güc
        print(saldıranisim,"adlı oyuncu",saldırılanisim,"adlı oyuncuya saldırdı.")
        print(saldırılanisim,"adlı oyuncu öldü")

def büyülüsaldırı(Saldıran,Saldırılan):
    saldıranisim = Saldıran["İsim"]
    saldırılanisim = Saldırılan["İsim"]
    güc = Saldıran["Güç"]
    zırh = Saldırılan["Zırh"]
    can = Saldırılan["Sağlık"]
    savunma = zırh + can
    if Saldırılan["Büyü"] == "Güneş":
        savunma += Büyüler["Güneş"]
    if Saldıran["Büyü"] == "Güneş":
        print(saldıranisim,"adlı oyuncunun büyüsü",Saldıran["Büyü"])
        savunma +=Büyüler["Güneş"]
        if savunma > güc:
            print(saldıranisim, "adlı oyuncu", saldırılanisim, "adlı oyuncuya saldırdı.")
            damage = savunma - güc
            print("Kalan Can:", damage)
        elif güc > savunma:
            damage = savunma - güc
            print(saldıranisim, "adlı oyuncu", saldırılanisim, "adlı oyuncuya saldırdı.")
            print(saldırılanisim, "adlı oyuncu öldü")
    elif Saldıran["Büyü"] == "Karabasan":
        print(saldıranisim, "adlı oyuncunun büyüsü", Saldıran["Büyü"])
        güc += Büyüler["Karabasan"]
        if savunma > güc:
            print(saldıranisim, "adlı oyuncu", saldırılanisim, "adlı oyuncuya saldırdı.")
            damage = savunma - güc
            print("Kalan Can:", damage)
        elif güc > savunma:
            damage = savunma - güc
            print(saldıranisim, "adlı oyuncu", saldırılanisim, "adlı oyuncuya saldırdı.")
            print(saldırılanisim, "adlı oyuncu öldü")



print("""
  ### [1]: Normal Saldırı
  ### [2]: Büyülü Saldırı
  ### [3]: Karakter Özellikleri
  ### [4]: Aktif Büyüler""")

raw1 = input("=> ")
if raw1 == "1":
    print("Karakterler;")
    for i in karakterler:
        print(i)
    sec_saldıran = input("Saldıracak Karakter => ")
    sec_savunan = input("Savunan Karakter => ")
    if (sec_savunan in karakterler) and (sec_saldıran in karakterler):
        saldır(karakterler[sec_saldıran],karakterler[sec_savunan])
    else:
        print("Yanlış Karakterleri girdiniz.")
elif raw1 == "2":
    print("Karakterler;")
    for i in karakterler:
        print(i)
    sec_saldıran = input("Saldıracak Karakter => ")
    sec_savunan = input("Savunan Karakter => ")
    if (sec_savunan in karakterler) and (sec_saldıran in karakterler):
        büyülüsaldırı(karakterler[sec_saldıran], karakterler[sec_savunan])
    else:
        print("Yanlış Karakterleri girdiniz."),
elif raw1 == "3":
    print("Karakterler;")
    for i in karakterler:
        print(i)
    raw2 = input("Bilgilerini öğrenmek istediğiniz karakter ismini girin => ")
    if raw2 in karakterler:
        print("""
        Karakter İsim: {}
        {} Güc: {}
        {} Sağlık: {}
        {} Zırh: {}
        {} Büyü: {}
        """.format(karakterler[raw2]["İsim"],raw2,karakterler[raw2]["Güç"],raw2,karakterler[raw2]["Sağlık"],raw2,karakterler[raw2]["Zırh"],raw2,karakterler[raw2]["Büyü"]))
    else:
        print("Yanlış karakter ismi girdiniz."),
elif raw1 == "4":
    print("Aktif Büyüler;")
    for i in Büyüler:
        print(i)
else:
    print("Yanlış Tuşladınız")