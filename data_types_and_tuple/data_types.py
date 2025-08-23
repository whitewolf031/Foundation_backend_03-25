# Ma'lumot turlari 2 xil turga bo'linadi
# 1. O'zgaruvchan - qo'shimcha o'zgaruvchi ochilmasdan
# o'zgartiriladigan ma'lumot turlari aytilad
# 2. O'zgarmas - qo'shimcha o'zgaruvchi ochilib
# o'zgartiriladigan ma'lumotlar aytiladi

# O'zgaruvchan
# List
# Dict
# set

# O'zgarmas
# string
# int - float(kasr sonlar) va integer(butun sonlar)
# bool
# tuple
#
# mevalar = ["olma", "Anor"]
# mevalar.append("Olcha")
# print(mevalar)
#
# string = "Anor"
# change = string.replace("Anor", "Olma")
# print(change)

# tuple = ()
# Afzaligi - ichida har qanday ma'lumot turi saqlay oladi
tuples = (2, "String", True, 5.4, [1,2,3,4,5], {"Name": "Ziyobek"}, (1,2,3))
# for x in tuples:
#     if x == 2:
#         print("Bu int")

# tuple da 2 ta method mavjud
# m = tuples.index("String")
# print(m)


n = tuples.count(2)
print(n)

