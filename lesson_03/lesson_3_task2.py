from smartphone import Smartphone

catalog = [
          Smartphone("Xiaomi", "Redmi12", "+79885555555"), 
          Smartphone("Samsung", "Galaxi S23", "+79884444444"), 
          Smartphone("Google", "Pixel 7", "+79883333333"), 
          Smartphone("Apple", "IPhone 6", "+79881111111"), 
          Smartphone("Nokia", "1280", "+79882222222")
          ]

for phone in catalog:
    print(f"{phone.brend} - {phone.model}. {phone.num}")
