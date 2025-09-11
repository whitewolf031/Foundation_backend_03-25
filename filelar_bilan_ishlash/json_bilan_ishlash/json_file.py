# # fronted har doim json format qabul qiladi
# # json format har doim dict
# # json - JavaScript Object Notation
#
# import json
#
# # jsonga o'girishni 2 xil usuli bor
# # dumps - dictni faqat jsonga o'girib beradi
# # dump - dictdan jsonga o'giradi va alohda json file ga yozib beradi
#
# # jsondan dict ga o'girishni 2 xil usuli bor
# # loads - shunchaki dictga o'giradi
# # load - dictga o'girib alohida file ga yozib beradi
# info = {
#     "Ustozim": "Sardorbek",
#     "Ustozim haqida": "Ustozim juda ajoyib mexeribon",
#     "Guruhlar": ["03-25", "08-25"],
#     "names": ["Ziyobek", "Ozodbek", "Sayodbek"],
#     "age": [12, 16, 12],
#     "Holatlar": ["Og'iroq to'g'irlanish payitida", "Axvoli chota neto ozidan ketyapdi", "Nu boladi xozirchaga lekin ortiqcha xazilar kop"]
# }
#
# # bu jsonga ogirish
# m = json.dumps(info)
# print(m)
# print(type(m))
# # jsondagi ma'lumotlarni qayta dictga ogirish
# new_dict = json.loads(m)
# print(new_dict)
# print(type(new_dict))
#
# # indent=4 - bu ma'lumotlarni json file da chiroyli qilib beradi
# with open("my_json1.json", "w") as my_json:
#     json.dump(info, my_json, indent=4)
#
# # vazifalar:
# # 1. ismlar
# # 2. yosh
# # 3. telefon raqam
# # 4. maktabilar
# # 5. Holati
#
#
# # with open("my_json1.json", "r") as my_json:
# #     new_dict2 = json.load(my_json)
# #     new_dict2["name"] = "Ozodbek"
# #     print(new_dict2)