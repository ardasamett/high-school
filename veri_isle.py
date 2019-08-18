# started coding 17.08.2019
# finished coding 18.08.2019
# -> Çok meraklı olduğum veri analizini 'ilk defa' tuple kullanarak cok kısıtlı özellikler ile kodlamaya çalıştım. Bu sürede Tuple'lar hakkında daha çok bilgim oldu, tam istediğim gibi bol hatalı(ve çözümlü), öğretici bir program kodlamış oldum.
# -> Programın amacı, sistemdeki kullanıcıların verilerini işlemek, hatalı yaş girimi varsa bunu tespit etmek ve gelir/yaş oranı ile işe yarayabilecek bireyleri belirlemek.
# -> Eklenebilecek bir çok özellik var aklımda, fakat daha fazla detaya girmek istemedim. Önemli olan mekanikleri oluşturmaktı.

veri = {} # Kullanıcı verileri burada depolanıyor
oranlar = {} # Gelir / Yaş oranları burada depolanıyor
oranlar_liste = [] # Tüm oranları görebilmek ve genel kullanıcı ortalaması için

def kullaniciekle(isim,yas,gelir):
    kullanicikac = len(veri) # En son kullanıcı numarasını buluyoruz
    veri["Kullanıcı_" + str(kullanicikac + 1)] = {} # Tuple içine tuple açıyoruz. (Daha çok veri için)
    veri["Kullanıcı_" + str(kullanicikac + 1)]["isim"] = isim
    veri["Kullanıcı_" + str(kullanicikac + 1)]["yas"] = yas
    veri["Kullanıcı_" + str(kullanicikac + 1)]["gelir"] = gelir
def yazdir(): # Kullanıcı verilerini gösterir
    for i in range(1, len(veri) + 2):
        if ("Kullanıcı_"+str(i)) not in veri:
            continue
        print("Kullanıcı_" + str(i), "=>", veri["Kullanıcı_" + str(i)]["isim"], "|| Yaş:",
              veri["Kullanıcı_" + str(i)]["yas"], "|| Gelir:", veri["Kullanıcı_" + str(i)]["gelir"])
def yaskontrol(): # Eğer yaş 130'dan büyük ise hatalı veri olarak geçiyor. Ve Tekrar düzenleniyor.
    for i in range(1,len(veri)+1):
        if(veri["Kullanıcı_"+str(i)]["yas"]) > 130:
            print(veri["Kullanıcı_"+str(i)]["isim"],"adlı kişinin yaşı",str(veri["Kullanıcı_"+str(i)]["yas"])+",","bir hata olabilir, veri değiştirildi.")
            oncekiveri = veri["Kullanıcı_"+str(i)]["yas"]
            veri["Kullanıcı_" + str(i)]["yas"] = ("Hatalı Veri Olabiliceğinden değiştirildi. Önceki veri:",oncekiveri)
def gelir_yas(): # Gelir / Yaş yapılarak işe yarayabilecek insanlar seçiliyor.
    for i in range(1, len(veri) + 1):
        kontrol1 = type(veri["Kullanıcı_" + str(i)]["yas"])
        kontrol2 = type(veri["Kullanıcı_" + str(i)]["yas"])
        if kontrol1 and kontrol2 != int: # Eğer yaş kontrolde sorun çıkarsa, yaş'ı integer değerden tuple'a çeviriyor. Bunları bu adımda eliyoruz.
            continue
        else:
            oran = veri["Kullanıcı_" + str(i)]["gelir"]/veri["Kullanıcı_" + str(i)]["yas"]
            oranlar["Kullanıcı_" + str(i)] = {}
            oranlar["Kullanıcı_" + str(i)]["isim"] = veri["Kullanıcı_" + str(i)]["isim"]
            oranlar["Kullanıcı_" + str(i)]["oran"] = oran
            oranlar_liste.append(oran)
    eniyioran = max(oranlar_liste)
    for i in range(1, len(oranlar_liste) + 1):
        if eniyioran == oranlar["Kullanıcı_"+str(i)]["oran"]:
            print(eniyioran,"oran ile en iyi",oranlar["Kullanıcı_"+str(i)]["isim"],"adlı kullanıcıdır")
def gelir_yas_ortalama():
    oran_toplam = 0
    for i in oranlar_liste:
        oran_toplam +=i
    print("Ortalama:",oran_toplam/len(oranlar_liste))



# ---- EKLENEN KULLANICILAR ---- #
kullaniciekle("Samet Arda Erdoğan",18,1000)
kullaniciekle("Bilgem Çakır",33,2500)
kullaniciekle("Fatih Acet",32,3050)
kullaniciekle("Doğukan Güven Nomak",34,2850)
kullaniciekle("Sadi Evren Seker",38,4000)
kullaniciekle("Barış Özcan",45,4250)
kullaniciekle("John Doe",4150,4150) ## Yaşı hatalı girilen kullanıcı
##

yazdir() # Kullanıcılar Yazılıyor
print("\n")
yaskontrol() # Yaş Kontrol Ediliyor
print("-- Veri değiştikten sonra, değişen kullanıcının yaş verisi aşağıdaki gibi düzenlendi --")
print(veri["Kullanıcı_7"]["yas"])
print("\n")
gelir_yas() # Gelir ve Yaş Oranlaması Yapılıyor
print("\n")
gelir_yas_ortalama() # Gelir ve Yaş Ortalaması Veriliyor