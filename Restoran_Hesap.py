## started coding 13.08.2019
## finished coding 13.08.2019

masalar = dict()
for i in range(1,11): # masa sayısı
    masalar[i] = 0


def HesapEkle():
    masano = int(input("Masa No: "))
    eklenecek = float(input("Eklenecek: "))
    önceki = masalar[masano]
    toplam = eklenecek + önceki
    masalar[masano] = toplam
    print("Başarıyla Eklendi.")

def HesapSil():
    masano = int(input("Masa No: "))
    silinecek = float(input("Silinecek: "))
    önceki = masalar[masano]
    toplam = önceki - silinecek
    masalar[masano] = toplam
    print("Başarıyla Silindi.")

while True:
    print("""
        [1]: Masaları Görüntüle
        [2]: Hesap Ekle
        [3]: Hesap Sil
        [Q]: Çıkış
       """)

    secim = input("İşlem Seçiniz => ")

    if secim == "1":
        for i in range(1,11):
            print("Masa {} için hesap: {}".format(i,masalar[i]))
        print("Devam Etmek İçin Tıklayın.")
        input()

    elif secim == "2":
        HesapEkle()
        print("Devam Etmek İçin Tıklayın.")
        input()
    elif secim == "3":
        HesapSil()
        print("Devam Etmek İçin Tıklayın.")
        input()
    elif secim == "q" or secim == "Q":
        print("Çıkış Yapılıyor..")
        quit()
