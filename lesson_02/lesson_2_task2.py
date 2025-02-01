def is_year_leap(num):
    return "True" if num % 4 == 0 else "Folse"

num = int(input("Введите год: "))

result = is_year_leap(num)
print(f"год {num}: - {result}")

