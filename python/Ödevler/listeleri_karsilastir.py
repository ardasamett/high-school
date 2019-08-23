## 2 Listeyi karşılaştırıp aynı ve farklı olanları basar.


liste1 = [1,2,3,4,5,6]
liste2 = [2,4,6,8,1,6]
liste3 = [] # Ortak olanlar buraya eklenecek
liste4 = [] # Farklı olanlar buraya eklenecek

#____________________ORTAK OLANLARI EKLEME____________________________
for i in range(0,6):
    for j in range(0,6):
        if liste1[i] in liste3: # Birden fazla ortak olursa onların elenmesini sağlıyor. (liste2'de 2 tane 6 var. Eğer bunu yazmasaydık liste3'e 2 Kere 6 ekleyecekti.)
            continue
        elif liste1[i] == liste2[j]:
            liste3.append(liste1[i])
#____________________FARKLI OLANLARI EKLEME___________________________
for i in liste1:
    if i not in liste3:
        liste4.append(i)
for i in liste2:
    if i not in liste3:
        liste4.append(i)
