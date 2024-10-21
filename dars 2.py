izohli_lugat = {
 "Algoritm": "Muammoni hal qilish uchun aniq belgilangan amallar ketma-ketligi.",
 "Funksiya": "Qayta foydalanish mumkin bo'lgan kod bo'lagi, vazifani bajaradi.",
 "O'zgaruvchi": "Ma'lumotlarni saqlash uchun nomlangan joy."
}

for kalit in sorted(izohli_lugat):
    print(f"{kalit}: {izohli_lugat[kalit]}")


davlatlar_poytaxtlar = {
"O'zbekiston": "Toshkent",
 "AQSh": "Vashington",
 "Rossiya": "Moskva", "Fransiya": "Parij"
}

print("Davlatlar (alifbo ketma-ketligida):")
for davlat in sorted(davlatlar_poytaxtlar):
 print(davlat)

print("\nPoytaxtlar (alifbo ketma-ketligida):")
for poytaxt in sorted(davlatlar_poytaxtlar.values()):
 print(poytaxt)



davlatlar_poytaxtlar = {
"O'zbekiston": "Toshkent",
 "AQSh": "Vashington",
 "Rossiya": "Moskva",
 "Fransiya": "Parij"
}
foydalanuvchi_davlat = input("Iltimos, davlat nomini kiriting: ")
if foydalanuvchi_davlat in davlatlar_poytaxtlar:
 print(f"{foydalanuvchi_davlat}ning poytaxti: {davlatlar_poytaxtlar[foydalanuvchi_davlat]}")
else:
 print("Bizda bunday ma'lumot yo'q")



menu = {
 "Osh": 30000,
"Lag'mon": 25000,
 "Shashlik": 15000,
 "Somsa": 10000,
 "Mastava": 18000
}
buyurtmalar = []
for i in range(3):
 taom = input(f"{i+1}-taomni kiriting: ")
 buyurtmalar.append(taom)

for taom in buyurtmalar:
    if taom in menu:
     print(f"{taom}ning narxi: {menu[taom]} so'm")
    else:

      print(f"Bizda {taom} yo'q")