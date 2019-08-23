# Girilen 2 sayının arasındaki sayıları toplayıp yazdırır.

sayi1 = 3
sayi2 = 6
toplam = 0

for i in range(sayi1+1,sayi2):
    toplam +=i

print("1. Sayı:",sayi1)
print("2. Sayı:",sayi2)
print("Aralarındaki sayılar toplamı:",toplam)