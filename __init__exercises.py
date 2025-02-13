# class Mobile:
#     def __init__(self, brand, color, model, year, where):
#         self.brand = brand
#         self.color = color
#         self.model = model
#         self.year = year
#         self.where = where

#     def show_info(self):
#         print(f"Mobile Phone: {self.brand}, {self.color}, {self.model}, {self.year}, {self.where}")

# #nesne oluştur
# mobile1 = Mobile("Samsung", "Green", "Galaxy", 2020, "South Korea")
# mobile2 = Mobile("Iphone", "Gray", "16Pro", 2021, "USA")
# mobile3 = Mobile("Huawei", "Blue", "Pura", 2024, "China")
# mobile4 = Mobile("HTC", "Black", "One", 2018, "USA")

# #BİLGİLERİ GÖSTER
# mobile1.show_info()
# mobile2.show_info()
# mobile3.show_info()
# mobile4.show_info()

# 2. __init__ Usage with Default Values
# class Person:
#     def __init__(self, name="Unknown", salary=0, age=0):
#         self.name = name
#         self.salary = salary
#         self.age = age

#     def introduce(self):
#         print(f"My name {self.name} and {self.salary} and {self.age} years old.")

# # farklı nesneler oluştur
# p1 = Person("Ali", 25000, 25)
# p2 = Person()

# p1.introduce()
# p2.introduce()
