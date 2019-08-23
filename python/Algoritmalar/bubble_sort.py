## started coding 23.08.2019
## finished coding 23.08.2019

liste = [9,1,2,8,3,7,4,6,5]

for i in range(0,len(liste)):
    for j in range(0,len(liste)-1):
        if liste[j] > liste[j+1]:
            liste [j+1],liste[j] = liste[j],liste[j+1]

print(liste)