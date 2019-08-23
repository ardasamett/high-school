## Girilen Sayı kadar aritmetik şekilde yıldız basar

stars = ""

howmanystars = int(input("How many stars?: "))
for i in range (1,howmanystars+1):
    stars += "*"
    print(stars)
