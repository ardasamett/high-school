## sayının tek mi çift mi olduğunu belirler.

sayi = 7

if sayi%2 == 0:
    print("Sayı Çift")
elif type(sayi) == float: # değer float ise hata verir
    print("Geçersiz Değer (float)")
else:
    print("Sayı Tek")