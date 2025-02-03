from smartphone import Smartphone

catalog = [
          Smartphone("Xiaomi", "Redmi12","8-988-555-55-55"), 
          Smartphone("Samsung", "Galaxi S23", "8-988-444-44-44"), 
          Smartphone("Google", "Pixel 7", "8-988-333-33-33"), 
          Smartphone("Apple", "IPhone 6", "8-988-111-11-11"), 
          Smartphone("Nokia", "1280", "8-988-222-22-22")
          ]

for phone in catalog:
    print(f"{phone.brend} - {phone.model}. {phone.num}")
