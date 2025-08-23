# dict - key=value, yani lug'at

phone_book = {
    "Ali": 546549564,
    "Vali": 5454545554,
    "Ozoddbek": "Quloqsiz"
}
# get key orqali topib value
# print(phone_book.get("Ali"))

# dictdan hamma ma'lumotlarni olib keladi
# print(phone_book.items())
# print(phone_book)

# phone_book.update({"Hasan": 54156156})
# print(phone_book)

# kesish korsatilgan key orqali
# removed = phone_book.pop("Vali")
# print(removed)

# oxirgi ma'lumotni kesish
# last = phone_book.popitem()
# print(last)

# ma'lumotni borib qo'shib keladi
# Ma'lumot bosa ochirib keladi
# phone_book.setdefault("Vali", 5454545554)
# print(phone_book)

# copy_book = phone_book.copy()
# print(copy_book)