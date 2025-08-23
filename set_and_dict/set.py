# set - bu tartiblangan ma'lumot turi va ichida o'zgarmas
# ma'lumot turlarini saqlaydi
# set har doim dublicate larni o'chirib tashidi har doim 1 chi
# ma'lumot yana bir marta qaytarilsa osha qaytarilganni ochiradi
# key=value bomasa bu set

# excample = {"Salom dunyo", 12, 12.4, True, (1,), 12, 1}
# print(excample)
# print(type(excample))

# print(string)

# add - bu setga ma'lumot qo'shish
# excample.add("Ozodbek uyquchi")
# print(excample)

# update() - bu bir nechta ma'lumot qo'shish
# excample.update()
# print(excample)

# ma'lumotni ochirish
# excample.remove(12)
# print(excample)
#
# # ma'lumotni ochirish
# # removdan farqi ma'lumot mavjud bomasa nolimidi
# excample.discard(15)
# print(excample)

# oxiridan kesib olib kelish
# removed = excample.pop()
# print(removed)

# tozalash
# excample.clear()
# print(excample)

# 2 set ni birlashtirish
string = {"Salom", "Dunyo", "Ozod", "Ziyobek", "Sayodbek"}
excample = {12, 12.4, True, 30, 5, 3}

print(string.union(excample))
# print(string, excample)