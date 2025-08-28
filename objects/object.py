# object (class)
from datetime import datetime


# object - bu biror bir narsani butunlay tasfirlash
# class ta 2 ta xarakteristicasi bor
# 1. atributlar
# 2. xususiyatlar

# Atributlar - bu class ni ichida ochilgan (yozilgan) o'zgaruvchilarga aytiladi
# Atributlar 2 turga bo'linadi.
# 1. class atributlari
# 2. excamplyar atributlar

# Xususiyatlar - bu class ni ichida ochilgan functiyalar lar
# agar class ni ichida constructor (__init__) boladigan bolsa bu object hisoblanadi
# agar class ichida constructor (__init__) bomasa bu shunchaki class
#
# class Perot:
#     # class atributi
#     # name = "Ozod maqtanchoq
#
#     # konstructor - yani classni ichidagi function larga ma'lumot uzatish
#     def __init__(self, names, age):
#         # self - bu kalit classni ichidagi xususiyatlarga ma'lumot uzatish uchun
#         self.names = names
#         self.age = age
#
#     # xususiyatlar bu classni ichida ochilgan function larga aytiladi
#     def speak(self):
#         return f"Mening ismim {self.names}"
# 1 - usul
# obj = Perot("Kesha", 2)
# print(obj.speak())
# print(type(obj))

#
# kontructorga ma'lumotlarni 3 xil turda bersak bo'ladi
# class Car:
#     def __init__(self, brand="Ford Mustang", color="white"):
#         self.brand = brand
#         self.color = color
#         # 2 - usul
#         self.name = "Sayodbek"
#
#     def show_info(self):
#         return f"Bu mashinaning brandi {self.brand} rangi {self.color}"
#
#
# obj = Car()
# print(obj.show_info())

# Amaliy vazifa:

class Car:
    def __init__(self, speeds, brand):
        self.speeds = speeds
        self.brand = brand

    def bmw_speed(self):
        speed = 0
        while speed != self.speeds:
            speed += 10
            print(f"Tezligi oshib boryapdi {speed}")

        return f"{self.brand} maksimal tezligi {speed}"


obj = Car(360, "BMW")
print(obj.bmw_speed())
















