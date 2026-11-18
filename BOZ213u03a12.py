liste = [1, 2, 3, 4, 5]

yeni_sayi = int(input("Yeni bir sayı giriniz: "))

liste[2] = yeni_sayi

del liste[-1]

print("Listenin son hali:", liste)
print("Listenin uzunluğu:", len(liste))
