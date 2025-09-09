# open() - och
# open function da ozini mode
# 1. x - mode -
# 2. w - mode - write
# 3. a - mode - append

# x mode mavjud bomasa yaratadi bosa error
# file = open("my_first_file.txt", "x")

# - bu file yaratib beradi yaratilgan bolsa error bermidi
# va ichiga yozish imkonini beradi.
# file = open("my_first_file.txt", "w+")
# file.write("Hello world!")
# m = file.read()
# print(m)

# file yaratib beradi qayta run error bermidi ichiga ma'lumot yozib beradi
# va har bir ma'lumotni orqasidan yozib ketadi
# file1 = open("my_first_file2.txt", mode="a")
# file1.write("Ziyobek va Sayodbek shu yerda")

# # r mode file ni o'qish uchun
# read = open("my_first_file1.txt", "r")
# m = read.read()
# print(m)

# file ochishni 2 xil usuli bor
# 1. file1 = open("my_first_file2.txt", mode="a")
# 2. with open("Ziyobek.docs", "a") as ziyobek:


# with open("Ziyobek.doc", "a") as ziyobek:
#     ziyobek.write("Ziyobek erinchoq")
#     # har doim file ni yopish kerak
#     ziyobek.close()
#
# with open("sayodbek.xlsx", "a") as sayodbek:
#     sayodbek.write("Sayodbek maqtanchoq")
#     # har doim file ni yopish kerak
#     sayodbek.close()

import os
#
# os.remove("Ziyobek.doc")

# if os.path.exists("my_first_file.txt"):
#     os.remove("my_first_file.txt")
#     print("Bu file o'chirildi")
# else:
#     print("Bunday file mavjud emas")


with open("my_first_file1.txt", "r") as ziyobek:
    # ziyobek.write("Ziyobek erinchoq")
    # bu but file ni oqidi
    # m = ziyobek.read()
    # bitda qatorni o'qish
    # m = ziyobek.readline()
    m = ziyobek.readable()
    print(m)
    # ziyobek.close()
