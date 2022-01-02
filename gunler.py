#2.soru
while True: #günler icin sözlük yapısı tanımlayacagım
    days={"monday":"pazartesi",
    "tuesday":"sali",
    "wednesday":"carsamba",
    "thrusday":"persembe",
    "friday":"cuma",
    "saturday":"cumartesi",
    "sunday":"pazar"}
    gun=str(input("Lutfen Turkce karsiligini ogrenmek istediginiz gunu giriniz: "))
    if gun not in days: 
        print("Yanlıs giris yaptiniz.")
        continue
    else:
        print(days[gun])
        continue
