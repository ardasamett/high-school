## 18.07.2019 started coding for my friend 
## 18.07.2019 finished coding

print("""
    ## Hesap Makinesi ##
          ## v1 ##
       ## Döngüsüz ##
""")

sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
print("1.Sayı:",sayi1,"\n2.Sayı:",sayi2)
print("""
============================

    [1]: Sayıları Topla 
    [2]: Sayıları Çıkar
    [3]: Sayıları Çarp
    [4]: Sayıları Böl

============================
""")

giris = (input("Yapmak İstediğiniz İşlemin Numarasını Girin => "))
if giris == "1":
    print("Cevap:",sayi1+sayi2)
elif giris == "2":
    print("Cevap:",sayi1-sayi2)
elif giris == "3":
    print("Cevap:",sayi1*sayi2)
elif giris == "4":
    print("Cevap:",sayi1/sayi2)
else:
    print("Hatalı Tuşladınız")
